"""Build the static blog for zenshindigital.com.
Usage: python3 build.py <site_dir>
Writes <site_dir>/blog/index.html, one page per post, blog/img/*, blog/blog.css, sitemap.xml, robots.txt
"""
import sys, os, shutil, json, html
from datetime import date
sys.path.insert(0, os.path.dirname(__file__))
from posts import POSTS

SITE = "https://zenshindigital.com"
out = sys.argv[1]
blog = os.path.join(out, "blog")
os.makedirs(os.path.join(blog, "img"), exist_ok=True)
here = os.path.dirname(os.path.abspath(__file__))
for f in os.listdir(os.path.join(here, "img")):
    shutil.copy(os.path.join(here, "img", f), os.path.join(blog, "img", f))
shutil.copy(os.path.join(here, "blog.css"), os.path.join(blog, "blog.css"))

import hashlib
CSSV = hashlib.md5(open(os.path.join(here, "blog.css"), "rb").read()).hexdigest()[:8]
posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)
e = html.escape
def nice(d):
    y, m, dd = map(int, d.split("-"))
    return date(y, m, dd).strftime("%B %-d, %Y")

FAVICON = """<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='8' fill='%236366f1'/><text x='50%' y='56%' dominant-baseline='middle' text-anchor='middle' font-family='system-ui,sans-serif' font-weight='800' font-size='19' fill='white'>Z</text></svg>" />"""

def head(title, desc, url, image=None, extra=""):
    og_img = f'<meta property="og:image" content="{SITE}/blog/img/{image}" />' if image else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}" />
  <link rel="canonical" href="{url}" />
  <meta property="og:title" content="{e(title)}" />
  <meta property="og:description" content="{e(desc)}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:type" content="article" />
  {og_img}
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
  <link rel="stylesheet" href="/blog/blog.css?v={CSSV}" />
  {FAVICON}
  {extra}
</head>
<body>
<header class="bnav"><div class="bwrap bnav-in">
  <a href="/" class="logo"><span class="logo-i">Z</span>Zenshin Digital</a>
  <nav><a href="/blog/">Blog</a><a href="/#about">About</a><a href="/#contact" class="btn">Book a Call</a></nav>
</div></header>
"""

AUTHOR = """<aside class="author">
  <img src="/assets/img/xabier-urrutia.jpg" alt="Xabier Urrutia" width="72" height="72">
  <div><strong>Xabier Urrutia</strong>
  <span>Performance marketing &amp; growth, with experience at Google, Meta, GroupM and Semrush. $100M+ in ad spend managed across Google, Meta, Amazon, LinkedIn, TikTok and more.</span></div>
</aside>"""

CTA = """<section class="bcta">
  <h2>Need help with your paid media?</h2>
  <p>Book a free 30-minute strategy call. I'll review your current setup and identify quick wins.</p>
  <a class="btn" href="mailto:hello@zenshindigital.com?subject=Strategy%20call">Book a Free Strategy Call</a>
</section>"""

FOOT = """<footer class="bfoot"><div class="bwrap">
  <span>© 2026 Zenshin Digital</span>
  <span><a href="/">Home</a> · <a href="/blog/">Blog</a> · <a href="/privacy.html">Privacy Policy</a></span>
</div></footer>
</body></html>"""

def src_html(sources):
    items = []
    for label, url in sources:
        items.append(f'<li><a href="{e(url)}" rel="noopener" target="_blank">{e(label)}</a></li>' if url else f"<li>{e(label)}</li>")
    return f'<div class="sources"><h2>Sources</h2><ul>{"".join(items)}</ul></div>'

# article pages
for i, p in enumerate(posts):
    url = f"{SITE}/blog/{p['slug']}.html"
    img_url = [f"{SITE}/blog/img/{p['image']}"] if p.get("image") else []
    ld = {"@context": "https://schema.org", "@type": "NewsArticle", "headline": p["title"],
          "description": p["description"], "datePublished": p["date"], "dateModified": p["date"],
          "image": img_url, "mainEntityOfPage": url,
          "author": {"@type": "Person", "name": "Xabier Urrutia", "url": f"{SITE}/#about"},
          "publisher": {"@type": "Organization", "name": "Zenshin Digital", "url": SITE}}
    extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    others = [q for q in posts if q is not p][:3]
    more = "".join(f'<a class="more-item" href="/blog/{q["slug"]}.html"><span class="tag">{e(q["platform"])}</span>{e(q["title"])}</a>' for q in others)
    shot = (f'<figure class="shot"><img src="/blog/img/{p["image"]}" alt="{e(p.get("caption") or p["title"])}">'
            + (f'<figcaption>{e(p["caption"])}</figcaption>' if p.get("caption") else '') + '</figure>') if p.get("image") else ""
    page = head(f"{p['title']} | Zenshin Digital", p["description"], url, p["image"], extra) + f"""
<main class="bwrap art">
  <a class="back" href="/blog/">← All articles</a>
  <div class="meta"><span class="tag">{e(p['platform'])}</span><time datetime="{p['date']}">{nice(p['date'])}</time></div>
  <h1>{e(p['title'])}</h1>
  <p class="lede">{e(p['description'])}</p>
  {shot}
  <div class="content">
    {p['body']}
    {src_html(p['sources'])}
  </div>
  {AUTHOR}
  {CTA}
  {'<section class="more"><h2>More paid media news</h2>' + more + '</section>' if others else ''}
</main>
""" + FOOT
    open(os.path.join(blog, f"{p['slug']}.html"), "w", encoding="utf-8").write(page)

# index
cards = "".join(f"""
  <a class="post" href="/blog/{p['slug']}.html">
    <div class="post-b">
      <div class="meta"><span class="tag">{e(p['platform'])}</span><time datetime="{p['date']}">{nice(p['date'])}</time></div>
      <h2>{e(p['title'])}</h2>
      <p>{e(p['description'])}</p>
      <span class="read">Read article →</span>
    </div>
  </a>""" for p in posts)
idx = head("Paid Media News | Zenshin Digital Blog",
           "The latest updates from Google Ads, Meta Ads, Amazon Ads, LinkedIn Ads, TikTok Ads and more, checked against official sources.",
           f"{SITE}/blog/") + f"""
<main class="bwrap">
  <section class="bhero">
    <span class="kicker">Blog</span>
    <h1>Paid Media <em>News</em></h1>
    <p>The latest updates from Google, Meta, Amazon, LinkedIn, TikTok and more, checked against official sources.</p>
  </section>
  <section class="grid">{cards}
  </section>
  {CTA}
</main>
""" + FOOT
open(os.path.join(blog, "index.html"), "w", encoding="utf-8").write(idx)

# sitemap + robots
urls = [(f"{SITE}/", posts[0]["date"]), (f"{SITE}/blog/", posts[0]["date"])] + [(f"{SITE}/blog/{p['slug']}.html", p["date"]) for p in posts]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
     "".join(f"  <url><loc>{u}</loc><lastmod>{d}</lastmod></url>\n" for u, d in urls) + "</urlset>\n"
open(os.path.join(out, "sitemap.xml"), "w").write(sm)
open(os.path.join(out, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("built", len(posts), "posts")
