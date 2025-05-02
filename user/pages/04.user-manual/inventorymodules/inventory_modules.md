---
title: 'Inventory Modules'
metadata:
    description: 'Filters are an effective search tool that can rapidly group records in a module.'
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
        - inventory
---

Financial Block and Fields
--------------------------

In order to give full access to all the calculations possible in
inventory modules, we have added a set of auto-calculated fields with
all the values. These fields will permit easier advanced reporting both
inside and outside of the application.

Additionally, we have added support for special tax types which are
summed up separately in order to simplify or make possible some common
tributation configurations present in many countries.

The fields have all been added to a new block called "Financial
Information" and they are:

-   **Gross total**: the sum of all line totals with no discounts nor
    individual taxes
-   **Line discount**: the sum of all individual line discounts
-   **Global discount**: the value of the global discount applied in the
    footer of the record
-   **Total discount**: the sum of line and global discount
-   **Net before global discount**: gross total minus individual line
    discounts
-   **Net total (after global discount)**: gross total minus ALL (total
    sum of all) discounts
-   **Tax retention**: the sum of all taxes marked as type retention
-   **Total tax**: the sum of all taxes applied
-   **Shipping and handling total**: a copy of the value in the footer
-   **Shipping and handling tax**: the sum of taxes applied to shipping
    and handling
-   **Adjustment**: a copy of the value in the footer
-   **Grand total**: a copy of the value in the footer

In a more mathematical notation, it would be

-   gross = ∑linetotals
-   line\_discount =∑line\_discounts
-   total\_discount = lined\_discount + global\_discount
-   net = gross - total\_discount
-   total\_tax = ∑line\_taxes + group\_tax
-   grand\_total = net + total\_tax + s&h + s&h\_tax + adjustment

The **retention tax** type can be established in the **tax settings**
page and is simply to sum them separately.

Inventory Details Line Module
-----------------------------

This section is intended to signify the meaning of InventoryDetails
fields. Since there are four main inventory modules, each field should
receive a separate meaning for each 'context' (the inventory module the
record belongs to). When the meaning is similar in all contexts, only
one will be provided.

### Inventory Details No

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>All</td>
<td>Give the record a unique identifier on the frontend</td>
</tr>
</tbody>
</table>

### Related To

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>All</td>
<td>Provide a link to the record this inventorydetailsline is used on. The type of module of this 'master' record is used as the context of the inventorydetails record</td>
</tr>
</tbody>
</table>

### Contacts

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quotes</td>
<td>B2C: To who are we offering the product or service<br />
B2B: Person in the organization who is responsible for the quote</td>
</tr>
<tr class="even">
<td>SalesOrder</td>
<td>B2C: To who are we selling the product or service<br />
B2B: Person in the organization who is responsible for the Sales Order</td>
</tr>
<tr class="odd">
<td>Invoice</td>
<td>B2C: To who are we invoicing the product or service<br />
B2B: Person in the organization who is responsible for the Invoice</td>
</tr>
<tr class="even">
<td>PurchaseOrder</td>
<td>Our sales representative at the Vendor</td>
</tr>
</tbody>
</table>

### Sequence No

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>All</td>
<td>Provide a whole number that signifies the sequence no. In which this inventory details line is placed when used in its context (e.g.: the 'master' record)</td>
</tr>
</tbody>
</table>

### Quantity

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quotes</td>
<td>How many units were offered to an account</td>
</tr>
<tr class="even">
<td>SalesOrder</td>
<td>How many units were sold to an account</td>
</tr>
<tr class="odd">
<td>Invoice</td>
<td>How many units were invoiced to an account</td>
</tr>
<tr class="even">
<td>PurchaseOrder</td>
<td>How many items were ordered at the vendor</td>
</tr>
</tbody>
</table>

### Tax Percent

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quotes, SalesOrder, Invoice</td>
<td>Is the sum of all tax percentages used on this line. So when, for instance a VAT of 21% was used and a Sales Tax of 2%, this field would carry 23%</td>
</tr>
<tr class="even">
<td>PurchaseOrder</td>
<td>The sum of all tax percentages as invoiced to us by the vendor. Should be 0 when creating PurchaseOrders.</td>
</tr>
</tbody>
</table>

### Discount percent

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quotes</td>
<td>The percentage of discount offered on this line</td>
</tr>
<tr class="even">
<td>SalesOrder, Invoice</td>
<td>The percentage of discount awarded on this line</td>
</tr>
<tr class="odd">
<td>PurchaseOrder</td>
<td>The percentage of discount awarded by the vendor for this product to us</td>
</tr>
</tbody>
</table>

### Net Price

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>All</td>
<td>An amount of money that follows the formula:<br />
(Unit Price * Quantity) – Line Discount Amount<br />
This is the amount of money the line represents after deducting discounts but before adding individual line taxes.</td>
</tr>
</tbody>
</table>

### Line Total

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>All</td>
<td>The final total of the line. This follows the formula:<br />
Net Price + Line Tax<br />
The is the amount of money the line represents after discount, after individual taxes</td>
</tr>
</tbody>
</table>

### Line Completed

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quotes</td>
<td>This field has no meaning</td>
</tr>
<tr class="even">
<td>SalesOrder</td>
<td>This field signifies whether all units of the line have been delivered. When no units have been delivered or a part of the sold units (field: Quantity) has been delivered, this field should remain unchecked.<br />
Only when all sold units have been delivered to the Organization this field should be set to 'yes'</td>
</tr>
<tr class="odd">
<td>Invoice</td>
<td>This field has no meaning</td>
</tr>
<tr class="even">
<td>PurchaseOrder</td>
<td>This field signifies whether all units ordered at the vendor (Quantity field) have been received by us. As long as there are more units in the Quantity-field than in the 'Delivered/Received' field, this field should remain unchecked<br />
When the no. in 'Units Delivered / Received' meets or exceeds the no. in 'Quantity', this field should be set to 'yes'.</td>
</tr>
</tbody>
</table>

### Cost Price

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quotes, SalesOrder, Invoice</td>
<td>This field indicates the cost price of the product or service, per unit</td>
</tr>
<tr class="even">
<td>PurchaseOrder</td>
<td>This field should be zero. The cost price of a product should, in the context of a purchase order, be represented on the 'Unit Price' field.</td>
</tr>
</tbody>
</table>

### Total Stock

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>All</td>
<td>This field should carry the value of the stock level of the related product of the line <strong>at the moment the line was created and the master-record was first saved.</strong> After the initial save, this field should never be altered.<br />
The stock we use to fill in this field will respect the units delivered/received field as such: when a master-record (like SalesOrders) ‘delivers’ units, the stock saved on this field will reflect the stock on the product, minus the units delivered on the first save. When a master-record receives products (like PurchaseOrders), the field will hold the product stock plus the units received at the first save.<br />
Subsequent changes to the units delivered/received field will not update this field.</td>
</tr>
</tbody>
</table>

### Remaining Units

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quotes</td>
<td>No meaning</td>
</tr>
<tr class="even">
<td>SalesOrder</td>
<td>The number of units that remain to be delivered to the Organization. Should always be the 'Quantity' minus the 'Units Delivered/Received'.</td>
</tr>
<tr class="odd">
<td>Invoice</td>
<td>No meaning</td>
</tr>
<tr class="even">
<td>PurchaseOrder</td>
<td>The number of units that remain to be received from the vendor. Should always be the 'Quantity' minus the 'Units Delivered/Received'.</td>
</tr>
</tbody>
</table>

### Products

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quotes</td>
<td>Which product/service are we offering?</td>
</tr>
<tr class="even">
<td>SalesOrder</td>
<td>Which product/service are we selling?</td>
</tr>
<tr class="odd">
<td>Invoice</td>
<td>Which product/service are we invoicing?</td>
</tr>
<tr class="even">
<td>PurchaseOrder</td>
<td>Which product/service are we buying?</td>
</tr>
</tbody>
</table>

### Organizations

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quotes</td>
<td>B2C: Empty, or the company the contact works in<br />
B2B: To who are we offering the product or service</td>
</tr>
<tr class="even">
<td>SalesOrder</td>
<td>B2C: Empty, or the company the contact works in<br />
B2B: To who are we selling the product or service</td>
</tr>
<tr class="odd">
<td>Invoice</td>
<td>B2C: Empty, or the company the contact works in<br />
B2B: To who are we invoicing the product or service</td>
</tr>
<tr class="even">
<td>PurchaseOrder</td>
<td>No meaning should be empty</td>
</tr>
</tbody>
</table>

### Vendor

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>All</td>
<td>If the Product field contains a Product (not a service), the main vendor of that product</td>
</tr>
<tr class="even">
<td>PurchaseOrder</td>
<td><strong>Concept: not in production:</strong><br />
From whom are we buying the product or service?</td>
</tr>
</tbody>
</table>

### Line Item ID

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>All</td>
<td>A reference to the legacy 'productinventoryrel' table ID</td>
</tr>
</tbody>
</table>

### Unit Price

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quotes, SalesOrder, Invoice</td>
<td>The unit price of the Product or Service on the Product-field</td>
</tr>
<tr class="even">
<td>PurchaseOrder</td>
<td>The cost price of the Product or Service on the Product-field</td>
</tr>
</tbody>
</table>

### Gross Price

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>All</td>
<td>The total amount of money this line represents, before discounts or individual taxes. The formula would be<br />
Quantity * Unit Price</td>
</tr>
</tbody>
</table>

### Discount Amount

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quotes, SalesOrder, Invoice</td>
<td>The discount awarded to the Organization for this particular line, represented as an absolute amount of money.<br />
When there is a direct discount awarded to this line, that amount will be placed here directly.<br />
When there is a discount percentage awarded to this line, the amount represented by that percentage will be calculated and automatically filled in here.</td>
</tr>
<tr class="even">
<td>PurchaseOrder</td>
<td>The discount awarded by the Vendor to us for this particular line, represented as an absolute amount of money. An administration department should later verify that this discount was actually deducted when we receive the Invoice.<br />
When there is a direct discount awarded to this line, that amount will be placed here directly.<br />
When there is a discount percentage awarded to this line, the amount represented by that percentage will be calculated and automatically filled in here.</td>
</tr>
</tbody>
</table>

### Line Tax

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>All</td>
<td>A quantified representation of the sum of all tax percentages. This follows the formula:<br />
Net Total * (Tax Percent / 100).<br />
The Net Total and the Line Tax together form the Line Total</td>
</tr>
</tbody>
</table>

### Units Delivered/Received

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quotes</td>
<td>No meaning</td>
</tr>
<tr class="even">
<td>SalesOrder</td>
<td>The number of units that have been delivered to the Organization.</td>
</tr>
<tr class="odd">
<td>Invoice</td>
<td>No meaning</td>
</tr>
<tr class="even">
<td>PurchaseOrder</td>
<td>The number of units that have been received from the vendor.</td>
</tr>
</tbody>
</table>

### Cost Total

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quotes, SalesOrder, Invoice</td>
<td>The total cost price of this line, represented as an amount of money. This follows the formula:<br />
Cost Price * Quantity</td>
</tr>
<tr class="even">
<td>PurchaseOrder</td>
<td>This field should always be zero</td>
</tr>
</tbody>
</table>

### Related Line Item ID

This field needs to be discussed. What I don't like is that it is uitype
1. Not only is this the wrong Uitype for an ID (should be 7 since it's
always a number), it's also not a reference field. So if we decide to
give some meaning to this field, we won't be able to use workflows on
it.

<table class="table table-striped">
<th>Context</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quotes</td>
<td>No meaning. Should be empty</td>
</tr>
<tr class="even">
<td>SalesOrder</td>
<td>References the InventoryDetails line on which this line was offered. So the context of the line referenced is a Quote</td>
</tr>
<tr class="odd">
<td>Invoice</td>
<td>References the InventoryDetails line on which this line was sold. So the context of the referenced line is a SalesOrder. There could be multiple Invoicelines referencing a single SalesOrderline since a SalesOrder could be Invoiced in multiple tranches</td>
</tr>
<tr class="even">
<td>PurchaseOrder</td>
<td>References a possible InventoryDetails line on which this product was sold. Only applicable when there is a direct and true relationship between these lines. Meaning: a product sold to an Organization on a SalesOrder is ordered at a Vendor in the same Quantity.<br />
Note: there could be 'collector' lines for PurchaseOrders, e.g.: PurchaseOrder lines that order Products in one line that are meant to fulfill multiple SalesOrderlines. This can, in this configuration only be done by relating those records on a M:M basis.</td>
</tr>
</tbody>
</table>

Some Internals
--------------

### vtiger\_productcurrencyrel

This table holds the relation of the unit price of the product for each
currency configured in the application. It contains two values:

-   the **actual unit price** of the product in each currency. This is
    the price introduced by the user in the application
-   the **converted price** of the product in each currency. This
    represents the mathematical calculation of the price in that
    currency based on the conversion rate. This value is not used
    anywhere in the application, it is only a reference value
