#!/usr/bin/env python3
"""Genera las ilustraciones del libro como SVG (sin depender de la red).

Produce, en assets/images/:
  - <id>.svg        ilustración de cabecera por actividad (temática según su tipo)
  - sep-<rango>.svg  escena de separador por rango de edad
  - portada.svg      escena de portada

Las ilustraciones son vectoriales, planas y consistentes con la paleta del libro.
Puedes sustituir cualquier archivo por un PNG del mismo nombre (p. ej. <id>.png) y
el build lo usará en su lugar.
"""
from __future__ import annotations
import glob, hashlib, random
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "images"

# Paleta
PAL = {
    "verde":"#2E7D5B","azul":"#3E6E94","coral":"#E8744F","ambar":"#F2A03D",
    "morado":"#7E57A6","rosa":"#D24D6E","verde2":"#5B9E4A","crema":"#FBF7F0",
}
ACCENTS = ["#2E7D5B","#3E6E94","#E8744F","#F2A03D","#7E57A6","#D24D6E","#5B9E4A"]

TIPO_COLOR = {
    "experimento":"#3E6E94","sensorial":"#7E57A6","recreativa":"#E8744F",
    "juego":"#2E7D5B","emocional":"#D24D6E","arte":"#F2A03D","naturaleza":"#5B9E4A",
}

# Glifo central por tipo (contenido interno de un <svg viewBox 0 0 24 24>)
GLYPHS = {
    "experimento":'<path d="M9 3h6M10 3v6.2L5.4 17.3A2 2 0 0 0 7.1 20.4h9.8a2 2 0 0 0 1.7-3.1L14 9.2V3"/><path d="M8.2 14h7.6"/>',
    "sensorial":'<path d="M7 11V6.5a1.4 1.4 0 0 1 2.8 0V10"/><path d="M9.8 10V5.4a1.4 1.4 0 0 1 2.8 0V10"/><path d="M12.6 10V6.2a1.4 1.4 0 0 1 2.8 0V11"/><path d="M15.4 11V8.2a1.4 1.4 0 0 1 2.7 0v5.1a6 6 0 0 1-6 6.7H11a5.4 5.4 0 0 1-4-2.2L4.4 14a1.5 1.5 0 0 1 2.3-1.9L8 13.4"/>',
    "recreativa":'<circle cx="13.5" cy="5.2" r="2"/><path d="M13.2 8.2 9.6 11l2.4 2.6-1 5.4"/><path d="M12 13.6 16 16l1.4 4"/><path d="M9.6 11 5.5 10"/><path d="M12 13.6 7.5 14.2"/>',
    "juego":'<rect x="4.5" y="4.5" width="15" height="15" rx="3"/><circle cx="9" cy="9" r="1.1" fill="currentColor" stroke="none"/><circle cx="15" cy="9" r="1.1" fill="currentColor" stroke="none"/><circle cx="12" cy="12" r="1.1" fill="currentColor" stroke="none"/><circle cx="9" cy="15" r="1.1" fill="currentColor" stroke="none"/><circle cx="15" cy="15" r="1.1" fill="currentColor" stroke="none"/>',
    "emocional":'<path d="M12 19.5 4.8 12.3a4.3 4.3 0 0 1 6-6.1l1.2 1.1 1.2-1.1a4.3 4.3 0 0 1 6 6.1z"/>',
    "arte":'<path d="M12 3.5a8.5 8.5 0 1 0 0 17c1.5 0 2-1 2-2 0-1.4 1-2 2.2-2H18a2.7 2.7 0 0 0 2.7-2.7A8.7 8.7 0 0 0 12 3.5Z"/><circle cx="8" cy="10" r="1.1" fill="currentColor" stroke="none"/><circle cx="12" cy="7.6" r="1.1" fill="currentColor" stroke="none"/><circle cx="15.6" cy="9.6" r="1.1" fill="currentColor" stroke="none"/>',
    "naturaleza":'<path d="M5 19c0-7 5-13 14-14 .5 6-2 14-10 14a4 4 0 0 1-4-4Z"/><path d="M6.5 17.5C9 14 12.5 11.5 16 10"/>',
}


def _h2(s): return tuple(int(s[i:i+2],16) for i in (1,3,5))
def _2h(t): return "#%02x%02x%02x" % t
def mix(c1,c2,t):
    a,b=_h2(c1),_h2(c2); return _2h(tuple(round(a[i]+(b[i]-a[i])*t) for i in range(3)))
def tint(c,t): return mix(c,"#ffffff",t)
def shade(c,t): return mix(c,"#000000",t)


def rng_for(seed:str)->random.Random:
    return random.Random(int(hashlib.md5(seed.encode()).hexdigest(),16))


def decor_for_tipo(tipo:str, color:str, r:random.Random)->str:
    """Elementos decorativos dispersos propios de cada tipo."""
    out=[]
    pts=[(190,120),(1010,150),(250,330),(980,330),(130,230),(1060,250)]
    r.shuffle(pts)
    if tipo=="experimento":           # burbujas
        for (x,y) in pts[:5]:
            rad=r.randint(10,26); out.append(f'<circle cx="{x}" cy="{y}" r="{rad}" fill="{tint(color,.4)}" opacity=".75"/>')
            out.append(f'<circle cx="{x-rad*.35:.0f}" cy="{y-rad*.35:.0f}" r="{rad*.3:.0f}" fill="#fff" opacity=".6"/>')
    elif tipo=="sensorial":           # ondas
        for (x,y) in pts[:4]:
            out.append(f'<path d="M{x-34} {y}q17 -16 34 0 17 16 34 0" stroke="{tint(color,.35)}" stroke-width="6" fill="none" stroke-linecap="round"/>')
    elif tipo=="recreativa":          # estrellas de movimiento
        for (x,y) in pts[:5]:
            out.append(star(x,y,r.randint(12,20),tint(color,.3)))
    elif tipo=="juego":               # bloques
        for (x,y) in pts[:5]:
            s=r.randint(20,34); out.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="6" fill="{tint(color,.35)}" transform="rotate({r.randint(-18,18)} {x} {y})"/>')
    elif tipo=="emocional":           # corazones
        for (x,y) in pts[:5]: out.append(heart(x,y,r.randint(16,26),tint(color,.3)))
    elif tipo=="arte":                # manchas de color
        for (x,y) in pts[:6]:
            out.append(f'<circle cx="{x}" cy="{y}" r="{r.randint(10,20)}" fill="{r.choice(ACCENTS)}" opacity=".55"/>')
    else:                              # naturaleza: hojas/árboles
        for (x,y) in pts[:5]:
            out.append(f'<path d="M{x} {y+22}q-22 -10 -16 -34 24 -2 16 34z" fill="{tint(color,.3)}"/>')
    # confeti
    for _ in range(10):
        out.append(f'<circle cx="{r.randint(60,1140)}" cy="{r.randint(40,420)}" r="{r.randint(3,7)}" fill="{r.choice(ACCENTS)}" opacity=".5"/>')
    return "".join(out)


def star(cx,cy,rad,fill):
    import math
    pts=[]
    for i in range(10):
        ang=-math.pi/2+i*math.pi/5; rr=rad if i%2==0 else rad*.45
        pts.append(f"{cx+rr*math.cos(ang):.1f},{cy+rr*math.sin(ang):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"/>'

def heart(cx,cy,s,fill):
    return f'<path transform="translate({cx-s} {cy-s*0.9}) scale({s/12})" d="M12 19.5 4.8 12.3a4.3 4.3 0 0 1 6-6.1l1.2 1.1 1.2-1.1a4.3 4.3 0 0 1 6 6.1z" fill="{fill}"/>'


def hero_svg(act:dict)->str:
    tipo=act["tipo"]; color=TIPO_COLOR[tipo]; r=rng_for(act["id"])
    W,H=1200,460
    cx=r.choice([430,600,770]); cy=235
    bg=tint(color,.88); hill=tint(color,.62); ring=tint(color,.5)
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">']
    parts.append(f'<rect width="{W}" height="{H}" rx="0" fill="{bg}"/>')
    # blobs grandes
    parts.append(f'<circle cx="{r.randint(120,260)}" cy="{r.randint(60,140)}" r="{r.randint(80,130)}" fill="{tint(color,.74)}"/>')
    parts.append(f'<circle cx="{r.randint(950,1120)}" cy="{r.randint(300,420)}" r="{r.randint(90,150)}" fill="{tint(color,.78)}"/>')
    # colina inferior
    parts.append(f'<path d="M0 {H} L0 360 Q {W/2} 300 {W} 360 L{W} {H} Z" fill="{hill}"/>')
    # decoración por tipo
    parts.append(decor_for_tipo(tipo,color,r))
    # motivo central: círculo blanco + glifo del tipo
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="118" fill="{ring}"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="100" fill="#fff"/>')
    s=7.4; sw=f"{7.5/s:.2f}"
    parts.append(f'<g transform="translate({cx-12*s:.1f} {cy-12*s:.1f}) scale({s})" '
                 f'fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" '
                 f'stroke-linejoin="round" color="{color}">{GLYPHS[tipo]}</g>')
    parts.append("</svg>")
    return "".join(parts)


BAND_GRAD = {
    "0-2":("#6FB3A0","#3E6E94"),
    "3-5":("#F4A94A","#E8744F"),
    "6-8":("#6BB05A","#2E7D5B"),
    "9-12":("#4E7CA8","#7E57A6"),
}

def divider_svg(rango:str)->str:
    c1,c2=BAND_GRAD[rango]; r=rng_for("sep-"+rango)
    W,H=850,1100
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">']
    p.append(f'<defs><linearGradient id="g" x1="0" y1="0" x2="0.5" y2="1">'
             f'<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>')
    p.append(f'<rect width="{W}" height="{H}" fill="url(#g)"/>')
    # sol/luna
    p.append(f'<circle cx="650" cy="230" r="120" fill="#fff" opacity=".22"/>')
    p.append(f'<circle cx="650" cy="230" r="78" fill="#fff" opacity=".30"/>')
    # colinas
    p.append(f'<path d="M0 760 Q 250 640 480 740 T 850 720 L850 1100 L0 1100Z" fill="#fff" opacity=".14"/>')
    p.append(f'<path d="M0 880 Q 300 780 560 860 T 850 840 L850 1100 L0 1100Z" fill="#fff" opacity=".12"/>')
    # estrellas/puntos
    for _ in range(26):
        x,y=r.randint(40,810),r.randint(40,680)
        p.append(star(x,y,r.randint(6,14),"#ffffff") if r.random()<.5
                 else f'<circle cx="{x}" cy="{y}" r="{r.randint(3,7)}" fill="#fff" opacity=".5"/>')
    # scrim inferior para legibilidad del texto
    p.append(f'<rect x="0" y="820" width="{W}" height="280" fill="#000" opacity=".18"/>')
    p.append("</svg>")
    return "".join(p)


def portada_svg()->str:
    r=rng_for("portada"); W,H=850,1100
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">']
    p.append('<defs><linearGradient id="cg" x1="0" y1="0" x2="0.3" y2="1">'
             '<stop offset="0" stop-color="#3a936b"/><stop offset=".55" stop-color="#2E7D5B"/>'
             '<stop offset="1" stop-color="#245d44"/></linearGradient></defs>')
    p.append(f'<rect width="{W}" height="{H}" fill="url(#cg)"/>')
    # sol arriba derecha
    p.append('<circle cx="700" cy="170" r="90" fill="#F2A03D" opacity=".85"/>')
    # casa simple (abajo izquierda)
    p.append('<g opacity=".9"><rect x="90" y="900" width="160" height="120" rx="6" fill="#FBF7F0" opacity=".25"/>'
             '<path d="M80 905 L170 840 L260 905 Z" fill="#E8744F" opacity=".6"/></g>')
    # árbol (abajo derecha)
    p.append('<g opacity=".85"><rect x="690" y="940" width="20" height="80" rx="6" fill="#FBF7F0" opacity=".3"/>'
             '<circle cx="700" cy="920" r="55" fill="#5B9E4A" opacity=".55"/></g>')
    # globos / bloques decorativos repartidos en bordes
    spots=[(140,300),(720,520),(150,560),(700,760),(120,760)]
    for (x,y) in spots:
        kind=r.random()
        if kind<.4:  # globo
            p.append(f'<circle cx="{x}" cy="{y}" r="34" fill="{r.choice(ACCENTS)}" opacity=".55"/>'
                     f'<line x1="{x}" y1="{y+34}" x2="{x}" y2="{y+90}" stroke="#fff" stroke-width="2" opacity=".4"/>')
        elif kind<.7:  # bloque
            p.append(f'<rect x="{x-22}" y="{y-22}" width="44" height="44" rx="8" fill="{r.choice(ACCENTS)}" opacity=".5" transform="rotate({r.randint(-15,15)} {x} {y})"/>')
        else:  # estrella
            p.append(star(x,y,26,"#F2A03D"))
    # confeti
    for _ in range(22):
        p.append(f'<circle cx="{r.randint(40,810)}" cy="{r.randint(60,1040)}" r="{r.randint(3,7)}" fill="#fff" opacity=".25"/>')
    p.append("</svg>")
    return "".join(p)


def main():
    IMG.mkdir(parents=True, exist_ok=True)
    acts=[yaml.safe_load(open(f,encoding="utf-8")) for f in sorted(glob.glob(str(ROOT/"data/activities/*.yaml")))]
    for a in acts:
        (IMG/f"{a['id']}.svg").write_text(hero_svg(a),encoding="utf-8")
    for rango in BAND_GRAD:
        (IMG/f"sep-{rango}.svg").write_text(divider_svg(rango),encoding="utf-8")
    (IMG/"portada.svg").write_text(portada_svg(),encoding="utf-8")
    print(f"Generadas {len(acts)} ilustraciones + {len(BAND_GRAD)} separadores + portada en {IMG}")


if __name__=="__main__":
    main()
