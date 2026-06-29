#!/usr/bin/env python3
"""Construye el libro: datos YAML + plantillas Jinja2 -> HTML -> PDF (WeasyPrint) + EPUB (pandoc).

Uso:
    python scripts/build.py            # genera HTML, PDF y EPUB en dist/
    python scripts/build.py --html     # solo HTML (rápido, para iterar maquetación)
"""
from __future__ import annotations
import sys, re, unicodedata
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TEMPLATES = ROOT / "templates"
STYLES = ROOT / "styles"
ASSETS = ROOT / "assets"
DIST = ROOT / "dist"

EDAD_ORDER = {"0-2": 0, "3-5": 1, "6-8": 2, "9-12": 3}


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_activities() -> list[dict]:
    acts = []
    for p in sorted((DATA / "activities").glob("*.yaml")):
        a = load_yaml(p)
        a["_file"] = p.name
        acts.append(a)
    acts.sort(key=lambda a: (EDAD_ORDER.get(a.get("edad", ""), 99), a.get("orden", 999)))
    return acts


def load_icons() -> dict:
    icons = {}
    for p in (ASSETS / "icons").glob("*.svg"):
        icons[p.stem] = p.read_text(encoding="utf-8")
    return icons


def resolve_image(stem: str) -> str | None:
    """Devuelve la ruta relativa de la imagen para 'stem', prefiriendo PNG sobre SVG.

    Así, si el usuario coloca un PNG propio (p. ej. 0a2-01.png) sobreescribe la
    ilustración SVG generada. Devuelve None si no existe ninguna.
    """
    if not stem:
        return None
    for ext in (".png", ".jpg", ".svg"):
        if (ASSETS / "images" / f"{stem}{ext}").exists():
            return f"assets/images/{stem}{ext}"
    return None


def build_html(book: dict, acts: list[dict], icons: dict, extra_css: str = "") -> str:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True, lstrip_blocks=True,
    )
    tipos = book["tipos"]

    # Validar datos de las actividades antes de renderizar (errores claros)
    for a in acts:
        ref = a.get("_file", a.get("id", "actividad"))
        if a.get("tipo") not in tipos:
            raise ValueError(f"{ref}: tipo '{a.get('tipo')}' no definido en book.yaml")
        if a.get("edad") not in EDAD_ORDER:
            raise ValueError(f"{ref}: rango de edad '{a.get('edad')}' no válido")

    # Resolver imágenes de cada actividad (con fallback a None)
    for a in acts:
        a["imagen_src"] = resolve_image(a.get("id", ""))

    # Imágenes de portada y separadores de capítulo
    cover_src = resolve_image("portada")
    edades = book["edades"]
    for e in edades:
        e["cover_src"] = resolve_image(f"sep-{e['rango']}")

    inline_css = (STYLES / "print.css").read_text(encoding="utf-8")
    if extra_css:
        inline_css += "\n/* override */\n" + extra_css

    tmpl = env.get_template("book.html.j2")
    return tmpl.render(
        meta=book["meta"], palette=book["palette"], tipos=tipos,
        edades=edades, leyenda=book["leyenda"], textos=book["textos"],
        actividades=acts, icons=icons,
        has_cover=bool(cover_src), cover_src=cover_src,
        inline_css=inline_css,
    )


def build_pdf(html_path: Path, out: Path) -> None:
    from weasyprint import HTML
    HTML(filename=str(html_path), base_url=str(ROOT)).write_pdf(str(out))


def epub_cover(pdf_path: Path) -> Path | None:
    """Portada raster para el EPUB (Kindle requiere raster con el título).

    Si el usuario provee assets/images/portada.png se usa tal cual; si no, se
    rasteriza la PRIMERA página del PDF ya construido (que incluye la escena de
    portada y el título en la tipografía Fraunces incrustada)."""
    png = ASSETS / "images" / "portada.png"
    if png.exists():
        return png
    if pdf_path.exists():
        try:
            import pypdfium2 as pdfium
            doc = pdfium.PdfDocument(str(pdf_path))
            out = DIST / "_cover.png"
            doc[0].render(scale=2.6).to_pil().save(str(out))
            return out
        except Exception as e:
            print(f"  (aviso: no se pudo rasterizar la portada: {e})")
    return None


def build_epub(book: dict, html_path: Path, out: Path, pdf_path: Path) -> None:
    import pypandoc
    meta = book["meta"]
    extra = [
        f"--metadata=title:{meta['titulo']}",
        f"--metadata=subtitle:{meta['subtitulo']}",
        f"--metadata=author:{meta['autor']}",
        f"--metadata=lang:{meta['idioma']}",
        f"--css={STYLES/'epub.css'}",
        f"--resource-path={ROOT}",
        "--split-level=2",
        "--toc", "--toc-depth=2",
    ]
    cover = epub_cover(pdf_path)
    if cover:
        extra.append(f"--epub-cover-image={cover}")
    try:
        pypandoc.convert_file(
            str(html_path), to="epub3", format="html",
            outputfile=str(out), extra_args=extra,
        )
    except OSError as e:
        print("  (aviso: no se pudo generar el EPUB: falta 'pandoc' en el sistema. "
              f"Instálalo o usa 'pip install pypandoc-binary'. Detalle: {e})")


def build_bw(pdf_path: Path, out: Path) -> bool:
    """Genera una versión en escala de grises (interior B/N para KDP, barato de
    imprimir) a partir del PDF a color, usando Ghostscript. Devuelve True si OK."""
    import shutil, subprocess
    gs = shutil.which("gs") or shutil.which("gswin64c")
    if not gs:
        print("  (aviso: Ghostscript no está instalado; no se generó la versión B/N. "
              "Instálalo con 'apt-get install ghostscript').")
        return False
    cmd = [gs, "-dNOPAUSE", "-dBATCH", "-dQUIET", "-sDEVICE=pdfwrite",
           "-sProcessColorModel=DeviceGray", "-sColorConversionStrategy=Gray",
           "-dOverrideICC", "-dAutoRotatePages=/None",
           f"-sOutputFile={out}", str(pdf_path)]
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  (aviso: falló la conversión a B/N: {e})")
        return False


# Sangrado KDP: página = trim + sangrado (8.625x11.25). Las secciones a sangre
# (portada y separadores) crecen para llenar la página completa.
KDP_BLEED_CSS = "@page{ size:8.625in 11.25in; }\n.cover, .chapter-divider{ height:285.75mm; }"


def _arg_value(prefix: str) -> str | None:
    for a in sys.argv:
        if a.startswith(prefix):
            return a.split("=", 1)[1]
    return None


def main() -> None:
    only_html = "--html" in sys.argv
    kdp = "--kdp" in sys.argv
    bw = "--bw" in sys.argv
    edad = _arg_value("--edad=")
    DIST.mkdir(exist_ok=True)
    book = load_yaml(DATA / "book.yaml")
    acts = load_activities()
    icons = load_icons()

    slug = "Tiempo-de-Calidad"
    # Modo serie: un solo rango de edad -> libro independiente
    if edad:
        acts = [a for a in acts if a.get("edad") == edad]
        book["edades"] = [e for e in book["edades"] if e["rango"] == edad]
        if not acts or not book["edades"]:
            raise SystemExit(f"--edad={edad} no coincide con ninguna actividad/rango")
        banda = book["edades"][0]["titulo"]
        book["meta"] = dict(book["meta"])
        book["meta"]["subtitulo"] = (f"+{len(acts)} actividades y experimentos sin "
                                     f"pantallas para niños de {banda}")
        slug = f"Tiempo-de-Calidad-{edad}"
    print(f"Actividades cargadas: {len(acts)}" + (f" (edad {edad})" if edad else ""))

    # HTML de pantalla (8.5x11)
    html = build_html(book, acts, icons)
    html_path = DIST / "book.html"
    html_path.write_text(html, encoding="utf-8")
    print(f"HTML -> {html_path}")
    if only_html:
        return

    pdf_path = DIST / f"{slug}.pdf"
    build_pdf(html_path, pdf_path)
    print(f"PDF  -> {pdf_path}")

    epub_path = DIST / f"{slug}.epub"
    build_epub(book, html_path, epub_path, pdf_path)
    print(f"EPUB -> {epub_path}")

    if bw:
        if build_bw(pdf_path, DIST / f"{slug}-BN.pdf"):
            print(f"PDF B/N -> {DIST / f'{slug}-BN.pdf'}")

    # Interior listo para imprenta KDP (con sangrado)
    if kdp:
        html_kdp = build_html(book, acts, icons, extra_css=KDP_BLEED_CSS)
        html_kdp_path = DIST / "book-kdp.html"
        html_kdp_path.write_text(html_kdp, encoding="utf-8")
        kdp_pdf = DIST / f"{slug}-KDP.pdf"
        build_pdf(html_kdp_path, kdp_pdf)
        print(f"PDF KDP (sangrado) -> {kdp_pdf}")
        if bw and build_bw(kdp_pdf, DIST / f"{slug}-KDP-BN.pdf"):
            print(f"PDF KDP B/N -> {DIST / f'{slug}-KDP-BN.pdf'}")


if __name__ == "__main__":
    main()
