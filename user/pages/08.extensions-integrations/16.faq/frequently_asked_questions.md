---
title: 'Frequently Asked Questions'
metadata:
    description: 'Frequently Asked Questions'
    author: 'Joe Bordes'
content:
    items:
        - '@self.children'
    limit: 5
    order:
        by: date
        dir: desc
    pagination: true
    url_taxonomy_filters: true
taxonomy:
    category:
        - course
    tag:
        - faq
---

<div class="notices blue">
<h3>How can I add new fonts to pdfmaker? I need to use Helvetica Neue Light</h3>
</div>

PDFMaker uses the mpdf library so you'll find a definitive answer at <br>
<a href="http://www.mpdf1.com/mpdf/index.php">http://www.mpdf1.com/mpdf/index.php</a> or <br>
<a href="https://discussions.vtiger.com/index.php?p=/discussion/53074/pdf-maker-own-font/p1">https://discussions.vtiger.com/index.php?p=/discussion/53074/pdf-maker-own-font/p1</a> <br>
I've styled my pdfs with a css file referenced from each pdf template. If you can do it this will be the way.
