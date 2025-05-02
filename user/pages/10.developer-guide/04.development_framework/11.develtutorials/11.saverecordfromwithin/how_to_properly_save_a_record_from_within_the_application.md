---
title: 'How to properly save a record from within the application'
metadata:
    description: 'How to properly save a record from within the application'
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
    tag:
        - howto
---

<div class="notices blue">
Please <a href="https://blog.corebos.org/blog/feedingdatatosave"> read this very well explained article </a> from Luke.
</div>

Background
----------

The application gets and sends information from/to two sources:

- **Database**
- **User/Browser**

thus, it expects to get information coming from these sources in their
native format and sends information to them in their native format. So
if we get a date from the database, it will be in the ISO standard
database format but if we get a date from the browser it will be in the
current user's format.

Since the application expects the information to be in these formats it
does all the work necessary to get the information correctly into the
right format when moving it around. For example, if it reads a date from
the database and sends it to the browser it will first change it to the
current user's format, and when that date comes from the browser it will
format it into ISO standard to be saved in the database.

To accomplish this transforming of formats, which must happen for all
types of fields, the application has a set of functions that do the work
and that we can use freely:

-   to prepare a date for showing in the browser, we would use the
    **DateTimeField-&gt;getDisplayDate()** method and to save it in the
    database we would use **DateTimeField-&gt;getDBInsertDateValue()**

<div class="notices blue">
You can find all the Date/Time
functionality in the class <i>DateTimeField</i> in the file
<i>include/fields/DateTimeField.php </i></div>

-   for **currency or numeric** fields we have functions that transform
    the internal float database type to the formatting settings of the
    user (**CurrencyField::convertToUserFormat**) and the reverse
    (**CurrencyField::convertToDBFormat**)

<div class="notices blue">You can find all the Currency
functionality in the class <i>CurrencyField</i> in the file
<i>include/fields/CurrencyField.php</i></div>

-   for **text** fields we use **to\_html()** and **decode\_html()**
    which use the native PHP functions **htmlentities()** and
    **html\_entity\_decode()**

<div class="notices red">
Although it may seem that text
fields would not require transformation the issue appears when using
special, non-ascii characters. These characters are converted to HTML to
show them in the browser, so if we don't turn them back into UTF8
characters then we would be saving the direct HTML into the database.
<br><br>
<strong>NOTE:</strong> this is done at the direct database retrieval level, so even
from an application point of view the information is retrieved from the
database in HTML format</div>

Pitfalls
--------

The functionality described in the previous section works well in
general but produces a significant problem when we are programming new
features inside the application.

The issue is when we launch a *$crmentity-&gt;retrieve\_entity\_info()*
to get the information of a record and we want to change the value in
one or more fields and save the record back. The information that comes
out of the *$crmentity-&gt;retrieve\_entity\_info()* call is in database
format (it is coming in from the database), but the information we are
sending into the *$crmentity-&gt;save()* is expected to be in the
user/browser format so we have to transform the fields into their
display format just to have them transformed again to be saved
correctly.

This issue can appear in various parts of the application. Mainly it
will appear in the workflow custom functions and in special process
functionality added.

There are two ways to do this transformation, **manually** or using the
**DataTransform** class.

-   Manually basically means to use the necessary functions you need to
    transform each field. The idea is that you know what you are trying
    to do and the different types of fields you have to transform so you
    apply the methods you need in each case.
-   DataTransform is a class dedicated exclusively to transforming
    fields. It has high level methods that can transform all fields in a
    module and individual transformation methods for each field type.

Example of DataTransform transformation
---------------------------------------

The DataTransform was introduced with the Web Service interface where
the problem of making sure the information being sent in was consistent
and in the correct format.

The idea is that you give the class methods a meta information object
that contains all the information of each field and it will apply the
correct formatting to each one. So to use this class we need to first
get an instantiation of the meta information class:
```php
    $handler = vtws_getModuleHandlerFromName('Events', $adminUser);
    $meta = $handler->getMeta();
```
Now we call the DataTransform method using this *$meta* object.
```php
    $focus->column_fields = DataTransform::sanitizeForInsert($focus->column_fields,$meta);
```
Let's see a real example. Imagine a function to re-open a closed ticket.
This action which appears as a link in the detail view action panel will
first execute a series of tests to make sure the ticket can be re-opened
and, if so, will change the state of the ticket. We want to do a full
save so all programmed workflows and events take place.

At some point in the execution of the action the status change is
authorized and this code is executed:
```php
    $ticket = CRMEntity::getInstance('HelpDesk');
    $ticket->retrieve_entity_info($recordid, 'HelpDesk');
    $ticket->id = $recordid;
    $ticket->column_fields['ticketstatus'] = $newStatus;
    $ticket->mode = 'edit';
    $ticket->save('HelpDesk');
```
The previous code **is wrong** and will lose date, currency and special
characters. The **correct** way to do this would be like this:
```php
    $ticket = CRMEntity::getInstance('HelpDesk');
    $ticket->retrieve_entity_info($recordid, 'HelpDesk');
    $ticket->id = $recordid;
    $ticket->column_fields['ticketstatus'] = $newStatus;
    $ticket->mode = 'edit';
    $handler = vtws_getModuleHandlerFromName('HelpDesk', $adminUser);
    $meta = $handler->getMeta();
    $ticket->column_fields = DataTransform::sanitizeForInsert($ticket->column_fields,$meta);
    $ticket->column_fields = DataTransform::sanitizeTextFieldsForInsert($ticket->column_fields,$meta);
    $ticket->save('HelpDesk');
```
Example of manual transformation
--------------------------------

In our [Timecontrol](https://github.com/tsolucio/Timecontrol) module we
have this situation and we resolved it with a manual transformation
basically because we didn't know of the existence of the DataTransform
class then.

This is the situation: a timecontrol record is started, on the detail
view of the record there is a stop watch and a button to stop the time
counting. This save button launches an action in the application to
update the total time on the record and close the timecontrol. This
*save* action retrieves the whole record, updates the end time fields
and saves the record. If we don't transform the fields to the expected
user/browser formatting the values are lost.

<div class="notices blue">
We could have proceeded to a direct
database update of the fields we need to change, that way we avoid the
full save and all the transformation issues that appear. The problem
with that approach is that any workflows or events will not be launched.
Depending on the functionality of your module and your change you may be
able to do that or not.</div>

Let's look at the code and comment it:
```php
    $focus->retrieve_entity_info($_REQUEST['record'], $currentModule);
    foreach($focus->column_fields as $fieldname => $val) {      
      $focus->column_fields[$fieldname] = decode_html($focus->column_fields[$fieldname]);
    }
    $date = new DateTimeField(null);
    $focus->column_fields['date_end'] = $date->getDisplayDate($current_user);
    $focus->column_fields['time_end'] = $date->getDisplayTime($current_user);
```
First we transform all fields with the **decode\_html()**. This is
overkill as it transform even the date and numeric fields, not only the
text fields, but since that function will not affect the date and
numeric fields we can take this approach and make sure the we encode any
additional text custom fields that may be added. Then we take care of
the end date field setting it to "NOW" and putting it into the user
format

<div class="notices red">
Note that this is REALLY wrong, we
are not taking into consideration other date and currency fields that
may be added to the module, but hopefully you'll get the
idea.</div>
