---
title: 'Invoice relation with assets and service contracts'
metadata:
    description: 'Invoice relation with assets and service contracts'
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
        - module
    tag:
        - assets
        - service contracts
        - invoice
---

On the product lines of an invoice we will find icon buttons that will permit us to establish a relation between assets and service contracts for each line.

![](invoiceasset01.png?width=100%)

For the product lines, the idea is to be able to quickly see the assets related to the product line sale and create new assets for that line. Hovering over the icon will show a list of related assets and clicking on the icon will take us to the asset creation screen filling in as much information as it can from the invoice.

![](invoiceasset02.png?width=100%)

For service lines, we can only create new service contracts by clicking on the icon as there is no invoice field on the service contract to establish the relation. The account and contract start date will be filled in from the invoice fields.
