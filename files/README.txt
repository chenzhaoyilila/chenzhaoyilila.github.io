FILES PAGE — 资料页管理说明
================================================================

The Files page (files.html) lists your PDFs and Markdown notes in two
separate groups. You only drop files into two folders and run one command.

资料页（files.html）把 PDF 和 Markdown 笔记分成两组展示。
你只需要把文件放进两个文件夹，然后运行一条命令。


----------------------------------------------------------------
WHERE FILES GO — 文件放哪里
----------------------------------------------------------------

  files/pdf/    PDF documents   PDF 文档
  files/md/     Markdown notes  Markdown 笔记

Nothing else in files/ is listed. 只有这两个文件夹里的文件会被列出。


----------------------------------------------------------------
ADD / UPDATE / REMOVE — 增加、更新、删除
----------------------------------------------------------------

1. Put the file in the right folder (or edit / delete it there).
   把文件放进对应文件夹（或者在里面修改、删除）。

2. Rebuild the list 重新生成列表:
       python3 build_files.py

3. Check it locally 本地检查:
       http://localhost:5510/files.html

4. Publish 发布:
       git add -A && git commit -m "Update files" && git push
   Live in about a minute. 大约一分钟后上线。

Always rerun build_files.py after any change — the page reads the generated
content/files.json, not the folders themselves. A file you add without
rebuilding will not appear; a file you delete without rebuilding leaves a
broken link.
每次改动后都要重新运行 build_files.py —— 页面读的是生成的
content/files.json，而不是文件夹本身。只加文件不生成，页面上不会出现；
只删文件不生成，页面上会留下一个失效链接。


----------------------------------------------------------------
TITLES AND DATES — 标题与日期
----------------------------------------------------------------

The filename becomes the title. Hyphens and underscores turn into spaces,
and Chinese filenames work fine.
文件名就是标题。连字符和下划线会变成空格，中文文件名也没问题。

  2026-09-25-game-theory-notes.pdf  ->  "game theory notes", 2026-09-25
  博弈论笔记.pdf                     ->  "博弈论笔记", file's modified date

An optional YYYY-MM-DD- prefix sets the date. Without it, the date is the
file's last-modified date. Newest files are listed first.
文件名开头可选加 YYYY-MM-DD- 作为日期；不加则使用文件的修改日期。
最新的排在最前面。

Markdown notes can override this with front matter at the top:
Markdown 笔记也可以在开头用 front matter 指定：

    ---
    title: 纳什均衡读书笔记
    date: 2026-09-25
    excerpt: One line shown under the title in the list.
    ---

If there is no `title:`, a first line like `# My Title` becomes the title.
没有写 title 的话，第一行的 `# 标题` 会被当作标题。


----------------------------------------------------------------
IMAGES IN NOTES — 笔记里的图片
----------------------------------------------------------------

Keep images next to the note and link them relatively, the same way
Typora, Obsidian and VS Code preview expects:
图片放在笔记旁边，用相对路径引用 —— 和 Typora、Obsidian、VS Code
预览的习惯一致：

    files/md/nash-notes.md
    files/md/images/payoff-matrix.png

    ![Payoff matrix](images/payoff-matrix.png)

build_files.py rewrites these so they also work on the website.
build_files.py 会自动改写路径，让它们在网站上也能正常显示。


----------------------------------------------------------------
BEFORE YOU PUBLISH — 发布前请确认
----------------------------------------------------------------

This repository is PUBLIC. Every file in files/ can be downloaded by
anyone, even if you never link to it.
这个仓库是公开的。files/ 里的每个文件任何人都能下载，即使你没有链接它。

  * Only your own work, or work you have the right to share.
    NOT textbooks, lecture scripts, paywalled papers, or course slides.
    只放你自己的作品，或你有权分享的内容。
    不要放教科书、讲义、付费论文、课程幻灯片。

  * No personal data — yours or anyone else's (IDs, addresses, grades).
    不要包含个人信息 —— 你的或他人的（证件号、住址、成绩等）。

  * Unsubmitted thesis drafts: see the plagiarism-check caveat — publishing
    early can make a checker flag your own text as copied.
    未提交的论文草稿：提前公开可能导致查重系统把你自己的文字判为抄袭。

  * Size: GitHub rejects any single file over 100 MB. Keep large PDFs
    compressed; every visitor downloads them in full.
    大小：单个文件超过 100 MB 会被 GitHub 拒绝。大 PDF 请先压缩，
    访客每次都要完整下载。

  * Deleting a file removes it from the site, but it stays in git history.
    If something sensitive was pushed, ask for help removing it properly.
    删除文件会让它从网站消失，但它仍留在 git 历史里。
    如果误传了敏感内容，需要专门清理历史。


----------------------------------------------------------------
NOTES — 备注
----------------------------------------------------------------

* PDFs elsewhere in the project stay blocked by .gitignore; only
  files/pdf/*.pdf is allowed through. 项目中其他位置的 PDF 仍被
  .gitignore 屏蔽，只有 files/pdf/ 里的会被提交。
* Don't hand-edit content/files.json; it is overwritten on every build.
  不要手改 content/files.json，每次生成都会覆盖。
* Two notes that end up with the same id stop the build with an error
  naming both; rename one or give it a `slug:`.
  两篇笔记的 id 重复时，脚本会报错并指出两个文件名；改名或加 slug 即可。
