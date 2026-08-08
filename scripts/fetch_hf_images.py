#!/usr/bin/env python3
"""Descarga las imágenes generadas en Higgsfield (URLs en assets/hf_urls.json) y
las guarda como assets/images/<stem>.jpg. Pensado para correr en un runner de
GitHub Actions (con internet), ya que el sandbox de la sesión no puede alcanzar
la CDN de Higgsfield.

Convierte a JPEG (más liviano y consistente con el resto) y elimina cualquier
archivo hermano del mismo stem con otra extensión.
"""
from __future__ import annotations
import json
import urllib.request
from io import BytesIO
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "images"
URLS = ROOT / "assets" / "hf_urls.json"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")


def main() -> int:
    urls = json.loads(URLS.read_text(encoding="utf-8"))
    IMG.mkdir(parents=True, exist_ok=True)
    ok = 0
    for stem, url in urls.items():
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
        img = Image.open(BytesIO(data)).convert("RGB")
        for ext in (".png", ".jpg", ".jpeg", ".webp"):
            p = IMG / f"{stem}{ext}"
            if p.exists():
                p.unlink()
        dest = IMG / f"{stem}.jpg"
        img.save(dest, "JPEG", quality=88)
        print(f"guardado {dest.name}  ({dest.stat().st_size // 1024} KB)")
        ok += 1
    print(f"Listo: {ok}/{len(urls)} imágenes descargadas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
