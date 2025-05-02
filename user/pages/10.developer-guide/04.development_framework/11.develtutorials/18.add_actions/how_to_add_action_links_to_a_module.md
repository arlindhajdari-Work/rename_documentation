---
title: 'How to add action links to a module'
metadata:
    description: 'How to add action links to a module'
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
        - links
---

### Action links

Action links are **hooks** into the user interface that can be created directly in the database without having to change any code. At most you will have to create new code to attend to the new actions.

===

These actions will be easily upgradeable going forward as they are saved in the database and no base code changes are required.

We have links to enhance the **List View**, the **Detail View** and some special hooks to load CSS and javascript to react to the new actions. See below for more information.

Adding a new action can be done in **two ways**. The **first** is when creating a module in it's manifest file. There is a specific section there to add custom links that looks like this:

```xml
<customlinks>
  <customlink>
    <linktype>DETAILVIEWWIDGET</linktype>
    <linklabel>Execute</linklabel>
    <linkurl><![CDATA[module=cbupdater&action=cbupdaterAjax&file=cbupdaterWidget&record=$RECORD$]]></linkurl>
    <linkicon><![CDATA[]]></linkicon>
    <sequence>0</sequence>
    <handler_path><![CDATA[]]></handler_path>
    <handler_class><![CDATA[]]></handler_class>
    <handler><![CDATA[]]></handler>
    </customlink>
    <customlink>
    <linktype>LISTVIEWBASIC</linktype>
    <linklabel>GetUpdates</linklabel>
    <linkurl><![CDATA[javascript:gotourl('index.php?module=cbupdater&action=getupdates')]]></linkurl>
    <linkicon><![CDATA[]]></linkicon>
    <sequence>0</sequence>
    <handler_path><![CDATA[]]></handler_path>
    <handler_class><![CDATA[]]></handler_class>
    <handler><![CDATA[]]></handler>
  </customlink>
</customlinks>
```

The above code is extracted from the coreBOSUpdater manifest.xml file. It adds a DETAILVIEWWIDGET and a LISTVIEWBASIC action. As can be seen the action has these parameters:

<table class="table table-striped">
<th>linktype</th>
<th>Type of Link like DETAILVIEW etc..</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>linklabel</td>
<td>Label to use for the link when displaying (will be translated)</td>
</tr>
<tr class="even">
<td>linkurl</td>
<td>URL of the action link. You can use the special variables $RECORD$ which will evaluate to the current record ID and $MODULE$ which evaluates to the current module</td>
</tr>
<tr class="odd">
<td>linkicon</td>
<td>path to a small 16x16 icon to show before the DETAILVIEWBASIC action link</td>
</tr>
<tr class="even">
<td>sequence</td>
<td>order in which the actions should be displayed</td>
</tr>
<tr class="odd">
<td>handler_path</td>
<td>currently not used</td>
</tr>
<tr class="even">
<td>handler_class</td>
<td>currently not used</td>
</tr>
<tr class="odd">
<td>handler</td>
<td>currently not used</td>
</tr>
</tbody>
</table>

The **second** form is for when we have an already installed module and we want to modify it. In this case we have to load the vtlib programming API, get a link to our module and execute the **addLink()** method. This looks like this:

    include_once('vtlib/Vtiger/Module.php');
    $module = Vtiger_Module::getInstance('Contacts');
    $module->addLink('LISTVIEWBASIC', 'LBL_SELECT_ALL', 'toggleSelectAllEntries_ListView();');

or

    include_once('vtlib/Vtiger/Module.php');
    $mod_acc = Vtiger_Module::getInstance('Accounts');
    $mod_acc->addLink('DETAILVIEWBASIC', 'Add Ticket', 'index.php?module=HelpDesk&action=EditView&parent_id=$RECORD$');

The first example adds a button to the list view of the contacts module while the second adds a link to the right action panel of accounts.

You can get a copy of the full script in the [build/HelperScripts directory of coreBOS](https://github.com/tsolucio/corebos/tree/master/build/HelperScripts).

### Action links on List View

We have two possible options on the list view. The **LISTVIEWBASIC** value will add a new button on the list view exactly the same as the already existing buttons, while the **LISTVIEW** value will add the link to a "More actions" drop down menu.

### Action links on Detail View

We have three types of possible actions on the detail view screen. The **DETAILVIEWBASIC** option will add a link to the right action panel, at the same level as the normal existing links. The **DETAILVIEW** option will add the link inside a "More Actions" drop down menu. This is useful when we have many options.

Finally the **DETAILVIEWWIDGET** option will permit us to add a small widget (box) on the right action panel, within which we will be able to execute some actions. Very useful to add functionality to the module.

The **DETAILVIEWWIDGET** URL is called within the context of the application, it does not need index.php because that will be called always. You simply have to add the MVC parameters. This will normally be in the form;

    module={MODULE}&action={MODULE}Ajax&file={ACTION}...

<div class="notices blue">
As of coreBOS January 2015 any javascript code sent with the widget content will be executed automatically making it easy to load some additional libraries and/or execute some process.

You can study the <a href="https://github.com/tsolucio/Timecontrol"><i>Timecontrol</i></a> module stop watch widget and also the  <a href="https://github.com/tsolucio/corebos/commit/cbfb301b12688d260fc3c5d7144cdea163da5868"><i>Mass Image Upload widget on Products</i></a>
</div>

### Other Action links

Three other types of links exist that will permit us to insert CSS (**HEADERCSS**), javascript (**HEADERSCRIPT**) and a global drop down menu (**HEADERLINK**) with actions on the upper right button bar. See the next section for more information.

### Summary of Action link types

<table class="table table-striped">
<th>Linktype</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LISTVIEWBASIC</td>
<td>Button on the list view</td>
</tr>
<tr class="even">
<td>LISTVIEW</td>
<td>Drop down menu on the list view</td>
</tr>
<tr class="odd">
<td>DETAILVIEW</td>
<td>Drop down menu on the right action panel in detail view</td>
</tr>
<tr class="even">
<td>DETAILVIEWBASIC</td>
<td>Link on the right action panel in detail view</td>
</tr>
<tr class="odd">
<td>DETAILVIEWWIDGET</td>
<td>Small widget block section at the bottom of the right action panel on detail view. Look at the Timecontrol stopwatch for an example. It can also be a <a href="../../../developer-guide/development_framework/develtutorials/add_special_block">full fledged block inserted into the existing field blocks</a></td>
</tr>
<tr class="even">
<td>HEADERSCRIPT</td>
<td>The link will be treated as a javascript type and will be imported in the head section of the HTML output page as &lt;script type='text/javascript' src='linkurl'&gt;&lt;/script&gt;</td>
</tr>
<tr class="odd">
<td>HEADERCSS</td>
<td>The link will be treated as a CSS type and will be imported in the head section of the HTML output page as &lt;link rel='stylesheet' type='text/css' href='linkurl&gt;</td>
</tr>
<tr class="even">
<td>HEADERLINK</td>
<td>You can see these link grouped under More on the top header panel. Useful if you want to provide utility tools like Bookmarklet etc.</td>
</tr>
</tbody>
</table>

### Business Actions

[Read about the Business Actions module for an easy way to add links without coding](../../../../05.configuration-tools/03.business-actions)
