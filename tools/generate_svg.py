import math
import os

OUTPUT_DIR = r"c:\Users\goran\AppData\Local\Temp"

def latlon_to_svg(lat, lon, lat_min, lat_max, lon_min, lon_max, w, h, pad):
    cos_lat = math.cos(math.radians((lat_min + lat_max) / 2))
    lon_range_km = (lon_max - lon_min) * 111.32 * cos_lat
    lat_range_km = (lat_max - lat_min) * 111.32
    scale = min((w - 2 * pad) / lon_range_km, (h - 2 * pad) / lat_range_km)
    x = pad + (lon - lon_min) * 111.32 * cos_lat * scale
    y = (h - pad) - (lat - lat_min) * 111.32 * scale
    return x, y

def make_svg(title, points, segments, w=820, h=520, pad=70):
    lats = [p["lat"] for p in points.values()]
    lons = [p["lon"] for p in points.values()]
    lat_min, lat_max = min(lats), max(lats)
    lon_min, lon_max = min(lons), max(lons)
    margin = 0.15
    lat_pad = (lat_max - lat_min) * margin
    lon_pad = (lon_max - lon_min) * margin
    lat_min -= lat_pad; lat_max += lat_pad
    lon_min -= lon_pad; lon_max += lon_pad

    coords = {
        name: latlon_to_svg(p["lat"], p["lon"], lat_min, lat_max, lon_min, lon_max, w, h, pad)
        for name, p in points.items()
    }

    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
                 f'style="background:#f8f5f0;font-family:sans-serif">')
    lines.append(f'  <text x="{w//2}" y="28" text-anchor="middle" '
                 f'font-size="16" font-weight="bold" fill="#333">{title}</text>')

    # Segments
    for a, b, groups in segments:
        x1, y1 = coords[a]
        x2, y2 = coords[b]
        lines.append(f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                     f'stroke="#7a9cbf" stroke-width="2" stroke-opacity="0.8"/>')

    # Points
    for name, (x, y) in coords.items():
        is_start = points[name].get("start", False)
        color = "#e05c2a" if is_start else "#2a6ee0"
        r = 7 if is_start else 6
        lines.append(f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}" stroke="white" stroke-width="1.5"/>')

    # Labels
    for name, (x, y) in coords.items():
        dx, dy = points[name].get("label_off", (0, -12))
        lines.append(f'  <text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="middle" '
                     f'font-size="11" font-weight="bold" fill="#222">{name}</text>')

    lines.append('</svg>')
    return "\n".join(lines)

# ── KALNIK ──────────────────────────────────────────────────────────────────
kalnik_points = {
    "KT 1":    {"lat": 46.127997, "lon": 16.467275, "start": True,  "label_off": (0, -12)},
    "KT DJZA": {"lat": 46.132319, "lon": 16.467033, "label_off": (14, 5)},
    "KT DIA":  {"lat": 46.133553, "lon": 16.472736, "label_off": (14, 4)},
    "KT DSZA": {"lat": 46.135308, "lon": 16.466717, "label_off": (0, -12)},
    "KT DZA":  {"lat": 46.133419, "lon": 16.465994, "label_off": (-16, 4)},
    "KT LSIA": {"lat": 46.134567, "lon": 16.457569, "label_off": (0, -12)},
    "KT LZA":  {"lat": 46.131314, "lon": 16.443431, "label_off": (0, -12)},
    "KT LJIA": {"lat": 46.131314, "lon": 16.454394, "label_off": (0, -12)},
    "KT LIA":  {"lat": 46.132033, "lon": 16.459858, "label_off": (0, 16)},
}

kalnik_segments = [
    ("KT 1",    "KT DJZA", "sve"),
    ("KT DJZA", "KT DIA",  "G1,G3"),
    ("KT DJZA", "KT DZA",  "G5"),
    ("KT DJZA", "KT LSIA", "G4"),
    ("KT DJZA", "KT LIA",  "G2,G6"),
    ("KT DIA",  "KT DSZA", "G6"),
    ("KT DIA",  "KT LSIA", "G5,G6"),  # dijagonala
    ("KT DSZA", "KT DZA",  "G1-G6"),
    ("KT DZA",  "KT LSIA", "G3"),
    ("KT DZA",  "KT LIA",  "G1"),
    ("KT LSIA", "KT LZA",  "G1,G5"),
    ("KT LSIA", "KT LIA",  "G2"),
    ("KT LZA",  "KT LJIA", "G1-G6"),
    ("KT LJIA", "KT LIA",  "G4"),
]

# ── OKIĆ ────────────────────────────────────────────────────────────────────
okic_points = {
    "DOM":     {"lat": 45.749131, "lon": 15.703069, "start": True,  "label_off": (14, 5)},
    "KT JA":   {"lat": 45.750239, "lon": 15.700853, "label_off": (-16, 4)},
    "KT JZA":  {"lat": 45.752475, "lon": 15.697236, "label_off": (-18, 4)},
    "KT ZA":   {"lat": 45.753553, "lon": 15.692358, "label_off": (0, -12)},
    "KT SZA":  {"lat": 45.756147, "lon": 15.697922, "label_off": (-18, 4)},
    "KT SA":   {"lat": 45.759253, "lon": 15.697406, "label_off": (0, -12)},
    "KT SIA":  {"lat": 45.757733, "lon": 15.701897, "label_off": (14, 4)},
    "KT SIB":  {"lat": 45.757694, "lon": 15.704631, "label_off": (14, 4)},
    "KT JIA":  {"lat": 45.753422, "lon": 15.703028, "label_off": (14, 4)},
}

okic_segments = [
    ("DOM",    "KT JA",  "G1,G4"),
    ("DOM",    "KT JZA", "G2"),
    ("DOM",    "KT ZA",  "G3"),
    ("KT JA",  "KT JZA", "G1"),
    ("KT JA",  "KT ZA",  "G4"),
    ("KT JZA", "KT SZA", "G2"),
    ("KT JZA", "KT SA",  "G1"),
    ("KT ZA",  "KT SZA", "G3"),
    ("KT ZA",  "KT SIA", "G4"),
    ("KT SZA", "KT SA",  "G2"),
    ("KT SZA", "KT SIA", "G3"),
    ("KT SA",  "KT SIB", "G1,G2"),
    ("KT SIA", "KT JIA", "G3,G4"),
    ("KT SIB", "DOM",    "G1,G2"),
    ("KT JIA", "DOM",    "G3,G4"),
]

svg_kalnik = make_svg("Kalnik — kontrolne točke", kalnik_points, kalnik_segments)
svg_okic   = make_svg("Okić — kontrolne točke",   okic_points,   okic_segments)

with open(os.path.join(OUTPUT_DIR, "kalnik_kt.svg"), "w", encoding="utf-8") as f:
    f.write(svg_kalnik)

with open(os.path.join(OUTPUT_DIR, "okic_kt.svg"), "w", encoding="utf-8") as f:
    f.write(svg_okic)

print("OK: kalnik_kt.svg, okic_kt.svg")
