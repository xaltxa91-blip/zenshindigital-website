# Blog articles for zenshindigital.com/blog. Newest first is handled by date sort.
# Rules: data only, no opinions. Every fact must come from an official platform page or a trusted
# industry source, listed in `sources`. Facts that are not confirmed by the platform must say so.
# image: a raw platform screenshot in _blog_src/img (optional), shown in a branded window frame.
# shot_label: text in the frame's top bar (defaults to platform). caption: shown under it.
# takeaways: 3-5 short bullet facts shown at the top. faq: list of (question, answer) pairs,
# also output as FAQPage structured data for Google.

POSTS = [
  dict(
    slug="gtm-tracking-implementation-with-claude",
    date="2026-11-26",
    modified="2026-11-26",
    platform="Tracking",
    title="GTM tracking for Google Ads, Meta, GA4 and more, implemented with Claude",
    seo_title="GTM Tracking Implementation with Claude: Google Ads, Meta & GA4 (2026)",
    description="We successfully implemented Google Tag Manager tracking for Google Ads, Meta, GA4 and more with Claude. Here's how Claude connects to each platform, what it can audit and build, and what to watch out for.",
    image=None,
    takeaways=[
      "We successfully implemented GTM tracking for Google Ads, Meta, GA4 and more with Claude.",
      "Meta offers official Ads AI Connectors for Claude, in open beta since April 29, 2026.",
      "Google's official Google Ads API MCP server is read-only, for analysis and diagnostics.",
      "Google Tag Manager and GA4 connect through third-party connectors, since Claude's directory has no first-party Google Ads, GA4 or Meta Ads connector.",
    ],
    body="""
<p>Conversion tracking is often the hardest part of paid media, and the place where small mistakes cost the most: wrong conversion values, sales counted twice, or tags firing before consent. We recently implemented <strong>Google Tag Manager (GTM) tracking for Google Ads, Meta, GA4 and more with Claude</strong>, working directly in GTM, Google Ads, Meta and GA4. The implementation was successful, and Claude caught a gap between the attribution setup and the live website code before the first sale came in.</p>
<p>Here is what is possible today, based on the platforms' own announcements and documentation.</p>

<h2>How Claude connects to ad platforms</h2>
<p>Claude connects to external tools through <strong>connectors</strong> built on the Model Context Protocol (MCP), an open standard that Anthropic launched in November 2024. Each platform is connected differently:</p>
<div class="tbl"><table>
  <thead><tr><th>Platform</th><th>Connection</th><th>Access</th></tr></thead>
  <tbody>
    <tr><td>Meta Ads</td><td>Meta's official Ads AI Connectors (open beta since April 29, 2026)</td><td>Reporting, campaign management, catalog management and signal diagnostics</td></tr>
    <tr><td>Google Ads</td><td>Google's open-source Google Ads API MCP server (released October 7, 2025)</td><td>Read-only, for analysis and diagnostics</td></tr>
    <tr><td>Google Tag Manager &amp; GA4</td><td>Third-party connectors</td><td>Depends on the connector: some can audit, build and clean up GTM containers</td></tr>
  </tbody>
</table></div>
<p>Several guides note that Claude's connector directory currently has no first-party Google Ads, GA4 or Meta Ads connector. Meta's connector is added separately, and Google's MCP server is set up by developers.</p>

<h2>Meta: official AI connectors</h2>
<p>Meta announced the open beta of its <strong>Meta Ads AI Connectors</strong> on April 29, 2026, for AI agents from Anthropic (Claude) and OpenAI. They cover reporting, campaign management, catalog management and <strong>signal diagnostics</strong>: access to signal health and quality information, which helps prioritise Conversions API setup.</p>

<h2>Google Ads: official MCP server, read-only</h2>
<p>Google released the open-source <strong>Google Ads API MCP server</strong> on October 7, 2025. The initial version is <strong>read-only</strong>, designed for diagnostics and analytics: it can list accessible accounts and run Google Ads Query Language (GAQL) queries for campaign metrics, budgets and status. It cannot change accounts.</p>

<h2>What Claude can do for tracking</h2>
<ul>
  <li><strong>Audit:</strong> review GTM containers, tags, triggers and variables, GA4 events and conversion setups across Google Ads and Meta.</li>
  <li><strong>Build:</strong> with connectors that have write access, create GA4 events, GTM tags and triggers, Google Ads conversion tracking and Meta Pixel + Conversions API setups.</li>
  <li><strong>Check:</strong> consent setup, duplicate events between platforms, and conversion values, currency and order IDs.</li>
  <li><strong>Clean up:</strong> find outdated or duplicate tags and triggers in old containers.</li>
</ul>

<h2>What to watch out for</h2>
<ul>
  <li><strong>Check permissions:</strong> know whether a connector can only read data or can also make changes.</li>
  <li><strong>Review before publishing:</strong> keep GTM changes in a workspace draft and test them in Preview mode before publishing.</li>
  <li><strong>Verify after launch:</strong> confirm that conversions arrive in Google Ads, Meta Events Manager and GA4 with the right values.</li>
  <li><strong>Consent and privacy:</strong> tracking still has to follow consent requirements and data processing agreements, whoever sets it up.</li>
</ul>
""",
    faq=[
      ("Can Claude set up Google Ads conversion tracking?",
       "Yes, through connectors. Google's official Google Ads API MCP server is read-only, so building conversion tracking requires connectors with write access to Google Tag Manager and Google Ads."),
      ("Does Meta have an official connector for Claude?",
       "Yes. Meta announced the open beta of its Meta Ads AI Connectors on April 29, 2026, for AI agents from Anthropic and OpenAI, covering reporting, campaign management, catalog management and signal diagnostics."),
      ("Is there an official Google Ads connector in Claude's directory?",
       "Not currently. Google publishes an open-source Google Ads API MCP server for developers, but Claude's connector directory has no first-party Google Ads, GA4 or Meta Ads connector."),
      ("Is it safe to let AI change my tracking setup?",
       "Keep changes in a GTM workspace draft, test them in Preview mode, and verify that conversions arrive correctly in each platform before and after publishing."),
    ],
    sources=[
      ("PPC Land: Meta opens its ad system to Claude and ChatGPT with new AI connectors", "https://ppc.land/meta-opens-its-ad-system-to-claude-and-chatgpt-with-new-ai-connectors/"),
      ("Google Ads Developer Blog: Open Source Google Ads API MCP Server (October 7, 2025)", "https://developers.google.com/ads/blog/posts/2025/10/open-source-google-ads-api-mcp-server"),
      ("Google Ads API: Google Ads MCP server developer guide", "https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server"),
      ("Search Engine Land: Google open-sources ads API MCP server", "https://searchengineland.com/google-open-sources-ads-api-mcp-server-463219"),
    ],
  ),
  dict(
    slug="amazon-black-friday-ads-chatgpt",
    date="2026-11-25",
    modified="2026-11-25",
    platform="ChatGPT Ads",
    title="Amazon is running Black Friday ads in ChatGPT",
    seo_title="Amazon Runs Black Friday Ads in ChatGPT (US): Format & What's Unclear",
    description="According to Digiday, Amazon is running a new round of Black Friday ads in ChatGPT in the US, in ChatGPT's standard ad format. It's unclear whether the ads were bought directly from OpenAI or through Amazon DSP.",
    image=None,
    takeaways=[
      "Digiday reports that Amazon is running a new round of Black Friday ads in ChatGPT in the US.",
      "The ads use ChatGPT's standard format, separate from the conversation, with a favicon, headline, description and “Learn more” button.",
      "It's unclear whether Amazon bought them directly from OpenAI or through Amazon DSP.",
      "Amazon and OpenAI declined to comment.",
    ],
    body="""
<p>Amazon is running a new round of <strong>Black Friday ads in ChatGPT</strong> in the US, according to <strong>Digiday</strong>, which reported on <strong>November 24, 2026</strong> that it had seen the ads. Neither company has confirmed it: Amazon and OpenAI both declined to comment on Digiday's article.</p>

<h2>What the ads look like</h2>
<ul>
  <li><strong>Format:</strong> the same format as typical ChatGPT ads, separate from the user conversation, with a favicon, headline, description and a “Learn more” call to action.</li>
  <li><strong>Content:</strong> the ads promote Amazon Black Friday deals.</li>
  <li><strong>Destination:</strong> they direct users to Amazon to complete their purchases.</li>
  <li><strong>Market:</strong> the US.</li>
</ul>

<h2>How Amazon bought the ads is unclear</h2>
<p>Digiday says it is unclear whether Amazon bought its ChatGPT ads <strong>directly from OpenAI</strong> or through its own <strong>Amazon DSP</strong>.</p>
<p>In September, Amazon Ads announced a partnership that lets advertisers buy ChatGPT inventory through Amazon DSP. According to Digiday, the integration initially gives <strong>select US advertisers</strong> access to ChatGPT's ad inventory.</p>

<h2>ChatGPT's shopping results</h2>
<p>Separately from the ads, Digiday reports that ChatGPT's shopping experience links to Amazon search results, drawing on third-party deal-tracking websites to identify products, discounts and up-to-date pricing.</p>

<h2>How ChatGPT ads can be bought</h2>
<p>For more on buying options in ChatGPT, see our <a href="/chatgpt-ads.html">ChatGPT Ads page</a>.</p>
""",
    faq=[
      ("Is Amazon advertising in ChatGPT?",
       "According to Digiday, which saw the ads, Amazon is running Black Friday ads in ChatGPT in the US. Amazon and OpenAI declined to comment."),
      ("What do the Amazon ads in ChatGPT look like?",
       "They use ChatGPT's standard ad format: separate from the conversation, with a favicon, headline, description and a “Learn more” call to action."),
      ("Can advertisers buy ChatGPT ads through Amazon DSP?",
       "Amazon Ads announced in September a partnership that initially gives select US advertisers access to ChatGPT's ad inventory through Amazon DSP."),
    ],
    sources=[
      ("Digiday: Amazon is buying ChatGPT ads (November 24, 2026)", "https://digiday.com/marketing/amazon-is-buying-chatgpt-ads-while-blocking-openai-crawlers/"),
    ],
  ),
  dict(
    slug="microsoft-advertising-pinterest-integration",
    date="2026-11-24",
    modified="2026-11-24",
    platform="Microsoft Ads",
    title="Microsoft Advertising campaigns are coming to Pinterest",
    seo_title="Microsoft Advertising x Pinterest Integration: Where Ads Run, Markets & Details",
    description="Pinterest and Microsoft Advertising announced an integration that lets eligible Microsoft Advertising campaigns extend to Pinterest's home feed, search and related Pins, starting in North America, Australia and New Zealand, without new buying tools.",
    image=None,
    takeaways=[
      "Eligible Microsoft Advertising campaigns can extend to Pinterest's visual search and shopping inventory.",
      "Ads run in Pinterest's open-auction inventory across the home feed, search and related Pins.",
      "No new buying tools are required: advertisers use their usual Microsoft buying and measurement workflows.",
      "The integration starts in North America, Australia and New Zealand.",
    ],
    body="""
<p>Pinterest announced on <strong>November 23, 2026</strong> a new integration with <strong>Microsoft Advertising</strong>. It lets Microsoft Advertising customers extend eligible campaigns to Pinterest's visual search and shopping inventory, without new buying tools.</p>

<h2>How the integration works</h2>
<ul>
  <li><strong>Inventory:</strong> Pinterest's open-auction inventory across the <strong>home feed, search and related Pins</strong>.</li>
  <li><strong>Bidding:</strong> Pinterest describes a custom contextual bidding model built on Pinterest search queries, contextual signals and first-party intent data.</li>
  <li><strong>Buying:</strong> no new buying tools are needed. The integration runs on programmatic infrastructure, and advertisers use familiar buying and measurement workflows.</li>
  <li><strong>Demand:</strong> comes from Microsoft's first-party ecosystem, which Pinterest lists as Bing, MSN, Xbox, Microsoft Casual Games and Microsoft Outlook.</li>
  <li><strong>Markets:</strong> “The integration will be available in North America, Australia, and New Zealand to start.”</li>
</ul>

<h2>What Pinterest and Microsoft said</h2>
<p>Jason Fairchild, GM of Programmatic and Affiliate at Pinterest: <em>“We're bringing premium inventory and Pinterest intent signals into the workflows advertisers already use.”</em></p>
<p>Jason Mckay, general manager of Microsoft Advertising Global Partnerships, said the integration lets advertisers <em>“extend campaigns into Pinterest inventory using familiar buying and measurement workflows.”</em></p>

<h2>Pinterest's audience numbers</h2>
<div class="tbl"><table>
  <thead><tr><th>Metric</th><th>Pinterest's figure</th></tr></thead>
  <tbody>
    <tr><td>Monthly active users</td><td>661 million</td></tr>
    <tr><td>Monthly searches</td><td>80 billion, more than half with commercial intent</td></tr>
    <tr><td>Unbranded text searches</td><td>More than 96%</td></tr>
  </tbody>
</table></div>

<h2>What is not specified yet</h2>
<ul>
  <li><strong>Eligible campaign types:</strong> the announcement says “eligible Microsoft Advertising campaigns” but does not name which ones.</li>
  <li><strong>Opt-in or opt-out:</strong> not addressed.</li>
  <li><strong>Reporting:</strong> the announcement mentions familiar measurement tools, but no placement-level reporting details.</li>
  <li><strong>Other markets:</strong> no dates beyond the starting markets.</li>
</ul>
""",
    faq=[
      ("Can Microsoft Ads campaigns run on Pinterest?",
       "Pinterest and Microsoft Advertising announced an integration that lets eligible Microsoft Advertising campaigns extend to Pinterest's home feed, search and related Pins. Pinterest says it will be available in North America, Australia and New Zealand to start."),
      ("Where is the Microsoft Advertising and Pinterest integration available?",
       "In North America, Australia and New Zealand to start."),
      ("Do I need a Pinterest Ads account or a new tool?",
       "Pinterest says the integration works without requiring new buying tools, using familiar Microsoft buying and measurement workflows."),
      ("Which Microsoft campaign types are eligible?",
       "The announcement refers to “eligible Microsoft Advertising campaigns” without naming specific campaign types."),
    ],
    sources=[
      ("Pinterest Newsroom: Pinterest and Microsoft Advertising integration (November 23, 2026)", "https://newsroom.pinterest.com/news/pinterest-microsoft-advertising-integration-2026/"),
    ],
  ),
  dict(
    slug="youtube-shorts-ads-likes-engaged-view-conversions",
    date="2026-11-23",
    modified="2026-11-23",
    platform="Google Ads",
    title="YouTube Shorts ads: a like, comment or share now counts for engaged-view conversions",
    seo_title="YouTube Shorts Ads: Likes, Comments & Shares Now Count for Engaged-View Conversions",
    description="Google now counts a like, comment or share on a YouTube Shorts ad the same way as 5 seconds of viewing when deciding whether a later conversion gets engaged-view credit. Here's what changed and how other Shorts metrics count.",
    image=None,
    takeaways=[
      "A like, comment or share on a YouTube Shorts ad now qualifies for an engaged-view conversion (EVC), like 5 seconds of viewing or a call-to-action click.",
      "The viewer still has to convert within the engaged-view conversion window.",
      "Likes, comments and shares also count as engagements and TrueView views on Shorts ads.",
      "In Video view campaigns billed per view, those interactions can be billable events.",
    ],
    body="""
<p>Google has changed what it takes for a <strong>YouTube Shorts ad</strong> to earn an <strong>engaged-view conversion (EVC)</strong>. A like, comment or share on the ad now counts the same way as five seconds of viewing. The change appears in Google's help page “About YouTube ads and view metrics”, and was reported this week by PPC Land and by Adriaan Dekker.</p>

<h2>The new engaged-view conversion definition</h2>
<p>Google's help page now reads: <em>“YouTube Shorts engaged view conversion (EVC) counted, when a viewer watches 5 seconds of the ad, clicks the call-to-action on the video ad, or the user clicks the like, comment, or share button on the video ad, and then converts within the Engaged-view conversion window.”</em></p>
<div class="tbl"><table>
  <thead><tr><th>Engaged-view conversion on Shorts</th><th>Before</th><th>Now</th></tr></thead>
  <tbody>
    <tr><td>Viewer watches 5 seconds</td><td>Yes</td><td>Yes</td></tr>
    <tr><td>Viewer clicks the call-to-action</td><td>Yes</td><td>Yes</td></tr>
    <tr><td>Viewer likes, comments or shares</td><td>No</td><td>Yes</td></tr>
  </tbody>
</table></div>
<p>In all cases, the viewer must then convert within the engaged-view conversion window.</p>

<h2>Other Shorts metrics</h2>
<p>Google's help page also lists likes, comments and shares for these Shorts ad metrics:</p>
<ul>
  <li><strong>Engagements:</strong> counted when viewers watch 5 seconds, click the call-to-action, or click like, comment or share.</li>
  <li><strong>TrueView views:</strong> counted when a viewer watches 10 seconds or until the end of the video (whichever comes first), clicks the call-to-action, or clicks like, comment or share.</li>
  <li><strong>Billing:</strong> according to Google's FAQ, “For Video View campaigns billed to views, views, clicks on the like, comment, or share button would become billable events.”</li>
</ul>

<h2>What it means for reporting</h2>
<p>Because more interactions now qualify, Shorts ads can record more engaged-view conversions than before for the same activity. When comparing EVC numbers before and after the change, the new definition is a factor to take into account.</p>
""",
    faq=[
      ("What is an engaged-view conversion on YouTube Shorts?",
       "A conversion counted when a viewer watches 5 seconds of a Shorts ad, clicks its call-to-action, or clicks like, comment or share, and then converts within the engaged-view conversion window."),
      ("Does a like on a Shorts ad count as a view?",
       "Yes. On Shorts ads, a TrueView view is counted when a viewer clicks the like, comment or share button, as well as after 10 seconds of viewing (or the full video if shorter) or a call-to-action click."),
      ("Can likes on Shorts ads cost money?",
       "In Video view campaigns billed per view, Google says clicks on the like, comment or share button can become billable events."),
    ],
    sources=[
      ("Google Ads Help: About YouTube ads and view metrics", "https://support.google.com/google-ads/answer/2375431"),
      ("Google Ads Help: Frequently asked questions", "https://support.google.com/google-ads/answer/16041383"),
      ("PPC Land: Google lets a like stand in for 5 seconds of viewing in Shorts conversions", "https://ppc.land/google-lets-a-like-stand-in-for-5-seconds-of-viewing-in-shorts-conversions/"),
    ],
  ),
  dict(
    slug="google-ads-under-re-review-status",
    date="2026-11-22",
    modified="2026-11-22",
    platform="Google Ads",
    title="Google explains the “Under re-review” ad status: why approved ads stop serving",
    seo_title="Google Ads “Under re-review” Status Explained: Triggers, Duration & Appeals",
    description="Google has updated its policy documentation to explain the “Under re-review” status: previously approved ads can be re-reviewed when the ad, landing page or account is flagged. The ads show “Eligible (limited)” and don't serve, typically for up to 48 hours.",
    image=None,
    takeaways=[
      "Previously approved ads or assets can be re-reviewed if they, their landing page or the associated account get flagged.",
      "During a re-review, the ad shows as “Eligible (limited)” and does not serve.",
      "Re-reviews typically conclude within 48 hours, though this is not guaranteed.",
      "The re-review itself can't be appealed, because it is not a policy decision. A resulting disapproval or suspension can be.",
    ],
    body="""
<p>Google has updated its policy documentation to explain the <strong>“Under re-review”</strong> ad status, according to PPC News Feed, which reported the change on <strong>November 21, 2026</strong>. The update was spotted by Hana Kobzová. The status itself is not new: advertisers first spotted it in their accounts in August 2026. What's new is Google's official explanation.</p>

<h2>What triggers a re-review</h2>
<p>Ads and assets that were already approved can be reviewed again. According to the updated documentation, a re-review can happen when any of these gets flagged:</p>
<ul>
  <li>the <strong>ad or asset</strong> itself</li>
  <li>its <strong>destination</strong> (the landing page)</li>
  <li>the <strong>associated account</strong></li>
</ul>

<h2>What happens during the re-review</h2>
<div class="tbl"><table>
  <thead><tr><th>Question</th><th>Answer</th></tr></thead>
  <tbody>
    <tr><td>Which status is shown?</td><td>“Eligible (limited)”</td></tr>
    <tr><td>Does the ad serve?</td><td>No. Ads under re-review do not serve.</td></tr>
    <tr><td>How long does it take?</td><td>Re-reviews typically conclude within 48 hours. This is typical, not guaranteed.</td></tr>
    <tr><td>Can I appeal?</td><td>Not the re-review itself, because it is not a policy decision. If it ends in a disapproval or suspension, those decisions can be appealed.</td></tr>
  </tbody>
</table></div>

<h2>Why it matters this week</h2>
<p>Black Friday falls on <strong>November 27, 2026</strong>. Because an ad under re-review does not serve while it shows “Eligible (limited)”, an approved ad can stop delivering without being disapproved, and there is no appeal to speed it up.</p>

<h2>How to check your ads</h2>
<ol>
  <li>In Google Ads, open <strong>Campaigns → Ads</strong> (or <strong>Assets</strong>) and look at the <strong>Status</strong> column.</li>
  <li>Hover over an “Eligible (limited)” status to see the reason: it can mean a re-review or a policy restriction, such as location or age limits.</li>
  <li>If an ad or asset is under re-review, there is no appeal for the re-review itself. If it ends in a disapproval, you can fix the ad or appeal the decision from the <strong>Policy manager</strong>.</li>
</ol>
""",
    faq=[
      ("What does “Under re-review” mean in Google Ads?",
       "A previously approved ad or asset is being reviewed again because the ad, its landing page or the associated account was flagged."),
      ("Does an ad under re-review still serve?",
       "No. During the re-review the ad shows “Eligible (limited)” and does not serve."),
      ("How long does a Google Ads re-review take?",
       "Re-reviews typically conclude within 48 hours, but this is not guaranteed."),
      ("Can I appeal a re-review?",
       "No. The re-review is not a policy decision, so it can't be appealed. If it ends in a disapproval or suspension, you can appeal that decision."),
    ],
    sources=[
      ("PPC News Feed: Google explains “Under re-review” ad status (November 21, 2026)", "https://ppcnewsfeed.com/ppc-news/2026-11/google-explains-under-re-review-ad-status/"),
      ("Google Ads Help: About the ad review process", "https://support.google.com/adspolicy/answer/1722120"),
    ],
  ),
  dict(
    slug="microsoft-ads-bing-ai-overviews-november-2026",
    date="2026-11-20",
    modified="2026-11-20",
    platform="Microsoft Ads",
    title="Microsoft Ads now shows ads in Bing's AI Overviews, plus 5 more November updates",
    seo_title="Microsoft Ads in Bing AI Overviews + What's New in November 2026",
    description="Ads in AI Overviews on Bing are now available in all markets except China, served through existing campaigns including Performance Max and AI Max. Plus AI Max URL inclusions, Discover feed ads, AI content labels, Xbox Video for Brands and the Microsoft Advertising MCP server.",
    image=None,
    takeaways=[
      "Ads can now appear next to AI Overviews on Bing, in all markets except China.",
      "No separate campaign is needed: ads serve through existing campaigns, including Performance Max and AI Max.",
      "AI Max now supports URL inclusions, to choose which site sections it can use.",
      "AI content transparency controls, to declare AI-generated images and videos, are generally available.",
      "Microsoft also announced ads in its new Discover feed and Xbox Video for Brands.",
    ],
    body="""
<p>Microsoft Advertising published its monthly product update on <strong>November 19, 2026</strong>. The biggest change: <strong>ads in AI Overviews on Bing</strong> are now available in all markets except China. Here is everything in the update.</p>

<h2>Ads in AI Overviews on Bing</h2>
<p>AI Overviews are AI-generated summaries in Bing search results. Ads can now appear next to them when an advertiser's offer is relevant. Microsoft's example: a travel offer shown beside an AI-generated itinerary for Snowdonia National Park.</p>
<ul>
  <li><strong>Markets:</strong> “Ads in AI Overviews are now available in all markets except China.”</li>
  <li><strong>Campaigns:</strong> no separate campaign setup is required. Ads serve through existing campaigns, including <strong>Performance Max</strong> and <strong>AI Max</strong>.</li>
  <li><strong>Context:</strong> the placement follows <strong>ads in Copilot</strong>, Microsoft's ads in its AI assistant.</li>
  <li><strong>Not covered in the announcement:</strong> reporting for the placement and specific ad formats.</li>
</ul>

<h2>AI Max URL inclusions</h2>
<p>Rolling out now. Advertisers can specify which sections of their website AI Max can use, both as traffic destinations and as sources for ad text and search term matching. Microsoft's example: adding holiday gift guide pages. It builds on the messaging guidelines Microsoft added to AI Max in October 2026.</p>

<h2>Ads in Discover</h2>
<p>Discover is Microsoft's new AI-powered content feed on the Microsoft Edge desktop new tab page and in Windows. According to Microsoft:</p>
<ul>
  <li>It is backed by trusted publishers and more than 3,500 creators.</li>
  <li>It shows 35% fewer ads per page than classic MSN (October 2026 internal data).</li>
  <li>Ads in Discover show 35% higher viewability and 8–12% higher click-through rates.</li>
  <li>It is live in the US, Canada, UK, Australia and India. Advertisers should contact their account team.</li>
</ul>

<h2>AI content transparency controls</h2>
<p>Now generally available. Advertisers can declare whether images or videos are AI-generated and choose a visible watermark where supported.</p>
<ul>
  <li>Declarations can be managed in bulk through the Ads Studio Library, the APIs and product feeds.</li>
  <li>Microsoft's AI detection signals are available as a reference, but advertisers remain responsible for their declarations.</li>
  <li>Covered: Product Ads, Multimedia Ads, Audience Ads, Display Ads, Video Ads and Performance Max assets.</li>
</ul>

<h2>Xbox Video for Brands</h2>
<p>Introduced earlier in November: full-screen, non-skippable video ads that play before cloud gaming sessions and help eligible players unlock access, without interrupting active gameplay. Advertisers can reuse existing premium video or CTV creative.</p>

<h2>Microsoft Advertising MCP server</h2>
<p>The MCP server connects AI assistants such as Copilot, ChatGPT and Claude to a Microsoft Advertising account, to ask plain-language questions about performance, creative, conversion tracking, targeting and policy reviews, and to make account changes. It has been in open pilot since July 2026.</p>

<h2>Automated bidding upgrade</h2>
<p>The update also recaps the bidding upgrade announced earlier in the week: bids meet CPA and ROAS targets more consistently, adjust nearly twice as fast after target changes, and pace budgets more evenly. <a href="/blog/microsoft-ads-automated-bidding-upgrade.html">Read our full article on the bidding upgrade</a>.</p>
""",
    faq=[
      ("Where are ads in AI Overviews on Bing available?",
       "In all markets except China, according to Microsoft Advertising's November 2026 update."),
      ("Do I need a new campaign to show ads in Bing AI Overviews?",
       "No. Microsoft says no separate campaign setup is required. Ads serve through existing campaigns, including Performance Max and AI Max."),
      ("What are AI Max URL inclusions?",
       "A setting that lets advertisers choose which sections of their website AI Max can use as landing pages and as sources for ad text and search term matching."),
      ("Where is Microsoft's Discover feed available?",
       "On the Microsoft Edge desktop new tab page and in Windows, live in the US, Canada, UK, Australia and India."),
    ],
    sources=[
      ("Microsoft Advertising blog: What's new in Microsoft Advertising this November", "https://about.ads.microsoft.com/en/blog/post/november-2026/put-ai-to-work-engaging-customers-in-more-places-whats-new-in-microsoft-advertising-this-november"),
    ],
  ),
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
