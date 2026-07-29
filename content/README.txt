THOUGHTS / DIARY / NEWSLETTER — HOW TO ADD CONTENT
随笔 / 日记 / 通讯 —— 如何添加内容
================================================================

------------------------------------------------------------
ENGLISH
------------------------------------------------------------

1) MAIN DATA FILE
   Edit:  content/posts.json

   Each item in the "posts" array can include:
     - slug        (required) URL-safe id, e.g. "my-weekly-note"
     - title       (required)
     - date        (optional) e.g. "2026-04-04"
     - excerpt     short text shown on the home-page card
     - tags        optional array of strings.
                   Include "newsletter" so the post shows up when a visitor
                   clicks "Newsletter" (hero, nav, or the newsletter block).
     - coverImage  optional card thumbnail, e.g. "content/images/cover.jpg"
     - bodyHtml    full article HTML for the detail page (thought.html?slug=...)

   Add a post by copying an existing block and changing slug + fields.
   Keep valid JSON: commas between objects, double quotes for strings,
   and escape any double quote inside bodyHtml as  \"

2) IMAGES
   Put image files in:  content/images/
   Reference them in bodyHtml or coverImage as:
     content/images/yourphoto.jpg

3) PREVIEW
   Open the site with a local server (e.g. Live Server), NOT file://,
   so the browser is allowed to load content/posts.json.

4) DETAIL PAGE
   Home -> Thoughts section -> click a card -> thought.html?slug=YOUR_SLUG

5) SHARE A NEWSLETTER-ONLY VIEW
   index.html?view=newsletter#thoughts
   (opens the page with the Newsletter filter already on)

NOTE: The 中/EN toggle switches the site's own labels (nav, buttons, headings).
Your post text (title, excerpt, bodyHtml) shows exactly as you write it in
posts.json — write each post in whichever language you want.

------------------------------------------------------------
中文
------------------------------------------------------------

1) 主数据文件
   编辑：  content/posts.json

   "posts" 数组中的每一项可以包含：
     - slug        （必填）URL 安全的编号，例如 "my-weekly-note"
     - title       （必填）标题
     - date        （可选）日期，例如 "2026-04-04"
     - excerpt     首页卡片上显示的简短摘要
     - tags        （可选）字符串数组。
                   加入 "newsletter" 后，访客点击 “Newsletter / 通讯”
                   （首页大按钮、导航或通讯板块）时就会显示这篇文章。
     - coverImage  （可选）卡片缩略图，例如 "content/images/cover.jpg"
     - bodyHtml    详情页（thought.html?slug=...）的完整文章 HTML

   复制一个已有的代码块、修改 slug 和各字段，即可添加新文章。
   请保持 JSON 合法：对象之间用逗号分隔、字符串用双引号；
   bodyHtml 内部的双引号要转义为  \"

2) 图片
   把图片文件放在：  content/images/
   在 bodyHtml 或 coverImage 中这样引用：
     content/images/yourphoto.jpg

3) 预览
   请使用本地服务器（如 Live Server）打开网站，不要用 file://，
   否则浏览器无法加载 content/posts.json。

4) 详情页
   首页 -> 随笔板块 -> 点击卡片 -> thought.html?slug=你的SLUG

5) 分享“仅通讯”视图
   index.html?view=newsletter#thoughts
   （打开后会自动应用 Newsletter 筛选）

说明：中/EN 切换按钮只切换网站自身的标签（导航、按钮、标题）。
文章内容（title、excerpt、bodyHtml）会原样显示你在 posts.json 中写的文字，
所以每篇文章可以用你想要的任意语言来写。
