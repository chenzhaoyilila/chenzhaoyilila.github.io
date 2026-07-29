WHERE TO PUT YOUR PDF FILES  ·  简历 PDF 放在哪里
================================================================

------------------------------------------------------------
ENGLISH
------------------------------------------------------------

1) MAIN FILE
   Put your resume PDF in THIS folder (the same folder as index.html):

     Live_Server_Web/
       index.html
       resume.html
       resume.pdf        <-- your resume, named exactly "resume.pdf"

   The viewer page (resume.html) loads:
     - iframe:            resume.pdf
     - "Open in new tab": resume.pdf

   So the filename must be exactly  resume.pdf
   (or rename your file and update resume.html — search for "resume.pdf").

2) HOW VISITORS OPEN IT
   On the home page, the hero button "View PDF / 查看简历" opens resume.html.
   There is no PDF link in the top-right nav.

3) ADD MORE PDFs LATER
   - Copy extra PDFs into this same folder, e.g. portfolio.pdf
   - Edit resume.html: duplicate the iframe / link blocks, or add a list of links.

------------------------------------------------------------
中文
------------------------------------------------------------

1) 主文件
   把简历 PDF 放在“本文件夹”中（与 index.html 同一层）：

     Live_Server_Web/
       index.html
       resume.html
       resume.pdf        <-- 你的简历，文件名必须正好是 “resume.pdf”

   预览页面（resume.html）会加载：
     - iframe 内嵌：    resume.pdf
     - “在新标签页打开”：resume.pdf

   因此文件名必须正好是  resume.pdf
   （或者改名后，在 resume.html 中搜索 “resume.pdf” 并一并修改）。

2) 访客如何打开
   在首页点击主按钮 “View PDF / 查看简历” 即可打开 resume.html。
   右上角导航中没有单独的 PDF 链接。

3) 以后添加更多 PDF
   - 把其它 PDF 复制到同一文件夹，例如 portfolio.pdf
   - 编辑 resume.html：复制 iframe / 链接的代码块，或做成一个链接列表。
