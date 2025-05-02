---
title: 'Web service Method Reference'
metadata:
    description: 'The API gives us a way of executing the basic operations of Create, Retrieve, Update, and Delete against any module installed in the associated coreBOS'
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
        - webservice
    tag:
        - reference
---

## CRUD Operations

The API gives us a way of executing the basic operations of Create,
Retrieve, Update, and Delete against any module installed in the
associated coreBOS. Obviously, permission restrictions exist for the
connected user as if he were inside coreBOS itself.

### Create

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Creates a new record in the application.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>create(elementType:String, element:Object):Object</td>
</tr>
<tr>
<td><strong>Send Type:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; elementType: module name where we want to create the record<br />
=&gt; element: map with all the field-value entries to save</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>An object with all the information of the new record</td>
</tr>
<tr>
<td><strong>Examples:</td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/020lib_createContact.php">Development Tool</a></td>
</tr>
</tbody>
</table>
<br>


The Create operation also supports a virtual meta-field named
**relations** which contains an array of web service IDs with which we
want to relate the record being created. You can see an [example of this
here](https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/410_createServiceWithRelation.php).

#### Create Inventory Modules

Inventory modules are special in many ways due to their master-detail
relation with products and services, different tax mode, and support for
taxes among other features. In order to support this functionality
through the web service API, these modules have a set of additional
rules.

<u>Product Items/Lines</u>

These modules support a virtual field named **pdoInformation**, this
field contains an array of line items with this format:
```php
    'pdoInformation' => array(
     array(
        "productid"=>2618,
        "comment"=>'cmt1',
        "qty"=>1,
        "listprice"=>10,
        'discount'=>0,  // 0 no discount, 1 discount
        "discount_type"=>'amount',  //  amount/percentage
        "discount_percentage"=>0,  // not needed nor used if type is amount
        "discount_amount"=>0,  // not needed nor used if type is percentage
      ),
      array(
        "productid"=>2619,
        "qty"=>2,
        "comment"=>'cmt2',
        "listprice"=>10,
        'discount'=>1,
        "discount_type"=>'percentage',  //  amount/percentage
        "discount_percentage"=>2,
        "discount_amount"=>0
      ),
    ),
```
-   This is mandatory for inventory modules
-   This is also supported in update
-   [you can see an example
    here](https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/440_libcreateSO.php)

<u>Tax Mode</u>

Tax mode, group or individual is also mandatory. It is set with [the
'taxtype'
field](https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/440_libcreateSO.php#L50)

<u>Product Taxes</u>

Taxes are always applied as per system settings. In other words, you can
NOT set taxes in the web service call, the taxes will be automatically
set as they are defined in the application. So, if the taxtype is Group,
all the available/active taxes defined in settings will be applied to
the inventory record. If the taxtype is individual, the taxes configured
in each product will be applied automatically.

<u>Shipping charges and taxes</u>

Shipping charge is [set using the field
'shipping\_handling\_charge'](https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/440_libcreateSO.php#L44).

Shipping taxes are set [using the tax name defined in
Settings.](https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/440_libcreateSO.php#L45:L47)

### Retrieve

Get all the values the user has access to, of an existent record in the
application. Given a web service ID of a record this service will return
an array with all the fields and their values.

Note that the way coreBOS works is that you get the values in the format
of the database but you must return them in the format of the user.
There is a way to [inform coreBOS to accept values in database format](../11.skipconvertfields ) and there is a Global
Variable (**Webservice\_Return\_FormattedValues**) to retrieve values in
the format of the user connected to the API.

All reference type fields which are pointing to another record will have
valid web service IDs.

In all retrieve operations a series of special fields are included which
contain extended information to reduce the number of network calls.

\* for all reference fields with a value, we will get a virtual field
with the same name of the field followed by "ename". This field contains
an array of 3 values:
-   module: the module of the record saved in the field (each related field may contain more than one module)
-   reference: the string representation of the record, so we don't have to make another call to the coreBOS application
-   cbuuid of the record
-   if the module has image fields the information of the image will be returned in a virtual field with the same name of the field    followed by "imageinfo".
-    if the record is a user, the role name assigned to the user will also be returned


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Get all the values the user has access to, of an existent record in the application.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>retrieve(id:string):Object</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>GET</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; id: web service ID or cbuuid of the record we want to recover</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>An object with all the information of the record</td>
</tr>
<tr>
<td><strong>URL Format:</td>
<td><code>http://corebos_url/webservice.php?operation=retrieve&amp;sessionName=[session id]&amp;id=[wsid]</code></td>
</tr>
<tr>
<td><strong>Examples:</td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/040lib_retrieve.php">Development Tool</a></td>
</tr>
</tbody>
</table>
<br>

### Update

This service updates ALL the fields of a given record. Once again; ALL
FIELDS. This endpoint does not support updating of individual fields,
so, in many cases, updating becomes a two-step operation; first retrieve
all the records, assign the new values leaving the others untouched and
update the whole record.

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Updates ALL the fields of a given record.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>update(element:Object):Object</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; element: record object with fields to update. It is mandatory to set the ID field in the Object and send in all fields</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>An object with all the information of the record (even <a href="../../developer-guide/webservice-development/methodreference#retrieve">extended information</a>)</td>
</tr>
<tr>
<td><strong>Examples:</td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/060lib_update.php">Development Tool</a></td>
</tr>
</tbody>
</table>
<br>

The Update operation also supports a virtual meta-field named
**relations** which contains an array of web service IDs with which we
want to relate the record being updated. You can see an [example of this
here](https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/410_createServiceWithRelation.php).

### Delete

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Eliminate any record we have permission to delete.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>delete(id:string):string</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; id: web service ID or cbuuid of the record we want to delete</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>successful</td>
</tr>
<tr>
<td><strong>Examples:</td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/070lib_delete.php">Development Tool</a></td>
</tr>
</tbody>
</table>
<br>

### Revise

The main difference between Revise and Update is that for revise you can
send only those fields that need to be changed, but with update, you
need to send all the mandatory fields to update a record.

If you send unknown fields then it will silently ignore them, the reason
for this behavior is that the user may not have permission for a few
fields and the system may not know if these fields are not available in
the system or the user does not have permission for these fields.


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Updates fields of a given record.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>revise(element:Object):Object</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; element: record object with fields to update. It is mandatory to set the ID field in the Object</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>An object with all the information of the record (even <a href="../../developer-guide/webservice-development/methodreference#retrieve">extended information</a>)</td>
</tr>
<tr>
<td><strong>Examples:</td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/450_libreviseSO.php">Development Tool</a></td>
</tr>
</tbody>
</table>
<br>

### CRUD Users

The current API supports the manipulation of users as if it were any
other entity, that is, you can use Create, Update, Retrieve, and Query
as with any other entity. The restriction is that it must be an
administrator user who executes the calls, as happens within the
application or you will only be able to get information about the
connected user.

In order to delete a user, the **DeleteUser** method must be used
because, as within the application and unlike the normal Delete, it is
necessary to give the recipient user of the records assigned to the user
that we are going to delete.

<https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/028lib_createUser.php>

<https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/060lib_updateUser.php>

<https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/070lib_deleteUser.php>


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>deleteUser</th>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Permits us to delete a user and transfer all his assigned records to another user.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>deleteUser(id:string, newOwnerId:string):string</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; id: user web service ID that will be deleted<br />
=&gt; newOwnerId: user web service ID to transfer records to</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>successfull</td>
</tr>
</tbody>
</table>
<br>


Users have two other additional endpoints that permit them to change their password and Access Key.

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>changePassword</th>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Permits a user to change his password or the password of another user if the connected user is an administrator.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>changePassword(id:string, oldPassword:string, newPassword:string, confirmPassword:string):string</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; id: user web service ID<br />
=&gt; oldPassword. you can set this value to the special string `nocheck_old_password` to force not validating the old password<br />
=&gt; newPassword<br />
=&gt; confirmPassword</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>=&gt; permission error message<br />
=&gt; success message with the new <strong>Access Key</strong></td>
</tr>
<tr>
<td><strong>Comments:</td>
<td><div class="notices red"> >Note that the changePassword function will change also the Access Key of the user, so your next login will have to be with the new Access Key that is returned from the call. The new Access Key will only be visible in this response so be sure to save it.</div></td>
</tr>
</tbody>
</table>
<br>




<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>changeAccessKey</td>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Permits a user to change his Access Key or the Access Key of another user if the connected user is an administrator.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>changeAccessKey(id:string):string</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; id: user web service ID</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>=&gt; permission error message<br />
=&gt; success message with the new <strong>Access Key</strong></td>
</tr>
</tbody>
</table>
<br>

### CRUD Documents

[Read full information here](../03.docenhance)

### Adding Comments

Most modules support the (now) standard ModComments module to manage
comments on the records. Since ModComments is a normal module it can be
managed using the CRUD commands indicated above.

There are two historical modules which have a non-standard way of
managing comments: Support Tickets (HelpDesK) and Frequently Asked
Questions (Faq). For these two modules, we have a specific endpoint:
**addTicketFaqComment**


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Function used to add comments to Tickets and Faq.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>addTicketFaqComment(id:string, values:Object):Object</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; id: web service id of the trouble ticket or faq to which we must attach the comment<br />
=&gt; values: array with the parameters of the comment. these parameters can be:<br />
'from_portal' 0 or 1: 0 = 'user', 1 = 'customer'<br />
'parent_id' webservice id of the contact creating the comment from the portal<br />
'comments' string, comment to add</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>An object with all the information of the record (even <a href="../../developer-guide/webservice-development/methodreference#retrieve">extended information</a>)</td>
</tr>
<tr>
<td><strong>Examples:</strong></td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/328_addTicketFaqComment.php">Development Tool</a></td>
</tr>
</tbody>
</table>
<br>

### CRUD Mass Operations

Since network calls are very expensive we have added **mass operations**
for the main actions.

#### MassCreate (MassUpsert)

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Create a set of records.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>MassCreate(elements:array of Objects):Object</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; elements: an array of Object to create (see below for the accepted structure)</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>An object with two elements:<br />
=&gt; success_creates: array of created Object<br />
=&gt; failed_creates: array of Object that could not be created with their error message</td>
</tr>
</tbody>
</table>
<br>

The Mass Create elements structure is an intelligent layout that permits
us not only to create many records in one call but also to establish
relationships among the different records.

The generic structure looks like this
```php

    [
        {
          "elementType" : "modulex",
          "referenceId" : "refRecord1",
          "element" : {
            "field" : "value"
          }
        },
        {
          "elementType" : "moduley",
          "referenceId" : "refRecord2",
          "element" : { 
            "field" : "value",
            "modulex_field" : "@{refRecord1.id}"
          }
        }
    ...
    ]
```   

Each element of the array represents a record to be created. It contains
an **elementType** so we know what module to create the record in, a
**referenceId** that identifies the record inside the structure, and a
**field-value Object** with the fields of the new record.

The reference fields in a record can reference existing records in the
application but they can also reference new records that will be created
using the **referenceId** field. This would permit us to create a
Contact record and then a Potential record related to the Contact that
has just been created.

An example structure to test with:
```php
    [
        {
          "elementType" : "HelpDesk",
          "referenceId" : "",
          "element" : {
            "ticket_title":"support ticket 1",
            "parent_id":"@{refAccount1.id}",
            "assigned_user_id":"19x5",
            "product_id":"@{refProduct.id}",
            "ticketpriorities":"Low",
            "ticketstatus":"Open",
            "ticketseverities":"Minor",
            "hours":"1.1",
            "ticketcategories":"Small Problem",
            "days":"1",
            "description":"ST mass create test 1",
            "solution":"",
          }
        },
        {
          "elementType" : "HelpDesk",
          "referenceId" : "",
          "element" : {
            "ticket_title":"support ticket 2",
            "parent_id":"@{refAccount2.id}",
            "assigned_user_id":"19x5",
            "product_id":"@{refProduct.id}",
            "ticketpriorities":"Low",
            "ticketstatus":"Open",
            "ticketseverities":"Minor",
            "hours":"1.1",
            "ticketcategories":"Small Problem",
            "days":"1",
            "description":"ST mass create test 2",
            "solution":"",
          }
        },
        {
          "elementType" : "HelpDesk",
          "referenceId" : "",
          "element" : {
            "ticket_title":"support ticket 3",
            "parent_id":"@{refAccount1.id}",
            "assigned_user_id":"19x5",
            "product_id":"14x2617",
            "ticketpriorities":"Low",
            "ticketstatus":"Open",
            "ticketseverities":"Minor",
            "hours":"1.1",
            "ticketcategories":"Small Problem",
            "days":"1",
            "description":"ST mass create test 3",
            "solution":"",
          }
        },
        {
          "elementType" : "Accounts",
          "referenceId" : "refAccount1",
          "element" : {
            "accountname":"MassCreate Test 1",
            "website":"https://corebos.org",
            "assigned_user_id":"19x5",
            "description":"mass create test",
          }
        },
        {
          "elementType" : "Accounts",
          "referenceId" : "refAccount2",
          "element" : {
            "accountname":"MassCreate Test 2",
            "website":"https://corebos.org",
            "assigned_user_id":"19x5",
            "description":"mass create test",
          }
        },
        {
          "elementType" : "Accounts",
          "referenceId" : "",
          "element" : {
            "accountname":"MassCreate Test",
            "website":"https://corebos.org",
            "assigned_user_id":"19x1",
            "description":"mass create just another account with no relations",
          }
        },
        {
          "elementType" : "Products",
          "referenceId" : "",
          "element" : {
            "productname":"MassCreate Test",
            "website":"https://corebos.org",
            "assigned_user_id":"19x1",
            "description":"mass create product test",
          }
        },
    ]
```
and you can see some more examples [in the unit
tests](https://github.com/tsolucio/coreBOSTests/blob/master/include/Webservices/MassCreateTest.php).

**MassUpsert** The Mass create method can work also as a Mass Upsert
method as it supports search and update functionality by means of the
"searchon" parameter which you can add to any record in the composite
object entries that create accepts.

The "searchon" parameter is a comma-separated list of fields you want to
search on. The method will search for equality on all given fields using
the values in the "elements" array. This is the exact same syntax you
will find in the Upsert method below.

You can [find an example in the unit
tests.](https://github.com/tsolucio/coreBOSTests/blob/master/include/Webservices/MassCreateTest.php#L203)

#### MassRetrieve

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Retrieve a set of records.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>MassRetrieve(ids:string):array of Object</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; ids: a comma-separated string of web service ID of the records to retrieve</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>An array of Object with all the information of the records that were possible to obtain</td>
</tr>
</tbody>
</table>

<br>


#### MassUpdate


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Update a set of records.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>MassUpdate(elements:array of Objects):Object</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; elements: an array of Object to update, each one must contain the web service ID of the record to update and the field-value list of fields to update</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>An object with two elements:<br />
=&gt; success_updates: array of updated IDs<br />
=&gt; failed_updates: array of IDs that could not be updated with their error message</td>
</tr>
</tbody>
</table>
<br>

#### MassDelete

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Delete a set of records.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>MassUpdate(elements:array of Objects):Object</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; ids: comma-separated list of web service IDs to delete</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>An object with two elements:<br />
=&gt; success_deletes: array of deleted IDs<br />
=&gt; failed_deletes: array of IDs that could not be deleted with their error message</td>
</tr>
</tbody>
</table>
<br>

### Validations. Create, Update and Revise with Validations

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Apply application configured validations on a set of fields.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>ValidateInformation(context:Object):Object</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>=&gt; context: an Object with the field-value pairs to validate. Either a "module" or a "record" entry must exist in the object. If "record" is given the validations will be evaluated with the fields of the record.</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>true or false in the success field. If false is returned the result will contain an array with all the validations that have failed</td>
</tr>
</tbody>
</table>
<br>


Besides the ValidateInformation endpoint, we also have create and update
options that are identical to their base counterparts explained above
just that they will validate the values before executing any operation
and return the error messages without taking any action if the
validations do not pass.

-   **CreateWithValidation** [Development
    Tool](https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/020_createContactValidation.php)
-   **UpdateWithValidation**
-   **ReviseWithValidation**

### Upsert

The **upsert** method will permit us to execute a search on some fields
in a module, if we find a record that matches the search we will update
it with the given values, if no record can be found we will create a new
one with the given values. So it is a Search and Update or Create in one
call.


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Search and update or create a record.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>upsert(elementType:string, element:Object, searchOn:string , updatedfields:string ):Object</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>=&gt; elementType: module name where we search and operate<br />
=&gt; element: record object with fields to update/create<br />
=&gt; searchOn: comma-separated list of fields to search on, the values will be obtained from element<br />
=&gt; updatedfields: comma-separated list of fields to update if the record is found, the values will be obtained from element</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>An object with all the information of the record updated/created (even <a href="../../developer-guide/webservice-development/methodreference#retrieve">extended information</a>)</td>
</tr>
<tr>
<td><strong>Examples:</strong></td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/065_libUpsert.php">Development Tool</a></td>
</tr>
</tbody>
</table>
<br>

### Relations

coreBOS API supports defining 1:N and N:N relations between modules.

By setting a value in a foreign key (relation field or uitype 10) we
establish a direct relationship between two modules.

The Create and Update operations also support a virtual meta-field named
**relations** which contains an array of web service IDs with which we
want to relate the record being created or updated. You can see an
[example of this
here](https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/410_createServiceWithRelation.php).

Finally, we have two endpoints that can establish or delete many to many
relations with a large set of records: **SetRelation** and
**UnsetRelation**



<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>SetRelation</th>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Sets relations between one record and a set of other records.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>SetRelation(relate_this_id:string, with_these_ids:Map):Map</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>=&gt; relate_this_id: web service ID of the main record to relate<br />
=&gt; with_these_ids: array of web service IDs to relate to the main record</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>An object with all the information of the record updated/created (even <a href="../../developer-guide/webservice-development/methodreference#retrieve">extended information</a>)</td>
</tr>
<tr>
<td><strong>Examples:</strong></td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/424lib_setrelated.php">Development Tool</a></td>
</tr>
</tbody>
</table>
<br>
<br>


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>UnsetRelation</th>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Deletes relations between one record and a set of other records.</td>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>UnsetRelation(unrelate_this_id:string, with_these_ids:Map):Map</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>=&gt; unrelate_this_id: web service ID of the main record to unrelate<br />
=&gt; with_these_ids: array of web service IDs to unrelate from the main record</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td></td>
</tr>
<tr>
<td><strong>Examples:</strong></td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/424lib_setrelated.php">Development Tool</a></td>
</tr>
</tbody>
</table>
<br>
<br>

Metadata information
--------------------

### List Types


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>listtypes</th>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Returns a list of module names the currently connected user has access to.</td>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>listtypes(fieldTypeList:string):Map</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>GET</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>=&gt; fieldTypeList: comma-separated list of field types the modules must have. Is optional.</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>list of modules the user has access to which contain at least one field of the types given. If no types are given all accessible modules are returned</td>
</tr>
<tr>
<td><strong>URL Format:</strong></td>
<td><code>http://corebos_url/webservice.php?operation=listtypes&amp;sessionName=[session id]&amp;fieldTypeList=phone,email</code></td>
</tr>
<tr>
<td><strong>Examples:</strong></td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/090lib_listtypes.php">Development Tool</a></td>
</tr>
</tbody>
</table>
<br>
<br>




### Describe

The Describe service gives us detailed information about the module
which we are trying to access. It will inform us both of the types of
actions permitted and all the information of the fields which we have
access to.

This is extremely important as it is the only way to obtain the objectid
of a module. In the introduction, we explained that each record in web
service has a unique identifier composed of the module web service id
and the record's crmid. The Describe service returns the module id we
need to construct this unique identifier.

The object returned by this service contains:

-   idPrefix - web service module ID
-   isEntity - true if it is an entity, false if it is an extension
-   label – label name of the module translated to the language of the
    connected user
-   label\_raw – internal label name of the module
-   name – internal name of the module.
-   createable – boolean value indicating if the connected user can
    create new records.
-   updateable - boolean value indicating if the connected user can
    update existing records.
-   deleteable - boolean value indicating if the connected user can
    delete existing records.
-   retrieveable - boolean value indicating if the connected user can
    retrieve records.
-   labelFields - main fields that represent the records in the module,
    the link fields
-   filterFields - the default column fields to show when listing the
    records. Contains also the link fields and page size
-   relatedModules - all the information of the modules related to this
    module
-   fields - an array that contains all the accessible fields and their
    related information. Each field has these values:
    -   name – internal field name.
    -   label – label name translated
    -   label\_raw – internal label name
    -   mandatory – a boolean value which indicates if it is mandatory
        on creation or not.
    -   type – array with field data type information.
    -   default – the default value of the field.
    -   nullable – boolean value indicating if the field can be empty.
    -   editable – boolean value indicating if the field can be
        modified.
    -   uitype – UI type of the field
    -   typeofdata – basic validation information
    -   sequence – order of the fields in the application
    -   quickcreate – boolean value indicating if the field is present
        in quick create or not
    -   [displaytype]( ../../04.development_framework/11.develtutorials/04.field_structure)
    -   summary – letter indicating if the field is present in the page
        header information
        -   T: should appear in title
        -   H: should appear in header
        -   B: should appear in body
        -   N: does not appear in page header
    -   block – array with block information
        -   blockid: internal ID of the block
        -   blocksequence: order of the block
        -   blocklabel: raw label of the block
        -   blockname: translated label of the block


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>Describe</th>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Returns metadata of a list of module names.</td>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>describe(elementType:string):Map</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>GET</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>=&gt; elementType: comma-separated list of modules.</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>see above</td>
</tr>
<tr>
<td><strong>URL Format:</strong></td>
<td><code>http://corebos_url/webservice.php?operation=describe&amp;sessionName=[session id]&amp;elementType=Contacts,Accounts</code></td>
</tr>
<tr>
<td><strong>Examples:</strong></td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/080lib_describe.php">Development Tool</a></td>
</tr>
</tbody>
</table>
<br>
<br>

### Filters/Views


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getfilterfields</th>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Retrieve the default list of fields to show in a list view along with the link field and pagesize</td>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>getfilterfields(module:String):Map</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>=&gt; module: module name to get the fields for</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>A map object with a list of the fields, the link fields and the default page size</td>
</tr>
<tr>
<td><strong>URL Format:</strong></td>
<td><code>http://corebos_url/webservice.php?operation=getfilterfields&amp;sessionName=[session id]&amp;module=[name]</code></td>
</tr>
</tbody>
</table>
<br>
<br>



<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getViewsByModule</td>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Retrieve a list of available filters on a module with all the available information of each: fields, conditions, default, and also the link field and page size. This method is similar to getFiltersByModule being the difference one property (HTML output) and that this method applies permission based on the coreBOS Custom View Management module.</td>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>getViewsByModule(module:String):Map</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>=&gt; module: module name to get the filters for</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>A map object with a list of the filters, the link fields, and the default page size</td>
</tr>
<tr>
<td><strong>URL Format:<strong></td>
<td><code>http://corebos_url/webservice.php?operation=getViewsByModule&amp;sessionName=[session id]&amp;module=[name]</code></td>
</tr>
</tbody>
</table>
<br>
<br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getFiltersByModule</td>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Retrieve a list of available filters on a module with all the available information of each: fields, conditions, default, and also the link field and page size. This method is similar to getViewsByModule being the difference one property (HTML output) and that this method applies permission based on the Custom View Management (filters, public, and approve).</td>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>getFiltersByModule(module:String):Map</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:<strong></td>
<td>=&gt; module: module name to get the filters for</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>A map object with a list of the filters in HTML and array format and the link fields</td>
</tr>
<tr>
<td><strong>URL Format:</strong></td>
<td><code>http://corebos_url/webservice.php?operation=getFiltersByModule&amp;sessionName=[session id]&amp;module=[name]</code></td>
</tr>
</tbody>
</table>
<br>
<br>

### **User Information**

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getPortalUserInfo</td>
</tr>
<tr class="odd">
<td><strong>Purpose:</strong></td>
<td>Retrieve a list of available fields for the connected user</td>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>getPortalUserInfo():Map</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td></td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>'date_format','first_name','last_name','email1','id','is_admin','roleid','rolename','language','currency_grouping_pattern','currency_decimal_separator','currency_grouping_separator','currency_symbol_placement'</td>
</tr>
<tr>
<td><strong>URL Format:</strong></td>
<td><code>http://corebos_url/webservice.php?operation=getPortalUserInfo&amp;sessionName=[session id]</code></td>
</tr>
</tbody>
</table>
<br>
<br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getPortalUserDateFormat</td>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Retrieve the date format of the connected user</td>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>getPortalUserDateFormat():Map</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td></td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>date_format, if none is set ISO (yyyy-mm-dd) will be returned</td>
</tr>
<tr>
<td><strong>URL Format:</strong></td>
<td><code>http://corebos_url/webservice.php?operation=getPortalUserDateFormat&amp;sessionName=[session id]</code></td>
</tr>
</tbody>
</table>
<br>
<br>


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getAllUsers</td>
</tr>
<tr>
<td><strong>Purpose:</td>
<td>Retrieve a list of all existing users name</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>getAllUsers():Map</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td></td>
</tr>
<tr>
<td><strong>Response:</td>
<td>list of user names indexed by ID</td>
</tr>
<tr>
<td><strong>URL Format:</td>
<td><code>http://corebos_url/webservice.php?operation=getAllUsers&amp;sessionName=[session id]</code></td>
</tr>
</tbody>
</table>
<br>
<br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getAssignedUserList</td>
</tr>
<tr>
<td><strong>Purpose:</td>
<td>Retrieve a list of all users with access to a module</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>getAssignedUserList(module):Map</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>GET</td>
</tr>
<tr >
<td><strong>Parameters:</td>
<td>=&gt; module: module name to get the users for</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>list of user IDs and names</td>
</tr>
<tr>
<td><strong>URL Format:</td>
<td><code>http://corebos_url/webservice.php?operation=getAssignedUserList&amp;sessionName=[session id]&amp;module=[name]</code></td>
</tr>
</tbody>
</table>
<br>
<br>


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getUsersInSameGroup</td>
</tr>
<tr>
<td><strong>Purpose:</td>
<td>return all the users in the groups that the given user is part of.</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>getUsersInSameGroup(id:String):Map</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; id: userid to get the group users for. Note: application ID not web service ID</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>array user names of all the users in the groups that this user is part of indexed by their ID</td>
</tr>
<tr>
<td><strong>URL Format:</td>
<td><code>http://corebos_url/webservice.php?operation=getUsersInSameGroup&amp;sessionName=[session id]&amp;id=[userid]</code></td>
</tr>
</tbody>
</table>
<br>
<br>

### Other Information

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getRelatedModulesManytoOne</td>
</tr>
<tr>
<td><strong>Purpose:</td>
<td>Returns an array of metadata information about the modules related to the given module in N:1 mode.</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>getRelatedModulesManytoOne(module:string):array of Map</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>GET</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; module: main module for which we want to know the list of related modules.</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>An array of module information which contains:<br />
=&gt; name: related module name<br />
=&gt; label: translated module label<br />
=&gt; field: field that relates the modules</td>
</tr>
</tbody>
</table>
<br>
<br>
<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>GetRelatedModulesOneToMany</td>
</tr>
<tr>
<td><strong>Purpose:</td>
<td>Returns an array of metadata information about the modules related to the given module in 1:N mode.</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>GetRelatedModulesOneToMany(module:string):array of Map</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>GET</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; module: main module for which we want to know the list of related modules.</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>An array of module information which contains:<br />
=&gt; name: related module name<br />
=&gt; label: translated module label<br />
=&gt; field: field that relates the modules</td>
</tr>
</tbody>
</table>
<br>
<br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getRelatedModulesInfomation</td>
</tr>
<tr>
<td><strong>Purpose:</td>
<td>Returns an array of metadata information about the modules related to the given module.</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>getRelatedModulesInfomation(module:string):array of Map</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; module: main module for which we want to know the list of related modules.</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>An array of module information which contains:<br />
=&gt; related_tabid: internal ID of the module<br />
=&gt; related_module: module name<br />
=&gt; label: module label<br />
=&gt; labeli18n: translated module label<br />
=&gt; actions: supported actions<br />
=&gt; relationId: internal relation ID<br />
=&gt; relatedfield: field that relates the module<br />
=&gt; relationtype: 1:N or N:N<br />
=&gt; filterFields: array of fields that should be listed when showing the related records</td>
</tr>
<tr>
<td><strong>Notes:</td>
<td>The information returned with this function is present in the Describe response</td>
</tr>
</tbody>
</table>
<br>
<br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getReferenceValue</td>
</tr>
<tr>
<td><strong>Purpose:</td>
<td>convert web service IDs into their entity names.</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>getReferenceValue(id:string):string</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>GET</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; id: PHP serialized array of web service IDs to convert.</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>A web service ID indexed map with these three entries:<br />
=&gt; module: the module of the record in the field<br />
=&gt; reference: entity name reference<br />
=&gt; cbuuid: of the record</td>
</tr>
<tr>
<td><strong>Notes:</td>
<td>The information returned with this function is equivalent to the "ename" virtual fields returned by Retrieve</td>
</tr>
</tbody>
</table>
<br>
<br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getModulePermissionQuery</td>
</tr>
<tr>
<td><strong>Purpose:</td>
<td>returns SQL query restrictions that must be applied to enforce application permissions. This is used to generate external SQL reports with tools like SuperSet or Metabase while applying the same rules configured inside the application.</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>getModulePermissionQuery(module:string):Map</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>GET</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; module: name of the module for which we want to retrieve the restrictions.</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>A map with these three entries:<br />
=&gt; permissonTable: if a temporary table is required this will contain it's name<br />
=&gt; permissionQuery: full permission query<br />
=&gt; permissionJoin: only the join conditions of the query</td>
</tr>
</tbody>
</table>
<br>
<br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td><strong>getPicklistValues</strong></td>
</tr>
<tr>
<td><strong>Purpose:</td>
<td>get picklist fields for the given module and all their possible values.</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>getPicklistValues(module:string):Map</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; module: name of the module for which we want to retrieve the picklist values.</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>A map of picklist fields and all their values</td>
</tr>
</tbody>
</table>
<br>
<br>
<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td><strong>getEntityNum</strong></td>
</tr>
<tr>
<td><strong>Purpose:</td>
<td>get the auto numeric field prefixes of all modules with a uitype 4 field.</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>getEntityNum():Map</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td></td>
</tr>
<tr>
<td><strong>Response:</td>
<td>A map of auto numeric prefixes with module names as key</td>
</tr>
</tbody>
</table>
<br>
<br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td><strong>findByPortalUserName</strong></td>
</tr>
<tr>
<td><strong>Purpose:</td>
<td>Returns if a portal user with the given name exists or not.</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>findByPortalUserName(username:string):Object</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; username: string.</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>boolean: if a portal user with that name exists or not</td>
</tr>
<tr>
<td><strong>URL Format:</td>
<td><code>http://corebos_url/webservice.php?operation=findByPortalUserName&amp;sessionName=[session id]&amp;username=joebordes</code></td>
</tr>
</tbody>
</table>
<br>
<br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td><strong>getMaxLoadSize</strong></td>
</tr>
<tr>
<td><strong>Purpose:</td>
<td>Returns maximum upload size as per PHP settings, so we can adapt our external application to the configured restrictions in the server.</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>getMaxLoadSize():String</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td></td>
</tr>
<tr>
<td><strong>Response:</td>
<td>return maximum upload size as per PHP settings</td>
</tr>
<tr>
<td><strong>URL Format:</td>
<td><code>http://corebos_url/webservice.php?operation=getMaxLoadSize&amp;sessionName=[session id]</code></td>
</tr>
</tbody>
</table>
<br>
<br>

There are two deprecated endpoints that you can use to get specific
information that is already available using **Describe**. These methods
will not be eliminated, so they can be used if you need them.

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<th><strong>getUItype</strong></th>
</tr>
<tr>
<td><strong>Purpose:</td>
<td>Returns a list of all the fields in the module with their uitype.</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>getUItype(module:string):List</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; module: module name.</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>list of fields and their type</td>
</tr>
<tr>
<td><strong>URL Format:</td>
<td><code>http://corebos_url/webservice.php?operation=getUItype&amp;sessionName=[session id]&amp;module=Contacts</code></td>
</tr>
</tbody>
</table>
<br>
<br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td><strong>vtyiicpng_getWSEntityId</strong></td>
</tr>
<tr>
<td><strong>Purpose:</td>
<td>Returns the given modules' web service entity ID.</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>vtyiicpng_getWSEntityId(entityName:string):String</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; entityName: module name.</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>string with the modules' web service ID</td>
</tr>
<tr>
<td><strong>URL Format:</td>
<td><code>http://corebos_url/webservice.php?operation=vtyiicpng_getWSEntityId&amp;sessionName=[session id]&amp;entityName=Contacts</code></td>
</tr>
</tbody>
</table>
<br>
<br>

<h2>Other Operations</h2>
<h3>Search Global Variable</h3>

[SearchGlobalVar](../../../05.configuration-tools/04.global-variables)

<h3>Translations</h3>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>This method permits us to use the translations in the application in our frontend application.</td>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Profile:</td>
<td>gettranslation(totranslate:Map, language:string, module:string):Map</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; totranslate: Object with the keys to translate, the value will be ignored if a translation exists or returned if no translation exists<br />
=&gt; language: a valid application language identifier (e.g. es_es)<br />
=&gt; module: module to start the translations from</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>A map object with all the keys translated where possible</td>
</tr>
<tr>
<td><strong>Examples:</td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/324_getTranslate.php">Developer Tool</a></td>
</tr>
</tbody>
</table>
<br>
<br>

<h3> Javascript Logging </h3>

The <strong>jsLog</strong> endpoint permits us to send any message from javascript to
our coreBOS backend. If we activate the [javascript logging
section](https://github.com/tsolucio/corebos/blob/master/log4php.properties#L58)
we will be able to send messages from javascript to our logs directory
for tracing.

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Updates fields of a given record.</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>jsLog(level:string, message:string)</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; level: log4php logging level<br />
=&gt; message: the string to write in the log if the given level is matched</td>
</tr>
<tr>
<td><strong>Response:</td>
<td></td>
</tr>
</tbody>
</table>
<br>
<br>

### Sync

The sync service returns the complete set of changes that occurred to
all records **assigned to the connected user** from a given date and
time.

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Returns a SyncResult object which contains all the changes that occurred in the application since the parameter modifiedTime to records <strong>assigned to the connected user</strong>. Optionally, if the connected user is an administrator he can ask for all changes in the application disregarding who the records are assigned to. The OnDemand configuration setting variable <strong>$cbodCSAppSyncUser</strong> will permit you to define additional non-admin users that will be able to download changes in all modules.</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>sync(modifiedTime: Timestamp, elementType: String, syncType: String):SyncResult</td>
</tr>
<tr>
<td><strong>Send as:</td>
<td>GET</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>=&gt; modifiedTime: timestamp of last synchronization<br />
=&gt; elementType: optional parameter, name of the module(s) we want to get the changes for, if not set all records affected in all modules will be returned. Can be a comma-separated list of module names<br />
=&gt; syncType: a string which can be empty or contain the value 'application'. If it is 'application' and the connected user is an administrator, all changes to the application will be returned.</td>
</tr>
<tr>
<td><strong>Response:</td>
<td>SyncResult object with changes:<br />
<code>SyncResult {
updated:[Object] //List of created or modified objects.
deleted:[Id] //List of webserviceid of deleted objects
lastModifiedTime:Timestamp // date/time of last change, this can be used in the next call to the sync service to get next set of changes
}</code></td>
</tr>
<tr>
<td><strong>URL Format:</td>
<td><code>http://corebos_url/webservice.php?operation=sync&amp;sessionName=[session
id]&amp;modifiedTime=[timestamp]&amp;elementType=[elementType]</code></td>
</tr>
<tr>
<td><strong>Examples:</td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/050_sync.php">Development Tool</a></td>
</tr>
</tbody>
</table>

<br>
------------------------------------------------------------------------

[Next](../03.docenhance)| Chapter 6:Working with Documents and Images.

------------------------------------------------------------------------
