---
title: 'Importing Data::Inventory modules'
metadata:
    description: Import of Inventory modules (Quotes, SO, PO and Invoices) is very similar to the normal import process, the only difference appears in the mapping of fields.'
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
        - importing
    tag:
        - data
        - import
---

Import of Inventory modules (Quotes, SO, PO and Invoices) is very similar to the normal import process, the only difference appears in the mapping of fields.

If the module being imported is an inventory module the field mapping step of the import process will show not only the fields of the module but also a set of "virtual" fields that represent the product/service lines of the module.

These fields must be mapped to columns being imported from the CSV file. Basically they represent the fields that can be found in the product lines of the inventory modules as can be seen in the next table:

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Field Name</strong></td>
<td>Description</th>
</tr>
<tr>
<td><strong>Item Name</strong></td>
<td>Product or Service. Should be in import format Products::::ProductName or Services::::ServiceName. The item will be created if it does not exist</td>
</tr>
<tr>
<td><strong>Item Comment</strong></td>
<td>Description of the product or service</td>
</tr>
<tr>
<td><strong>Quantity</strong></td>
<td>The number of units sold on this line</td>
</tr>
<tr>
<td><strong>List Price</strong></td>
<td>The unit price of product or service in this line</td>
</tr>
<tr>
<td><strong>Item Discount Amount</strong></td>
<td>Direct discount if applied</td>
</tr>
<tr>
<td><strong>Item Discount Percent</strong></td>
<td>Percentage discount if applied</td>
</tr>
<tr>
<td><strong>Discount Amount</strong></td>
<td>Direct discount of the Quote, SO, PO or Invoice if applied. This field, although repeated in every line of the import CSV will be applied only once to the total of the record being imported</td>
</tr>
<tr>
<td><strong>Discount Percent</strong></td>
<td>Percentage discount of the Quote, SO, PO or Invoice if applied. This field, although repeated in every line of the import CSV will be applied only once to the total of the record being imported</td>
</tr>
<tr>
<td><strong>S&H Amount</strong></td>
<td>Shipping and handling costs of the Quote, SO, PO or Invoice. This field, although repeated in every line of the import CSV will be applied only once to the total of the record being imported</td>
</tr>
<tr>
<td><strong>Currency</strong></td>
<td>Currency the record should be created with. This currency must exist in the system, it will NOT be created. This field, although repeated in every line of the import CSV will be applied only once to the total of the record being imported</td>
</tr>
</tbody>
</table>
<br>

So, to import an inventory module we need a flat or denormalized view of the record where all the information of the record is repeated as many times as product lines are required. In other words, our CSV file will have one row per each product line in a record, each row will have different values in the special product line columns and the exact same values in the common base field of the entity.

For example, this [CSV file](sales_order.csv) contains 3 SalesOrder records, The first one has 4 product lines, 2 products and 2 services:

```
Products::::Cd-R CD Recordable
Products::::Double Panel See-thru Clipboard
Services::::srv
Services::::srv2
```

the other two Sales Order have two products each. As can be seen the base fields like "Subject", "Contact", "Organization" or Billing and Shipping details are all repeated identically on all lines. When importing only the values of one row will be used, but they should be repeated on all lines.

The import process will group lines by the **"Subject"** column so this column MUST be unique for each record in the CSV file. This is **very important** because this is how the program identifies which product lines belong to each record. Let me repeat that again in a more colorful way:

<div class="notices red">
The import process will group lines by the <strong> "Subject" </strong> column so this column MUST be unique for each record in the CSV file. This is <strong> very important </strong> because this is how the program identifies which product lines belong to each record.
</div>

See next the contents of the CSV file described.


<table class="table table-striped">
	<thead>
	<tr class="row0">
		<th class="col0">Subject</th><th class="col1">Opportunity Name</th><th class="col2">Customer No</th><th class="col3">SalesOrder No</th><th class="col4">Quote Name</th><th class="col5">Purchase Order</th><th class="col6">Contact Name</th><th class="col7">Due Date</th><th class="col8">Carrier</th><th class="col9">Pending</th><th class="col10">Status</th><th class="col11">Sales Commission</th><th class="col12">Excise Duty</th><th class="col13">Organization Name</th><th class="col14">Assigned To</th><th class="col15">Created Time</th><th class="col16">Modified Time</th><th class="col17">Billing Address</th><th class="col18">Shipping Address</th><th class="col19">Billing <span class="search_hit">PO</span> Box</th><th class="col20">Shipping <span class="search_hit">PO</span> Box</th><th class="col21">Billing City</th><th class="col22">Shipping City</th><th class="col23">Billing State</th><th class="col24">Shipping State</th><th class="col25">Billing Postal Code</th><th class="col26">Shipping Postal Code</th><th class="col27">Billing Country</th><th class="col28">Shipping Country</th><th class="col29">Terms &amp; Conditions</th><th class="col30">Description</th><th class="col31">Enable Recurring</th><th class="col32">Frequency</th><th class="col33">Start Period</th><th class="col34">End Period</th><th class="col35">Payment Duration</th><th class="col36">Invoice Status</th><th class="col37">Adjustment</th><th class="col38">Total</th><th class="col39">Sub Total</th><th class="col40">Tax Type</th><th class="col41">Discount Amount</th><th class="col42">Discount Percent</th><th class="col43">S&amp;H Amount</th><th class="col44">Currency</th><th class="col45">Item Name</th><th class="col46">Quantity</th><th class="col47">List Price</th><th class="col48">Item Comment</th><th class="col49">Item Discount Amount</th><th class="col50">Item Discount Percent</th><th class="col51">VAT</th><th class="col52">Sales</th><th class="col53">Service</th><th class="col54">V.A.T.</th>
	</tr>
	</thead>
	<tbody><tr class="row1">
		<td class="col0"><span class="search_hit">SO</span>_vtiger</td><td class="col1"> </td><td class="col2"> </td><td class="col3"><span class="search_hit">SO</span>1</td><td class="col4"><span class="search_hit">Quotes</span>::::Vendor_Quote</td><td class="col5"> </td><td class="col6">Contacts::::Jones Barbara</td><td class="col7">2015-04-13</td><td class="col8">FedEx</td><td class="col9"> </td><td class="col10">Created</td><td class="col11">0.00</td><td class="col12">0.00</td><td class="col13">Accounts::::t3M Invest A/S</td><td class="col14">admin</td><td class="col15">2014-06-26 23:12:15</td><td class="col16">2015-06-02 20:44:51</td><td class="col17">999 Baker Way</td><td class="col18">123 Anywhere Street</td><td class="col19"> </td><td class="col20"> </td><td class="col21">San Mateo</td><td class="col22">San Jose</td><td class="col23">CA</td><td class="col24">CA</td><td class="col25">15191</td><td class="col26">63999</td><td class="col27">USA</td><td class="col28">USA</td><td class="col29"> </td><td class="col30"> </td><td class="col31">0</td><td class="col32"> </td><td class="col33"> </td><td class="col34"> </td><td class="col35"> </td><td class="col36"> </td><td class="col37">100.000</td><td class="col38">4232.900</td><td class="col39">4182.900</td><td class="col40">individual</td><td class="col41">100.000</td><td class="col42">0.00</td><td class="col43">50.000</td><td class="col44">USA Dollars</td><td class="col45">Products::::Cd-R CD Recordable</td><td class="col46">3.00</td><td class="col47">130.000</td><td class="col48">This is test comment for product of <span class="search_hit">Quotes</span></td><td class="col49">20.000</td><td class="col50">0.00</td><td class="col51">14.50</td><td class="col52">0.00</td><td class="col53">12.50</td><td class="col54">0.00</td>
	</tr>
	<tr class="row2">
		<td class="col0"><span class="search_hit">SO</span>_vtiger</td><td class="col1"> </td><td class="col2"> </td><td class="col3"><span class="search_hit">SO</span>1</td><td class="col4"><span class="search_hit">Quotes</span>::::Vendor_Quote</td><td class="col5"> </td><td class="col6">Contacts::::Jones Barbara</td><td class="col7">2015-04-13</td><td class="col8">FedEx</td><td class="col9"> </td><td class="col10">Created</td><td class="col11">0.00</td><td class="col12">0.00</td><td class="col13">Accounts::::t3M Invest A/S</td><td class="col14">admin</td><td class="col15">2014-06-26 23:12:15</td><td class="col16">2015-06-02 20:44:51</td><td class="col17">999 Baker Way</td><td class="col18">123 Anywhere Street</td><td class="col19"> </td><td class="col20"> </td><td class="col21">San Mateo</td><td class="col22">San Jose</td><td class="col23">CA</td><td class="col24">CA</td><td class="col25">15191</td><td class="col26">63999</td><td class="col27">USA</td><td class="col28">USA</td><td class="col29"> </td><td class="col30"> </td><td class="col31">0</td><td class="col32"> </td><td class="col33"> </td><td class="col34"> </td><td class="col35"> </td><td class="col36"> </td><td class="col37">100.000</td><td class="col38">4232.900</td><td class="col39">4182.900</td><td class="col40">individual</td><td class="col41">100.000</td><td class="col42">0.00</td><td class="col43">50.000</td><td class="col44">USA Dollars</td><td class="col45">Products::::Double Panel See-thru Clipboard</td><td class="col46">3.00</td><td class="col47">1230.000</td><td class="col48">This is test comment for product of SalesOrder</td><td class="col49">200.000</td><td class="col50">0.00</td><td class="col51">0.00</td><td class="col52">0.00</td><td class="col53">0.00</td><td class="col54">0.00</td>
	</tr>
	<tr class="row3">
		<td class="col0"><span class="search_hit">SO</span>_vtiger</td><td class="col1"> </td><td class="col2"> </td><td class="col3"><span class="search_hit">SO</span>1</td><td class="col4"><span class="search_hit">Quotes</span>::::Vendor_Quote</td><td class="col5"> </td><td class="col6">Contacts::::Jones Barbara</td><td class="col7">2015-04-13</td><td class="col8">FedEx</td><td class="col9"> </td><td class="col10">Created</td><td class="col11">0.00</td><td class="col12">0.00</td><td class="col13">Accounts::::t3M Invest A/S</td><td class="col14">admin</td><td class="col15">2014-06-26 23:12:15</td><td class="col16">2015-06-02 20:44:51</td><td class="col17">999 Baker Way</td><td class="col18">123 Anywhere Street</td><td class="col19"> </td><td class="col20"> </td><td class="col21">San Mateo</td><td class="col22">San Jose</td><td class="col23">CA</td><td class="col24">CA</td><td class="col25">15191</td><td class="col26">63999</td><td class="col27">USA</td><td class="col28">USA</td><td class="col29"> </td><td class="col30"> </td><td class="col31">0</td><td class="col32"> </td><td class="col33"> </td><td class="col34"> </td><td class="col35"> </td><td class="col36"> </td><td class="col37">100.000</td><td class="col38">4232.900</td><td class="col39">4182.900</td><td class="col40">individual</td><td class="col41">100.000</td><td class="col42">0.00</td><td class="col43">50.000</td><td class="col44">USA Dollars</td><td class="col45">Services::::srv</td><td class="col46">3.00</td><td class="col47">1.000</td><td class="col48"> </td><td class="col49">0.000</td><td class="col50">0.00</td><td class="col51">0.00</td><td class="col52">0.00</td><td class="col53">0.00</td><td class="col54">0.00</td>
	</tr>
	<tr class="row4">
		<td class="col0"><span class="search_hit">SO</span>_vtiger</td><td class="col1"> </td><td class="col2"> </td><td class="col3"><span class="search_hit">SO</span>1</td><td class="col4"><span class="search_hit">Quotes</span>::::Vendor_Quote</td><td class="col5"> </td><td class="col6">Contacts::::Jones Barbara</td><td class="col7">2015-04-13</td><td class="col8">FedEx</td><td class="col9"> </td><td class="col10">Created</td><td class="col11">0.00</td><td class="col12">0.00</td><td class="col13">Accounts::::t3M Invest A/S</td><td class="col14">admin</td><td class="col15">2014-06-26 23:12:15</td><td class="col16">2015-06-02 20:44:51</td><td class="col17">999 Baker Way</td><td class="col18">123 Anywhere Street</td><td class="col19"> </td><td class="col20"> </td><td class="col21">San Mateo</td><td class="col22">San Jose</td><td class="col23">CA</td><td class="col24">CA</td><td class="col25">15191</td><td class="col26">63999</td><td class="col27">USA</td><td class="col28">USA</td><td class="col29"> </td><td class="col30"> </td><td class="col31">0</td><td class="col32"> </td><td class="col33"> </td><td class="col34"> </td><td class="col35"> </td><td class="col36"> </td><td class="col37">100.000</td><td class="col38">4232.900</td><td class="col39">4182.900</td><td class="col40">individual</td><td class="col41">100.000</td><td class="col42">0.00</td><td class="col43">50.000</td><td class="col44">USA Dollars</td><td class="col45">Services::::srv2</td><td class="col46">22.00</td><td class="col47">10.000</td><td class="col48"> </td><td class="col49">0.000</td><td class="col50">0.00</td><td class="col51">0.00</td><td class="col52">0.00</td><td class="col53">0.00</td><td class="col54">0.00</td>
	</tr>
	<tr class="row5">
		<td class="col0"><span class="search_hit">SO</span>_vtiger5usrp</td><td class="col1"> </td><td class="col2"> </td><td class="col3"><span class="search_hit">SO</span>3</td><td class="col4"><span class="search_hit">Quotes</span>::::Vendor_Quote</td><td class="col5"> </td><td class="col6">Contacts::::Miller Maria</td><td class="col7">2007-08-11</td><td class="col8">USPS</td><td class="col9"> </td><td class="col10">Approved</td><td class="col11">0.00</td><td class="col12">0.00</td><td class="col13">Accounts::::demovtiger</td><td class="col14">admin</td><td class="col15">2014-06-26 23:12:17</td><td class="col16">2014-06-26 23:12:17</td><td class="col17">345 Sugar Blvd.</td><td class="col18">123 Anywhere Street</td><td class="col19"> </td><td class="col20"> </td><td class="col21">San Francisco</td><td class="col22">San Jose</td><td class="col23">CA</td><td class="col24">CA</td><td class="col25">82696</td><td class="col26">63999</td><td class="col27">USA</td><td class="col28">USA</td><td class="col29"> </td><td class="col30"> </td><td class="col31">0</td><td class="col32"> </td><td class="col33"> </td><td class="col34"> </td><td class="col35"> </td><td class="col36"> </td><td class="col37">100.000</td><td class="col38">1080.000</td><td class="col39">1030.000</td><td class="col40">individual</td><td class="col41">100.000</td><td class="col42">0.00</td><td class="col43">50.000</td><td class="col44">USA Dollars</td><td class="col45">Products::::Vtiger 5 Users Pack</td><td class="col46">1.00</td><td class="col47">1230.000</td><td class="col48">This is test comment for product of SalesOrder</td><td class="col49">200.000</td><td class="col50">0.00</td><td class="col51">0.00</td><td class="col52">0.00</td><td class="col53">0.00</td><td class="col54">0.00</td>
	</tr>
	<tr class="row6">
		<td class="col0"><span class="search_hit">SO</span>_vtiger5usrp</td><td class="col1"> </td><td class="col2"> </td><td class="col3"><span class="search_hit">SO</span>3</td><td class="col4"><span class="search_hit">Quotes</span>::::Vendor_Quote</td><td class="col5"> </td><td class="col6">Contacts::::Miller Maria</td><td class="col7">2007-08-11</td><td class="col8">USPS</td><td class="col9"> </td><td class="col10">Approved</td><td class="col11">0.00</td><td class="col12">0.00</td><td class="col13">Accounts::::demovtiger</td><td class="col14">admin</td><td class="col15">2014-06-26 23:12:17</td><td class="col16">2014-06-26 23:12:17</td><td class="col17">345 Sugar Blvd.</td><td class="col18">123 Anywhere Street</td><td class="col19"> </td><td class="col20"> </td><td class="col21">San Francisco</td><td class="col22">San Jose</td><td class="col23">CA</td><td class="col24">CA</td><td class="col25">82696</td><td class="col26">63999</td><td class="col27">USA</td><td class="col28">USA</td><td class="col29"> </td><td class="col30"> </td><td class="col31">0</td><td class="col32"> </td><td class="col33"> </td><td class="col34"> </td><td class="col35"> </td><td class="col36"> </td><td class="col37">100.000</td><td class="col38">1080.000</td><td class="col39">1030.000</td><td class="col40">individual</td><td class="col41">100.000</td><td class="col42">0.00</td><td class="col43">50.000</td><td class="col44">USA Dollars</td><td class="col45">Products::::Vtiger 50 Users Pack</td><td class="col46">1.00</td><td class="col47">1230.000</td><td class="col48">This is test comment for product of SalesOrder</td><td class="col49">200.000</td><td class="col50">0.00</td><td class="col51">0.00</td><td class="col52">0.00</td><td class="col53">0.00</td><td class="col54">0.00</td>
	</tr>
	<tr class="row7">
		<td class="col0"><span class="search_hit">SO</span>_vendtl</td><td class="col1"> </td><td class="col2"> </td><td class="col3"><span class="search_hit">SO</span>5</td><td class="col4"><span class="search_hit">Quotes</span>::::<span class="search_hit">SO</span>_Quote</td><td class="col5"> </td><td class="col6">Contacts::::Wilson Susan</td><td class="col7">2007-02-28</td><td class="col8">BlueDart</td><td class="col9"> </td><td class="col10">Approved</td><td class="col11">0.00</td><td class="col12">0.00</td><td class="col13">Accounts::::vtigeruser</td><td class="col14">admin</td><td class="col15">2014-06-26 23:12:19</td><td class="col16">2014-06-26 23:12:19</td><td class="col17">123 Anywhere Street</td><td class="col18">123 Anywhere Street</td><td class="col19"> </td><td class="col20"> </td><td class="col21">Sunnyvale</td><td class="col22">San Jose</td><td class="col23">CA</td><td class="col24">CA</td><td class="col25">70388</td><td class="col26">63999</td><td class="col27">USA</td><td class="col28">USA</td><td class="col29"> </td><td class="col30"> </td><td class="col31">0</td><td class="col32"> </td><td class="col33"> </td><td class="col34"> </td><td class="col35"> </td><td class="col36"> </td><td class="col37">100.000</td><td class="col38">1080.000</td><td class="col39">1030.000</td><td class="col40">individual</td><td class="col41">100.000</td><td class="col42">0.00</td><td class="col43">50.000</td><td class="col44">USA Dollars</td><td class="col45">Products::::Vtiger 5 Users Pack</td><td class="col46">1.00</td><td class="col47">1230.000</td><td class="col48">This is test comment for product of SalesOrder</td><td class="col49">200.000</td><td class="col50">0.00</td><td class="col51">0.00</td><td class="col52">0.00</td><td class="col53">0.00</td><td class="col54">0.00</td>
	</tr>
	<tr class="row8">
		<td class="col0"><span class="search_hit">SO</span>_vendtl</td><td class="col1"> </td><td class="col2"> </td><td class="col3"><span class="search_hit">SO</span>5</td><td class="col4"><span class="search_hit">Quotes</span>::::<span class="search_hit">SO</span>_Quote</td><td class="col5"> </td><td class="col6">Contacts::::Wilson Susan</td><td class="col7">2007-02-28</td><td class="col8">BlueDart</td><td class="col9"> </td><td class="col10">Approved</td><td class="col11">0.00</td><td class="col12">0.00</td><td class="col13">Accounts::::vtigeruser</td><td class="col14">admin</td><td class="col15">2014-06-26 23:12:19</td><td class="col16">2014-06-26 23:12:19</td><td class="col17">123 Anywhere Street</td><td class="col18">123 Anywhere Street</td><td class="col19"> </td><td class="col20"> </td><td class="col21">Sunnyvale</td><td class="col22">San Jose</td><td class="col23">CA</td><td class="col24">CA</td><td class="col25">70388</td><td class="col26">63999</td><td class="col27">USA</td><td class="col28">USA</td><td class="col29"> </td><td class="col30"> </td><td class="col31">0</td><td class="col32"> </td><td class="col33"> </td><td class="col34"> </td><td class="col35"> </td><td class="col36"> </td><td class="col37">100.000</td><td class="col38">1080.000</td><td class="col39">1030.000</td><td class="col40">individual</td><td class="col41">100.000</td><td class="col42">0.00</td><td class="col43">50.000</td><td class="col44">USA Dollars</td><td class="col45">Products::::Brother Ink Jet Cartridge</td><td class="col46">1.00</td><td class="col47">1230.000</td><td class="col48">This is test comment for product of SalesOrder</td><td class="col49">200.000</td><td class="col50">0.00</td><td class="col51">0.00</td><td class="col52">0.00</td><td class="col53">0.00</td><td class="col54">0.00</td>
	</tr>
</tbody></table></div>


<h2> Taxes </h2>

Currently, due to limitations of the system we cannot define the tax settings of the record being imported. All taxes defined in the system at the moment of the import will be applied to the records created.

<div class="notices red">
All taxes defined in the system at the moment of the import will be applied to the records created.
</div>

This means that you have to group your import records in sets of identical taxes, define and set those taxes in the application and import the set. Then repeat the process for each set of changing taxes.