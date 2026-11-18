# Channel (service) pages: zenshindigital.com/<slug>.html
# Facts only. Product names must match the platforms' own current naming. The "Latest news"
# section is filled automatically from blog posts whose `platform` equals `platform` below.
# `reviewed`: date the evergreen text was last checked against the platform's official pages.

CHANNELS = [
  dict(
    slug="google-ads",
    platform="Google Ads",
    reviewed="2026-11-19",
    seo_title="Google Ads Management: Search, Performance Max, YouTube & AI Max",
    description="Google Ads management by Zenshin Digital: Search with AI Max, Performance Max, Shopping, Demand Gen and YouTube campaigns, set up and optimised by ex-Google specialists.",
    h1="Google Ads <em>Management</em>",
    lede="Reach people at the moment they search, shop and watch, across Google Search, Shopping, YouTube, Gmail, Discover and the Display Network.",
    manage=[
      ("Search & AI Max", "Search campaigns that capture high-intent queries, including AI Max for Search with its search term matching and final URL expansion."),
      ("Performance Max", "One campaign across all Google channels, driven by your conversion goals, audience signals and creative assets."),
      ("Shopping", "Product ads from your Merchant Center feed, with feed quality and product structure set up for profitable sales."),
      ("Demand Gen", "Visual ads on YouTube, Discover and Gmail to create demand and reach new audiences."),
      ("YouTube / Video", "Video campaigns for awareness, consideration and conversions on YouTube and Google video partners."),
      ("Tracking & Measurement", "Conversion tracking with Google Tag and Enhanced Conversions, so bidding optimises for real results."),
    ],
    faq=[
      ("Is there a minimum budget for Google Ads?", "Google Ads has no minimum spend. You set a daily budget per campaign and can change or pause it at any time."),
      ("What is AI Max for Search?", "AI Max for Search is a set of features for Search campaigns that uses Google AI to match more search terms, customise ad text and choose the best landing page on your site."),
      ("What is Performance Max?", "Performance Max is a goal-based campaign type that runs across all Google Ads channels from a single campaign, including Search, YouTube, Display, Discover, Gmail and Maps."),
    ],
  ),
  dict(
    slug="meta-ads",
    platform="Meta Ads",
    reviewed="2026-11-19",
    seo_title="Meta Ads Management: Facebook & Instagram Ads, Advantage+",
    description="Meta Ads management by Zenshin Digital: Facebook, Instagram, Messenger and Threads campaigns with Advantage+, creative testing and Conversions API tracking, by ex-Meta specialists.",
    h1="Meta Ads <em>Management</em>",
    lede="Grow on Facebook, Instagram, Messenger and Threads with campaigns built around strong creative, clean conversion data and Meta's AI.",
    manage=[
      ("Advantage+ Campaigns", "Meta's AI-driven campaign setup for sales, leads and app installs, with automated targeting, budget and placements."),
      ("Creative Testing", "Image, video and carousel ads, flexible format ads and existing posts, tested systematically to find what drives results."),
      ("Lead Generation", "Instant Forms and website lead campaigns, with lead quality tracked back to your CRM."),
      ("Retargeting & Audiences", "Website, app and engagement audiences, used alongside Advantage+ audience."),
      ("Conversions API", "Server-side tracking with the Meta Pixel and Conversions API for more reliable measurement."),
      ("Reporting", "Clear reporting on the results that matter for your business, not only platform metrics."),
    ],
    faq=[
      ("Where do Meta ads appear?", "Meta ads can appear on Facebook, Instagram, Messenger, Threads and the Audience Network, depending on the placements selected."),
      ("Is there a minimum budget for Meta Ads?", "There is no minimum commitment. You set a daily or lifetime budget per campaign or ad set, and can change or pause it at any time."),
      ("What is the Conversions API?", "The Conversions API sends conversion events from your server directly to Meta. Used with the Meta Pixel, it makes measurement more reliable."),
    ],
  ),
  dict(
    slug="amazon-ads",
    platform="Amazon Ads",
    reviewed="2026-11-19",
    seo_title="Amazon Ads Management: Sponsored Products, Brands, Display & DSP",
    description="Amazon Ads management by Zenshin Digital: Sponsored Products, Sponsored Brands, Sponsored Display and Amazon DSP campaigns, built for profitable growth on Amazon and beyond.",
    h1="Amazon Ads <em>Management</em>",
    lede="Win the moment shoppers search on Amazon, and reach audiences on Amazon's streaming, publishing and third-party inventory.",
    manage=[
      ("Sponsored Products", "Ads for individual products in Amazon search results and on product pages, structured for profitable ACoS and TACoS."),
      ("Sponsored Brands", "Brand ads with your logo, headline and products or video, linking to your Brand Store or product pages."),
      ("Sponsored Display", "Display ads that reach relevant shoppers on and off Amazon, based on their shopping activity."),
      ("Amazon DSP", "Programmatic display, video and audio ads using Amazon's audience data, also available to brands that don't sell on Amazon."),
      ("Streaming TV", "Video ads on Prime Video and other Amazon streaming placements."),
      ("Policy & Creative Compliance", "Ad copy and creatives checked against Amazon Ads policies, to avoid rejections."),
    ],
    faq=[
      ("Do I need to sell on Amazon to advertise?", "For Sponsored Products and Sponsored Brands, yes: you need to be a seller or vendor on Amazon. Amazon DSP and some other formats are also available to brands that don't sell on Amazon."),
      ("What is the difference between ACoS and TACoS?", "ACoS is ad spend divided by ad-attributed sales. TACoS is ad spend divided by total sales, including organic sales."),
      ("Can I write prices in my Amazon ads?", "On Amazon retail placements, numerical prices or savings are only allowed when Amazon renders them dynamically in the ad. See our article on Amazon's pricing policy update."),
    ],
  ),
  dict(
    slug="linkedin-ads",
    platform="LinkedIn Ads",
    reviewed="2026-11-19",
    seo_title="LinkedIn Ads Management: B2B Lead Generation & Thought Leader Ads",
    description="LinkedIn Ads management by Zenshin Digital: Sponsored Content, Thought Leader Ads, Lead Gen Forms and Conversation Ads that reach decision-makers by job title, company and industry.",
    h1="LinkedIn Ads <em>Management</em>",
    lede="Reach decision-makers by job title, seniority, company and industry, and turn them into qualified B2B leads.",
    manage=[
      ("Sponsored Content", "Single image, video, carousel and document ads in the LinkedIn feed."),
      ("Thought Leader Ads", "Promote posts from your founders and employees to reach a wider professional audience."),
      ("Lead Gen Forms", "Pre-filled LinkedIn forms that capture leads without leaving the platform, synced to your CRM."),
      ("Conversation & Message Ads", "Direct messages in LinkedIn inboxes, for events, demos and offers."),
      ("Account-Based Targeting", "Company lists and matched audiences to focus spend on your target accounts."),
      ("Insight Tag & CAPI", "Conversion tracking with the LinkedIn Insight Tag and Conversions API."),
    ],
    faq=[
      ("Who can I target on LinkedIn?", "LinkedIn lets you target by professional attributes such as job title, job function, seniority, company, company size and industry, as well as by your own matched audiences."),
      ("What are Thought Leader Ads?", "Thought Leader Ads let a company promote posts published by its employees or other members, from their personal profiles."),
      ("What are Lead Gen Forms?", "Lead Gen Forms are forms pre-filled with a member's LinkedIn profile data, so people can submit their details without leaving LinkedIn."),
    ],
  ),
]
