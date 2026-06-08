#!/usr/bin/env python3
"""Genera TODAS las imágenes de cada actividad con Together AI (FLUX.1):
hero (<id>.png), materiales (<id>-mat.png) y 3 viñetas de pasos (<id>-s1..3.png).

Los prompts (en inglés, para evitar texto incrustado) viven en
scripts/img_prompts.py -> PROMPTS[id] = {accent, hero, mat, steps[3]}.
La API key se lee de TOGETHER_API_KEY o de /tmp/together.key.

Uso:
    python scripts/gen_images.py                 # genera lo que falte (todas)
    python scripts/gen_images.py 0a2             # solo ids que empiezan con 0a2
    python scripts/gen_images.py 0a2-13 6a8-10   # ids exactos
    python scripts/gen_images.py 0a2 --kinds mat,steps   # solo esos tipos
    python scripts/gen_images.py 0a2 --force     # regenera aunque existan
"""
from __future__ import annotations
import os, sys, time, json, io, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "images"
API = "https://api.together.xyz/v1/images/generations"
MODEL = "black-forest-labs/FLUX.1-schnell"
UA = "curl/8.0"

sys.path.insert(0, str(ROOT / "scripts"))
from img_prompts import PROMPTS  # noqa: E402

SUBJ = {
    "0a2": "a baby or toddler around one year old together with a parent",
    "3a5": "a preschool child around four years old",
    "6a8": "a school-age child around seven years old",
    "9a12": "a preteen child around ten years old",
}

STYLE = ("Flat vector illustration in a warm, modern children's book style. "
         "Simple rounded shapes, soft shadows, clean lines. Cream background #FBF7F0, "
         "accent color {accent}, warm natural palette of green #2E7D5B, blue #3E6E94, "
         "coral #E8744F and amber #F2A03D. Inclusive and diverse, tender and safe. "
         "A picture only, with absolutely no text, no words, no letters, no numbers, "
         "no captions, no labels and no signage anywhere. ")

HERO_TMPL = STYLE + ("Cozy home setting. Centered vertical composition with generous "
                     "margins. Scene: {subj} {scene}.")
MAT_TMPL = STYLE + ("Neat flat-lay seen from directly above of craft and play materials "
                    "arranged tidily on a light wooden table, no people: {scene}.")
STEP_TMPL = STYLE + ("Square close-up vignette, soft and simple. Scene: {scene}.")

def key() -> str:
    k = os.environ.get("TOGETHER_API_KEY")
    if not k and Path("/tmp/together.key").exists():
        k = Path("/tmp/together.key").read_text().strip()
    if not k:
        sys.exit("Falta TOGETHER_API_KEY (o /tmp/together.key)")
    return k

def generate(prompt: str, k: str) -> bytes:
    body = json.dumps({"model": MODEL, "prompt": prompt,
                       "width": 1024, "height": 1024, "steps": 4, "n": 1}).encode()
    req = urllib.request.Request(API, data=body, headers={
        "Authorization": f"Bearer {k}", "Content-Type": "application/json", "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        url = json.load(r)["data"][0]["url"]
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=120) as r:
        return r.read()

def jobs(ids):
    """Genera la lista de (archivo, prompt) a producir para los ids dados."""
    for id_ in ids:
        p = PROMPTS[id_]
        grp = id_.rsplit("-", 1)[0]
        subj = SUBJ[grp]
        acc = p["accent"]
        if "hero" in p:
            yield (f"{id_}.png", "hero", HERO_TMPL.format(accent=acc, subj=subj, scene=p["hero"]))
        if "mat" in p:
            yield (f"{id_}-mat.png", "mat", MAT_TMPL.format(accent=acc, scene=p["mat"]))
        for n, st in enumerate(p.get("steps", []), 1):
            yield (f"{id_}-s{n}.png", "steps", STEP_TMPL.format(accent=acc, scene=st))

def main() -> None:
    from PIL import Image
    k = key(); OUT.mkdir(parents=True, exist_ok=True)
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    kinds = None
    for a in sys.argv:
        if a.startswith("--kinds"):
            kinds = set(sys.argv[sys.argv.index(a) + 1].split(",")) if a == "--kinds" else set(a.split("=", 1)[1].split(","))
    ids = [i for i in PROMPTS if (not args or any(i == a or i.startswith(a) for a in args))]
    ids.sort()
    todo = [(f, kind, pr) for i in ids for (f, kind, pr) in jobs([i]) if (kinds is None or kind in kinds)]
    pending = [t for t in todo if force or not (OUT / t[0]).exists()]
    print(f"{len(ids)} actividades · {len(todo)} imágenes · {len(pending)} por generar", flush=True)
    ok = 0
    for j, (fname, kind, prompt) in enumerate(pending, 1):
        for attempt in range(8):
            try:
                data = generate(prompt, k)
                Image.open(io.BytesIO(data)).convert("RGB").save(OUT / fname)
                ok += 1; print(f"[{j}/{len(pending)}] {fname} OK", flush=True); break
            except urllib.error.HTTPError as e:
                wait = min(60, 6 * 2 ** attempt) if e.code == 429 else 2 ** attempt
                print(f"[{j}/{len(pending)}] {fname} HTTP {e.code}; retry {wait}s", flush=True); time.sleep(wait)
            except Exception as e:
                print(f"[{j}/{len(pending)}] {fname} err {e}; retry", flush=True); time.sleep(2 ** attempt)
        else:
            print(f"[{j}/{len(pending)}] {fname} FALLÓ", flush=True)
        time.sleep(1.5)
    print(f"\nListas {ok}/{len(pending)}", flush=True)

if __name__ == "__main__":
    main()
