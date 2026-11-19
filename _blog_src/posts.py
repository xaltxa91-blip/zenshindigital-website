# Blog articles for zenshindigital.com/blog. Newest first is handled by date sort.
# Rules: data only, no opinions. Every fact must come from an official platform page or a trusted
# industry source, listed in `sources`. Facts that are not confirmed by the platform must say so.
# image: a raw platform screenshot in _blog_src/img (optional), shown in a branded window frame.
# shot_label: text in the frame's top bar (defaults to platform). caption: shown under it.
# takeaways: 3-5 short bullet facts shown at the top. faq: list of (question, answer) pairs,
# also output as FAQPage structured data for Google.

POSTS = [
  dict(
    slug="microsoft-ads-automated-bidding-upgrade",
    date="2026-11-19",
    modified="2026-11-19",
    platform="Microsoft Ads",
    title="Microsoft Ads rolls out its biggest bidding upgrade in a decade",
    seo_title="Microsoft Ads Automated Bidding Upgrade: tCPA, tROAS & Pacing (Nov 2026)",
    description="Microsoft Advertising is upgrading its automated bidding models: bids adjust nearly twice as fast to new CPA and ROAS targets, hit targets more consistently and pace budgets more evenly. Here are the details, Microsoft's data and its recommendations.",
    image=None,
    takeaways=[
      "Microsoft Advertising calls it its “biggest upgrade to bidding models in a decade”.",
      "Bids adjust nearly twice as quickly when advertisers change a CPA or ROAS target.",
      "Bids meet CPA and ROAS targets more consistently, and budgets pace more evenly through the day.",
      "The upgrade is applied automatically and is rolling out to more accounts over time.",
      "Microsoft recommends changing targets in 15% steps and not using maximum CPC limits.",
    ],
    body="""
<p>Microsoft Advertising announced on <strong>November 18, 2026</strong> what it calls its <strong>“biggest upgrade to bidding models in a decade”</strong>. The announcement, by Carlo Buchmann, Principal Product Manager at Microsoft Advertising, covers automated bid strategies including <strong>Maximize Conversion Value, Target ROAS, Target CPA</strong> (Maximize Conversions with a CPA target) and <strong>Enhanced CPC</strong>.</p>
<p>The upgrade is applied automatically. Microsoft describes it as “the first stage” of its updates, with improvements rolling out to more accounts over time and “more to come in 2027”.</p>

<h2>What changes</h2>
<ul>
  <li><strong>Speed:</strong> “Bids adjust nearly twice as quickly when advertisers update a CPA or ROAS target.”</li>
  <li><strong>Consistency:</strong> bids meet CPA and ROAS targets more consistently, without sacrificing volume or value.</li>
  <li><strong>Pacing:</strong> budgets pace more evenly throughout the day, and campaigns ramp up to full budget faster.</li>
</ul>

<h2>Microsoft's reported results</h2>
<p>Microsoft shared these figures from its own internal data:</p>
<div class="tbl"><table>
  <thead><tr><th>Bid strategy</th><th>Result</th><th>Data</th></tr></thead>
  <tbody>
    <tr><td>Maximize Conversion Value or Target ROAS</td><td>About 10% more conversion value per click at similar ROAS</td><td>Global, Search and Audience Network, August 2026</td></tr>
    <tr><td>Search campaigns moving from Target CPA to Target ROAS</td><td>About 8% more conversion value on average at similar ROAS</td><td>Global, August–September 2026</td></tr>
    <tr><td>Moving from Enhanced CPC to Maximize Conversions with a CPA target</td><td>About 18% more conversions at a similar cost per action</td><td>Global, June–July 2026</td></tr>
  </tbody>
</table></div>

<h2>Microsoft's recommendations</h2>
<ol>
  <li><strong>Set up conversion tracking.</strong> Automated bidding needs it. Microsoft recommends Universal Event Tracking (UET), with the Conversions API alongside it for broader coverage. Offline conversion import is another option.</li>
  <li><strong>Pick the strategy based on conversion volume.</strong> With at least 5 conversions, start with a conversion-based strategy instead of Enhanced CPC. With fewer than 5, start with Enhanced CPC to build conversion history, then move to Maximize Conversions (with a target CPA) or Maximize Conversion Value (with a target ROAS).</li>
  <li><strong>Change targets in 15% steps.</strong> Targets can be changed at any time, but large CPA increases or ROAS decreases can cause short-term volatility while the system recalibrates. Microsoft recommends changes of 15% at a time, reviewed after one conversion cycle.</li>
  <li><strong>Don't use maximum CPC limits.</strong> According to Microsoft, a max CPC overrides CPA and ROAS targets and can cause missed goals, even when the cap is above the average CPC. Microsoft suggests budgets, bid targets and conversion value rules instead.</li>
  <li><strong>Evaluate at the right level.</strong> Ideally wait for 30 conversions in 30 days, review 1–2 conversion cycles after major changes, and judge results at campaign or portfolio level by conversions and CPA or ROAS, not by keyword CPCs.</li>
</ol>

<h2>Changes that cause volatility</h2>
<p>According to Microsoft, major changes such as launching a new campaign, switching bid strategy, or adding or removing conversion goals tend to cause volatility while the bidding system calibrates.</p>
""",
    faq=[
      ("Do I need to opt in to the new Microsoft Ads bidding models?",
       "No. Microsoft applies the upgrade automatically and is rolling it out to more accounts over time."),
      ("Which bid strategies are affected?",
       "Microsoft's announcement names Maximize Conversion Value, Target ROAS, Target CPA (Maximize Conversions with a CPA target) and Enhanced CPC."),
      ("How much should I change my CPA or ROAS target at once?",
       "Microsoft recommends changing targets in 15% increments and reviewing the results after one conversion cycle."),
      ("Should I use a maximum CPC with automated bidding?",
       "Microsoft does not recommend it: a max CPC overrides CPA and ROAS targets and can cause missed goals, even when it is set above the average CPC."),
    ],
    sources=[
      ("Microsoft Advertising blog: Building the next generation of automated bidding at Microsoft Advertising", "https://about.ads.microsoft.com/en/blog/post/november-2026/building-the-next-generation-of-automated-bidding-at-microsoft-advertising"),
    ],
  ),
  dict(
    slug="meta-ads-5-existing-posts-one-ad",
    date="2026-11-18",
    modified="2026-11-18",
    platform="Meta Ads",
    title="Meta Ads Manager now lets you add up to 5 existing posts in one ad",
    seo_title="Meta Ads: Up to 5 Existing Posts in One Ad (New Ads Manager Option)",
    description="Meta Ads Manager is showing a new option to add up to 5 published posts to a single ad, with Meta showing each person the post they're most likely to engage with. Here's what is confirmed and what is still unknown.",
    image="meta-ads-5-posts-screenshot.jpg",
    shot_label="Meta Ads Manager",
    caption="Meta Ads Manager: the new “0 of 5 posts selected” field under Ad creative",
    takeaways=[
      "Under “Use existing posts”, advertisers can now select up to 5 published posts in one ad.",
      "Meta shows each person the post it predicts they're most likely to engage with.",
      "Before, this setup allowed 1 existing post per ad.",
      "Meta has not published an announcement, help page or rollout details yet.",
    ],
    body="""
<p>Meta Ads Manager is showing a new option for ads built from existing posts: instead of one published post per ad, advertisers can now select <strong>up to 5 posts in a single ad</strong>. The option was shared on LinkedIn by Bram Van der Hallen (Edge.be) on November 17, 2026, and reported by PPC Land the same day. We can also see it in our own Meta Ads Manager account, as the screenshot above shows.</p>
<p>Meta has not announced the change or documented it in its Business Help Center yet, so some details are still unknown. This article covers what can be confirmed from Ads Manager itself.</p>

<h2>Where to find the new option in Ads Manager</h2>
<ol>
  <li>Create or edit an ad and go to the <strong>ad level</strong>.</li>
  <li>Under <strong>Ad setup</strong>, choose <strong>“Use existing posts”</strong>.</li>
  <li>In the <strong>Ad creative</strong> section, the <strong>Posts</strong> field now shows a counter, for example “0 of 5 posts selected”.</li>
  <li>Click <strong>“Select posts”</strong> to pick up to 5 published posts, or enter a post ID.</li>
</ol>
<p>In the accounts where it has appeared, Ads Manager shows this notice: <em>“Now you can select up to 5 posts, and we'll show each person the one they're most likely to engage with.”</em></p>

<h2>How it works</h2>
<p>All selected posts sit inside one ad. For each person who sees the ad, Meta chooses the post it predicts that person is most likely to engage with. Until now, promoting 5 existing posts under the same setup required 5 separate ads.</p>
<p>Ads that use existing posts are different from new ad creatives: they run the original organic post, so the reactions, comments and shares the post already has stay visible on the ad.</p>

<h2>What is still unknown</h2>
<p>Because Meta has not published documentation, these points are not confirmed:</p>
<ul>
  <li><strong>Rollout:</strong> which countries and accounts have the option, and when it will reach everyone.</li>
  <li><strong>Eligibility:</strong> which campaign objectives and placements support it.</li>
  <li><strong>Reporting:</strong> whether results can be broken down per post.</li>
  <li><strong>Selection signal:</strong> Meta describes the choice only as the post a person is “most likely to engage with”. It's not stated whether this follows the ad set's optimisation goal, such as traffic, leads or sales.</li>
  <li><strong>Ad limits:</strong> whether an ad with 5 posts counts as 1 ad towards a Page's ad limit.</li>
  <li><strong>API:</strong> whether the option is available in the Marketing API.</li>
</ul>

<h2>Related Meta features</h2>
<p>The new option sits next to other Meta formats that test several assets inside one ad:</p>
<ul>
  <li><strong>Flexible format ads</strong> let advertisers add up to 10 images and videos to one ad, and Meta chooses which to show.</li>
  <li><strong>Advantage+ creative</strong> enhancements appear in the same Ad creative section of Ads Manager.</li>
</ul>
<p>The difference: flexible format ads use new media files, while this option uses posts that are already published on the Page or Instagram account.</p>
""",
    faq=[
      ("How many existing posts can I add to one Meta ad?",
       "Up to 5, under “Use existing posts” in the Ad creative section of Ads Manager. Previously the limit was 1 post per ad."),
      ("How does Meta choose which post to show?",
       "Meta shows each person the post it predicts they're most likely to engage with. Meta has not published more detail on the selection."),
      ("Is the option available in all accounts?",
       "Not confirmed. Meta has not announced a rollout, so it may only appear in some accounts for now."),
      ("Can I see results per post?",
       "Not confirmed. Meta has not documented per-post reporting for this option yet."),
    ],
    sources=[
      ("PPC Land: One Meta ad can now carry up to 5 existing posts", "https://ppc.land/one-meta-ad-can-now-carry-up-to-5-existing-posts/"),
      ("Screenshot from our Meta Ads Manager account (November 18, 2026)", None),
    ],
  ),

  dict(
    slug="amazon-ads-price-claims-policy",
    date="2026-11-17",
    modified="2026-11-18",
    platform="Amazon Ads",
    title="Amazon Ads bans claims like “Best price” and “Unbeatable price” in ads",
    seo_title="Amazon Ads Pricing Policy Update: “Best Price” Claims Banned (Nov 2026)",
    description="Amazon Ads updated its Pricing and promotions policy on November 15, 2026. Price superlatives like “Best price”, “Unbeatable price” and “Wholesale price” are not allowed on Amazon's own placements. Here are the new rules by placement.",
    image=None,
    takeaways=[
      "Amazon Ads updated its “Pricing and promotions” policy page on November 15, 2026.",
      "Price superlatives and unprovable price claims, like “Best price” or “Unbeatable price”, are not allowed on Amazon retail or non-retail placements.",
      "On Amazon retail, numerical prices or savings are only allowed when Amazon renders them dynamically in the ad.",
      "The page gives no effective date or transition period.",
    ],
    body="""
<p>Amazon Ads updated its <strong>“Pricing and promotions”</strong> policy page on <strong>November 15, 2026</strong>. The page is part of the Policies and guidelines section of the Amazon Ads Support Center, and it sorts the rules by where the ad runs (supply type) instead of by ad product. It gives no effective date, changelog or transition period.</p>
<p>Several other Amazon Ads policy pages show the same update date: Claims and substantiation, Real estate, News and journalism, Animal related products and services, and Gambling and games.</p>

<h2>Price claims that are no longer allowed</h2>
<p>The policy prohibits price superlatives and competitive, misleading or unprovable price claims on Amazon retail and non-retail placements. Amazon lists these as examples (the list is not complete):</p>
<ul>
  <li>“Best price” or “Top price”</li>
  <li>“Unbeatable price”</li>
  <li>“Competitive price”</li>
  <li>“Best possible price”</li>
  <li>“Introductory price”</li>
  <li>“Wholesale price”</li>
  <li>“Never before seen price”</li>
  <li>“Price advantage”</li>
</ul>

<h2>Rules for Amazon retail placements</h2>
<p>Amazon retail covers Amazon.com retail placements and Whole Foods Market digital placements. Here the policy states:</p>
<ul>
  <li><strong>Prices and savings:</strong> “Numerical prices or savings are only permitted when rendered dynamically in the ad by Amazon.” Prices or savings written into the creative itself are not allowed.</li>
  <li><strong>Landing page match:</strong> pricing, savings and promotional claims must match the landing page for the full campaign.</li>
  <li><strong>Multi-product pages and Brand Stores:</strong> when an ad links to a page with several products, at least 10% of the products (or the share required in that country) must carry the maximum saving claimed in the ad.</li>
  <li><strong>Deal teasing</strong> is not allowed.</li>
  <li><strong>Urgency language</strong> that pressures a decision, such as “buy now or regret later”, is not allowed.</li>
</ul>

<h2>Rules for non-retail Amazon placements</h2>
<p>Non-retail supply covers <strong>IMDb, Fire TV and Streaming TV</strong>. Here, claims must be available for the full campaign and must disclose material conditions, such as exclusions, delivery costs, subscriptions or bundles. The ban on price superlatives and unprovable claims also applies.</p>

<h2>Rules for the open internet</h2>
<p>For ads on third-party publisher sites and apps, the advertiser is responsible for accuracy, for complying with applicable laws, and for meeting the publisher's own requirements. The page gives no list of banned wording for this supply type.</p>

<h2>How to check your Amazon ads against the new rules</h2>
<ol>
  <li>Search your headlines, custom images and video copy for the phrases listed above.</li>
  <li>For ads on Amazon retail, remove prices or savings written into the creative. Only prices Amazon shows dynamically are allowed.</li>
  <li>Check that every price, saving or promotion in the ad matches the landing page for the whole campaign.</li>
  <li>For ads that link to a Brand Store or multi-product page, check that at least 10% of the products carry the maximum saving you claim.</li>
  <li>For IMDb, Fire TV and Streaming TV ads, add any material conditions, such as delivery costs or subscriptions.</li>
</ol>
""",
    faq=[
      ("When did Amazon Ads update its pricing policy?",
       "The Pricing and promotions policy page shows an update date of November 15, 2026. Amazon has not given a separate effective date or transition period."),
      ("Can I write prices in my Amazon ad creative?",
       "On Amazon retail placements, numerical prices or savings are only allowed when Amazon renders them dynamically in the ad. Prices written into the creative are not allowed there."),
      ("Which placements does the ban on “Best price” claims cover?",
       "Amazon retail (Amazon.com and Whole Foods Market digital) and non-retail Amazon supply (IMDb, Fire TV and Streaming TV)."),
      ("Is the list of banned phrases complete?",
       "No. Amazon gives the phrases as examples. Any price superlative or competitive, misleading or unprovable price claim is covered."),
    ],
    sources=[
      ("Amazon Ads: Creative acceptance policies", "https://advertising.amazon.com/ad-specs/en/policy/creative-acceptance"),
      ("PPC Land: Amazon bans “best price” claims in ads on its store, IMDb and Fire TV", "https://ppc.land/amazon-bans-best-price-claims-in-ads-on-its-store-imdb-and-fire-tv/"),
    ],
  ),

  dict(
    slug="google-ai-max-search-term-matchtype",
    date="2026-11-16",
    modified="2026-11-18",
    platform="Google Ads",
    title="Google Ads {search_term_matchtype}: how to track AI Max expansion clicks",
    seo_title="Google Ads {search_term_matchtype}: Track AI Max Expansion Clicks",
    description="Google Ads added the {search_term_matchtype} ValueTrack parameter. Here's what each value means and how to separate AI Max expansion clicks from real exact, phrase and broad match clicks.",
    image=None,
    takeaways=[
      "{search_term_matchtype} records the match type of the search term that triggered your ad.",
      "Values: e (exact), p (phrase), b (broad), a (AI Max).",
      "When AI Max expands a keyword, {matchtype} still shows the keyword's match type, while {search_term_matchtype} shows “a”.",
      "It can be used in final URLs, tracking templates and custom parameters.",
    ],
    body="""
<p>Google Ads has added a new ValueTrack parameter, <code>{search_term_matchtype}</code>, to its help documentation. It records the match type of the <strong>search term</strong> that triggered your ad, and it makes it possible to see which clicks came from <strong>AI Max for Search</strong> expansions, even when they were credited to an exact or phrase match keyword.</p>
<p>The parameter was first reported on November 11, 2026 by PPC News Feed. Google has not published a separate announcement or a launch date.</p>

<h2>{matchtype} vs. {search_term_matchtype}</h2>
<p>Google's ValueTrack documentation defines the two parameters like this:</p>
<ul>
  <li><code>{matchtype}</code>: “The match type of the keyword that triggered your ad.”</li>
  <li><code>{search_term_matchtype}</code>: “The match type of the search term that triggered your ad.”</li>
</ul>
<p>Both return the same set of values:</p>
<div class="tbl"><table>
  <thead><tr><th>Value</th><th>{matchtype}</th><th>{search_term_matchtype}</th></tr></thead>
  <tbody>
    <tr><td><code>e</code></td><td>Exact</td><td>Exact</td></tr>
    <tr><td><code>p</code></td><td>Phrase</td><td>Phrase</td></tr>
    <tr><td><code>b</code></td><td>Broad</td><td>Broad</td></tr>
    <tr><td><code>a</code></td><td>AI Max (keywordless match)</td><td>AI Max (expansions and keywordless matches)</td></tr>
  </tbody>
</table></div>

<h2>Why the new parameter matters for AI Max</h2>
<p>With AI Max for Search, Google can match a keyword to search terms beyond its own match type. In that case, <code>{matchtype}</code> still reports the keyword's match type, for example <code>e</code> for an exact match keyword. <code>{search_term_matchtype}</code> reports <code>a</code>, showing the click actually came from an AI Max expansion.</p>
<p>Combined with <code>{targetid}</code> (keywords start with “kwd”, AI Max keywordless matches with “kwl”) and <code>{keyword}</code> (empty for keywordless matches), the parameters separate three types of traffic:</p>
<div class="tbl"><table>
  <thead><tr><th>Traffic type</th><th>{matchtype}</th><th>{search_term_matchtype}</th><th>{keyword}</th></tr></thead>
  <tbody>
    <tr><td>Standard keyword match</td><td>e, p or b</td><td>e, p or b</td><td>Filled</td></tr>
    <tr><td>AI Max expansion of a keyword</td><td>e, p or b</td><td>a</td><td>Filled</td></tr>
    <tr><td>AI Max keywordless match</td><td>a</td><td>a</td><td>Empty</td></tr>
  </tbody>
</table></div>
<p>The scale of AI Max expansions is growing. According to Smarter Ecommerce data reported by PPC Land, the share of exact match impressions served through AI Max expansions rose from about 0% in January 2025 to nearly 29% by July 2026, across 383 million EMEA ecommerce Search impressions with AI Max active. With <code>{matchtype}</code> alone, all of those clicks would have looked like exact match.</p>

<h2>How to set it up</h2>
<ol>
  <li>In Google Ads, open the tracking template at account, campaign or ad group level. ValueTrack parameters can also go in the final URL or in custom parameters.</li>
  <li>Add the parameters to your template. For example:
    <pre><code>{lpurl}?keyword={keyword}&amp;matchtype={matchtype}&amp;search_term_matchtype={search_term_matchtype}</code></pre>
    Keep <code>{lpurl}</code> at the start. Google's AI Max guidance recommends this, because final URL expansion can send clicks to other pages of your site.</li>
  <li>Test the template with the “Test” option in Google Ads before saving.</li>
  <li>In your analytics or CRM, filter the URL parameters:
    <ul>
      <li><strong>AI Max expansion traffic:</strong> matchtype is e, p or b, and search_term_matchtype is a.</li>
      <li><strong>Standard keyword traffic:</strong> search_term_matchtype is e, p or b.</li>
    </ul>
  </li>
</ol>

<h2>AI Max for Search: timeline</h2>
<ul>
  <li><strong>May 2025:</strong> Google launches AI Max for Search campaigns, with search term matching, text customisation and final URL expansion.</li>
  <li><strong>July 2025:</strong> a “Search terms match type” segment is added to the Keywords report.</li>
  <li><strong>September 1, 2026:</strong> Google starts upgrading broad match and automatically created assets campaigns to AI Max for Search.</li>
  <li><strong>November 2026:</strong> <code>{search_term_matchtype}</code> appears in Google's ValueTrack documentation.</li>
</ul>
""",
    faq=[
      ("What does “a” mean in {search_term_matchtype}?",
       "“a” means the search term was matched by AI Max for Search, either as an expansion of one of your keywords or as a keywordless match."),
      ("What is the difference between {matchtype} and {search_term_matchtype}?",
       "{matchtype} is the match type of your keyword. {search_term_matchtype} is the match type of the search term that actually triggered the ad. They differ when AI Max expands a keyword."),
      ("Where can I use {search_term_matchtype}?",
       "Like other ValueTrack parameters, in the final URL, the tracking template or custom parameters."),
      ("Does {search_term_matchtype} work in Performance Max?",
       "Google's help page does not list it for Performance Max. It is documented for Search campaigns, including AI Max for Search."),
    ],
    sources=[
      ("Google Ads Help: Set up tracking with ValueTrack parameters", "https://support.google.com/google-ads/answer/6305348"),
      ("Google Ads Help: About ValueTrack parameters", "https://support.google.com/google-ads/answer/2375447"),
      ("PPC Land: Google's new parameter shows when an “exact” click was really AI Max", "https://ppc.land/googles-new-parameter-shows-when-an-exact-click-was-really-ai-max/"),
    ],
  ),
]
