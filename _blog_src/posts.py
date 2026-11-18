# Blog articles for zenshindigital.com/blog — newest first is handled by date sort.
# Each body is HTML. Data only, no opinions.

POSTS = [
  dict(
    slug="meta-ads-5-existing-posts-one-ad",
    date="2026-11-18",
    platform="Meta Ads",
    title="Meta Ads Manager: up to 5 existing posts in one ad",
    description="Some Meta Ads Manager accounts can now select up to 5 published posts in a single ad. Meta has not announced it yet.",
    image="meta-ads-5-existing-posts-one-ad.jpg",
    body="""
<p>Some Meta Ads Manager accounts now show a new option: under <strong>“Use existing posts”</strong>, advertisers can select <strong>up to 5 published posts in one ad</strong>. I found it in my own Ads Manager account.</p>
<h2>What's new</h2>
<ul>
  <li>Select up to 5 published posts in a single ad, under “Use existing posts”.</li>
  <li>Meta shows each person the post they're most likely to engage with.</li>
  <li>Previously, an ad could use only 1 existing post.</li>
</ul>
<h2>Still unknown</h2>
<ul>
  <li>Meta has not published an official announcement or rollout details yet.</li>
</ul>
""",
    sources=[("Screenshot from my Meta Ads Manager account", None)],
  ),
  dict(
    slug="amazon-ads-price-claims-policy",
    date="2026-11-17",
    platform="Amazon Ads",
    title="Amazon Ads bans claims like “Unbeatable price” in ad copy",
    description="Amazon Ads updated its advertising copy policy on November 15, 2026. Price claims such as “Best price” or “Wholesale price” are no longer allowed on Amazon's own placements.",
    image="amazon-ads-price-claims-policy.jpg",
    body="""
<p>Amazon Ads updated its <strong>advertising copy policy</strong> on <strong>November 15, 2026</strong>. The changes apply to ads on Amazon's own placements.</p>
<h2>Example phrases now banned in ads</h2>
<ul>
  <li>Best / Top price</li>
  <li>Unbeatable price</li>
  <li>Competitive price</li>
  <li>Wholesale price</li>
  <li>Never before seen price</li>
</ul>
<h2>Also in the update</h2>
<ul>
  <li>On Amazon retail, prices or savings can only appear when they are rendered by Amazon, not written in the creative.</li>
  <li>Health, environmental, origin and comparison claims are allowed with dated evidence.</li>
  <li>The policy covers Amazon retail, IMDb, Fire TV and Streaming TV.</li>
  <li>No transition period has been announced.</li>
</ul>
""",
    sources=[("Amazon Ads: Advertising copy policy", "https://advertising.amazon.com/resources/ad-policy/creative-acceptance/advertising-copy")],
  ),
  dict(
    slug="google-ai-max-search-term-matchtype",
    date="2026-11-16",
    platform="Google Ads",
    title="Google Ads: new {search_term_matchtype} parameter shows AI Max expansion clicks",
    description="A new ValueTrack parameter, {search_term_matchtype}, shows when a click on an exact-match keyword actually came from an AI Max expansion.",
    image="google-ai-max-search-term-matchtype.jpg",
    body="""
<p>Google Ads has documented a new ValueTrack parameter, <code>{search_term_matchtype}</code>. It shows how the search term actually matched, including clicks that came from <strong>AI Max</strong> expansions.</p>
<h2>Same click, two parameters</h2>
<p>When AI Max expands an exact-match keyword:</p>
<ul>
  <li><code>{matchtype}</code> returns <strong>e</strong>, so it looks like an exact match.</li>
  <li><code>{search_term_matchtype}</code> returns <strong>a</strong>, an AI Max expansion.</li>
</ul>
<h2>{search_term_matchtype} values</h2>
<ul>
  <li><strong>e</strong>: exact</li>
  <li><strong>p</strong>: phrase</li>
  <li><strong>b</strong>: broad</li>
  <li><strong>a</strong>: AI Max expansions and keywordless</li>
</ul>
<h2>Google's example tracking template</h2>
<pre><code>{lpurl}?keyword={keyword}&amp;matchtype={matchtype}&amp;search_term_matchtype={search_term_matchtype}</code></pre>
""",
    sources=[("Google Ads Help: About ValueTrack parameters", "https://support.google.com/google-ads/answer/2375447"),
             ("PPC Land", "https://ppc.land/googles-new-parameter-shows-when-an-exact-click-was-really-ai-max/")],
  ),
]
