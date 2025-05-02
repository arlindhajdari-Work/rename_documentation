---
title: 'Business Mappings and Conditions'
metadata:
    description: 'Business Maps general'
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
        - businessmappings
        - adminmanual
    tag:
        - businessmaps
---

The Business Mappings and Conditions module permits **implementors** to define high-level configuration options for the execution of the application.

===

Using different types of structured XML, JSON or direct SQL, this module will define conditions, field mappings, and other advanced logic to modify the functionality of the application without the need to get into programming details.

This module also serves another purpose: separating the programmers from the implementors. In other words, it permits the programmers to create functionality in the application while giving to the implementor total control on **how** that functionality should act in different cases for different installations.

With this module, we achieve a much more configurable application without the need to depend on specific programming knowledge.

Note that in the end, many of these mappings or conditions are actually a washed down configuration screen. Many times, from a programmers point of view, creating certain functionality is easy, the problem is creating a GUI for the user to be able to configure the different options that are present in the code. Usually, we spend more time programming the interface than the actual solution. With Business Mappings and Conditions we create a spartan, manual but generic interface to many features without getting to complicated nor repeating work over and over.

## Business Mappings Store

We have a relation of different Business Mappings we use where you can find a whole set of different Business Mappings which can be used in your application directly or with easy modifications to adapt them to your needs.

[Have a look here](../../07.knowledge-base/10.configuration-store) and please share your settings with us!


## Fields of Business Mappings

-  **Map Name:** this is a textual identifier of the mapping. It is very important to use the exact name that each feature requires as that is what the code looks for. These names are constantly evolving as we add new features that use the mappings module
-   **Map Number:** autonumeric reference field
-   **Map Type:** the type of mapping that is required, Depending on the type, the structure of the contents field is different
-   **Map Contents:** the actual definition of the mappings, normally this will be an XML structure

## Types of Business Mappings

There are currently these different types of mappings:

- [Condition Query](condition-query)
- [Condition Expression](condition-expression)
- [(Field) Mapping](mapping)
- [Extended Field Information Mapping](extendedfieldinfo)
- [Record Access Control](record_access_control)
- [List Columns](list_columns)
- [Record Set Mapping](record_set)
- [Module Set Mapping](module_set)
- [Field Set Mapping](field_set)
- [Master Detail Mapping](masterdetailmapping)
- [IOMap](iomap)
- [Information Map](infomap)
- [Field Dependency](field_dependency)
- [Validations](validations)
- [Related Panes](relatedpanes)
- [Import](import)
- [Duplicate Records](duplicaterecords)
- [Global Search Autocomplete](globalsearch)
- [Detail View Layout](detailviewlayout)
- [Decision Table](decisiontable)
- [REST/SOAP call and retrieval](webservicecall)
- [Application menu](02.application-menu)
- [Kanban View](16.kanban)
- [Pivot View](21.pivot)
- [Mass Upsert Grid](29.massupsertgrid)
- [Popupfilter](30.popupfilter)

Depending on the type of business mapping the contents of the record changes as explained next.

<div class="notices red">
The two most typical business map errors are:<br>

-  giving the record the wrong name: most business maps are launched depending on their name, so you must set it correctly<br>
-  invalid XML: https://www.xmlvalidation.com </div>

## How it works

### How an implementor can use a Business Mapping

Once a programmer has established the code changes to use a Business Mapping, the implementor has to create, one or more, records in the module with that type of Business Mapping.

Usually, the programmer will have created some examples and documentation on the exact formatting and options supported by the business mapping type.

Once created and configured the code will use the mapping.

Optionally, the implementor can create more than one mapping of this type with different configurations and then associate each one to different users, with the help of the Global Variable module.

### How a programmer can use a Business Mapping

The idea is to get the mapping to apply and then pass in the parameters so the mapping can be processed.

The correct way to do this is using the global variable module so that the mappings are dependent on the users and pass in the default mapping which you should have created.

```php
 $cbMapid = GlobalVariable::getVariable('BusinessMapping_SalesOrder2Invoice', cbMap::getMapIdByName('SalesOrder2Invoice'));
  if ($cbMapid) {
	$cbMap = cbMap::getMapByID($cbMapid);
	$focus->column_fields = $cbMap->Mapping($so_focus->column_fields,$focus->column_fields);
  } else {
...
```

All global variable whose name starts with 'BusinessMapping_' will return the associated mapping.

In the code above, the Mapping called 'SalesOrder2Invoice' is the default mapping.

If the mapping is found we apply it by calling the type of mapping and passing the required parameters for each type.

You should consider implementing the 'else' part in case no mapping is found.

### How a programmer can add a Business Mapping Type

Adding a new process is rather simple:

- Add your mapping type to the changeset file so it gets added in the business mapping picklist
  - build/changeSets/cbMapAddMapTypes.php
  - <a href="https://github.com/tsolucio/corebos/blob/master/build/changeSets/cbMapAddMapTypes.php#L25">see the code</a>
- Add the translation of the mapping type to the modules/cbMap/language files
- Copy the file modules/cbMap/processmap/processMap.php to a file named as your mapping inside this same directory
- Now modify this file to process your mapping. Basically you will need a convert method that will convert the XML into a PHP array and then add methods that read the array and return answers, values or parts of that array
- Once you have done that you will be able to launch your mapping by loading the CRMID and calling the mapping name.

Let's look at a real example: <a href="https://github.com/tsolucio/corebos/commit/5a6df91cfc9467ffb1c7dbd5b0aa171f202c050f">List Columns Mappings</a>

As you can see in the commit, we add the ListColumns type to the picklist and translation files. Then we add a new script that, first documents the required XML structure, then converts the XML to an array for easier processing and then defines a set of helper methods to extract information from the mapping.

Finally you can see <a href="https://github.com/tsolucio/corebos/blob/master/include/utils/ListViewUtils.php#L988">how this is used here</a>. Once we have a Mapping ID, we load it:

```php
$cbMap = cbMap::getMapByID($cbMapid);
```

and then call the ListColumns mapping type to initialize the internals (call processMap) and from there we call the helper methods to get the information we need:

```php
$focus->search_fields = $cbMap->ListColumns()->getSearchFields();
```

### How to add a Business Mapping Type Generator

Each Business Map record has an action link named "Generate Map". This link opens a window with a specific editor for each type of map which will help us construct the map in a more or less graphical way.

coreBOS gives the programmer of the map the necessary infrastructure to simply implement the editor and not have to worry about the details.

If you want to create an editor for your map you must:

- create a class named
```php
gen<MapName>
```

inside the directory modules/cbMap/generatemap

- the class extends generatecbMap:
```php
class genModuleSetMapping extends generatecbMap {
```

- the class must contain two methods:
  - **generateMap()** this method will be called once the editor window is opened and will be in charge of sending to the screen all the editor contents.
      - The method should include the file **modules/cbMap/generatemap/GenMapHeader.php** before any output. This script will output the  normal coreBOS includes like LDS (among others).
      - The method should include the file **$smarty→display('modules/cbMap/GenMapFooter.tpl')**; at the end which will close the HTML and BODY opened in the header
      - The contents generated by the method must contain a javascript function that captures all the required information and sends it to the **saveMapAction(params);** function. params is the typical parameter/value query string used in the browser (separated by &) and will be sent to coreBOS as the POST body of the save event
    - **convertToMap()** which will have to read from the $_REQUEST the values it needs and return the constructed map that will be saved by coreBOS


You can find an example in the Module Set Mapping

<br>
------------------------------------------------------------------------

[Next](condition-query) | Chapter 1: Condition Query.

------------------------------------------------------------------------