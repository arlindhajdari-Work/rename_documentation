---
title: 'coreBOS Events, Links and Hooks'
metadata:
    description: 'coreBOS permits the implementor/developer to add functionality to the existing application in three different ways: Events, Links and Hooks'
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
        - events
        - links
        - hooks
---

### Explanation

coreBOS permits the implementor/developer to add functionality to the existing application in three different ways: **Events**, **Links** and **Hooks**.

===

**Events** occur at special points in the execution of the application and the eventing system permits us to insert our own code and functionality at these points, while **Hooks** permit us to enhance the existing functionality of objects and modules as if the code had always been there. The difference is very subtle and basically resides in the way the developer's new code must be added for it to be functional. The **Events** system requires the developer to create a new class that extends the base event class, add the functionality to this class and register it into the system for it to be called, while the **Hooks** system will require adding specifically named functions and files to certain places for it to be found and executed accordingly.

**Links** are a mix between Events and Hooks as they permit us to load specific code as if it had always been there, including buttons and links, but they require to be registered in the application to be loaded.

As I have already said the difference between events and hooks is very subtle, even some types of links are hard to distinguish from hooks. In the end they are simply different ways of changing the default behavior of the application and you need to choose which one you need depending on the goal of your change.

If you read the [official definition of a hook](http://en.wikipedia.org/wiki/Hooking) or a [webhook](http://en.wikipedia.org/wiki/Webhook), you can see that there is really no distinction, they are all ways to change the behavior of the application. coreBOS makes a distinction based on the way you insert the hook into the application, in other words, depending on the steps the programmer has to take to get the hook into the system. Looking at it that way we have:

- **Events**: require that you create a specific class and launch some specific code to register the new functionality
- **Links**: require that you create a URL and register the action using some specific code
- **Hooks**: require that you create some specific code and do some steps that do not fall into the previous two categories

So, in the end the only difference is how you insert your code into the application depending on what you need to hook into.

### EVENTS: Types and usage

When you want to extend coreBOS, you can use the event API, which provides a simple way of adding actions without making any modification to the base code files.

To add a new event handler, you will need to define a class that extends the **VTEventHandler** abstract class. For example:

```php
class SimpleHandler extends VTEventHandler{
    public function handleEvent($name, $data){
    global $log;
    $log->fatal("This handler has been called for the $name event and prints this message to the log file.");
    }
}
```

Then you have to register the handler in the system with this code:

```php
require 'include/events/include.inc';
$em = new VTEventsManager($adb);
$em->registerHandler($eventName, $filePath, $className);
```

this can be done in an individual one-shot script or added to the **vtlib\_handler()** method to be executed when installing a new module or extension.

The eventing system supports two types: **actions and filters**.

An **action** will be called to do some tasks without returning a value. Actions use the **handleEvent($handlerType, $parameter)** method in the Event class, which must exist.

A **filter** will be called to do some tasks and will return a value, with which some action will be done in the application. Normally the returned value will be the same $parameter with some modifications. Filters use the **handleFilter($handlerType, $parameter)** method, which will return the new $parameter value.

### Event Launching

Events are launched for ALL modules and executed ALWAYS.

That means that we must encapsulate or protect our event code inside a condition that makes sure we are in the correct module. Looking at the different examples you can see that almost all of them start with a

"*if ($moduleName=='whatever')*"

<div class="notices blue"> This is the "de facto" standard</div>

It also means that we have to be especially careful with the things that are done, our code has to be fast and efficient in order to not block the user experience, and also resistant to errors.

Although this may seem an incorrect approach, experience shows that it is extremely powerful for many situations.

That said, the "save" events (and some others) support conditions directly in their definition and also dependency launching. These events have a "condition" column and a "dependent on" column.

The **condition column** can accept expressions following this syntax:

The accepted grammer is:
- comparision | inclause
- where
-   comparision is: SYMBOL == value
-   inclause is: SYMBOL IN listelement
-   listelement is: [ value (, value )* ]
-   SYMBOL can be: (a fieldname) | moduleName | id

for example, we can use expressions like:

```
moduleName in ['Contacts', 'Potentials']
moduleName == 'Accounts'
employees == '131'
id == '74'
rating in ['Active','Acquired']
```

The **dependent column** is a JSON encoded array of event handlers that must be executed before the one being defined. So you can ask the system to execute your event after some other event has finished.

### Supported events

<div class="notices blue"> Note that inside each event type the set of active events will be executed in order of creation (sorted by their eventid) as <a href="https://discussions.corebos.org/showthread.php?tid=1351">can be read here</a>.
</div>

#### vtiger.entity.beforesave.modifiable

This event is an internal event that is launched before any other event when an entity is saved. It should not be used.

#### vtiger.entity.beforesave

This event is fired before an entity is saved. You will be passed a **[VTEntityData](../../../03.architecture-concepts/74.vtentitydata)** object representing the saved entity. It should be noted that new objects may not have an id (if it is being created). You can modify the contents of VTEntityObject.

#### vtiger.entity.beforesave.final

This event is an internal event that is launched after all other BEFORESAVE events when an entity is saved. It should not be used.

#### vtiger.entity.aftersave.first

This event is fired after an entity is saved, but before workflows and standard aftersave events but the local save\_module() method of the object has been executed.

#### vtiger.entity.aftersave

This event is fired after an entity is saved, even the local save\_module() method of the object has been executed. This also provides a **[VTEntityData](../../../03.architecture-concepts/74.vtentitydata)** object.

#### vtiger.entity.aftersave.final

This event is an internal event that is launched after all other SAVE events have occurred. It should not be used.

#### vtiger.entity.beforedelete

This event is fired before an entity is deleted. You will be passed a **[VTEntityData](../../../03.architecture-concepts/74.vtentitydata)** object representing the entity that will be eliminated.

#### vtiger.entity.afterdelete

This event is fired after an entity is deleted. You will be passed a **[VTEntityData](../../../03.architecture-concepts/74.vtentitydata)** object representing the deleted object. Be careful as this object can no longer be referenced
using the applications' methods.

#### vtiger.entity.afterrestore

This event is fired after an entity has been recovered from the Recycle Bin. You will be passed a **[VTEntityData](../../../03.architecture-concepts/74.vtentitydata)** object representing the entity that has been restored.

#### vtiger.entity.beforegroupdelete

This event is fired before deleting a group. You will be passed an array with this structure:

```php
array(
    'groupid' => $groupId; // Group Id to be deleted:: integer
    'transferToId' => $transferId; // Id of the group/user to which record ownership is to be transferred:: integer
);
```

#### corebos.header.premenu

Will be triggered in the header of coreBOS, right after the announcement marquee has been rendered and before the application menu. It supports a generic way of sending some output before the menu.

This event does not receive any parameters.

#### corebos.header

Will be triggered in the header of coreBOS, right after the menu has been rendered and before the call to the module to be loaded. It supports a generic way of sending some output before any module output.

This event does not receive any parameters.

#### corebos.footer.prefooter

Will be triggered in the footer of coreBOS, right before calling the code to output the default application footer.

This event does not receive any parameters.

#### corebos.footer

Will be triggered in the footer of coreBOS, when the whole execution has ended. If the logged-in user is an admin user this event will be used to print out a time execution summary of the events.

This event does not receive any parameters.

![](corebosheaderfooterhooks.png?width=100%)

#### corebos.popup.footer

Will be triggered in the footer of the coreBOS popup window when capturing a record in a uitype 10 field, when the whole execution has ended.

This event does not receive any parameters.

#### corebos.filter.listview.querygenerator.before

Will be triggered before QueryGenerator will be used to create the Query for the List View Entries. It can be used to manipulate the QueryGenerator, adding or eliminating fields to be used by the List View.

This event receives $queryGenerator as a parameter and must return the same object.

#### corebos.filter.listview.querygenerator.after

Will be triggered after QueryGenerator was used to create the Query for the List View Entries. it can be used to manipulate the QueryGenerator, adding or eliminating fields to be used by the List View.

This event receives $queryGenerator as a parameter and must return the same object.

#### corebos.filter.listview.querygenerator.query

Will be triggered once the QueryGenerator has completely finished and will receive the generated query as a string, so it can be manipulated. Using this event you could override the result of the QueryGenerator.

This event receives $list\_query as a parameter and must return the same object.

#### corebos.filter.listview.render

Will be triggered at the end of every List View Entry (row in the table) generation and receives the final HTML code of every column in one row. Could be used to manipulate the HTML of each column inside List View

Receives an array with three elements of the current row:

<table class="table table-striped">
<th>$parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>$columnHtml</td>
<td>html of the content of every column (Not the &lt;td&gt; itself)</td>
</tr>
<tr class="even">
<td>$row</td>
<td>complete Fetch of the Row from DB Query</td>
</tr>
<tr class="odd">
<td>$recordID</td>
<td>associated recordID of this row</td>
</tr>
</tbody>
</table>

#### corebos.filter.listview.header

Will be triggered at the end of the creation of the List View table header (header row in the table) and receives the final HTML code of every column in the header row. Could be used to manipulate the HTML of each column inside the header or for adding a new column header

#### corebos.filter.listview.filter.show

This event will be called for each filter to be shown in the list view filters picklist. It will receive an array with the full details of the filter to be loaded and expects a boolean (True/False) response that will indicate if the filter is to be added to the picklist or not.

#### corebos.filter.editview.setObjectValues

This event will be called when a new record is being created. It will receive the new CRMEntity object so you can add default values to any field using the column\_field property. Obviously, you could do other verification or functionality tasks.

You must return the object given.

<div class="notices blue">The <a href="https://github.com/tsolucio/coreBOSAddress"><i>coreBOSAddress</i></a> module has an exceptional example of how this works by filling in the address fields when creating a new record from its related list.</div>

#### corebos.filter.link.show

This event will be called for each Link to be loaded in the application. It will receive an array with the full details of the link to be loaded and expects a boolean (True/False) response that will indicate if the link is to be added or not.

#### corebos.filter.ModComments.canAdd

This event must return a true or false value and will be called in three parts of the application:

- showing the ModComments widget on the detail view of a record. If false is returned the user will not be able to see the add widget section
- when saving a comment via the detail view widget. If false is returned the comment will not be created
- when saving a comment in the module. If false is returned an error message will be shown on screen and the comment will not be created

#### corebos.filter.ModComments.queryCriteria

This event will be called when constructing the SQL query to retrieve the comments associated with a record. We must return a part of the *WHERE* condition that modifies the final query.

#### corebos.entity.link.before

Action launched BEFORE two entities are about to be related. The action receives the names and IDs of the records being related.

#### corebos.entity.link.after

Action launched AFTER two entities have been related. The action receives the names and IDs of the records being related.

#### corebos.entity.link.delete

Action launched when two entities are about to be UNrelated (BEFORE). The action receives the names and IDs of the records being UNrelated.

#### corebos.entity.link.delete.final

Action launched when two entities have just been UNrelated (AFTER). The action receives the names and IDs of the records being UNrelated.

#### corebos.filter.preSaveCheck

Filter launched before starting the Save process. Will receive, the $\_REQUEST variable and the current object trying to be saved. It must return, besides these two input parameters, an error status, an error message, an error action and an array of variables to return to the edit screen the process was initiated from. 

[You can read a little more about this filterhere](../../../03.architecture-concepts/78.precrud)

#### corebos.filter.preEditCheck

Filter launched before starting the Edit process. Will receive, the $\_REQUEST variable, the Smarty object and the current object trying to be edited.

[You can read a little more about this filter here](../../../03.architecture-concepts/78.precrud)

#### corebos.filter.preViewCheck

Filter launched before starting the Detail View process. Will receive, the $\_REQUEST variable, the Smarty object and the current object trying to be viewed.

[You can read a little more about this filter here](../../../03.architecture-concepts/78.precrud)

#### corebos.filter.preDeleteCheck

Filter launched before deleting a record. Will receive, the current object trying to be deleted and must return a boolean indicating if the action may proceed or not and a message to show in case it cannot.

[You can read a little more about this filter here](/en/devel/corebos_hooks/precrud)

#### corebos.audit.\[authenticate|login|login.attempt|logout|action\]

Actions called on the indicated events

#### corebos.filter.inventory.getprice

When the application requires a product/service price, it will get the unit price field from the database and then call this filter with some information so we can calculate some other price to be returned.

This filter receives these parameters:

- the unit price
- the discount (always 0 as the application does not natively calculate this)
- an array with these values:
  - inventory module we are on
  - module id if we are editing
  - accountid (maybe 0 if not selected)
  - contactid (maybe 0 if not selected)
  - productid/serviceid
  - related\_module

#### corebos.filter.announcement

return the announcement to show. permits creating dynamic announcements

### Custom Permission Hooks

**corebos.permission.\[accessquery|ispermitted\]**: [Custom Permission Hooks](../../../03.architecture-concepts/80.corebos_permission_hooks)

### Events Examples

When you register an event in the application the details are saved in the **vtiger\_eventhandlers** table, so the best way to find examples of the different types of events above is to look in that table for real working code. For example, you can find there:

<table class="table table-striped">
<th>event_name</th>
<th>handler_path</th>
<th>handler_class</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>vtiger.entity.aftersave</td>
<td>modules/SalesOrder/RecurringInvoiceHandler.php</td>
<td>RecurringInvoiceHandler</td>
<td>Takes care of preparing information for
 the cron script that converts sales orders into invoices</td>
</tr>
<tr class="even">
<td>vtiger.entity.beforesave</td>
<td>data/VTEntityDelta.php</td>
<td>VTEntityDelta</td>
<td>This class handles the "Has Changed" condition in workflows.
 This part saves the information <strong>before</strong> it is saved in the database.</td>
</tr>
<tr class="odd">
<td>vtiger.entity.aftersave</td>
<td>data/VTEntityDelta.php</td>
<td>VTEntityDelta</td>
<td>This class handles the "Has Changed" condition in workflows.
 This part saves the information <strong>after</strong> it is saved in the database.</td>
</tr>
<tr class="even">
<td>vtiger.entity.aftersave</td>
<td>modules/com_vtiger_workflow/VTEventHandler.inc</td>
<td>VTWorkflowEventHandler</td>
<td>Takes care of launching workflows</td>
</tr>
<tr class="odd">
<td>vtiger.entity.afterrestore</td>
<td>modules/com_vtiger_workflow/VTEventHandler.inc</td>
<td>VTWorkflowEventHandler</td>
<td>Takes care of launching workflows</td>
</tr>
<tr class="even">
<td>vtiger.entity.aftersave.final</td>
<td>modules/HelpDesk/HelpDeskHandler.php</td>
<td>HelpDeskHandler</td>
<td>Takes care of sending emails and other tasks related to tickets</td>
</tr>
<tr class="odd">
<td>vtiger.entity.aftersave.final</td>
<td>modules/ModTracker/ModTrackerHandler.php</td>
<td>ModTrackerHandler</td>
<td>Takes care of registering changes that happen to the record</td>
</tr>
<tr class="even">
<td>vtiger.entity.beforedelete</td>
<td>modules/ModTracker/ModTrackerHandler.php</td>
<td>ModTrackerHandler</td>
<td>Takes care of registering changes that happen to the record</td>
</tr>
<tr class="odd">
<td>vtiger.entity.beforesave</td>
<td>modules/ServiceContracts/ServiceContractsHandler.php</td>
<td>ServiceContractsHandler</td>
<td>Takes care of updating the hours used</td>
</tr>
<tr class="even">
<td>vtiger.entity.aftersave</td>
<td>modules/ServiceContracts/ServiceContractsHandler.php</td>
<td>ServiceContractsHandler</td>
<td>Takes care of updating the hours used</td>
</tr>
<tr class="odd">
<td>vtiger.entity.aftersave</td>
<td>modules/Emails/evcbrcHandler.php</td>
<td>evcbrcHandler</td>
<td>Takes care of updating the read-only email fields
 on Potential, Projects and Tickets (among others)</td>
</tr>
<tr class="even">
<td>vtiger.entity.aftersave</td>
<td>modules/Calendar4You/GoogleSync4YouHandler.php</td>
<td>GoogleSync4YouHandler</td>
<td>Takes care of sending calendar events to Google Calendar</td>
</tr>
<tr class="odd">
<td>vtiger.entity.beforedelete</td>
<td>modules/Calendar4You/GoogleSync4YouHandler.php</td>
<td>GoogleSync4YouHandler</td>
<td>Takes care of deleting calendar events to Google Calendar</td>
</tr>
<tr class="even">
<td>corebos.footer</td>
<td>build/HelperScripts/coreBOSEventsExample.php</td>
<td>coreBOSEventsExample</td>
<td>Prints a text to footer</td>
</tr>
<tr class="odd">
<td>corebos.footer.prefooter</td>
<td>build/HelperScripts/coreBOSEventsExample.php</td>
<td>coreBOSEventsExample</td>
<td>Prints a text above default application footer</td>
</tr>
<tr class="even">
<td>corebos.header</td>
<td>build/HelperScripts/coreBOSEventsExample.php</td>
<td>coreBOSEventsExample</td>
<td>Prints a text to header</td>
</tr>
<tr class="odd">
<td>corebos.header.premenu</td>
<td>build/HelperScripts/coreBOSEventsExample.php</td>
<td>coreBOSEventsExample</td>
<td>Prints a text to above menu</td>
</tr>
<tr class="even">
<td>corebos.filter.listview.querygenerator.before</td>
<td>build/HelperScripts/coreBOSEventsExample.php</td>
<td>coreBOSEventsExample</td>
<td>Adds homephone field to query generator,
 can be seen on any Contacts list view</td>
</tr>
<tr class="odd">
<td>corebos.filter.listview.querygenerator.after</td>
<td>build/HelperScripts/coreBOSEventsExample.php</td>
<td>coreBOSEventsExample</td>
<td>Removes homephone field from query generator, 
can be seen on any Contacts list view filter with the homephone field</td>
</tr>
<tr class="even">
<td>corebos.filter.listview.querygenerator.query</td>
<td>build/HelperScripts/coreBOSEventsExample.php</td>
<td>coreBOSEventsExample</td>
<td>This example simply outputs the SQL to the browser</td>
</tr>
<tr class="odd">
<td>corebos.filter.listview.render</td>
<td>build/HelperScripts/coreBOSEventsExample.php</td>
<td>coreBOSEventsExample</td>
<td>This example adds a new column with a text input field for homephone 
when on the Contacts module and a new row link to go directly to the "More Information" 
section when on Accounts</td>
</tr>
<tr class="even">
<td>corebos.filter.listview.header</td>
<td>build/HelperScripts/coreBOSEventsExample.php</td>
<td>coreBOSEventsExample</td>
<td>This adds the column header for the new text homephone field in the "render" example</td>
</tr>
<tr class="odd">
<td>corebos.filter.listview.filter.show</td>
<td>build/HelperScripts/coreBOSEventsExample.php</td>
<td>coreBOSEventsExample</td>
<td>This example eliminates the filter named "Contacts Address" 
from the Contacts filter picklist</td>
</tr>
<tr class="even">
<td>corebos.filter.editview.setObjectValues</td>
<td>build/HelperScripts/coreBOSEventsExample.php</td>
<td>coreBOSEventsExample</td>
<td>This example fills in the <strong>Lead Source</strong> picklist and <strong>Assistant</strong> on Accounts when creating a new record</td>
</tr>
<tr class="odd">
<td>corebos.filter.link.show</td>
<td>build/HelperScripts/coreBOSEventsExample.php</td>
<td>coreBOSEventsExample</td>
<td>This example eliminates all Detail View links. 
Once activated you will see that no module has ModComments and many 
of their action links have disappeared</td>
</tr>
<tr class="even">
<td>corebos.filter.ModComments.canAdd</td>
<td>build/HelperScripts/coreBOSEventsExample.php</td>
<td>coreBOSEventsExample</td>
<td>This example eliminates the add comment feature
 for the crmid record with value 2</td>
</tr>
<tr class="odd">
<td>corebos.filter.ModComments.queryCriteria</td>
<td>build/HelperScripts/coreBOSEventsExample.php</td>
<td>coreBOSEventsExample</td>
<td>This example hides all comments that belong to user
 with ID equal to 1</td>
</tr>
</tbody>
</table>

<div class="notices blue"> For the coreBOSEventsExample.php examples you can find the script to register the events in the HelperScripts directory: build/HelperScripts/coreBOSEventsLoader.</div>

### HOOKS: Types and usage

Each hook requires its' own specific magic and steps to get them working and cover different aspects of functionality enhancement.

- [Popup open hook](../../../03.architecture-concepts/75.popup_capture_hook)
- [Popup capture hook](../../../03.architecture-concepts/75.popup_capture_hook)
- [Popup query hook](../../../03.architecture-concepts/75.popup_capture_hook)
- [Related List hook](../../../03.architecture-concepts/75.popup_capture_hook)
- afterImportRecord

### LINKS: Types and usage

**Links** permit us to add buttons and action links and also to load javascript and CSS into the application.

To register these actions into coreBOS we use the vtlib API interface **addLink()** method:

```php
    include_once('vtlib/Vtiger/Module.php');
    $moduleInstance = Vtiger_Module::getInstance('ModuleName');
    $moduleInstance->addLink(<LinkType>, <LinkLabel>, <LinkURL>, <IconPath>);
```

<table class="table table-striped">
<th>LinkType</th>
<th>Type of Link (see below)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LinkLabel</td>
<td>Label to use for the link when displaying</td>
</tr>
<tr class="even">
<td>LinkURL</td>
<td>URL of the link. You can use variables like <strong>$MODULE$</strong>
 and <strong>$RECORD$</strong> which will be replaced with the values of the current module and crmid</td>
</tr>
<tr class="odd">
<td>IconPath</td>
<td>full path to an icon that will be used in the right action panel</td>
</tr>
</tbody>
</table>
<br>

You can find a real example in the [add Action Link Helper Script](../../06.helperscripts/item.md#addactionlinkphp)

<br>
<table class="table table-striped">
<th>Type</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DETAILVIEWBASIC</td>
<td>Link on the right action panel of a record</td>
</tr>
<tr class="even">
<td>DETAILVIEW</td>
<td>Hover menu on the right action panel of a record that contains the link</td>
</tr>
<tr class="odd">
<td>DETAILVIEWWIDGET</td>
<td>A block of code contained in a box on the view of a record. It can either
 be a small box on the action panel or a <a href="../../../developer-guide/development_framework/develtutorials/add_special_block">full fledged block inserted into the existing field blocks</a></td>
</tr>
<tr class="even">
<td>LISTVIEWBASIC</td>
<td>Button on the top of the list view of a module</td>
</tr>
<tr class="odd">
<td>LISTVIEW</td>
<td>Hover menu on the top of the list view of a module that contains the link</td>
</tr>
<tr class="even">
<td>HEADERLINK</td>
<td>Hover menu on the top of the browser screen that contains the link. 
It appears next to the Preferences icon and is a global action link</td>
</tr>
<tr class="odd">
<td>HEADERSCRIPT</td>
<td>Permits the inclusion of a javascript file located in the application</td>
</tr>
<tr class="even">
<td>HEADERCSS</td>
<td>Permits the inclusion of a CSS style file located in the application</td>
</tr>
<tr class="odd">
<td>HEADERSCRIPT_POPUP</td>
<td>Permits the inclusion of a javascript file located in the popup screen of the application</td>
</tr>
<tr class="even">
<td>HEADERCSS_POPUP</td>
<td>Permits the inclusion of a CSS style file located in the popup screen of the application</td>
</tr>
<tr class="odd">
<td>PRESAVE</td>
<td>Permits us to launch code when the user clicks on the SAVE button 
BEFORE the operation is done. We will be able to execute code in the PHP 
application and force the execution of a javascript function. The javascript 
function takes full control of the save process which means that it must 
submit the form if it decides to. In order to do that it will receive the 
parameters: edit_type, formName, action, callback, any parameters sent by the php code</td>
</tr>
</tbody>
</table>

<br>

<div class="notices red">Get more details in the [development tutorial](../18.add_actions).</div>

### coreBOS JavaScript Hooks

[Read all about them here](../../../03.architecture-concepts/81.corebosjshooks)
