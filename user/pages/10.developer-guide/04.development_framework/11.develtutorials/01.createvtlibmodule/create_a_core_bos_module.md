---
title: 'Create a coreBOS module'
metadata:
    description: 'Create a coreBOS module'
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
        - module
    tag:
        - module
---

The most important part of creating a new module is defining the module completely. Once you have clearly defined all the fields and the relation of the module with the other modules in the system the implementation is just copy paste and fill in.

===

This is the process I follow.

**Module Name**: this name will serve as the start for translation files and also as the internal name of the module. As with any name it should be significant and identify what the module represents but it also must be unique in your coreBOS install. I recommend prefixing a company identifier. The internal name must be a valid PHP identifier. For example

<table class="table table-striped">
<th>Name:</th>
<th>Just Log It</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Internal Name:</td>
<td>cbJustLogIt</td>
</tr>
</tbody>
</table>

**Repository**: create a repository to manage your module. For example,
[https://github.com/tsolucio/cbJustLogIt](https://github.com/tsolucio/cbJustLogIt)

Now we have to **define the fields**, their validations and their
layout. I use a template that defines the block name followed by each
field definition in the order I want them to appear on the screen. In
this layout, I also indicate which field will be the record link
identifier and any special functionality I need the fields to have. This
looks like this

<table class="table table-striped">
<th>Block: JustLogIt</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>columnname</td>
<td>uitype</td>
<td>fieldname</td>
<td>fieldlabel</td>
<td>displaytype</td>
<td>type_of_data</td>
<td>Comments</td>
</tr>
<tr class="even">
<td>doneon</td>
<td>5</td>
<td>doneon</td>
<td>Date</td>
<td>1</td>
<td>D~O</td>
<td></td>
</tr>
<tr class="odd">
<td>justlogitno</td>
<td>4</td>
<td>justlogitno</td>
<td>Log No</td>
<td>1</td>
<td>V~M</td>
<td>MODULE REFERENCE FIELD</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>hora</td>
<td>14</td>
<td>hora</td>
<td>Time</td>
<td>1</td>
<td>T~M</td>
<td></td>
</tr>
<tr class="even">
<td>smownerid</td>
<td>53</td>
<td>assigned_user_id</td>
<td>Assigned To</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>operation</td>
<td>1</td>
<td>operation</td>
<td>Event</td>
<td>1</td>
<td>V~O</td>
<td></td>
</tr>
<tr class="odd">
<td>createdtime</td>
<td>70</td>
<td>createdtime</td>
<td>Created Time</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>moreinfo</td>
<td>1</td>
<td>moreinfo</td>
<td>Value</td>
<td>1</td>
<td>V~O</td>
<td></td>
</tr>
<tr class="even">
<td>modifiedtime</td>
<td>70</td>
<td>modifiedtime</td>
<td>Modified Time</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>rel_id</td>
<td>10</td>
<td>rel_id</td>
<td>Related To</td>
<td>1</td>
<td>V~O</td>
<td>Accounts, Contacts</td>
</tr>
<tr class="odd">
<td>rel_module</td>
<td>1</td>
<td>rel_module</td>
<td>Related Module</td>
<td>2</td>
<td>V~O</td>
<td>save the setype of the module rel_id if set in save_module</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>donefrom</td>
<td>1</td>
<td>donefrom</td>
<td>Done From</td>
<td>2</td>
<td>V~O</td>
<td>save $_SERVER['REMOTE_ADDR'] in save_module</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Block: Custom information</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Block: Description</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>description</td>
<td>19</td>
<td>description</td>
<td>Description</td>
<td>1</td>
<td>V~O</td>
<td></td>
</tr>
</tbody>
</table>

Note:

-   how I mark the justlogitno field as the link field for the module,
-   how I group the fields two by two to indicate each row
-   how I add a comment on how and where to fill in the two displaytype
    2 fields
-   how I accommodate space for the default fields
-   how I specify the modules supported by the uitype 10 capture field
-   **ALL** field and column names **MUST** be in lower case

Next up are the **list view fields**. We have to choose from the fields
above which ones will appear on the "All" filter, which ones appear in
the popup when we try to select a record from this module and also which
fields appear on any related list this module may be related to. I
simply indicate them like this

<table class="table table-striped">
<th>List View Fields:</th>
<th>justlogitno, fecha, hora, operation, moreinfo, Assigned To</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Related List Fields:</td>
<td>justlogitno, fecha, hora, operation, moreinfo, Assigned To</td>
</tr>
<tr class="even">
<td>Popup Search Fields:</td>
<td>justlogitno, fecha, hora, operation, moreinfo, Assigned To</td>
</tr>
</tbody>
</table>

Now we must **define the relations** this module has with other modules
in the system. These will be indicated by the uitype 10 fields above and
any many to many relations the module may have

<table class="table table-striped">
<th>Related Lists:</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Accounts</td>
<td>get_dependents_list</td>
</tr>
<tr class="even">
<td>Contacts</td>
<td>get_dependents_list</td>
</tr>
<tr class="odd">
<td>Documents</td>
<td>get_attachments</td>
</tr>
</tbody>
</table>

Next, we must **define the initial sharing privileges** and the
distribution license of the module.

<table class="table table-striped">
<th>Module:</th>
<th>public</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>License:</td>
<td>Visage</td>
</tr>
</tbody>
</table>

Finally, we must **specify any additional functionality**. This is where
we will explain cron jobs, event handlers and any special widgets or
operations the module will have.

Reached this point we have a clear idea of everything we need to create
our module and we can start coding.

[You can download a text template here](moduletemplate.zip)


The steps are

**1.-** copy the [vtlib/ModuleDir directory](https://github.com/tsolucio/corebos/tree/master/vtlib/ModuleDir)
to the "modules" directory renaming it to the internal name of your
module

    cp -a vtlib/ModuleDir modules/cbJustLogIt

**2.-** rename the three ModuleFile files to the name of your module

    cd modules/cbJustLogIt
    rename 's/ModuleFile/cbJustLogIt/g' ModuleFile*

**3.-** edit manifest.xml and fill in the definitions you created

**3.1.-** Change the name and label

**3.2.-** Change the parent which is the name of the menu you want the
module to be in

**3.3.-** Change the description and the license

**3.4.-** Add the SQL to create the main table.

**3.4.1.-** This table must be the name of your module in **lowercase**
prefixed with "vtiger\_".

**3.4.2.-** It must contain the internal primary key which is the name
of your module in **lowercase** followed by "id"

**3.4.3.-** Add a field for all the fields in your module except the
common \_crmentity fields

**3.4.4.-** Add any index your users may need. In other words, stop to
think about how your module is going to be used, on which fields will
your user be searching and sorting. Add a database index on those
fields.

**3.5.-** Change the name of the custom field table

**3.6.-** Now for each block and field fill in the fields XML
accordingly. There are a lot of existing manifest.xml files in the
application for you to study.

**3.7.-** Fill in the All filter fields

**3.8.-** Fill in the sharing access, default actions, related lists,
and other special settings

**4.-** Each module has a main file that defines its class. This file
was copied in step 1 and renamed in step 2. So we now have a file
called:

    modules/cbJustLogIt/cbJustLogIt.php

edit this main module file and change

**4.1.-** the module class name

**4.2.-** replace **MODULE\_NAME\_LOWERCASE** with the **lowercase**
internal name of your module

**4.3.-** replace **MODULE\_REFERENCE\_FIELD** with the name of your
modules' reference field

**4.4.-** now fix the related list and popup fields array

**4.5.-** set the module record autoincrement prefix

    $this->setModuleSeqNumber('configure', $modulename, $modulename.'-', '0000001');

**5.-** Translate

**5.1.-** Get the set of labels used and copy them to the
en\_us.lang.php file

    grep -i label manifest.xml

Once he en\_us.lang.php is translated copy it to any other language file
and translate accordingly.

Finally create any additional logic that is needed: save module,
eventhandlers, cron,...

Now you are ready to install and test. Use the
build/HelperScripts/installmodule.php script.

Before installing I like to make a dump of the database so I can easily
recover if I made a mistake and try again. Normally the errors appear in
the manifest field definitions, typical copy-paste errors.

In order to be able to send this module to any coreBOS, you have to set
up a specific structure.

<div class="notices blue">
 If the module is just for your
install you can copy the files into place and use the install module
script </div>

The structure looks like this:

    manifest.xml
    modules/
      ModuleName/
       <Module Related Files>
       language/
        en_us.lang.php
        <Other language Files>
    templates/
      <Smarty templates of the Module>

The manifest in the top level is a copy of the one inside the modules
directory.

You can now compress this structure into a .zip and send it to any
coreBOS in the world.

<div class="notices blue"> If your repository is publically
available on GitHub you can have your users install it directly from the
GitHub URL </div>

A very good [reference for creating modules can be found here](https://discussions.corebos.org/documentation/lib/exe/fetch.php?media=devel:vtlib-2.1.pdf).
This is a VERY interesting read as it will give you knowledge on how to
create a module using the vtlib API which will be useful for you to be
able to change modules once installed.

<div class="notices blue"> This is just the basic skeleton and
functionality of a module. There are a lot of things that you can
customize, so look for help on
<a href="https://gitter.im/corebos/discuss">Gitter</a> or the
<a href="http://discussions.corebos.org/>forum</a>

 </div>
