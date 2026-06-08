#!/usr/bin/env python3
"""Genera las ilustraciones de actividad con Together AI (FLUX.1) y las guarda en
assets/images/<id>.png. La API key se lee de la variable de entorno
TOGETHER_API_KEY o del archivo /tmp/together.key (NO se commitea ninguna key).

Uso:
    python scripts/gen_flux.py            # genera las que falten
    python scripts/gen_flux.py --force    # regenera todas
    python scripts/gen_flux.py 0a2-01 6a8-03   # solo esos ids
"""
from __future__ import annotations
import os, sys, time, json, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "images"
API = "https://api.together.xyz/v1/images/generations"
MODEL = "black-forest-labs/FLUX.1-schnell"

def key() -> str:
    k = os.environ.get("TOGETHER_API_KEY")
    if not k:
        f = Path("/tmp/together.key")
        if f.exists():
            k = f.read_text().strip()
    if not k:
        sys.exit("Falta TOGETHER_API_KEY (o /tmp/together.key)")
    return k

# Color de acento por tipo
EXP, SEN, REC, JUE, EMO, ART, NAT = (
    "#3E6E94", "#7E57A6", "#E8744F", "#2E7D5B", "#D24D6E", "#F2A03D", "#5B9E4A")

# Sujeto por rango de edad
SUBJ = {
    "0a2": "a baby or toddler around one year old together with a parent",
    "3a5": "a preschool child around four years old",
    "6a8": "a school-age child around seven years old",
    "9a12": "a preteen child around ten years old",
}

# (id, accent, escena en inglés SIN nombrar la actividad para evitar texto)
ITEMS = [
    # 0 a 2
    ("0a2-01", SEN, "exploring a woven basket filled with everyday wooden spoons, fabric scraps and natural objects; the baby reaches in with curiosity"),
    ("0a2-02", SEN, "blowing soft soap bubbles that float and shimmer while the baby reaches up to touch them, delighted"),
    ("0a2-03", SEN, "gazing at a clear sensory bottle filled with water, glitter and floating shapes, calm and mesmerized, the parent holding it"),
    ("0a2-04", SEN, "splashing and pouring water between cups and small containers with a spoon, having fun"),
    ("0a2-05", SEN, "touching a soft patchwork blanket made of many different fabric textures"),
    ("0a2-06", EMO, "playing peekaboo, the parent hiding and reappearing behind their hands while the baby giggles"),
    ("0a2-07", EMO, "in front of a mirror making happy faces and discovering their own reflection together"),
    ("0a2-08", REC, "making music with pots, wooden spoons and tins used as drums, joyful and lively"),
    ("0a2-09", REC, "crawling and climbing over a soft course of cushions and blankets, the parent encouraging"),
    ("0a2-10", JUE, "stacking cups and boxes into a little tower and knocking it down, laughing together"),
    ("0a2-11", ART, "finger painting with colorful yogurt on a tray, messy hands and a big happy smile"),
    ("0a2-12", JUE, "putting objects into a box and taking them out again, delighted by the surprise"),
    # 3 a 5
    ("3a5-01", EXP, "watching a homemade volcano erupt with colorful foam on a tray, amazed"),
    ("3a5-02", EXP, "watching drops of food coloring swirl and spread across a plate of milk, fascinated"),
    ("3a5-03", SEN, "kneading and shaping soft homemade dough with their hands at a table"),
    ("3a5-04", SEN, "reaching a hand into a closed mystery box to guess a hidden object only by touch, curious"),
    ("3a5-05", REC, "jumping and balancing across an obstacle course built from cushions and blankets in the living room"),
    ("3a5-06", REC, "rolling a soft ball to knock down a set of plastic bottles arranged like bowling pins"),
    ("3a5-07", JUE, "playing pretend shop with cardboard coins and little boxes of goods on a small counter"),
    ("3a5-08", JUE, "running around the home collecting objects of every color into a rainbow basket"),
    ("3a5-09", EMO, "drawing simple round faces showing happy, angry and sad feelings on paper"),
    ("3a5-10", ART, "stamping colorful shapes onto paper using stamps cut from potatoes and vegetables"),
    ("3a5-11", ART, "gluing leaves, petals and little twigs onto paper to make a nature collage"),
    ("3a5-12", NAT, "outdoors with a cardboard magnifying glass discovering little bugs in the garden"),
    # 6 a 8
    ("6a8-01", EXP, "stacking honey, water and oil in colored layers inside a clear glass and watching them separate, amazed"),
    ("6a8-02", EXP, "launching a balloon rocket sliding along a long string across the room, excited"),
    ("6a8-03", ART, "making a small colorful salt mandala, coloring salt with chalk in little bowls"),
    ("6a8-04", SEN, "reaching into a closed mystery box to guess a hidden object by touch"),
    ("6a8-05", REC, "moving through a homemade obstacle course of jumps, tunnels and balance beams indoors"),
    ("6a8-06", REC, "bowling with plastic bottles as pins, rolling a ball to knock them all down"),
    ("6a8-07", JUE, "drawing their own board game with a winding path on cardboard, with dice and tokens"),
    ("6a8-08", JUE, "following a trail of clue cards around the house to find a hidden treasure box"),
    ("6a8-09", EMO, "holding a calm-down glitter jar and watching the glitter swirl slowly, peaceful"),
    ("6a8-10", ART, "performing a puppet show with handmade cardboard puppets behind a little stage"),
    ("6a8-11", NAT, "outdoors with a magnifying glass and a notebook exploring nature and sketching findings"),
    ("6a8-12", EXP, "rubbing a balloon on their hair and using static to lift small paper bits, surprised"),
    # 9 a 12
    ("9a12-01", EXP, "doing marker chromatography, watching ink colors separate upward on a wet paper strip, curious"),
    ("9a12-02", EXP, "building a homemade water clock from bottles, watching water drip to measure time"),
    ("9a12-03", JUE, "writing secret coded messages with a homemade paper cipher wheel at a desk"),
    ("9a12-04", JUE, "setting up a homemade escape room with puzzles and small locked boxes for the family"),
    ("9a12-05", JUE, "designing a strategy board game from scratch with a board, pieces and rules"),
    ("9a12-06", REC, "moving through a challenging balance and obstacle course in the yard or hallway"),
    ("9a12-07", REC, "making juggling balls and learning to juggle three of them in the air"),
    ("9a12-08", EMO, "placing letters and small keepsakes into a time capsule box to open in a year, thoughtful"),
    ("9a12-09", EMO, "a family pulling folded question slips from a jar and talking warmly together on the sofa"),
    ("9a12-10", ART, "drawing a comic page with empty panels and blank speech balloons, inventing a hero character"),
    ("9a12-11", ART, "flipping a hand-drawn flipbook at the corner of a notebook, the little drawings coming to life"),
    ("9a12-12", NAT, "planting and watering small herb seedlings in little pots and watching them grow"),
]

TMPL = ("Flat vector illustration in a warm, modern children's book style. "
        "Simple rounded shapes, soft shadows, clean lines. Cream background #FBF7F0, "
        "accent color {accent}, warm natural palette of green #2E7D5B, blue #3E6E94, "
        "coral #E8744F and amber #F2A03D. Cozy home setting, inclusive and diverse, "
        "tender and safe. Centered vertical composition with generous margins. "
        "A picture only, with absolutely no text, no words, no letters, no numbers, "
        "no captions, no labels and no signage anywhere. Scene: {subj} {scene}.")

UA = "curl/8.0"  # el WAF de Together bloquea el User-Agent de urllib

def generate(prompt: str, k: str) -> bytes:
    body = json.dumps({"model": MODEL, "prompt": prompt,
                       "width": 1024, "height": 1024, "steps": 4, "n": 1}).encode()
    req = urllib.request.Request(API, data=body, headers={
        "Authorization": f"Bearer {k}", "Content-Type": "application/json",
        "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        url = json.load(r)["data"][0]["url"]
    dl = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(dl, timeout=120) as r:
        return r.read()

def main() -> None:
    k = key()
    OUT.mkdir(parents=True, exist_ok=True)
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    todo = [it for it in ITEMS if (not args or it[0] in args)]
    from PIL import Image
    import io
    ok = 0
    for i, (id_, accent, scene) in enumerate(todo, 1):
        dst = OUT / f"{id_}.png"
        if dst.exists() and not force:
            print(f"[{i}/{len(todo)}] {id_} ya existe, salto"); ok += 1; continue
        subj = SUBJ[id_.rsplit("-", 1)[0]]
        prompt = TMPL.format(accent=accent, subj=subj, scene=scene)
        import urllib.error
        for attempt in range(8):
            try:
                data = generate(prompt, k)
                Image.open(io.BytesIO(data)).convert("RGB").save(dst)
                print(f"[{i}/{len(todo)}] {id_} OK -> {dst.name}", flush=True); ok += 1
                break
            except urllib.error.HTTPError as e:
                wait = min(60, 6 * 2 ** attempt) if e.code == 429 else 2 ** attempt
                print(f"[{i}/{len(todo)}] {id_} HTTP {e.code}; reintento en {wait}s", flush=True)
                time.sleep(wait)
            except Exception as e:
                wait = 2 ** attempt
                print(f"[{i}/{len(todo)}] {id_} error ({e}); reintento en {wait}s", flush=True)
                time.sleep(wait)
        else:
            print(f"[{i}/{len(todo)}] {id_} FALLÓ tras 8 intentos", flush=True)
        time.sleep(3)
    print(f"\nListas: {ok}/{len(todo)}")

if __name__ == "__main__":
    main()
