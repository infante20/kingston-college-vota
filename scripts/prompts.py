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

# (re-disparo: regenerar 10 imágenes con FLUX tras recargar crédito en Together)

PALETA = "verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D"
CREMA = "#FBF7F0"

# Tamaños (múltiplos de 32, requisito de FLUX1.1-pro; alta resolución)
SIZE_ACT = (1440, 480)    # banner horizontal de actividad (1440/32=45, 480/32=15)
SIZE_PAGE = (1088, 1440)  # portada y separadores (1088/32=34, 1440/32=45)

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


# El TEMA va primero (los modelos priorizan el inicio del prompt); el estilo después.
def estilo(acento: str, orientacion: str) -> str:
    return (f"Estilo: ilustración plana (flat vector) de libro infantil, cálida, amigable "
            f"y moderna; formas redondeadas, sombras suaves, líneas limpias; fondo crema "
            f"{CREMA}, acento {acento}, paleta ({PALETA}); composición {orientacion}; "
            f"manos con cinco dedos. SIN texto, SIN letras, SIN carteles.")


def portada_prompt() -> str:
    return (f"Una familia (madre, padre y un niño pequeño) disfruta en casa SIN PANTALLAS: "
            f"leen un libro de papel y arman bloques de madera en el living, escena cálida "
            f"y luminosa. Nada de teléfonos, tablets, computadores ni televisores. Deja la "
            f"mitad superior despejada para sobreponer un título; predomina el verde. "
            f"{estilo('#2E7D5B', 'vertical (formato libro)')}")


def sep_prompt(rango: str) -> str:
    return (f"{SEP_ESCENA[rango].capitalize()}. Composición de página completa, con la "
            f"franja inferior más despejada para sobreponer el título del capítulo. "
            f"{estilo('#3E6E94', 'vertical (página completa)')}")


def activity_prompt(a: dict) -> str:
    acento = TIPO_ACENTO[a["tipo"]]
    subj = SUBJ[a["edad"]]
    gancho = (a.get("gancho") or "").strip()
    return (f"Escena protagonista: {subj} realizando la actividad «{a['titulo']}» — "
            f"{gancho} Muestra al niño EN ACCIÓN, en primer plano, con los materiales "
            f"caseros característicos de la actividad. "
            f"{estilo(acento, 'horizontal (banner apaisado)')}")


def all_targets() -> list[tuple[str, str, tuple[int, int]]]:
    """Devuelve [(stem, prompt, (w,h))] para portada, separadores y 48 actividades."""
    book = load_book()
    out: list[tuple[str, str, tuple[int, int]]] = [("portada", portada_prompt(), SIZE_PAGE)]
    for e in book["edades"]:
        out.append((f"sep-{e['rango']}", sep_prompt(e["rango"]), SIZE_PAGE))
    for a in load_activities():
        out.append((a["id"], activity_prompt(a), SIZE_ACT))
    return out
