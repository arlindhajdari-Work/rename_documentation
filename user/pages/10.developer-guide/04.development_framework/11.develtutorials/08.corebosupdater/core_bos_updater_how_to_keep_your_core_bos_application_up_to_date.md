---
title: 'coreBOS Updater :: How to keep your coreBOS application up to date'
metadata:
    description: 'Learn how to keep your coreBOS application constantly and easily up to date with the updater concept.'
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
        - updater
    tag:
        - migration
        - update
        - version
---

<u>coreBOS 5.5</u> has brought a new tool to our *powerful business operating system* : **coreBOS Updater**.

Since we have a **very stable and tested code base**, and thanks to the
powerful code administration and distribution system that
[GitHub](https://github.com) gives us, it just seems natural to put your
coreBOS install under code versioning with git (be that private or open)
and point a remote to the [public, open-source coreBOS project](https://github.com/tsolucio/corebos).

Once you have that setup, updating your code with our (constant) changes
is fairly easy, as git carries all the heavy weight during **merge**,
leaving us to fix the minor details.

So with the approach above and the fact that the majority of changes we
make are also **tested and stable**, you really don't have to wait for
us to release an official download to get the new features, you just
update your code and _apply the database changes_ the new code may require.

<div class="notices red">
Wait!! Apply database changes??? How do you do that? git doesn't do that, how do I know what changes I need to apply?
</div>

Enter **coreBOS Updater**.

**coreBOS Updater** is a tool that will control the state of our
database with respect to the code and will be able to automatically
apply the pending changes that are needed. This way the upgrade process
is converted into these steps:

1.  update your code with git (or manually if you are brave :-))
2.  log into the application and go to the coreBOS Updater module
3.  click on the "Load Updates" button
4.  click on the "Apply All" button

**You are finished! That easy!** coreBOS updater has taken care of all
the pending database changes and your code and database are in sync and
ready for you to start working.

Going forward all future releases of coreBOS will follow this procedure
to apply database changes for the upgrades.

If you have a look at the module you will see that each changeset is
created as a record in the module. You can see the **details** of the
change and also **undo** some of them, all those which are not pure
**system** updates. The **system** type changesets are mandatory for the
application to work correctly.

# coreBOS Updater :: How to prepare and distribute system changes


From a developer's point of view, the coreBOS Updater tool is a clean way
of recording database changes in code. This permits us to control (to
some extent) the set of database changes that are needed in our version
control system.

Since we are actually programming the changes in files, we then version
those changes along with the rest of file changes that define the new
feature or bug fix and it all gets registered in the versioning system.

To help us prepare the database changes coreBOS updater is going to take
care of all the dirty work it can for us, so we basically just have to
write the changes that are needed.

Step 1: Define the change and the file that contains the work to be done
------------------------------------------------------------------------

Create a new file in *modules/cbupdater/cbupdates/yourproject.xml* and
add your definition to the list of changes.

<div class="notices red"> The file
<i>modules/cbupdater/cbupdater.xml</i> is the main change file of the coreBOS
application. Although you can use this file to register your changes the
correct way to distribute them is by creating your own changeset XML
file inside the <i>modules/cbupdater/cbupdates</i> directory. When coreBOS
Updater looks for changes it reads them from the base
<i>modules/cbupdater/cbupdater.xml</i> file and then looks for any .xml file
inside <i>modules/cbupdater/cbupdates</i> to pickup those changes also. That
way each programmer can easily distribute changes without overwriting
the base application changesets.</div>

The XML changeSet element contains various entries of which only two are
mandatory, but all recommended:

<table class="table table-striped">
<td><strong>author</td>
<td>optional</td>
<td>Name of the person or company adding this changeset</td>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>description</td>
<td>optional</td>
<td>Explanation of the goals of this changeset</td>
</tr>
<tr class="even">
<td><strong>filename</td>
<td>mandatory</td>
<td>Name of the file which contains the changes. This file can be anywhere on the file system as long as it is accessible by coreBOS. We propose and recommend that these changesets be saved all together in <em>build/changeSets</em> directory</td>
</tr>
<tr class="odd">
<td><strong>classname</td>
<td>mandatory</td>
<td>Name of the class that implements the changes (explained next)</td>
</tr>
<tr class="even">
<td><strong>systemupdate</td>
<td>optional</td>
<td>True if the changeset is mandatory, false if it can be undone</td>
</tr>
<tr class="odd">
<td><strong>perspective</td>
<td>optional</td>
<td>True if the changeset is a <a href="../../../developer-guide/development_framework/develtutorials/corebosupdater#corebos-updater-corebos-perspectives">perspective (see below)</a></td>
</tr>
<tr class="even">
<td><strong>continuous</td>
<td>optional</td>
<td>True if the changeset must/can be executed always. Certain changeset are very general and can be (or must be) applied many times.</td>
</tr>
</tbody>
</table>
<br>

An example:

```xml
<changeSet>
    <author>joebordes</author>
    <description>Custom field support on FAQ module</description>
    <filename>build/changeSets/cffaq.php</filename>
    <classname>cffaq</classname>
    <systemupdate>true</systemupdate>
    <perspective>false</perspective>
    <continuous>false</continuous>
</changeSet>
```

The file *modules/cbupdater/cbupdater.xsd* defines the official schema
accepted for the XML changeset file and it is used by coreBOS Updater to
validate the XML format.

![](cbupdater_xsd.png?width=100%)

Step 2: Implement your change
-----------------------------

-   copy *build/changeSets/cbupdate\_template.php* to the name you used
    in the XML &lt;filename&gt; element
-   edit your script
-   change the license
-   change the name of the class to the name you used in the XML
    &lt;classname&gt; element
-   edit the applyChange() function: locate the line that contains "do
    your magic here" and start adding your changes
-   edit the undoChange() function: locate the line that contains "undo
    your magic here" and start adding code to undo the change
-   test and validate

<div class="notices blue">If your change cannot be undone you
can eliminate the undo function completely and coreBOS Updater will take
care of it.</div>

You can find a whole bunch of **real examples** of different types in
the *build/changeSets* directory.

Step 3: Test, validate and version the change
---------------------------------------------

**Really!!**: Test, validate and version the change.

coreBOS Updater :: Class and helper functions explained
=======================================================

coreBOS Updater changes are implemented by extending the
**cbupdaterWorker** class. This class gives us all the functionality to
plug into the coreBOS system and do any type of action that may be
required.

Basically, the only method we need to override is the **applyChange()**
method. This method implements the changes that represent the changeset.
If your change can be undone then you must also override the
**undoChange()** method and add the necessary code to undo the change.

The rest of the methods that the **cbupdaterWorker** class implements
are helper methods and some auxiliar methods for functionality:

<table class="table table-striped">
<td>__construct</td>
<td>will load the changeset definition from the database, if it isn't found there an error will be shown and the process will stop. If all goes well this method starts the output formatting on screen</td>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>isApplied</td>
<td>boolean method which tells us the applied state as recorded in the database</td>
</tr>
<tr class="even">
<td><strong>isBlocked</td>
<td>boolean method which tells us if the change set is blocked. If a changeset is blocked it cannot be applied nor undone. It will automatically be ignored</td>
</tr>
<tr class="odd">
<td><strong>isContinuous</td>
<td>boolean method which tells us if the changeset is of type Continuous. Continuous changesets can be applied many times without breaking the system and will be picked up when launching an "Apply All"</td>
</tr>
<tr class="even">
<td><strong>isSystemUpdate</td>
<td>boolean method which tells us if the current changeset is a <em>system</em> changeset</td>
</tr>
<tr class="odd">
<td><strong>hasError</td>
<td>boolean method which indicates if there has been an error executing the changeset</td>
</tr>
<tr class="even">
<td><strong>markApplied($stoponerror=true)</td>
<td>helper method which does the work of cleaning up after the changeset has been applied. This must be executed at the end of a correct execution of <strong>applyChange()</strong></td>
</tr>
<tr class="odd">
<td><strong>markUndone($stoponerror=true)</td>
<td>helper method which does the work of cleaning up after the changeset has been undone. This must be executed at the end of a correct execution of <strong>undoChange()</strong></td>
</tr>
<tr class="even">
<td><strong>sendMsg($msg)</td>
<td>put the given successful message on screen following the coreBOS Updater on-screen formatting</td>
</tr>
<tr class="odd">
<td><strong>sendMsgError($msg)</td>
<td>put the given error message on screen following the coreBOS Updater on-screen formatting</td>
</tr>
<tr class="even">
<td><strong>finishExecution</td>
<td>closes the on screen formatting and outputs the results of the execution</td>
</tr>
<tr class="odd">
<td><strong>ExecuteQuery($query,$params=array())</td>
<td>helper method that permits us to send SQL commands to the database. This method shows the result on-screen and counts updates the SQL command succees/failure counters. With this method, it is not necessary to execute direct SQL commands against the global $adb object, although you can if you need/want to</td>
</tr>
<tr class="even">
<td><strong>deleteWorkflow($wfid)</td>
<td>helper method that permits us to delete workflows</td>
</tr>
<tr class="odd">
<td><strong>installManifestModule($module)</td>
<td>helper method that simplifies the task of installing a new module</td>
</tr>
<tr class="even">
<td><strong>isModuleInstalled($module)</td>
<td>helper method that looks in the vtiger_tab table to see if a given module is installed, be it active or not</td>
</tr>
<tr class="odd">
<td><strong>deleteAllPicklistValues($tableName, $moduleName)</td>
<td>will eliminate all the values in the given picklist</td>
</tr>
<tr class="even">
<td><strong>deletePicklistValues($values, $tableName, $moduleName)</td>
<td>will eliminate the given values from the given picklist</td>
</tr>
<tr class="odd">
<td><strong>setQuickCreateFields($moduleName, $qcfields)</td>
<td>will set the given fields to appear in the quick create form</td>
</tr>
<tr class="even">
<td><strong>massCreateFields($fieldLayout)</td>
<td>an easy structure to mass create blocks and fields in modules</td>
</tr>
<tr class="odd">
<td><strong>massHideFields($fieldLayout)</td>
<td>an array of fields to hide</td>
</tr>
<tr class="even">
<td><strong>massDeleteFields($fieldLayout)</td>
<td>an array of fields to delete</td>
</tr>
<tr class="odd">
<td><strong>massMoveFieldsToBlock($fieldLayout, $newblock)</td>
<td>move fields around</td>
</tr>
<tr class="even">
<td><strong>orderFieldsInBlocks($fieldLayout)</td>
<td>order fields</td>
</tr>
<tr class="odd">
<td><strong>convertTextFieldToPicklist($fieldname, $module, $multiple = false)</td>
<td>convert the given text field into a picklist. it will deduplicate and set the existing values</td>
</tr>
<tr class="even">
<td><strong>setTooltip($tooltips)</td>
<td>set the tooltip for the given fields</td>
</tr>
<tr class="odd">
<td><strong>removeAllMenuEntries($module)</td>
<td>remove the given module name from all menu entries it appears in</td>
</tr>
</tbody>
</table>

applyChange()
-------------

After reading the above functionality we can see that the applyChange()
method template prepares everything so we just have to write our
changes:
```php
function applyChange() {
  if ($this->isBlocked()) return true;
  if ($this->hasError()) $this->sendError();
  if ($this->isApplied()) {
     $this->sendMsg('Changeset '.get_class($this).' already applied!');
  } else {
     // do your magic here
     $this->sendMsg('Changeset '.get_class($this).' applied!');
     $this->markApplied();  // this should not be done if changeset is coninuous
  }
  $this->finishExecution();
}
```
First it makes sure there is no error and it isn't blocked, then it
checks if it is already applied, if that is ok, then it lets us do
whatever we need to do and it ends up marking the changeset done,
informing the user and finishing the changeset.

undoChange()
------------

After reading the above functionality we can see that the undoChange()
method template prepares everything so we just have to write code to
undo our changes:

```php
function undoChange() {
  if ($this->isBlocked()) return true;
  if ($this->hasError()) $this->sendError();
  if ($this->isSystemUpdate()) {
    $this->sendMsg('Changeset '.get_class($this).' is a system update, it cannot be undone!');
  } else {
    if ($this->isApplied()) {
       // undo your magic here
       $this->sendMsg('Changeset '.get_class($this).' undone!');
      $this->markUndone();  // this should not be done if changeset is coninuous
    } else {
     $this->sendMsg('Changeset '.get_class($this).' not applied!');
    }
  }
 $this->finishExecution();
}
```

First, it makes sure there is no error and it isn't blocked, then it
checks if it is a system update in which case it stops the execution as
system changesets cannot be undone. Next, it looks if it is applied
because if it isn't it can't be undone. If that is ok, then it lets us
do whatever we need to do and it ends up marking the changeset undone,
informing the user and finishing the changeset.

Examples
--------

You can find a whole bunch of **real examples** of different types in
the *build/changeSets* directory, but I am going to comment on a few of
the interesting ones.

<table class="table table-striped">
<td><a href="https://github.com/tsolucio/corebos/blob/master/build/changeSets/add_workflow_tags.php">add_workflow_tags.php</a></td>
<td>this one is interesting for two things: one is to see how a new workflow method is added using the <em>VTTaskType::registerTaskType()</em> method, and the other because it implements its own <em>isApplied()</em> because it looks for the new workflow tasks it wants to create before permitting it to be created</td>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="https://github.com/tsolucio/corebos/blob/master/build/changeSets/installcyp.php">installcyp.php</a></td>
<td>interesting to see how a module is installed and deactivated when undone</td>
</tr>
<tr class="even">
<td><a href="https://github.com/tsolucio/corebos/blob/master/build/changeSets/PotentialForecastAmount.php">PotentialForecastAmount.php</a></td>
<td>interesting to see how to add new fields and also a workflow associated with the field</td>
</tr>
<tr class="odd">
<td><a href="https://github.com/tsolucio/corebos/blob/master/build/changeSets/workflow_contactassignedto.php">workflow_contactassignedto.php</a></td>
<td>interesting to see how to add a workflow custom method and check if it can be undoone</td>
</tr>
</tbody>
</table>

Command Line Execution
----------------------

coreBOS updater has a set of scripts that permit loading and applying
changesets from the command line:

-   **getupdatescli.php** which loads changesets into the application
    from the default files or from an .xml file given as a parameter.
    This script returns a comma-separated list of changesets IDs created
-   **doworkcli.php** which can apply or undo a given set of coreBOS
    updater changesets or simply ALL
-   **loadapplychanges.php** which executes in order the two previous
    scripts to directly load and apply all changesets in a given .xml
    definition file

You can use this script in your composer.json file to apply changesets
after loading some modules:
```php
...
  },
  "scripts": {
    "post-install-cmd": [
    	"tsolucio\\ComposerInstall\\ComposerInstall::postPackageInstall",
    	"php modules/cbupdater/loadapplychanges.php modules/ConfigEditor/composer.xml"
    ],
    "post-update-cmd": "tsolucio\\ComposerInstall\\ComposerInstall::postPackageUpdate"
  }
}
```

coreBOS Perspective Changeset Loader
------------------------------------

The coreBOS Perspective changeset loader is an extension for
distributing coreBOS updater changesets. It gives the developer the
infrastructure to simply create the set of changesets that need to be
applied and distribute and apply them easily into any existing coreBOS
application.

Once defined the .xml change file and created all the changesets you can
send this extension to any coreBOS application or include it as part of
a perspective, to have the changes applied.

[We have created a template project on github](https://github.com/tsolucio/cbPerspectiveCS) which you can use
as a starting point for your changes or simply to study how it is done.

Ideally, you will create one of these extensions for your perspective in
such a way that it will require first for all the new modules to be
installed and then, the last one will be this extension which will apply
the final changes to get all the functionality into place.

## coreBOS Updater :: coreBOS Perspectives

**coreBOS Updater** is one fundamental step towards an important concept
that we have on our roadmap: <span style="color:red;">Perspectives</span>.

A perspective is a set of code and database changes that literally
convert a stock coreBOS system into a verticalization prepared for a
clearly defined market segment.

The other big step upon which the perspective concept stands is the
[code structure and packaging system](../05.packagemodules). Since
we have laid out the code in such a way that we do not need to update
packages and all the code is simply there, in place, ready to be
modified we can easily define a perspective as:

- a patch to change the code (this should not be required)
- an .xml coreBOS Updater changeset file and its associated worker scripts
- a composer.json file to install the new modules

The patch will add the changes that the code needs while the coreBOS
updater .xml changeset file and the composer.json file will define the
set of database changes and new modules that are needed to convert the
raw application into the verticalization we need.

[Read this blog post for more information](https://blog.corebos.org/blog/cbperspective)

coreBOS Updater :: Custom Changesets without coding
===================================================

The majority of changes in the updater will come from the coreBOS
project development effort. You will update your code and get new
changesets as required. These changeset records will be marked as
"Application Changesets" and you will not be able to edit nor delete them.

The other type of changesets are the ones you can create as any other
record in the application. These "manual" changesets support a very
restricted set of actions but can turn out to be very useful for customizing a coreBOS install for your users in certain cases.

Some of these **restrictions** are:

- you can only execute one action per changeset
- you cannot undo these changesets
- you can only execute the supported actions

The way these changesets work is by defining the action to execute with
a JSON object saved in the **description** field. The other fields are
either not used or maintain their normal meaning.

All the JSON objects have a set of common fields:

- **name**: a name for your changeset. this field is descriptive (not used)
- **description**: a description for your changeset. this field is descriptive (not used)
- **operation**: supported action
- **setting**: configuration options for the selected action

Next, we document the JSON format for each of the supported actions with some examples.

deleteAllPicklistValues
-----------------------

Will delete **ALL** the values in a picklist.

```php
{
"name": "del values industry",
"description": "delete all the current values in the industry picklist of Accounts",
"operation": "deleteAllPicklistValues",
"setting": {
    "table": "industry",
    "module": "Accounts"
  }
}
```

```php
{
"name": "del values building",
"description": "delete all the current values in the building picklist of Products",
"operation": "deleteAllPicklistValues",
"setting": {
    "table": "building",
    "module": "Products"
  }
}
```

deletePicklistValues
--------------------

Will delete **the given** values from a picklist.

```php
{
"name": "del values industry",
"description": "delete some values from the industry picklist of Accounts",
"operation": "deletePicklistValues",
"setting": {
    "table": "industry",
    "module": "Accounts",
    "values": ["Telecommunications", "Banking"]
  }
}
```

```php
{
"name": "del values prodtype",
"description": "delete some values from the prodtype picklist of Products",
"operation": "deletePicklistValues",
"setting": {
    "table": "prodtype",
    "module": "Products",
    "values": ["Sell", "Rent Holiday"]
  }
}
```

setQuickCreateFields
--------------------

Given an array of field names, this method will activate them in Quick
Create in the given order. All the other fields will be deactivated.

```php
{
"operation": "setQuickCreateFields",
"setting": {
    "fields": ["fieldname1", "fieldname2", "fieldname3"],
    "module": "Accounts"
  }
}
```

```php
{
"operation": "setQuickCreateFields",
"setting": {
    "fields": ["floor", "internet", "building"],
    "module": "Products"
  }
}
```

massCreateFields
----------------

Given an array of field definitions, this method will create or activate
the fields. The layout is an array of Module Name, Block Name, and Field Definition.

```php
{
"operation": "massCreateFields",
"setting":
  {
    "module":{
    "block name or ID":{
        "fieldname1": {
            "columntype": "decimal(10,3)",
            "typeofdata": "NN~O",
            "uitype": "1",
            "displaytype": "3",
            "label": "", // optional, if empty fieldname will be used
            "massedit":  0 | 1  // optional, if empty 0 will be set
            "mods": [module names], // used if uitype 10
            "vals": [picklist values], // used if uitype 15, 16 or 33
          },
        "fieldname2": {
            "columntype": "decimal(10,3)",
            "typeofdata": "NN~O",
            "uitype": "1",
            "displaytype": "3",
            "label": "", // optional, if empty fieldname will be used
            "massedit":  0 | 1  // optional, if empty 0 will be set
            "mods": [module names], // used if uitype 10
            "vals": [picklist values], // used if uitype 15, 16 or 33
          }
      }
    }
  }
}
```

```php
{
"operation": "massCreateFields",
"setting":
  {
    "Vendors": {
      "Custom Information": {
            "cal": {
              "columntype": "int(11)",
              "typeofdata": "V~O",
              "uitype": "10",
              "displaytype": "1",
              "label": "Sabi",
              "massedit":  "1",
              "mods":"Products"
            },
            "volume": {
              "columntype": "varchar(100)",
              "typeofdata": "V~O",
              "uitype": "1",
              "displaytype": "1",
              "label": "Volume",
              "massedit":  "1"
            }
      }
    }
  }
}
```

```php
{
"operation": "massCreateFields",
"setting":
  {
    "Vendors": {
      "Custom Information": {
            "palm": {
              "columntype": "int(11)",
              "typeofdata": "V~O",
              "uitype": "10",
              "displaytype": "1",
              "label": "Palm",
              "massedit":  "1",
              "mods":"Products"
            },
            "pressures": {
              "columntype": "varchar(100)",
              "typeofdata": "V~O",
              "uitype": "1",
              "displaytype": "1",
              "label": "Pressures",
              "massedit":  "1"
            }
      }
    },
  "Products": {
      "Custom Information": {
            "uniqueapplicationfieldname": {
              "columntype": "int(11)",
              "typeofdata": "V~O",
              "uitype": "15",
              "displaytype": "1",
              "label": "Values",
              "massedit":  "1",
              "vals":["Accounts","Bank","VICOBA"]
            },
            "volume": {
              "columntype": "varchar(100)",
              "typeofdata": "V~O",
              "uitype": "1",
              "displaytype": "1",
              "label": "Volume",
              "massedit":  "1"
            }
      }
    }
  }
}
```

massHideFields
--------------

Given an array of field names this method will hide the fields.

```php
{
"operation": "massHideFields",
"setting": {
    "fields": ["fieldname1", "fieldname2", "fieldname3"],
    "module": "Accounts"
  }
}
```

```php
{
"operation": "massHideFields",
"setting": {
    "fields": ["bill_street", "ship_street", "ownership"],
    "module": "Accounts"
  }
}
```

massDeleteFields
----------------

Given an array of field names this method will delete the fields.

```php
{
"operation": "massDeleteFields",
"setting": {
    "fields": ["fieldname1", "fieldname2", "fieldname3"],
    "module": "Accounts"
  }
}
```

```php
{
"operation": "massDeleteFields",
"setting": {
    "fields": ["website", "email1", "bill_city"],
    "module": "Accounts"
  }
}
```

massMoveFieldsToBlock
---------------------

Given an array of field names this method will move the fields to the specified Block.

```php
{
"operation": "massMoveFieldsToBlock",
"setting": {
    "fields": ["fieldname1", "fieldname2", "fieldname3"],
    "module": "Accounts",
    "block": "label or ID of the destination block"
  }
}
```

```php
{
"operation": "massMoveFieldsToBlock",
"setting": {
    "fields": ["city", "street"],
    "module": "Vendors",
    "block": "LBL_VENDOR_INFORMATION"
  }
}
```

orderFieldsInBlocks
-------------------

Given an array of blocks and field names, this method will sort the fields in the given order.

- All unspecified fields in the block will be moved to the end
- Any field that is not in the block will be ignored
- The layout is an array of Module Name, block, and Field Names

```php
{
"operation": "orderFieldsInBlocks",
"setting":
  {
    "Module":{
      "block label or ID": ["fieldname1", "fieldname2", "fieldname3"]
    }
  }
}
```

```php
{
"operation": "orderFieldsInBlocks",
"setting":
  {
    "Vendors":{
      "LBL_VENDOR_INFORMATION": ["vendorname", "vendor_no","glacct"]
    }
  }
}
```

```php
{
"operation": "orderFieldsInBlocks",
"setting":
  {
    "Vendors":{
      "LBL_VENDOR_INFORMATION": ["vendor_no", "vendorname","glacct"]
    },
    "Products":{
      "LBL_PRODUCT_INFORMATION": ["product_no", "productname","expiry_date"]
    }
  }
}
```

convertTextFieldToPicklist
--------------------------

Convert a text field into a picklist. It will fill the picklist with the
distinct values in the text field. The multiple parameter indicates if
the new picklist with be multiple (true) or simple (false)

```php
{
"operation": "convertTextFieldToPicklist",
"setting": {
    "module": "Accounts",
    "field": "industry",
    "multiple": false
  }
}
```

```php
{
"operation": "convertTextFieldToPicklist",
"setting": {
    "module": "Invoice",
    "field": "salescommission",
    "multiple": false
  }
}
```

setTooltip
----------

Set the tooltip configuration for fields. The layout is an array of Module Name, hover fields and Field Names

```php
{
"operation": "setTooltip",
"setting": [
  {
    "module": "Accounts",
    "hoverfield": "fieldname that triggers the tooltip",
    "fields2show": ["fieldname1", "fieldname2", "fieldname3"]
  }
]
}
```

```php
{
"operation": "setTooltip",
"setting": [
  {
    "module": "Vendors",
    "hoverfield": "vendorname",
    "fields2show": ["state", "street"]
  }
]
}
```

removeAllMenuEntries
--------------------

Will delete all menu entries of a given module.

```php
{
"name": "del Accounts from menu",
"description": "delete all Accounts module entries in the menu",
"operation": "removeAllMenuEntries",
"setting": {
    "module": "Accounts"
  }
}
```

```php
{
"name": "del invoice module from menu",
"description": "delete all invoice module entries in the menu",
"operation": "removeAllMenuEntries",
"setting": {
    "module": "Invoice"
  }
}
```
