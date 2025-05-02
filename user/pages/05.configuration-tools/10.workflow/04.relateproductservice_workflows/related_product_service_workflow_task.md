---
title: 'Related Product/Service Workflow Task'
metadata:
    description: 'Implementing a frequently demanded functionality which consists of automatically relating the products and services sold on an invoice or bought on a purchase order to the account or vendor selected on the record.'
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
        - updaterecord
        - related product 
---

The *Relate Products and/or Services to Accounts/Vendor and/or Contacts* workflow will implement a frequently demanded functionality which consists of automatically relating the products and services sold on an invoice or bought on a purchase order to the account or vendor selected on the record. This makes a lot of sense in many businesses where we want to be able to see a list of products that our client has bought directly on their "Products" related list.

This workflow is associated to Quotes, Sales Orders, Invoices and Purchase Orders and permits the automatic relation of the products and services on each of these modules with the Account, Vendor and/or Contact selected on the record.


===

![](wfrelatepdosrv01.png?width=100%)
![](wfrelatepdosrv02.png?width=100%)

As can be seen in the screen shots above, this workflow permits us to select which elements we want to relate and with which entities:

-   **Relate Product**: if it should relate products or not
-   **Relate Service**: if it should relate services or not
-   **Relate with Account/Vendor**: if it should relate the element(s) selected above to the Account or Vendor in case of Purchase Order.
-   **Relate with Contact**: if it should relate the element(s) selected above to the Contact

This was implemented in issue  ~*issue:191*

<br>
------------------------------------------------------------------------

[Next](../03.invokecustomfunction_workflows) | Chapter 8:Invoke Custom Functions Workflow Tasks.

------------------------------------------------------------------------