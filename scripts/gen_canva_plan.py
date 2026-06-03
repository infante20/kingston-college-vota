#!/usr/bin/env python3
"""Genera docs/canva-plan.md: guía de estilo + prompts de imagen para Canva.

Lee data/book.yaml y data/activities/*.yaml y produce un plan con:
  - especificaciones técnicas (tamaños, formato, nombre de archivo destino)
  - guía de estilo visual común
  - prompt de la portada
  - prompt de cada separador de edad
  - prompt de cada una de las 48 actividades (con su título ya neutralizado)

Los prompts están en español (Canva los entiende) y describen ilustraciones
planas tipo libro infantil, coherentes con la paleta del libro. Sin texto en
la imagen. Cada actividad indica el archivo destino assets/images/<id>.png, que
el build prioriza sobre el SVG vectorial.
"""
from __future__ import annotations
import glob
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent

PALETA = "verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D"
CREMA = "#FBF7F0"

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


def estilo(acento: str, orientacion: str) -> str:
    return (f"Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y "
            f"moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. "
            f"Fondo crema {CREMA}, color de acento principal {acento}. Paleta cálida y "
            f"natural ({PALETA}). Composición {orientacion} con márgenes generosos. "
            f"Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, "
            f"SIN números, SIN logotipos.")


def prompt_actividad(a: dict) -> str:
    acento = TIPO_ACENTO[a["tipo"]]
    subj = SUBJ[a["edad"]]
    gancho = (a.get("gancho") or "").strip()
    return (f"{estilo(acento, 'horizontal (banner apaisado)')} "
            f"Tema: {subj} realizando la actividad «{a['titulo']}». {gancho} "
            f"Muestra la acción de forma clara y simpática, con los materiales caseros "
            f"característicos de la actividad.")


def main():
    book = yaml.safe_load(open(ROOT / "data/book.yaml", encoding="utf-8"))
    tipos = book["tipos"]
    edades = book["edades"]
    acts = [yaml.safe_load(open(f, encoding="utf-8"))
            for f in sorted(glob.glob(str(ROOT / "data/activities/*.yaml")))]
    acts.sort(key=lambda a: (a["edad"], a["orden"]))

    L = []
    add = L.append
    add("# Plan de imágenes en Canva — *Tiempo de Calidad*\n")
    add("> Documento de trabajo. Cuando la sesión corra en un entorno con **red abierta** "
        "(o allowlist con `*.canva.com`) y el **conector de Canva activado**, se ejecuta "
        "este plan: por cada ítem se genera el diseño en Canva, se exporta a PNG y se "
        "descarga al **archivo destino** indicado. El build (`scripts/build.py`) ya "
        "prioriza los `.png` sobre los `.svg`, así que las imágenes de Canva reemplazan "
        "automáticamente a las ilustraciones vectoriales actuales.\n")

    add("## Especificaciones técnicas\n")
    add("| Recurso | Archivo destino | Tamaño sugerido | Orientación |")
    add("| --- | --- | --- | --- |")
    add("| Portada | `assets/images/portada.png` | 1700 × 2200 px | Vertical (8.5×11) |")
    for e in edades:
        add(f"| Separador {e['titulo']} | `assets/images/sep-{e['rango']}.png` | "
            f"1700 × 2200 px | Vertical (8.5×11) |")
    add("| Ilustración de actividad (×48) | `assets/images/<id>.png` | 1200 × 460 px | "
        "Horizontal (banner) |")
    add("\n**Formato de exportación:** PNG. **Sin texto en la imagen** (los títulos los "
        "pone la maquetación). Mantener coherencia de estilo y paleta entre todas.\n")

    add("## Guía de estilo visual (común a todo el libro)\n")
    add(f"- **Estilo:** ilustración plana (flat vector), tipo libro infantil; cálida, "
        f"amigable y moderna.")
    add(f"- **Paleta:** {PALETA}; fondo **crema {CREMA}**; tinta suave para detalles.")
    add(f"- **Acento por tipo de actividad:**")
    for k, v in tipos.items():
        add(f"  - {v['label']}: `{TIPO_ACENTO[k]}`")
    add("- **Personajes:** niñas y niños diversos e inclusivos, expresiones alegres y "
        "serenas; en 0-2 aparece la figura del cuidador.")
    add("- **Reglas:** formas redondeadas, sombras suaves, composición centrada con "
        "márgenes; **nada de texto, palabras, letras, números ni logos**.\n")

    add("---\n")
    add("## Portada\n")
    add(f"- **Archivo:** `assets/images/portada.png`")
    add(f"- **Prompt:**\n")
    add("```text")
    add(f"{estilo('#2E7D5B', 'vertical (formato libro)')} Escena de portada: una familia "
        f"disfrutando tiempo juntos en casa sin pantallas — jugando, leyendo y creando. "
        f"Ambiente hogareño cálido y luminoso, sensación de cercanía y alegría. Deja "
        f"espacio libre y despejado en el centro/parte superior para sobreponer el título "
        f"después. Predomina el verde de la paleta.")
    add("```\n")

    add("## Separadores de capítulo (uno por rango de edad)\n")
    for e in edades:
        acento = "#3E6E94"
        add(f"### {e['titulo']} — «{e['lema']}»")
        add(f"- **Archivo:** `assets/images/sep-{e['rango']}.png`")
        add("- **Prompt:**\n")
        add("```text")
        add(f"{estilo(acento, 'vertical (página completa)')} {SEP_ESCENA[e['rango']]}. "
            f"Composición de página completa, decorativa, con espacio inferior más "
            f"despejado para sobreponer el título del capítulo.")
        add("```\n")

    add("## Ilustraciones de actividades (48)\n")
    cur = None
    for a in acts:
        if a["edad"] != cur:
            cur = a["edad"]
            tit = next(e["titulo"] for e in edades if e["rango"] == cur)
            add(f"\n### {tit}\n")
        add(f"#### `{a['id']}` — {a['titulo']}  ·  *{tipos[a['tipo']]['label']}*")
        add(f"- **Archivo:** `assets/images/{a['id']}.png`")
        add("- **Prompt:**\n")
        add("```text")
        add(prompt_actividad(a))
        add("```\n")

    out = ROOT / "docs" / "canva-plan.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"Escrito {out} ({len(acts)} actividades + portada + {len(edades)} separadores)")


if __name__ == "__main__":
    main()
