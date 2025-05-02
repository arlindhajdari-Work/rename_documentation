---
title: 'GenDoc Template:: Motor Vehicle Bill of Sale'
metadata:
    description: 'Motor Vehicle Bill of Sale transaction template.'
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
        - integration
        - contribute
    tag:
        - gendoc
---

- [Motor Vehicle Bill of Sale template](../motorvehiclebillofsale.odt)
- [Motor Vehicle Bill of Sale example](../motorvehiclebillofsale.pdf)

This template requires adding custom fields on the Invoice and Product.

The goal of the template is to document the transaction of selling a car. We need some specific information of the vehicle and about the transaction.

The vehicle information will be on products and the transaction will be an invoice. On the **Invoice** we add:

<table class="table table-striped">
<tbody>
<tr>
<td>Down Payment:</td>
<td>{Invoice.cf_1227}</td>
</tr>
<tr>
<td>Transfer days:</td>
<td>{Invoice.cf_1228}</td>
</tr>
<tr>
<td>Inspection Days:</td>
<td>{Invoice.cf_1229}</td>
</tr>
<tr>
<td>Retain Amount:</td>
<td>{Invoice.cf_1230}</td>
</tr>
</tbody>
</table>

and on the **Products** we add:

<table class="table table-striped">
<tbody>
<tr>
<td>VIN:</td>
<td>{Products.cf_1219}</td>
</tr>
<tr>
<td>Make:</td>
<td>{Products.cf_1220}</td>
</tr>
<tr>
<td>Model:</td>
<td>{Products.cf_1221}</td>
</tr>
<tr>
<td>Color:</td>
<td>{Products.cf_1222}</td>
</tr>
<tr>
<td>Style:</td>
<td>{Products.cf_1223}</td>
</tr>
<tr>
<td>Year:</td>
<td>{Products.cf_1224}</td>
</tr>
<tr>
<td>Odometer:</td>
<td>{Products.cf_1225}</td>
</tr>
<tr>
<td>TitleN:</td>
<td>{Products.cf_1226}</td>
</tr>
</tbody>
</table>

Obviously the numbers assigned to your fields will be different and you will have to edit the template accordingly
