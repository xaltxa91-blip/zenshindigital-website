"""Branded social preview images (1200x630) for LinkedIn / X / WhatsApp link previews.
Rendered with Playwright. Images are cached: a new one is only rendered when the text changes.
"""
import hashlib, html, os

ICON = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "brand", "zenshin-icon.svg")).read()
e = html.escape


def _page(kicker, title, footer):
    size = 64 if len(title) <= 60 else 56 if len(title) <= 85 else 48
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:630px;font-family:'Inter Display','Inter',system-ui,sans-serif;color:#f0efff}}
.c{{width:1200px;height:630px;position:relative;overflow:hidden;padding:64px 72px;display:flex;flex-direction:column;
background:radial-gradient(700px 380px at 85% -10%,rgba(34,211,238,.28),transparent 70%),
radial-gradient(800px 420px at 10% 120%,rgba(99,102,241,.45),transparent 70%),linear-gradient(125deg,#07070f,#0d0d22 55%,#0a0a18)}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:36px 36px}}
.big{{position:absolute;right:-70px;bottom:-90px;width:430px;height:430px;opacity:.09}}
.top{{display:flex;align-items:center;gap:14px;position:relative}}
.top svg{{width:52px;height:52px}}
.brand{{font-size:28px;font-weight:700;letter-spacing:-.01em}}
.tag{{margin-left:auto;font-size:20px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#22d3ee;border:2px solid rgba(34,211,238,.45);padding:8px 18px;border-radius:999px}}
h1{{position:relative;margin-top:auto;font-size:{size}px;line-height:1.1;font-weight:700;letter-spacing:-.025em;max-width:1020px;text-wrap:balance}}
.f{{position:relative;margin-top:34px;font-size:22px;color:rgba(240,239,255,.6);display:flex;align-items:center;gap:14px}}
.f i{{width:44px;height:4px;border-radius:2px;background:linear-gradient(90deg,#6366f1,#22d3ee);display:block}}
</style></head><body><div class="c"><div class="grid"></div><div class="big">{ICON}</div>
<div class="top">{ICON}<span class="brand">Zenshin Digital</span>{f'<span class="tag">{e(kicker)}</span>' if kicker else ''}</div>
<h1>{e(title)}</h1><div class="f"><i></i>{e(footer)}</div></div></body></html>"""


def render_all(jobs, out_dir):
    """jobs: list of (filename, kicker, title, footer). Renders only missing/changed images."""
    os.makedirs(out_dir, exist_ok=True)
    todo = []
    for name, kicker, title, footer in jobs:
        h = hashlib.md5(f"{kicker}|{title}|{footer}|v1".encode()).hexdigest()[:10]
        stamp = os.path.join(out_dir, name + ".hash")
        path = os.path.join(out_dir, name)
        if os.path.exists(path) and os.path.exists(stamp) and open(stamp).read() == h:
            continue
        todo.append((path, stamp, h, _page(kicker, title, footer)))
    if not todo:
        return 0
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        for path, stamp, h, page in todo:
            pg.set_content(page)
            pg.wait_for_timeout(150)
            pg.screenshot(path=path, type="png")
            open(stamp, "w").write(h)
        b.close()
    return len(todo)
