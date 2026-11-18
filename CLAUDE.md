# zenshindigital.com — instructions for Claude

Static site for Zenshin Digital (paid media agency, founder Xabier Urrutia). Hostinger auto-deploys
the `main` branch to public_html on every push, so pushing = publishing.

- Voice: agency "we". Founder is named only in About, the author box, and blog bylines.
- Accuracy rules: facts only, no invented results, testimonials or case studies. Every blog or
  channel-page fact must come from an official platform page or a trusted industry source
  (PPC Land, Search Engine Land, Search Engine Roundtable, Social Media Today...). Unconfirmed
  things are labelled as unconfirmed.
- Blog articles: add to `_blog_src/posts.py`; channel pages: `_blog_src/channels.py`
  (update `reviewed` when checked). Then run `python3 _blog_src/build.py .` from the repo root.
  This regenerates /blog, the 10 channel pages (their "Latest news" comes from posts with the
  same `platform`), sitemap.xml and robots.txt. Never edit generated HTML by hand.
- Screenshots for articles go in `_blog_src/img` (raw platform screenshots, not LinkedIn images).
- Homepage is index.html + styles.css (dark). Blog is light reading mode. Bump the `?v=` on CSS
  links when changing CSS.
- Commit as: git -c user.name=Claude -c user.email=noreply@anthropic.com
