---
title: 'IOMap Business Mapping'
metadata:
    description: 'This map is a developer tool.'
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
        - adminmanuals
        - businessmappings
    tag:
        - iomap
---

This coreBOS developer map allows you to define the input and output parameters for various processes that can be programmed. However, it does not have any direct visual effect or functionality within the coreBOS application itself.

===

It can be used in two "modes", one, as a template for some script to retrieve and return values, the other, as a means to execute a set of workflows on some records and return outputs.

This is the structure of the map:

```xml
<map>
  <input>
    <fields>
      <field>
        <fieldname>recordid</fieldname>
      </field>
      <field>
        <fieldname>originmodule</fieldname>
      </field>
    </fields>
  </input>
  <output>
    <fields>
      <field>
        <fieldname>targetfield</fieldname> <!-- This is an expression -->
      </field>
      <field>
        <fieldname>getFromContext('testexp')</fieldname> <!-- This is an expression -->
      </field>
    </fields>
  </output>
  <actions>
    <forid>Records to execute the workflow on</forid>
     <action>workflow ID or name</action>
     <action>workflow ID or name</action>
     ...
  </actions>
</map>
```

Here's a breakdown of the different elements within the XML map:

- `<input>`: Specifies the input fields for the process. In this example, the input fields are "recordid" and "originmodule." These fields can be accessed and utilized within the process.

- `<output>`: Defines the output fields that the process generates. In this case, the output fields are "targetfield" and "getFromContext('testexp')". The "targetfield" is an expression that evaluates to a specific value, the value of the field, while "getFromContext('testexp')" is another expression that retrieves a value from the context variables produced by the workflow.

- `<actions>`: Specifies the actions to be performed by the map. The "forid" element defines the records on which the workflows should be executed, and the "action" element specifies the workflow's ID or name.

The functional map serves as a way to define the parameters and behavior of processes in a customizable manner. It can be executed using the web service "processmap" operation, allowing developers to leverage the map's defined input, output, and actions within their custom programming logic.

Overall, the functional map provides a flexible tool for developers to define and control the behavior of processes within coreBOS, enhancing the application's functionality according to specific business requirements.

<br>
------------------------------------------------------------------------

[Next]( ../14.infomap) | Chapter 12: Information Map.

------------------------------------------------------------------------