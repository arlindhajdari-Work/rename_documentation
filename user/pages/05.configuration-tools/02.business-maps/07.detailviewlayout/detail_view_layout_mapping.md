---
title: 'Detail View Layout Mapping'
metadata:
    description: 'Define a block layout for a module.'
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
        - adminmanual
        - businessmappings
    tag:
        - detailviewlayout
---

The coreBOS Detail View Layout Mapping is a configuration setting that allows you to customize the layout of the detail view for modules in the coreBOS application. The mapping defines the arrangement and appearance of fields, blocks, and related lists in the detail view of a module.

===

The purpose of this mapping is to define **a block layout for a module**. It holds equivalent information to the layout editor in the application settings. The difference is that blocks can be defined to contain different options and that we can have many maps/configurations for the same module, whereas in settings you can have only one layout for all users of the application.

This map can be used inside the application with the `Detail View Layout Widget` (see below), but its primary goal is to export different layouts to portal/external applications.

There are 6 types of blocks:

- **ApplicationFields**: this tells us to use the same layout that exists in the application for this block. This type uses the "blockid" directive to know which block to render
- **FieldList**: a list of rows and fields with the distribution we want. This type uses the "layout" directive
- **RelatedList**: a related list of records with actions
- **Widget**: this is a block that must be constructed following the [DetailViewWidget specification](../../../10.developer-guide/04.development_framework/11.develtutorials/16.add_special_block). You have full control of the space designated to this block
- **CodeWithoutHeader**: this will open a "div" and directly include your code inside
- **CodeWithHeader**: this will add a header following the look and feel of the default related-list blocks and then open a "div" and directly include your code inside

The Detail View Layout Mapping is specified using XML format. Here is an example of the mapping structure:

```xml
<map>
  <originmodule>
    <originname>ModuleName</originname>
  </originmodule>
  <blocks>
    <block>
      <label></label>
      <position></position>
      <sequence></sequence>
      <type></type> ApplicationFields | FieldList | RelatedList | Widget | CodeWithHeader | CodeWithoutHeader
      <blockid></blockid>
      <layout>
        <row>
          <column>fieldname</column>
        </row>
      </layout>
      <loadfrom></loadfrom> related list label or id | file to load | widget reference
      <handler_class></handler_class>
      <handler></handler>
    </block>
  </blocks>
</map>
```

Let's explain the dependencies between the directives and their meaning a little more.

The *type* directive defines the meaning of the rest of the directives.

If *type* is **ApplicationFields** we just need the **blockid** to get the fields from, so all the other directives are ignored.

If *type* is **FieldList** we just need the **layout** directive to get the list of fields to show and their distribution on screen, so all the other directives are ignored.

If *type* is **RelatedList** we just need the name or ID of the related list to show. This value is given in the directive **loadfrom**, so all the other directives are ignored.

If *type* is **Widget** then we have two ways of defining the widget to show. One is setting the directive *loadfrom* to the [DetailViewWidget specification](../../../10.developer-guide/04.development_framework/11.develtutorials/16.add_special_block) you need, usually starts with "block:". It would be what you would put in a [Business Action](../../03.business-actions/). The other option is to set *loadfrom* to the path of the file that contains the widget and use the directive *handler_class* to define the name of the widget. In this case, the two directives will be used to construct the Detail View Widget reference object, with no additional parameters. It would be constructed like this:

```
block://handler_class:loadfrom
```

If *type* is **CodeWithHeader** or **CodeWithoutHeader** we have two options depending on how the code has been created.

If it is a flat, function-based script, then we just need the name of the file that will be directly included in the flow of execution showing any output directly in the block. In this case, we just need the name of the file which will be obtained from the *loadfrom* directive.

If the script is class-based, then you can (optionally), define the name of the class to instantiate in the directive *handler_class* and the method to execute in the directive *handler*. If these two directives have values the code will be loaded like this:

```
$dvl = new handler_class();
$dvl->handler();
```

By customizing the Detail View Layout Mapping, you can arrange fields and related lists according to your specific requirements. This provides flexibility in designing the detail view layout, allowing you to organize information in a way that best suits your business processes and user preferences.

## Detail View Layout Widget

Constructing on this map we have created a widget that reads the different options and adds the result into a block in a modules' detail view. This permits us, for example, to show fields from a directly related module, or the result of some code.

Note that coreBOS already has mechanisms to add most of these types of blocks, which, in some cases can be easier than using this widget. The big advantage of the widget is that it is configured using [Business Actions](../../03.business-actions/) and these are natively applied per user/role/condition making it extremely flexible to show different blocks to different users or different types of records (for example).

As usual, putting pieces of the puzzle together to construct a beautiful picture.

The name of the widget is **showSetOfFieldsWidget** and the syntax of the business action for each type is:

```
block://showSetOfFieldsWidget:modules/Utilities/showSetOfFieldsWidget.php:record_id=$RECORD$&mapid=detailviewlayout_mapid
```

to get it in the right action panel you would use:

```
module=Utilities&action=UtilitiesAjax&file=showSetOfFieldsWidget&MODULE=HelpDesk&RECORDID=$RECORD$&dvmodule=Products&dvrecord=$product_id&mapid=detailviewlayout_mapid
```

The **ApplicationFields** and **FieldList** types require two additional parameters which represent the module (dvmodule) and record (dvrecord) from where they are supposed to get the fields to show.

```
block://showSetOfFieldsWidget:modules/Utilities/showSetOfFieldsWidget.php:record_id=$RECORD$&dvmodule=module_to_show&dvrecord=field_with_recordid&mapid=detailviewlayout_mapid
```

Watch the video presentation to get a full idea of the possibilities

[plugin:youtube](https://www.youtube.com/watch?v=RrTJ19hBBFE)

You can find next the relation of maps I used for testing in the video presentation.

**Detail View Widget**

```xml
<map>
<blocks>
  <block>
    <type>Widget</type>
    <label>coreBOS Website</label>
    <loadfrom><![CDATA[block://showHTMLBlock:modules/Utilities/showHTMLBlock.php:op=iframe&height=400px&ex=http%3A%2F%2Fcorebos.org%3Fifcrmid%3D%24RECORD%24%26ifmodule%3D%24MODULE%24]]></loadfrom>
  </block>
</blocks>
</map>
```

**Application Fields**

```xml
<map>
<originmodule>
    <originname>Products</originname>
</originmodule>
<blocks>
  <block>
    <type>ApplicationFields</type>
    <blockid>36</blockid>
  </block>
</blocks>
</map>
```

**Code With/Without Header**

```xml
<map>
<blocks>
  <block>
    <type>CodeWithHeader</type>
    <loadfrom>sayhi.php</loadfrom>
  </block>
</blocks>
</map>
```

The *sayhi.php* is a script in the root of the coreBOS install with this contents:

```php
<?php
echo "hello widget!";
```

**Field List**

```xml
<map>
<originmodule>
    <originname>Products</originname>
</originmodule>
<blocks>
  <block>
    <type>FieldList</type>
    <label>pdofields</label>
    <layout>
      <row><column>productname</column><column>productcode</column></row>
      <row><column>sales_start_date</column><column>sales_end_date</column><column>start_date</column><column>expiry_date</column></row>
      <row><column>vendor_id</column><column>vendor_part_no</column></row>
    </layout>
  </block>
</blocks>
</map>
```

**Related List**

```xml
<map>
<originmodule>
    <originname>HelpDesk</originname>
</originmodule>
<blocks>
  <block>
    <type>RelatedList</type>
    <label>ServiceContracts</label>
    <loadfrom>ServiceContracts</loadfrom>
  </block>
</blocks>
</map>
```

<br>
------------------------------------------------------------------------

[Next](../06.decisiontable) | Chapter 20: Decision Table.

------------------------------------------------------------------------