#!/usr/bin/env python3
"""Lógica compartida de prompts de imagen e índice de recursos del libro.

Lo usan:
  - scripts/gen_canva_plan.py      (documento con los prompts para Canva)
  - scripts/gen_images_together.py (generación real vía API de Together AI)

Cada "target" es (stem, prompt, (ancho, alto)) y el archivo destino es
assets/images/<stem>.png, que el build prioriza sobre el SVG vectorial.
"""
from __future__ import annotations
import glob
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent

# (re-disparo del workflow de generación de imágenes tras configurar el secreto)

PALETA = "verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D"
CREMA = "#FBF7F0"

# Tamaños (múltiplos de 16, requisito de FLUX; dentro del límite de FLUX1.1-pro)
SIZE_ACT = (1440, 560)    # banner horizontal de actividad (alta resolución)
SIZE_PAGE = (1088, 1440)  # portada y separadores (vertical ~8.5x11, alta resolución)

TIPO_ACENTO = {
    "experimento": "#3E6E94", "sensorial": "#7E57A6", "recreativa": "#E8744F",
    "juego": "#2E7D5B", "emocional": "#D24D6E", "arte": "#F2A03D", "naturaleza": "#5B9E4A",
}
SUBJ = {
    "0-2": "un bebé o niño pequeño (0-2 años) acompañado por su madre o padre",
    "3-5": "un niño o niña en edad preescolar (3-5 años)",
    "6-8": "un niño o niña en edad escolar (6-8 años)",
    "9-12": "un preadolescente (9-12 años)",
}
SEP_ESCENA = {
    "0-2": "escena tierna y calmada: un bebé descubriendo el mundo con los sentidos, "
           "objetos blandos y formas suaves, ambiente acogedor de hogar",
    "3-5": "escena alegre y juguetona: niños pequeños jugando e imaginando, cajas de "
           "cartón, pinturas y formas divertidas",
    "6-8": "escena de creación y descubrimiento: niños construyendo, experimentando y "
           "jugando con proyectos hechos a mano",
    "9-12": "escena de trabajo en equipo y desafíos: preadolescentes colaborando, "
            "investigando y creando proyectos en conjunto",
}


def load_book() -> dict:
    return yaml.safe_load(open(ROOT / "data/book.yaml", encoding="utf-8"))


def load_activities() -> list[dict]:
    acts = [yaml.safe_load(open(f, encoding="utf-8"))
            for f in sorted(glob.glob(str(ROOT / "data/activities/*.yaml")))]
    acts.sort(key=lambda a: (a["edad"], a["orden"]))
    return acts


def estilo(acento: str, orientacion: str) -> str:
    return (f"Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y "
            f"moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. "
            f"Fondo crema {CREMA}, color de acento principal {acento}. Paleta cálida y "
            f"natural ({PALETA}). Composición {orientacion} con márgenes generosos. "
            f"Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, "
            f"SIN números, SIN logotipos.")


def portada_prompt() -> str:
    return (f"{estilo('#2E7D5B', 'vertical (formato libro)')} Escena de portada: una "
            f"familia disfrutando tiempo juntos en casa sin pantallas — jugando, leyendo "
            f"y creando. Ambiente hogareño cálido y luminoso, sensación de cercanía y "
            f"alegría. Deja espacio libre y despejado en el centro/parte superior para "
            f"sobreponer el título después. Predomina el verde de la paleta.")


def sep_prompt(rango: str) -> str:
    return (f"{estilo('#3E6E94', 'vertical (página completa)')} {SEP_ESCENA[rango]}. "
            f"Composición de página completa, decorativa, con espacio inferior más "
            f"despejado para sobreponer el título del capítulo.")


def activity_prompt(a: dict) -> str:
    acento = TIPO_ACENTO[a["tipo"]]
    subj = SUBJ[a["edad"]]
    gancho = (a.get("gancho") or "").strip()
    return (f"{estilo(acento, 'horizontal (banner apaisado)')} "
            f"Tema: {subj} realizando la actividad «{a['titulo']}». {gancho} "
            f"Muestra la acción de forma clara y simpática, con los materiales caseros "
            f"característicos de la actividad.")


def all_targets() -> list[tuple[str, str, tuple[int, int]]]:
    """Devuelve [(stem, prompt, (w,h))] para portada, separadores y 48 actividades."""
    book = load_book()
    out: list[tuple[str, str, tuple[int, int]]] = [("portada", portada_prompt(), SIZE_PAGE)]
    for e in book["edades"]:
        out.append((f"sep-{e['rango']}", sep_prompt(e["rango"]), SIZE_PAGE))
    for a in load_activities():
        out.append((a["id"], activity_prompt(a), SIZE_ACT))
    return out
