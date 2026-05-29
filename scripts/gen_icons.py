#!/usr/bin/env python3
"""Genera los iconos SVG (tipos de actividad + reloj) en assets/icons/.

Iconos planos, trazo de 'currentColor' para poder teñirlos por CSS.
Se ejecuta una sola vez (o cuando se quiera regenerar el set).
"""
from pathlib import Path

ICONS_DIR = Path(__file__).resolve().parent.parent / "assets" / "icons"

# Cada glifo es el contenido interno de un <svg viewBox="0 0 24 24">.
# Trazo redondeado, sin relleno, estilo "line icon" amigable.
GLYPHS = {
    # Matraz / experimento
    "experimento": """
      <path d="M9 3h6M10 3v6.2L5.4 17.3A2 2 0 0 0 7.1 20.4h9.8a2 2 0 0 0 1.7-3.1L14 9.2V3"/>
      <path d="M8.2 14h7.6"/>
      <circle cx="10.5" cy="16.3" r=".7" fill="currentColor" stroke="none"/>
      <circle cx="13.4" cy="17.4" r=".6" fill="currentColor" stroke="none"/>
    """,
    # Mano / sensorial
    "sensorial": """
      <path d="M7 11V6.5a1.4 1.4 0 0 1 2.8 0V10"/>
      <path d="M9.8 10V5.4a1.4 1.4 0 0 1 2.8 0V10"/>
      <path d="M12.6 10V6.2a1.4 1.4 0 0 1 2.8 0V11"/>
      <path d="M15.4 11V8.2a1.4 1.4 0 0 1 2.7 0v5.1a6 6 0 0 1-6 6.7H11a5.4 5.4 0 0 1-4-2.2L4.4 14a1.5 1.5 0 0 1 2.3-1.9L8 13.4"/>
    """,
    # Figura saltando / recreativa-motriz
    "recreativa": """
      <circle cx="13.5" cy="5.2" r="2"/>
      <path d="M13.2 8.2 9.6 11l2.4 2.6-1 5.4"/>
      <path d="M12 13.6 16 16l1.4 4"/>
      <path d="M9.6 11 5.5 10"/>
      <path d="M12 13.6 7.5 14.2"/>
    """,
    # Dado / juego
    "juego": """
      <rect x="4.5" y="4.5" width="15" height="15" rx="3"/>
      <circle cx="9" cy="9" r="1.1" fill="currentColor" stroke="none"/>
      <circle cx="15" cy="9" r="1.1" fill="currentColor" stroke="none"/>
      <circle cx="12" cy="12" r="1.1" fill="currentColor" stroke="none"/>
      <circle cx="9" cy="15" r="1.1" fill="currentColor" stroke="none"/>
      <circle cx="15" cy="15" r="1.1" fill="currentColor" stroke="none"/>
    """,
    # Corazón / conexión emocional
    "emocional": """
      <path d="M12 19.5 4.8 12.3a4.3 4.3 0 0 1 6-6.1l1.2 1.1 1.2-1.1a4.3 4.3 0 0 1 6 6.1z"/>
    """,
    # Paleta de pintor / arte
    "arte": """
      <path d="M12 3.5a8.5 8.5 0 1 0 0 17c1.5 0 2-1 2-2 0-1.4 1-2 2.2-2H18a2.7 2.7 0 0 0 2.7-2.7A8.7 8.7 0 0 0 12 3.5Z"/>
      <circle cx="8" cy="10" r="1.1" fill="currentColor" stroke="none"/>
      <circle cx="12" cy="7.6" r="1.1" fill="currentColor" stroke="none"/>
      <circle cx="15.6" cy="9.6" r="1.1" fill="currentColor" stroke="none"/>
    """,
    # Hoja / naturaleza
    "naturaleza": """
      <path d="M5 19c0-7 5-13 14-14 .5 6-2 14-10 14a4 4 0 0 1-4-4Z"/>
      <path d="M6.5 17.5C9 14 12.5 11.5 16 10"/>
    """,
    # Reloj / duración
    "reloj": """
      <circle cx="12" cy="12" r="8"/>
      <path d="M12 7.5V12l3 2"/>
    """,
}


def write_icon(name: str, inner: str) -> None:
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
        'fill="none" stroke="currentColor" stroke-width="1.7" '
        'stroke-linecap="round" stroke-linejoin="round">'
        f"{inner.strip()}</svg>"
    )
    (ICONS_DIR / f"{name}.svg").write_text(svg, encoding="utf-8")


def main() -> None:
    ICONS_DIR.mkdir(parents=True, exist_ok=True)
    for name, inner in GLYPHS.items():
        write_icon(name, inner)
    print(f"Generados {len(GLYPHS)} iconos en {ICONS_DIR}")


if __name__ == "__main__":
    main()
