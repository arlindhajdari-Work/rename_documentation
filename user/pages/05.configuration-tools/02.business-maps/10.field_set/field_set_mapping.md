---
title: 'Field Set Mapping'
metadata:
    description: 'This map defines a heterogeneous set of fields that belong to some modules.'
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
        - fieldset
---

The Field Set Mapping allows you to define a heterogeneous set of fields that belong to various modules. This mapping is designed to provide flexibility in selecting a specific group of fields for mass operations or to include/exclude fields from a global process.

The accepted format for the Field Set Mapping is as follows:

```xml
<map>
  <module>
    <name>ModuleName</name>
    <fields>
      <field>
        <name>fieldname</name>
          <info>anything you need</info>
        </field>
      ...
    </fields>
  </module>
  ...
</map>
```

Within the `<map>` section, you can define multiple `<module>` elements. Each `<module>` element represents a module and contains a `<name>` tag specifying the module name. Inside the `<module>` tag, you can list the desired fields within the `<fields>` section. For each field, use the `<field>` tag, and specify the field name within the `<name>` tag. Optionally, you can include additional information or details about the field using the `<info>` tag.

Once the Field Set Mapping is defined, you can utilize the `getFieldSet()` method to retrieve the set of fields defined in the mapping. This method allows you to access the complete field set and perform operations or make decisions based on the included fields. Additionally, you can use the `getFieldSetModule($module)` method to retrieve the fields specifically defined for a particular module.

By using the Field Set Mapping and the corresponding methods, you can easily manage and work with a selected set of fields within your coreBOS application, enabling efficient mass operations and customization of global processes.

<br>
------------------------------------------------------------------------

[Next](../19.masterdetailmapping) | Chapter 10: Master Detail Mapping.

------------------------------------------------------------------------