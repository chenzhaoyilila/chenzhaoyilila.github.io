---
title: 这是一篇草稿（示例）
date: 2026-08-26
tags: [日记]
draft: true
---

这篇文章的 front matter 里写了 `draft: true`，所以它**只存在于你本地**。

- 它不会出现在 `content/posts.json` 里
- 因此就算你 commit + push，它也不会上线
- 只有把 `draft: true` 改成 `draft: false`，它才会被发布

确认这篇可以发布之后，改掉那一行，重新跑一次 `python3 build_posts.py` 就好。

> 检查完这套流程之后，可以直接删掉这个示例文件。
