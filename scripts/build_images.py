#!/usr/bin/env python3
"""Genera las ilustraciones del libro como SVG detallados (sin red).

Produce en assets/images/:
  - <id>.svg         escena de cabecera por actividad (detallada, según su tipo)
  - sep-<rango>.svg  escena de separador por rango de edad
  - portada.svg      escena de portada

Las ilustraciones son vectoriales, planas, con degradados, sombras suaves y
varios objetos por escena (estilo libro infantil). Puedes sustituir cualquier
archivo por un PNG del mismo nombre (<id>.png) y el build lo usará en su lugar.
"""
from __future__ import annotations
import glob, hashlib, math, random
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "images"

ACCENTS = ["#2E7D5B", "#3E6E94", "#E8744F", "#F2A03D", "#7E57A6", "#D24D6E", "#5B9E4A"]
TIPO_COLOR = {
    "experimento": "#3E6E94", "sensorial": "#7E57A6", "recreativa": "#E8744F",
    "juego": "#2E7D5B", "emocional": "#D24D6E", "arte": "#F2A03D", "naturaleza": "#5B9E4A",
}


# ----------------------------- color helpers -----------------------------
def _h(s): return tuple(int(s[i:i+2], 16) for i in (1, 3, 5))
def _x(t): return "#%02x%02x%02x" % tuple(max(0, min(255, round(v))) for v in t)
def mix(c1, c2, t):
    a, b = _h(c1), _h(c2); return _x(tuple(a[i] + (b[i] - a[i]) * t for i in range(3)))
def tint(c, t): return mix(c, "#ffffff", t)
def shade(c, t): return mix(c, "#000000", t)
def rng_for(seed): return random.Random(int(hashlib.md5(seed.encode()).hexdigest(), 16))


# ----------------------------- shape helpers -----------------------------
def star(cx, cy, r, fill, op=1.0):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * .45
        pts.append(f"{cx+rr*math.cos(ang):.1f},{cy+rr*math.sin(ang):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}" opacity="{op}"/>'

def heart(cx, cy, s, fill, op=1.0):
    return (f'<path transform="translate({cx-s} {cy-s*0.9}) scale({s/12})" opacity="{op}" '
            f'd="M12 19.5 4.8 12.3a4.3 4.3 0 0 1 6-6.1l1.2 1.1 1.2-1.1a4.3 4.3 0 0 1 6 6.1z" '
            f'fill="{fill}"/>')

def leaf(cx, cy, s, fill, rot=0):
    return (f'<path transform="translate({cx} {cy}) rotate({rot}) scale({s/24})" '
            f'd="M0 12 C0 2 10 -8 22 -10 C20 4 8 14 0 12 Z" fill="{fill}"/>')

def shadow(cx, cy, rx, ry=None):
    ry = ry or rx * 0.28
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#1b1a18" opacity="0.10"/>'

def circle_hi(cx, cy, r, fill):
    """Círculo con un brillo suave."""
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>'
            f'<circle cx="{cx-r*.32:.1f}" cy="{cy-r*.34:.1f}" r="{r*.3:.1f}" '
            f'fill="#ffffff" opacity="0.35"/>')

def sparkles(rng, n, x0, x1, y0, y1, colors):
    out = []
    for _ in range(n):
        x, y = rng.randint(x0, x1), rng.randint(y0, y1)
        if rng.random() < .5:
            out.append(star(x, y, rng.randint(5, 11), rng.choice(colors), .8))
        else:
            out.append(f'<circle cx="{x}" cy="{y}" r="{rng.randint(3,6)}" '
                       f'fill="{rng.choice(colors)}" opacity="0.6"/>')
    return "".join(out)


# ----------------------------- per-type scenes -----------------------------
GROUND_Y = 350

def scene_experimento(color, rng):
    """Matraz burbujeante + tubos de ensayo + chispas."""
    cx = 600
    liq = ACCENTS[rng.randrange(len(ACCENTS))]
    o = [shadow(cx, GROUND_Y + 8, 150)]
    # rejilla de tubos de ensayo
    for i, dx in enumerate((-220, -170)):
        tcol = ACCENTS[(rng.randrange(7))]
        x = cx + dx
        o.append(f'<rect x="{x-13}" y="220" width="26" height="120" rx="13" fill="#ffffff" stroke="{shade(color,.1)}" stroke-width="3"/>')
        o.append(f'<rect x="{x-10}" y="285" width="20" height="52" rx="10" fill="{tcol}"/>')
        o.append(f'<circle cx="{x-3}" cy="300" r="3" fill="#ffffff" opacity=".7"/>')
    # matraz Erlenmeyer
    o.append(f'<rect x="{cx-14}" y="180" width="28" height="55" rx="6" fill="#ffffff" stroke="{shade(color,.12)}" stroke-width="4"/>')
    o.append(f'<path d="M{cx-14} 230 L{cx-70} 330 Q{cx-74} 345 {cx-58} 345 L{cx+58} 345 Q{cx+74} 345 {cx+70} 330 L{cx+14} 230 Z" fill="#ffffff" stroke="{shade(color,.12)}" stroke-width="4"/>')
    o.append(f'<path d="M{cx-48} 300 L{cx-58} 330 Q{cx-62} 341 {cx-50} 341 L{cx+50} 341 Q{cx+62} 341 {cx+58} 330 L{cx+48} 300 Z" fill="{liq}"/>')
    o.append(f'<ellipse cx="{cx-30}" cy="316" rx="10" ry="4" fill="#ffffff" opacity=".3"/>')
    # burbujas saliendo
    for dy, r in ((-18, 7), (-42, 9), (-66, 6), (-92, 8)):
        o.append(f'<circle cx="{cx+rng.randint(-10,10)}" cy="{180+dy}" r="{r}" fill="{liq}" opacity="0.5"/>')
    o.append(sparkles(rng, 7, 760, 1120, 70, 300, [tint(color,.2), "#F2A03D", liq]))
    return "".join(o)

def scene_sensorial(color, rng):
    """Mano suave con ondas y formas flotando."""
    cx = 640
    o = [shadow(cx, GROUND_Y + 6, 140)]
    for i, (dx, dy, r) in enumerate(((-210, 150, 26), (-150, 240, 18), (210, 130, 22), (170, 250, 16))):
        o.append(circle_hi(cx+dx, dy, r, tint(ACCENTS[rng.randrange(7)], .25)))
    # ondas
    for i, y in enumerate((150, 200, 250)):
        o.append(f'<path d="M{cx-60} {y} q30 -22 60 0 t60 0" stroke="{tint(color,.3-i*.05)}" stroke-width="7" fill="none" stroke-linecap="round" opacity=".8"/>')
    # mano estilizada
    o.append(f'<g transform="translate({cx-70} 150) scale(5.4)" fill="{tint(color,.05)}" stroke="{shade(color,.12)}" stroke-width="0.4">'
             '<path d="M7 11V6.5a1.4 1.4 0 0 1 2.8 0V10M9.8 10V5.4a1.4 1.4 0 0 1 2.8 0V10M12.6 10V6.2a1.4 1.4 0 0 1 2.8 0V11M15.4 11V8.2a1.4 1.4 0 0 1 2.7 0v5.1a6 6 0 0 1-6 6.7H11a5.4 5.4 0 0 1-4-2.2L4.4 14a1.5 1.5 0 0 1 2.3-1.9L8 13.4" fill="#ffffff"/></g>')
    o.append(sparkles(rng, 8, 760, 1130, 60, 300, [tint(color,.1), "#F2A03D", "#D24D6E"]))
    return "".join(o)

def scene_recreativa(color, rng):
    """Pelota saltando con arco de movimiento + conos."""
    o = [shadow(720, GROUND_Y + 8, 150)]
    # arco de movimiento
    o.append(f'<path d="M470 330 Q620 150 770 330" stroke="{tint(color,.35)}" stroke-width="6" fill="none" stroke-dasharray="3 16" stroke-linecap="round"/>')
    # conos
    for x in (500, 560):
        o.append(shadow(x, 348, 30))
        o.append(f'<path d="M{x-22} 348 L{x} 286 L{x+22} 348 Z" fill="{color}"/>')
        o.append(f'<rect x="{x-26}" y="343" width="52" height="9" rx="4" fill="{shade(color,.12)}"/>')
        o.append(f'<rect x="{x-12}" y="312" width="24" height="7" fill="#ffffff" opacity=".6"/>')
    # pelota
    bx, by = 770, 300
    o.append(shadow(bx, 348, 34))
    o.append(circle_hi(bx, by, 40, "#ffffff"))
    o.append(f'<path d="M{bx-40} {by} a40 40 0 0 1 80 0" fill="{color}" opacity=".9"/>')
    o.append(f'<circle cx="{bx}" cy="{by}" r="40" fill="none" stroke="{shade(color,.1)}" stroke-width="3"/>')
    o.append(f'<path d="M{bx-40} {by} h80 M{bx} {by-40} v80" stroke="{shade(color,.1)}" stroke-width="3"/>')
    o.append(sparkles(rng, 6, 200, 460, 80, 260, [tint(color,.2), "#F2A03D"]))
    return "".join(o)

def scene_juego(color, rng):
    """Tablero, dado y fichas."""
    o = [shadow(620, GROUND_Y + 8, 170)]
    # tablero en perspectiva
    o.append(f'<g transform="translate(430 250) skewX(-12)">'
             f'<rect width="220" height="120" rx="10" fill="{tint(color,.55)}"/>')
    for r in range(2):
        for c in range(4):
            if (r + c) % 2 == 0:
                o.append(f'<rect x="{12+c*50}" y="{12+r*50}" width="46" height="46" rx="6" fill="{tint(color,.8)}"/>')
    o.append('</g>')
    # dado
    dx, dy = 760, 250
    o.append(shadow(dx, 352, 46))
    o.append(f'<rect x="{dx-44}" y="{dy-44}" width="88" height="88" rx="18" fill="#ffffff" stroke="{shade(color,.1)}" stroke-width="3"/>')
    for px, py in ((-22, -22), (22, -22), (0, 0), (-22, 22), (22, 22)):
        o.append(f'<circle cx="{dx+px}" cy="{dy+py}" r="7" fill="{color}"/>')
    # fichas
    for i, (x, col) in enumerate(((520, "#E8744F"), (560, "#F2A03D"), (600, "#3E6E94"))):
        o.append(f'<ellipse cx="{x}" cy="318" rx="16" ry="7" fill="{shade(col,.15)}"/>')
        o.append(f'<rect x="{x-12}" y="290" width="24" height="30" rx="10" fill="{col}"/>')
        o.append(f'<circle cx="{x}" cy="288" r="13" fill="{col}"/>')
        o.append(f'<circle cx="{x-4}" cy="284" r="4" fill="#ffffff" opacity=".4"/>')
    o.append(sparkles(rng, 6, 200, 420, 80, 240, [tint(color,.2), "#F2A03D"]))
    return "".join(o)

def figure(x, y, h, body, head=None, skin="#F2C9A0"):
    head = head or skin
    return (f'<ellipse cx="{x}" cy="{y+h+6}" rx="{h*.4:.0f}" ry="{h*.13:.0f}" fill="#1b1a18" opacity=".10"/>'
            f'<path d="M{x-h*.28:.0f} {y+h} Q{x-h*.30:.0f} {y+h*.35:.0f} {x:.0f} {y+h*.33:.0f} '
            f'Q{x+h*.30:.0f} {y+h*.35:.0f} {x+h*.28:.0f} {y+h} Z" fill="{body}"/>'
            f'<circle cx="{x}" cy="{y+h*.20:.0f}" r="{h*.17:.0f}" fill="{head}"/>')

def scene_emocional(color, rng):
    """Dos figuras (cuidador y niño) con un corazón."""
    o = []
    o.append(figure(540, 200, 140, color, skin="#F2C9A0"))
    o.append(figure(660, 250, 95, tint(color,.25), skin="#E8B98C"))
    o.append(heart(600, 175, 30, "#D24D6E"))
    o.append(heart(600, 175, 30, "#ffffff", 0.0))
    for _ in range(4):
        x, y = rng.randint(440, 780), rng.randint(90, 200)
        o.append(heart(x, y, rng.randint(10, 16), tint("#D24D6E", .3), .8))
    o.append(sparkles(rng, 5, 760, 1120, 80, 280, [tint(color,.2), "#F2A03D"]))
    return "".join(o)

def scene_arte(color, rng):
    """Caballete con lienzo, paleta y pincel."""
    o = [shadow(600, GROUND_Y + 10, 170)]
    # patas del caballete
    o.append(f'<path d="M540 350 L585 175 M660 350 L615 175 M600 320 L640 350" stroke="{shade(color,.2)}" stroke-width="9" stroke-linecap="round"/>')
    # lienzo
    o.append(f'<rect x="540" y="160" width="160" height="120" rx="6" fill="#ffffff" stroke="{shade(color,.1)}" stroke-width="4"/>')
    for i in range(3):
        c = ACCENTS[rng.randrange(7)]
        o.append(f'<path d="M{560+i*8} {200+i*22} q40 -26 90 0" stroke="{c}" stroke-width="10" fill="none" stroke-linecap="round" opacity=".9"/>')
    o.append(f'<circle cx="595" cy="200" r="14" fill="#F2A03D" opacity=".85"/>')
    # paleta
    o.append(f'<ellipse cx="800" cy="300" rx="62" ry="44" fill="{tint(color,.2)}" stroke="{shade(color,.12)}" stroke-width="3"/>')
    o.append(f'<ellipse cx="818" cy="312" rx="16" ry="11" fill="#ffffff"/>')
    for px, py, c in ((778, 282, "#E8744F"), (812, 278, "#3E6E94"), (840, 300, "#5B9E4A"), (790, 318, "#D24D6E")):
        o.append(f'<circle cx="{px}" cy="{py}" r="9" fill="{c}"/>')
    # salpicaduras
    o.append(sparkles(rng, 8, 220, 470, 90, 320, ACCENTS))
    return "".join(o)

def scene_naturaleza(color, rng):
    """Árbol frondoso, sol, mariposa y pasto."""
    o = []
    # sol
    o.append(f'<circle cx="280" cy="150" r="52" fill="#F2A03D" opacity=".9"/>')
    for k in range(12):
        a = k * math.pi / 6
        o.append(f'<line x1="{280+62*math.cos(a):.0f}" y1="{150+62*math.sin(a):.0f}" x2="{280+82*math.cos(a):.0f}" y2="{150+82*math.sin(a):.0f}" stroke="#F2A03D" stroke-width="5" stroke-linecap="round" opacity=".7"/>')
    # árbol
    tx = 720
    o.append(shadow(tx, GROUND_Y + 8, 120))
    o.append(f'<rect x="{tx-14}" y="250" width="28" height="105" rx="10" fill="{shade("#8a5a3c",.0)}"/>')
    o.append(f'<rect x="{tx-14}" y="250" width="10" height="105" fill="#ffffff" opacity=".12"/>')
    for cx, cy, r in ((tx, 200, 70), (tx-55, 235, 50), (tx+55, 235, 50), (tx, 250, 55)):
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{mix(color, "#5B9E4A", .3)}"/>')
    o.append(f'<circle cx="{tx-25}" cy="195" r="30" fill="#ffffff" opacity=".12"/>')
    for _ in range(5):
        o.append(f'<circle cx="{tx+rng.randint(-60,60)}" cy="{rng.randint(180,260)}" r="6" fill="#E8744F" opacity=".8"/>')
    # mariposa
    bx, by = 430, 240
    o.append(f'<g transform="translate({bx} {by})"><path d="M0 0 q-26 -22 -34 4 q-4 22 34 8 Z" fill="#E8744F"/>'
             '<path d="M0 0 q26 -22 34 4 q4 22 -34 8 Z" fill="#F2A03D"/>'
             '<path d="M0 0 q-20 14 -26 30 q18 6 26 -16 Z" fill="#D24D6E"/>'
             '<path d="M0 0 q20 14 26 30 q-18 6 -26 -16 Z" fill="#7E57A6"/>'
             '<line x1="0" y1="-6" x2="0" y2="34" stroke="#33312e" stroke-width="3"/></g>')
    # pasto
    for x in range(70, 1140, 40):
        h = rng.randint(14, 26)
        o.append(f'<path d="M{x} 350 q4 -{h} 8 0" stroke="{shade("#5B9E4A",.05)}" stroke-width="5" fill="none" stroke-linecap="round" opacity=".8"/>')
    return "".join(o)

SCENES = {
    "experimento": scene_experimento, "sensorial": scene_sensorial,
    "recreativa": scene_recreativa, "juego": scene_juego,
    "emocional": scene_emocional, "arte": scene_arte, "naturaleza": scene_naturaleza,
}


def hero_svg(act: dict) -> str:
    tipo = act["tipo"]; color = TIPO_COLOR[tipo]; rng = rng_for(act["id"])
    W, H = 1200, 460
    sky0, sky1 = "#FCF8F1", tint(color, .82)
    g0, g1 = tint(color, .62), shade(tint(color, .62), .12)
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">']
    p.append('<defs>'
             f'<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky0}"/><stop offset="1" stop-color="{sky1}"/></linearGradient>'
             f'<linearGradient id="grd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{g0}"/><stop offset="1" stop-color="{g1}"/></linearGradient>'
             f'<radialGradient id="glow" cx="0.5" cy="0.2" r="0.7"><stop offset="0" stop-color="#ffffff" stop-opacity="0.6"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></radialGradient>'
             '</defs>')
    p.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
    p.append(f'<rect width="{W}" height="{H}" fill="url(#glow)"/>')
    # nubes/blobs de fondo
    for _ in range(3):
        x, y, r = rng.randint(80, 1120), rng.randint(40, 120), rng.randint(30, 60)
        p.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff" opacity="0.18"/>')
    # colina trasera y suelo
    p.append(f'<path d="M0 {GROUND_Y} Q300 {GROUND_Y-50} 600 {GROUND_Y-15} T1200 {GROUND_Y-25} L1200 {H} L0 {H} Z" fill="{tint(color,.5)}" opacity=".6"/>')
    p.append(f'<path d="M0 {GROUND_Y+18} Q400 {GROUND_Y-18} 800 {GROUND_Y+10} T1200 {GROUND_Y} L1200 {H} L0 {H} Z" fill="url(#grd)"/>')
    # escena del tipo
    p.append(SCENES[tipo](color, rng))
    p.append("</svg>")
    return "".join(p)


# ----------------------------- portada y separadores -----------------------------
BAND_GRAD = {
    "0-2": ("#6FB3A0", "#3E6E94"), "3-5": ("#F4A94A", "#E8744F"),
    "6-8": ("#6BB05A", "#2E7D5B"), "9-12": ("#4E7CA8", "#7E57A6"),
}

def divider_svg(rango: str) -> str:
    c1, c2 = BAND_GRAD[rango]; r = rng_for("sep-" + rango)
    W, H = 850, 1100
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">']
    p.append('<defs>'
             f'<linearGradient id="g" x1="0" y1="0" x2="0.5" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'
             '<radialGradient id="sun" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffffff" stop-opacity="0.5"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></radialGradient>'
             '</defs>')
    p.append(f'<rect width="{W}" height="{H}" fill="url(#g)"/>')
    p.append('<circle cx="650" cy="230" r="150" fill="url(#sun)"/>')
    p.append('<circle cx="650" cy="230" r="80" fill="#ffffff" opacity=".30"/>')
    p.append(f'<path d="M0 760 Q250 640 480 740 T850 720 L850 1100 L0 1100Z" fill="#fff" opacity=".14"/>')
    p.append(f'<path d="M0 880 Q300 780 560 860 T850 840 L850 1100 L0 1100Z" fill="#fff" opacity=".12"/>')
    for _ in range(26):
        x, y = r.randint(40, 810), r.randint(40, 680)
        p.append(star(x, y, r.randint(6, 14), "#ffffff", .8) if r.random() < .5
                 else f'<circle cx="{x}" cy="{y}" r="{r.randint(3,7)}" fill="#fff" opacity=".5"/>')
    p.append(f'<rect x="0" y="820" width="{W}" height="280" fill="#000" opacity=".18"/>')
    p.append("</svg>")
    return "".join(p)

def portada_svg() -> str:
    r = rng_for("portada"); W, H = 850, 1100
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">']
    p.append('<defs>'
             '<linearGradient id="cg" x1="0" y1="0" x2="0.3" y2="1"><stop offset="0" stop-color="#3a936b"/><stop offset=".55" stop-color="#2E7D5B"/><stop offset="1" stop-color="#245d44"/></linearGradient>'
             '<radialGradient id="cs" cx="0.8" cy="0.16" r="0.5"><stop offset="0" stop-color="#F2A03D" stop-opacity="0.95"/><stop offset="1" stop-color="#F2A03D" stop-opacity="0"/></radialGradient>'
             '</defs>')
    p.append(f'<rect width="{W}" height="{H}" fill="url(#cg)"/>')
    p.append('<rect width="850" height="1100" fill="url(#cs)"/>')
    p.append('<circle cx="700" cy="170" r="80" fill="#F2A03D" opacity=".9"/>')
    p.append('<g opacity=".9"><rect x="90" y="900" width="160" height="120" rx="6" fill="#FBF7F0" opacity=".22"/><path d="M80 905 L170 840 L260 905 Z" fill="#E8744F" opacity=".6"/></g>')
    p.append('<g opacity=".85"><rect x="690" y="940" width="20" height="80" rx="6" fill="#FBF7F0" opacity=".3"/><circle cx="700" cy="918" r="58" fill="#5B9E4A" opacity=".55"/></g>')
    for (x, y) in [(140, 300), (720, 520), (150, 560), (700, 760), (120, 760)]:
        k = r.random()
        if k < .4:
            p.append(f'<circle cx="{x}" cy="{y}" r="34" fill="{r.choice(ACCENTS)}" opacity=".55"/><line x1="{x}" y1="{y+34}" x2="{x}" y2="{y+90}" stroke="#fff" stroke-width="2" opacity=".4"/>')
        elif k < .7:
            p.append(f'<rect x="{x-22}" y="{y-22}" width="44" height="44" rx="8" fill="{r.choice(ACCENTS)}" opacity=".5" transform="rotate({r.randint(-15,15)} {x} {y})"/>')
        else:
            p.append(star(x, y, 26, "#F2A03D"))
    for _ in range(22):
        p.append(f'<circle cx="{r.randint(40,810)}" cy="{r.randint(60,1040)}" r="{r.randint(3,7)}" fill="#fff" opacity=".22"/>')
    p.append("</svg>")
    return "".join(p)


def main():
    IMG.mkdir(parents=True, exist_ok=True)
    acts = [yaml.safe_load(open(f, encoding="utf-8"))
            for f in sorted(glob.glob(str(ROOT / "data/activities/*.yaml")))]
    for a in acts:
        (IMG / f"{a['id']}.svg").write_text(hero_svg(a), encoding="utf-8")
    for rango in BAND_GRAD:
        (IMG / f"sep-{rango}.svg").write_text(divider_svg(rango), encoding="utf-8")
    (IMG / "portada.svg").write_text(portada_svg(), encoding="utf-8")
    print(f"Generadas {len(acts)} ilustraciones + {len(BAND_GRAD)} separadores + portada en {IMG}")


if __name__ == "__main__":
    main()
