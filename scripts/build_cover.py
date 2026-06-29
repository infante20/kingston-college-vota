#!/usr/bin/env python3
"""Genera la PORTADA DE VENTA para tapa blanda KDP: un único PDF "wrap" con
contraportada + lomo + frente, al tamaño exacto que pide KDP (trim + sangrado +
lomo calculado según el número de páginas).

Uso:
  python scripts/build_cover.py                         # usa dist/Tiempo-de-Calidad-BN.pdf
  python scripts/build_cover.py --pages 233             # nº de páginas manual
  python scripts/build_cover.py --interior dist/X.pdf   # contar páginas de otro PDF
  python scripts/build_cover.py --paper cream|white|color

Notas KDP:
  - Lomo = páginas x grosor de papel (blanco/estándar color 0.002252", crema 0.0025").
  - Texto en el lomo solo si el libro tiene >= 100 páginas.
  - El código de barras lo coloca Amazon: se deja libre la zona inferior derecha
    de la contraportada (~2 x 1.2 in).
"""
from __future__ import annotations
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
IMG = ROOT / "assets" / "images"

TRIM_W, TRIM_H, BLEED = 8.5, 11.0, 0.125
THICK = {"white": 0.002252, "color": 0.002252, "cream": 0.0025}

# Texto de contraportada (edítalo a tu gusto)
BACK = {
    "kicker": "GUÍA PARA FAMILIAS · 0 A 12 AÑOS",
    "headline": "Menos pantallas, más momentos juntos.",
    "body": ("Más de 100 actividades y experimentos sin pantallas para hacer en casa, "
             "con materiales que ya tienes. Organizados por edad para que siempre "
             "encuentres algo a la medida de tu hijo o hija."),
    "bullets": [
        "43 experimentos de ciencia explicados paso a paso",
        "Juego, arte, sensorial y naturaleza para cada día",
        "Dificultad, materiales y duración a simple vista",
        "Ilustraciones a color y notas de seguridad",
    ],
    "footer": "Sin comprar nada caro. Sin pantallas. Solo tiempo de calidad.",
}


def page_count(args) -> int:
    if args.pages:
        return args.pages
    interior = Path(args.interior) if args.interior else (DIST / "Tiempo-de-Calidad-BN.pdf")
    import pypdfium2 as pdfium
    return len(pdfium.PdfDocument(str(interior)))


def front_src() -> str:
    for ext in (".jpg", ".png", ".svg"):
        if (IMG / f"portada{ext}").exists():
            return f"assets/images/portada{ext}"
    return ""


def build_html(pages, paper, title, subt, author, front, badge):
    spine = round(pages * THICK[paper], 4)
    full_w = round(BLEED + TRIM_W + spine + TRIM_W + BLEED, 4)
    full_h = round(TRIM_H + 2 * BLEED, 4)
    panel_w = round(BLEED + TRIM_W, 4)          # ancho de cada panel (con sangrado exterior)
    spine_text = pages >= 100

    css = f"""
    @font-face{{font-family:"Fraunces";font-weight:600;src:url("assets/fonts/Fraunces-600.woff2") format("woff2");}}
    @font-face{{font-family:"Fraunces";font-weight:400;src:url("assets/fonts/Fraunces-400.woff2") format("woff2");}}
    @font-face{{font-family:"Source Sans 3";font-weight:400;src:url("assets/fonts/SourceSans3-400.woff2") format("woff2");}}
    @font-face{{font-family:"Source Sans 3";font-weight:600;src:url("assets/fonts/SourceSans3-600.woff2") format("woff2");}}
    @font-face{{font-family:"Source Sans 3";font-weight:700;src:url("assets/fonts/SourceSans3-700.woff2") format("woff2");}}
    @page{{ size:{full_w}in {full_h}in; margin:0; }}
    *{{box-sizing:border-box; margin:0; padding:0}}
    html,body{{font-family:"Source Sans 3",sans-serif; color:#33312E;}}
    .wrap{{position:relative; width:{full_w}in; height:{full_h}in; overflow:hidden;}}
    /* ---- CONTRAPORTADA (izquierda) ---- */
    .back{{position:absolute; left:0; top:0; width:{panel_w}in; height:{full_h}in;
      background:radial-gradient(120% 90% at 30% 0%, #3a936b 0%, #2E7D5B 60%, #245d44 100%); color:#fff;}}
    .back-pad{{position:absolute; left:0.55in; right:0.4in; top:0.6in; bottom:0.55in;}}
    .b-kicker{{font-size:10pt; letter-spacing:.18em; opacity:.9}}
    .b-head{{font-family:"Fraunces",serif; font-size:25pt; line-height:1.12; margin:5mm 0 4mm;}}
    .b-body{{font-size:11.5pt; line-height:1.5; opacity:.96; max-width:5.6in;}}
    .b-list{{list-style:none; margin:6mm 0 0;}}
    .b-list li{{font-size:11pt; line-height:1.5; padding-left:7mm; position:relative; margin-bottom:2mm;}}
    .b-list li::before{{content:"✓"; position:absolute; left:0; color:#F2A03D; font-weight:700;}}
    .b-foot{{position:absolute; left:0.55in; right:2.2in; bottom:0.5in; font-family:"Fraunces",serif;
      font-style:italic; font-size:12.5pt; opacity:.95;}}
    .barcode{{position:absolute; right:0.45in; bottom:0.45in; width:2in; height:1.2in;
      background:rgba(255,255,255,.92); border-radius:4px; color:#9a958c; font-size:8pt;
      display:flex; align-items:center; justify-content:center; text-align:center; padding:4px;}}
    /* ---- LOMO (centro) ---- */
    .spine{{position:absolute; left:{panel_w}in; top:0; width:{spine}in; height:{full_h}in;
      background:#245d44; color:#fff; display:flex; align-items:center; justify-content:center;}}
    .spine-txt{{transform:rotate(90deg); white-space:nowrap; font-family:"Fraunces",serif;
      font-size:{ '13pt' if spine>=0.35 else '9pt' }; letter-spacing:.02em;}}
    /* ---- FRENTE (derecha) ---- */
    .front{{position:absolute; right:0; top:0; width:{panel_w}in; height:{full_h}in; overflow:hidden;}}
    .front-bg{{position:absolute; inset:0; width:100%; height:100%; object-fit:cover;}}
    .front-scrim{{position:absolute; inset:0;
      background:linear-gradient(180deg, rgba(20,40,30,.55) 0%, rgba(20,40,30,.18) 42%, rgba(20,40,30,.62) 100%);}}
    .front-in{{position:absolute; left:0.6in; right:0.6in; top:0.95in; z-index:2; text-align:center; color:#fff;
      background:rgba(18,34,26,.46); border-radius:14px; padding:9mm 7mm;}}
    .f-kicker{{font-size:12pt; letter-spacing:.26em; text-transform:uppercase; opacity:.92;}}
    .f-title{{font-family:"Fraunces",serif; font-size:56pt; line-height:1.02; margin:6mm 0 0;
      text-shadow:0 3px 16px rgba(0,0,0,.55);}}
    .f-sub{{font-size:15pt; margin-top:5mm; text-shadow:0 2px 10px rgba(0,0,0,.5);}}
    .f-badge{{display:inline-block; margin-top:7mm; padding:2.5mm 6mm; border:2px solid #fff;
      border-radius:999px; font-size:12pt; font-weight:600;}}
    .f-author{{position:absolute; left:0; right:0; bottom:0.7in; z-index:2; text-align:center;
      color:#fff; font-size:14pt; text-shadow:0 2px 8px rgba(0,0,0,.6);}}
    """

    spine_html = (f'<div class="spine"><div class="spine-txt">{title} · {author}</div></div>'
                  if spine_text else f'<div class="spine"></div>')
    bullets = "".join(f"<li>{b}</li>" for b in BACK["bullets"])
    front_bg = f'<img class="front-bg" src="{front}" alt="">' if front else ""

    html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head>
<body><div class="wrap">
  <div class="back"><div class="back-pad">
    <div class="b-kicker">{BACK['kicker']}</div>
    <div class="b-head">{BACK['headline']}</div>
    <p class="b-body">{BACK['body']}</p>
    <ul class="b-list">{bullets}</ul>
  </div>
  <div class="b-foot">{BACK['footer']}</div>
  <div class="barcode">Espacio reservado para el código de barras (lo coloca KDP)</div>
  </div>
  {spine_html}
  <div class="front">
    {front_bg}<div class="front-scrim"></div>
    <div class="front-in">
      <div class="f-kicker">Guía para familias</div>
      <h1 class="f-title">{title}</h1>
      <div class="f-sub">{subt}</div>
      <span class="f-badge">{badge}</span>
    </div>
    <div class="f-author">{author}</div>
  </div>
</div></body></html>"""
    return html, full_w, full_h


def _img(stem: str) -> str:
    for ext in (".jpg", ".png", ".svg"):
        if (IMG / f"{stem}{ext}").exists():
            return f"assets/images/{stem}{ext}"
    return ""


def main():
    import glob, yaml
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", type=int, default=0)
    ap.add_argument("--interior", default="")
    ap.add_argument("--paper", choices=list(THICK), default="white")
    ap.add_argument("--edad", default="", help="rango (0-2, 3-5, 6-8, 9-12) para portada de banda")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    book = yaml.safe_load((ROOT / "data/book.yaml").read_text(encoding="utf-8"))
    meta = book["meta"]
    title, author = meta.get("titulo", ""), meta.get("autor", "")

    if args.edad:
        e = next((x for x in book["edades"] if x["rango"] == args.edad), None)
        if not e:
            raise SystemExit(f"--edad={args.edad} no existe")
        n = len(glob.glob(str(ROOT / f"data/activities/{args.edad.replace('-', 'a')}-*.yaml")))
        subt = f"+{n} actividades y experimentos sin pantallas para niños de {e['titulo']}"
        front = _img(f"sep-{args.edad}") or _img("portada")
        badge = e["titulo"]
        if not (args.pages or args.interior):
            args.interior = str(DIST / f"Tiempo-de-Calidad-{args.edad}-BN.pdf")
        out = Path(args.out) if args.out else (DIST / f"Portada-KDP-{args.edad}.pdf")
    else:
        subt = meta.get("subtitulo", "")
        front = _img("portada")
        badge = "Edades 0 – 12"
        out = Path(args.out) if args.out else (DIST / "Portada-KDP-tapa-blanda.pdf")

    pages = page_count(args)
    html, w, h = build_html(pages, args.paper, title, subt, author, front, badge)
    spine = round(pages * THICK[args.paper], 4)

    html_path = DIST / "cover-wrap.html"
    html_path.write_text(html, encoding="utf-8")

    from weasyprint import HTML
    HTML(filename=str(html_path), base_url=str(ROOT)).write_pdf(str(out))
    print(f"Portada wrap -> {out}")
    print(f"  páginas={pages} · papel={args.paper} · lomo={spine:.3f} in · "
          f"tamaño total={w} x {h} in"
          + ("" if pages >= 100 else "  (lomo SIN texto: <100 págs)"))


if __name__ == "__main__":
    main()
