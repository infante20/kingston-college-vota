#!/usr/bin/env python3
"""Construye la SERIE por edad: un libro independiente por cada rango
(0-2, 3-5, 6-8, 9-12) más el tomo completo. Cada uno genera PDF a color, EPUB,
versión B/N y versión KDP con sangrado.

Uso:  python scripts/build_series.py
Salidas en dist/:
  Tiempo-de-Calidad-0-2.pdf / .epub / -0-2-BN.pdf / -0-2-KDP.pdf / -0-2-KDP-BN.pdf
  ... (igual para 3-5, 6-8, 9-12) ...
  Tiempo-de-Calidad.pdf (tomo completo) y sus variantes
"""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANDS = ["0-2", "3-5", "6-8", "9-12"]


def run(args):
    print(f"\n=== build {' '.join(args) or '(completo)'} ===")
    subprocess.run([sys.executable, str(ROOT / "scripts/build.py"), *args], check=True)


def main():
    for b in BANDS:
        run([f"--edad={b}", "--bw", "--kdp"])
    run(["--bw", "--kdp"])  # tomo completo
    print("\nSerie completa generada en dist/")


if __name__ == "__main__":
    main()
