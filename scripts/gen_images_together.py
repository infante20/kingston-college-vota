#!/usr/bin/env python3
"""Genera las imágenes del libro con la API de Together AI (modelos FLUX).

Lee los prompts desde scripts/prompts.py y, por cada recurso (portada, 4
separadores y 48 actividades), llama a la API de imágenes de Together pidiendo el
resultado en base64 (response_format=b64_json) — así se reciben los bytes por
`api.together.xyz` y no se depende de ninguna CDN externa (que el proxy podría
bloquear). Cada imagen se guarda en assets/images/<stem>.png, que el build
prioriza sobre el SVG vectorial.

Requisitos:
  - Entorno con acceso de red a `api.together.xyz` (política Completa o Custom).
  - Variable de entorno TOGETHER_API_KEY (o pasar --key).

Uso:
  python scripts/gen_images_together.py                 # genera lo que falte
  python scripts/gen_images_together.py --force         # regenera todo
  python scripts/gen_images_together.py --only portada,sep-0-2,0a2-01
  python scripts/gen_images_together.py --limit 3       # prueba con 3
  python scripts/gen_images_together.py --build         # reconstruye al terminar
"""
from __future__ import annotations
import argparse, base64, json, os, sys, time, urllib.error, urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prompts  # noqa: E402

ROOT = prompts.ROOT
IMG = ROOT / "assets" / "images"
API_URL = "https://api.together.xyz/v1/images/generations"
# Altísima calidad por defecto. Alternativas: black-forest-labs/FLUX.1-dev (alta
# calidad, más barato) o black-forest-labs/FLUX.1-schnell (rápido y económico).
DEFAULT_MODEL = "black-forest-labs/FLUX.1.1-pro"


def generate_one(key: str, model: str, prompt: str, w: int, h: int,
                 steps: int, retries: int = 5) -> bytes:
    payload = {
        "model": model, "prompt": prompt, "width": w, "height": h,
        "n": 1, "response_format": "b64_json",
    }
    # 'steps' solo aplica a modelos abiertos; los endpoints "pro" lo rechazan.
    if "pro" not in model:
        payload["steps"] = min(steps, 4) if "schnell" in model else steps
    body = json.dumps(payload).encode()
    delay = 3.0
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(
            API_URL, data=body,
            headers={"Authorization": f"Bearer {key}",
                     "Content-Type": "application/json"},
            method="POST")
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                data = json.loads(r.read())
            item = data["data"][0]
            if item.get("b64_json"):
                return base64.b64decode(item["b64_json"])
            # fallback si devolviera URL (mismo host permitido)
            if item.get("url"):
                with urllib.request.urlopen(item["url"], timeout=180) as ir:
                    return ir.read()
            raise RuntimeError(f"respuesta sin imagen: {item.keys()}")
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace")[:300]
            if e.code in (429, 500, 502, 503, 504) and attempt < retries:
                print(f"    HTTP {e.code} (intento {attempt}); reintento en {delay:.0f}s… {msg[:120]}")
                time.sleep(delay); delay *= 2; continue
            raise RuntimeError(f"HTTP {e.code}: {msg}") from None
        except urllib.error.URLError as e:
            if attempt < retries:
                print(f"    red {e.reason} (intento {attempt}); reintento en {delay:.0f}s…")
                time.sleep(delay); delay *= 2; continue
            raise
    raise RuntimeError("agotados los reintentos")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", default=os.environ.get("TOGETHER_API_KEY", ""))
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--steps", type=int, default=28,
                    help="pasos de difusión (solo modelos dev/schnell; 'pro' lo ignora)")
    ap.add_argument("--force", action="store_true", help="regenerar aunque exista el PNG")
    ap.add_argument("--only", default="", help="lista de stems separados por coma")
    ap.add_argument("--limit", type=int, default=0, help="máximo de imágenes a generar")
    ap.add_argument("--delay", type=float, default=1.0, help="pausa entre llamadas (s)")
    ap.add_argument("--build", action="store_true", help="ejecutar scripts/build.py al final")
    args = ap.parse_args()

    if not args.key:
        print("ERROR: falta TOGETHER_API_KEY (usa la variable de entorno o --key).")
        return 2

    IMG.mkdir(parents=True, exist_ok=True)
    targets = prompts.all_targets()
    if args.only:
        want = {s.strip() for s in args.only.split(",") if s.strip()}
        targets = [t for t in targets if t[0] in want]

    todo = [t for t in targets if args.force or not (IMG / f"{t[0]}.png").exists()]
    if args.limit:
        todo = todo[:args.limit]

    print(f"Modelo: {args.model} | a generar: {len(todo)}/{len(targets)} "
          f"(omitidas {len(targets)-len(todo)} ya existentes)")
    ok = fail = 0
    for i, (stem, prompt, (w, h)) in enumerate(todo, 1):
        dest = IMG / f"{stem}.png"
        print(f"[{i}/{len(todo)}] {stem}  ({w}x{h})")
        try:
            png = generate_one(args.key, args.model, prompt, w, h, args.steps)
            dest.write_bytes(png)
            print(f"    -> {dest}  ({len(png)//1024} KB)")
            ok += 1
        except Exception as e:
            print(f"    FALLO: {e}")
            fail += 1
        if i < len(todo) and args.delay:
            time.sleep(args.delay)

    print(f"\nListo: {ok} generadas, {fail} fallidas.")
    if args.build and ok:
        print("Reconstruyendo el libro…")
        os.system(f"cd {ROOT} && python3 scripts/build.py")
    elif ok:
        print("Ahora ejecuta: python3 scripts/build.py")
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
