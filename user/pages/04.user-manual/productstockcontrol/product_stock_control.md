---
title: 'Product Stock Control'
metadata:
    description: 'Product Stock Control'
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
        - workflow
    tag:
        - product
---

Stock is controlled through **workflows**.

- There is a default <u>workflow associated with Invoices</u> that will **decrement product stock** as soon as the invoice is created. This workflow can be deactivated and created against Sales Orders if you prefer to discount stock when the sale is made, not when it is paid.
- There is a default <u>workflow associated with Purchase Orders</u> that will **increment the product stock** when the order is set to status "**Received Shipment**"
- Invoice and SalesOrder have a special status, "**Cancel**", which will restore the product stock when they are set to that status
- Setting the status of the Purchase Order to anything different than "**Received Shipment**" will deduct the stock of that order
- Deleting and restoring the records is supported by the application so stock will be controlled correctly in these cases, although you should be careful with the legal requirements you may be subject to
- Editing and changing the quantities on an Invoice is also supported

Deduct stock on Sales Order
---------------------------

By default the application will deduct stock when you create an invoice. This is controlled by the default workflow associated to the Invoice module. To change this behaviour and deduct stock when the Sales Order is created and not the Invoice you must delete or deactivate the Invoice workflow and create the same workflow with the same "UpdateInventory" task but associated to the Sales Order module.
