#!/usr/bin/env python3
"""Genera la PORTADA DE VENTA para tapa blanda KDP: un único PDF "wrap" con
contraportada + lomo + frente, al tamaño exacto que pide KDP (trim + sangrado +
lomo calculado según el número de páginas).

Diseño (dirección de arte "best-seller del nicho"):
  - Frente: banda crema superior con el número-promesa gigante (+100 / +26),
    título display en Fraunces Black, badge circular de edad sobre la costura,
    ilustración reencuadrada abajo y franja verde con autor + serie.
  - Contraportada: gancho de dolor + bullets escaneables + caja de colección.
  - Lomo: verde oscuro, jerarquía título/autor y marcador de color de serie.

Uso:
  python scripts/build_cover.py                     # tomo completo
  python scripts/build_cover.py --edad=3-5          # tomo de una banda
  python scripts/build_cover.py --pages 233 --paper cream
"""
from __future__ import annotations
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
IMG = ROOT / "assets" / "images"

TRIM_W, TRIM_H, BLEED = 8.5, 11.0, 0.125
THICK = {"white": 0.002252, "color": 0.002252, "cream": 0.0025}

# Color de marcador de serie por tomo (lomo + acentos)
SERIE_COLOR = {"": "#F2A03D", "0-2": "#F2A03D", "3-5": "#E8744F",
               "6-8": "#3E6E94", "9-12": "#5B9E4A"}

BACK_EN = {
    "kicker": "100+ ACTIVITIES · A GUIDE FOR FAMILIES · AGES 0 TO 12",
    "headline": "The end of “Mom, I'm bored.”",
    "body": ("Do your kids ask for a screen the moment they're bored? Open this book "
             "to any page and in 5 minutes they'll be playing, mixing or building. "
             "100+ activities and experiments organized by age, using things you "
             "already have at home."),
    "bullets": [
        "43 step-by-step science experiments: volcanoes, invisible ink, circuits and more",
        "Games, art, sensory play and nature: ideas for every day and every mood",
        "Prep, materials and duration icons: pick an activity in 10 seconds",
        "Full-color illustrations and safety notes in every activity",
    ],
    "series": ("Looking for just your child's age? The QUALITY TIME series also "
               "comes in age volumes: 0–2 · 3–5 · 6–8 · 9–12."),
    "footer": "No fancy supplies. No screens. Just family memories.",
    "descriptor": "screen-free activities & science experiments",
    "badge_sub": "AGES", "series_label": "Quality Time Series",
    "barcode": "Reserved for barcode (placed by KDP)",
}

# Texto de contraportada (validado por marketing)
BACK = {
    "kicker": "MÁS DE 100 ACTIVIDADES · GUÍA PARA FAMILIAS · 0 A 12 AÑOS",
    "headline": "El fin de “mamá, estoy aburrido”.",
    "body": ("¿Tus hijos piden pantalla apenas se aburren? Abre este libro en "
             "cualquier página y en 5 minutos están jugando, mezclando o "
             "construyendo. Más de 100 actividades y experimentos organizados "
             "por edad, con materiales que ya tienes en casa."),
    "bullets": [
        "43 experimentos de ciencia paso a paso: volcanes, tinta invisible, circuitos y más",
        "Juego, arte, sensorial y naturaleza: ideas para cada día y cada ánimo",
        "Iconos de preparación, materiales y duración: elige en 10 segundos",
        "Ilustraciones a color y notas de seguridad en cada actividad",
    ],
    "series": ("¿Buscas solo la edad de tu hijo o hija? La serie TIEMPO DE CALIDAD "
               "también viene en tomos por edad: 0–2 · 3–5 · 6–8 · 9–12 años."),
    "footer": "Sin gastar de más. Sin pantallas. Puros recuerdos en familia.",
    "descriptor": "actividades y experimentos sin pantallas",
    "badge_sub": "EDADES", "series_label": "Serie Tiempo de Calidad",
    "barcode": "Espacio reservado para el código de barras (lo coloca KDP)",
}


def page_count(args) -> int:
    if args.pages:
        return args.pages
    interior = Path(args.interior) if args.interior else (DIST / "Tiempo-de-Calidad-BN.pdf")
    import pypdfium2 as pdfium
    return len(pdfium.PdfDocument(str(interior)))


def _img(stem: str) -> str:
    for ext in (".jpg", ".png", ".svg"):
        if (IMG / f"{stem}{ext}").exists():
            return f"assets/images/{stem}{ext}"
    return ""


def build_html(pages, paper, *, title, author, front, num, badge_num,
               badge_sub, marker, back) -> tuple[str, float, float]:
    spine = round(pages * THICK[paper], 4)
    full_w = round(BLEED + TRIM_W + spine + TRIM_W + BLEED, 4)
    full_h = round(TRIM_H + 2 * BLEED, 4)
    panel_w = round(BLEED + TRIM_W, 4)
    spine_text = pages >= 100

    css = f"""
    @font-face{{font-family:"Fraunces";font-weight:400;src:url("assets/fonts/Fraunces-400.woff2") format("woff2");}}
    @font-face{{font-family:"Fraunces";font-weight:600;src:url("assets/fonts/Fraunces-600.woff2") format("woff2");}}
    @font-face{{font-family:"Fraunces";font-weight:900;src:url("assets/fonts/Fraunces-900.woff2") format("woff2");}}
    @font-face{{font-family:"Source Sans 3";font-weight:400;src:url("assets/fonts/SourceSans3-400.woff2") format("woff2");}}
    @font-face{{font-family:"Source Sans 3";font-weight:600;src:url("assets/fonts/SourceSans3-600.woff2") format("woff2");}}
    @font-face{{font-family:"Source Sans 3";font-weight:700;src:url("assets/fonts/SourceSans3-700.woff2") format("woff2");}}
    @page{{ size:{full_w}in {full_h}in; margin:0; }}
    *{{box-sizing:border-box; margin:0; padding:0}}
    html,body{{font-family:"Source Sans 3",sans-serif; color:#33312E;}}
    .wrap{{position:relative; width:{full_w}in; height:{full_h}in; overflow:hidden; background:#245d44;}}

    /* ---- CONTRAPORTADA ---- */
    .back{{position:absolute; left:0; top:0; width:{panel_w}in; height:{full_h}in;
      background:radial-gradient(120% 90% at 30% 0%, #3a936b 0%, #2E7D5B 60%, #245d44 100%); color:#fff;}}
    .back-pad{{position:absolute; left:0.55in; right:0.4in; top:0.55in; bottom:0.55in;}}
    .b-kicker{{font-size:9.5pt; letter-spacing:.14em; opacity:.9; font-weight:600}}
    .b-head{{font-family:"Fraunces",serif; font-weight:900; font-size:31pt; line-height:1.08; margin:5mm 0 4mm;}}
    .b-body{{font-size:11.5pt; line-height:1.5; opacity:.97; max-width:5.9in;}}
    .b-list{{list-style:none; margin:5mm 0 0;}}
    .b-list li{{font-size:10.5pt; line-height:1.45; padding-left:7mm; position:relative; margin-bottom:2.2mm;}}
    .b-list li::before{{content:"✓"; position:absolute; left:0; color:#F2A03D; font-weight:700;}}
    .b-series{{margin-top:5mm; background:rgba(255,255,255,.14); border-radius:8px;
      padding:4mm 5mm; font-size:10.5pt; line-height:1.45; max-width:5.9in;}}
    .b-foot{{position:absolute; left:0.55in; right:2.3in; bottom:0.5in; font-family:"Fraunces",serif;
      font-style:italic; font-size:12.5pt; opacity:.95;}}
    .barcode{{position:absolute; right:0.45in; bottom:0.45in; width:2in; height:1.2in;
      background:rgba(255,255,255,.92); border-radius:4px; color:#9a958c; font-size:8pt;
      display:flex; align-items:center; justify-content:center; text-align:center; padding:4px;}}

    /* ---- LOMO ---- */
    .spine{{position:absolute; left:{panel_w}in; top:0; width:{spine}in; height:{full_h}in;
      background:#245d44; color:#fff; display:flex; align-items:center; justify-content:center;}}
    .spine-mark{{position:absolute; top:0.45in; left:50%; transform:translateX(-50%);
      width:{max(spine*0.55, 0.16):.3f}in; height:{max(spine*0.55, 0.16):.3f}in;
      border-radius:50%; background:{marker};}}
    .spine-txt{{transform:rotate(90deg); white-space:nowrap;
      font-size:{ '16pt' if spine>=0.42 else ('12pt' if spine>=0.25 else '9pt') };}}
    .spine-title{{font-family:"Fraunces",serif; font-weight:600;}}
    .spine-author{{font-family:"Source Sans 3",sans-serif; font-weight:400;
      font-size:{ '11pt' if spine>=0.42 else '8pt' }; opacity:.9;}}
    .spine-dot{{color:{marker}; font-weight:700;}}

    /* ---- FRENTE ---- */
    .front{{position:absolute; right:0; top:0; width:{panel_w}in; height:{full_h}in;
      overflow:hidden; background:#FBF7F0;}}
    .f-band{{position:absolute; top:0; left:0; right:0; height:4.15in; background:#FBF7F0;
      z-index:2; text-align:center; padding-top:0.52in; border-bottom:6pt solid #F2A03D;}}
    .f-num{{font-family:"Fraunces",serif; font-weight:900; font-size:104pt; line-height:.86;
      color:#E8744F; letter-spacing:-2pt;}}
    .f-num-sub{{font-size:13.5pt; font-weight:700; letter-spacing:.18em; color:#2E7D5B;
      text-transform:uppercase; margin-top:2.5mm;}}
    .f-title{{font-family:"Fraunces",serif; font-weight:900; font-size:76pt; line-height:.98;
      color:#33312E; margin-top:5mm;}}
    .f-img{{position:absolute; top:4.15in; left:0; right:0; bottom:0.85in; overflow:hidden;}}
    .f-img img{{width:100%; height:100%; object-fit:cover; object-position:center 78%;}}
    .f-badge{{position:absolute; top:3.52in; right:0.42in; width:1.72in; height:1.72in;
      border-radius:50%; background:#F2A03D; color:#33312E; transform:rotate(-7deg);
      display:flex; flex-direction:column; align-items:center; justify-content:center;
      box-shadow:0 3px 12px rgba(0,0,0,.25); z-index:3; border:4pt solid #FBF7F0;}}
    .f-badge-sub{{font-size:10.5pt; font-weight:700; letter-spacing:.12em;}}
    .f-badge-num{{font-family:"Fraunces",serif; font-weight:900; font-size:29pt; line-height:1.05;}}
    .f-foot{{position:absolute; bottom:0; left:0; right:0; height:0.85in; background:#245d44;
      color:#fff; z-index:3; display:flex; align-items:center; justify-content:center; gap:4mm;
      font-size:13pt; letter-spacing:.03em;}}
    .f-foot .sep{{color:{marker}; font-weight:700;}}
    .f-foot .serie{{font-size:10.5pt; text-transform:uppercase; letter-spacing:.14em; opacity:.9;}}
    """

    spine_html = (
        f'<div class="spine"><div class="spine-mark"></div>'
        f'<div class="spine-txt"><span class="spine-title">{title}</span>'
        f'&nbsp;<span class="spine-dot">·</span>&nbsp;'
        f'<span class="spine-author">{author}</span></div></div>'
        if spine_text else f'<div class="spine"><div class="spine-mark"></div></div>')
    bullets = "".join(f"<li>{b}</li>" for b in back["bullets"])
    front_img = f'<img src="{front}" alt="">' if front else ""
    title_html = title.replace("Tiempo de ", "Tiempo de<br>").replace("Quality Time", "Quality<br>Time")

    html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head>
<body><div class="wrap">
  <div class="back"><div class="back-pad">
    <div class="b-kicker">{back['kicker']}</div>
    <div class="b-head">{back['headline']}</div>
    <p class="b-body">{back['body']}</p>
    <ul class="b-list">{bullets}</ul>
    <div class="b-series">{back['series']}</div>
  </div>
  <div class="b-foot">{back['footer']}</div>
  <div class="barcode">{back['barcode']}</div>
  </div>
  {spine_html}
  <div class="front">
    <div class="f-band">
      <div class="f-num">{num}</div>
      <div class="f-num-sub">{back['descriptor']}</div>
      <h1 class="f-title">{title_html}</h1>
    </div>
    <div class="f-img">{front_img}</div>
    <div class="f-badge"><span class="f-badge-sub">{badge_sub}</span>
      <span class="f-badge-num">{badge_num}</span></div>
    <div class="f-foot"><span>{author}</span><span class="sep">·</span>
      <span class="serie">{back['series_label']}</span></div>
  </div>
</div></body></html>"""
    return html, full_w, full_h


def main():
    import glob, yaml
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", type=int, default=0)
    ap.add_argument("--interior", default="")
    ap.add_argument("--paper", choices=list(THICK), default="white")
    ap.add_argument("--edad", default="", help="rango (0-2, 3-5, 6-8, 9-12) para portada de banda")
    ap.add_argument("--lang", default="es", choices=["es", "en"])
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    src = "data/book.yaml" if args.lang == "es" else f"data/{args.lang}/book.yaml"
    book = yaml.safe_load((ROOT / src).read_text(encoding="utf-8"))
    meta = book["meta"]
    title, author = meta.get("titulo", ""), meta.get("autor", "")
    back = dict(BACK if args.lang == "es" else BACK_EN)
    slugbase = meta.get("slug", "Tiempo-de-Calidad")

    if args.edad:
        e = next((x for x in book["edades"] if x["rango"] == args.edad), None)
        if not e:
            raise SystemExit(f"--edad={args.edad} no existe")
        n = len(glob.glob(str(ROOT / f"data/activities/{args.edad.replace('-', 'a')}-*.yaml")))
        num = f"+{n}"
        badge_sub, badge_num = back["badge_sub"], args.edad.replace("-", "–")
        otras = [r for r in ("0-2", "3-5", "6-8", "9-12") if r != args.edad]
        n_exp = 0
        for f in glob.glob(str(ROOT / f"data/activities/{args.edad.replace('-', 'a')}-*.yaml")):
            if "tipo: experimento" in Path(f).read_text(encoding="utf-8"):
                n_exp += 1
        back["kicker"] = f"{n} ACTIVIDADES · GUÍA PARA FAMILIAS · {e['titulo'].upper()}"
        back["body"] = (f"¿Tus hijos piden pantalla apenas se aburren? Abre este libro en "
                        f"cualquier página y en 5 minutos están jugando, mezclando o "
                        f"construyendo. {n} actividades y experimentos pensados para "
                        f"niños de {e['titulo'].lower()}, con materiales que ya tienes en casa.")
        back["bullets"] = ([f"{n_exp} experimentos de ciencia paso a paso, a la medida de su edad"]
                           + BACK["bullets"][1:])
        back["series"] = ("Completa la colección TIEMPO DE CALIDAD con los otros tomos: "
                          + " · ".join(f"{r} años" for r in otras)
                          + ", o el tomo completo 0–12.")
        front = _img(f"sep-{args.edad}") or _img("portada")
        if not (args.pages or args.interior):
            args.interior = str(DIST / f"{slugbase}-{args.edad}-BN.pdf")
        out = Path(args.out) if args.out else (DIST / (f"Portada-KDP-{args.edad}.pdf" if args.lang == "es" else f"Cover-KDP-{args.edad}.pdf"))
        marker = SERIE_COLOR[args.edad]
    else:
        num = "+100"
        badge_sub, badge_num = back["badge_sub"], "0–12"
        front = _img("portada")
        if not (args.pages or args.interior):
            cand = DIST / f"{slugbase}-BN.pdf"
            if cand.exists():
                args.interior = str(cand)
        out = Path(args.out) if args.out else (DIST / ("Portada-KDP-tapa-blanda.pdf" if args.lang == "es" else "Cover-KDP-paperback.pdf"))
        marker = SERIE_COLOR[""]

    pages = page_count(args)
    html, w, h = build_html(pages, args.paper, title=title, author=author, front=front,
                            num=num, badge_num=badge_num, badge_sub=badge_sub,
                            marker=marker, back=back)
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
