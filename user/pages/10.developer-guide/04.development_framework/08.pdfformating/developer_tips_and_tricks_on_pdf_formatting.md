---
title: 'Developer Tips and Tricks on PDF Formatting'
metadata:
    description: 'Developer Tips and Tricks on PDF Formatting'
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
        - development 
        - pdf
    tag:
        - howto
        - obsolete
---

<div class="notices blue"> <h2> How to eliminate the background status watermark?</h2></div>

===

<h3>The next patch shows how to do this for Invoices: </h3>

```
diff --git a/modules/Invoice/InvoicePDFController.php b/modules/Invoice/InvoicePDFController.php
index f1a0605..25236c0 100644
--- a/modules/Invoice/InvoicePDFController.php
+++ b/modules/Invoice/InvoicePDFController.php
@@ -58,7 +58,7 @@ class Vtiger_InvoicePDFController extends Vtiger_InventoryPDFController{
 	}
 
 	function getWatermarkContent() {
-		return $this->focusColumnValue('invoicestatus');
+		return ''; //$this->focusColumnValue('invoicestatus');
 	}
 }
 ?>
```

