---
title: 'Record Set Mapping'
metadata:
    description: 'This map defines a heterogeneous set of record IDs. Simply a bunch of CRMIDs of records from different modules.'
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
        - recordset
---

The purpose of the Record ID Mapping is to define a heterogeneous set of record IDs. It allows you to gather CRMIDs from different modules into a single mapping. This can be useful for various purposes, such as performing mass operations on a specific set of records or excluding certain records from a global process.

===

In essence, the Record ID Mapping is similar to the [Condition Query Mapping](../04.condition-query) in terms of retrieving a set of records. However, the key difference is that the Record ID Mapping allows you to mix records from different modules without any specific conditions or queries. You simply provide the CRMIDs of the desired records, making it straightforward and hassle-free.

It's important to note that the set of records should be relatively small to ensure easy maintenance and avoid complexity.

The accepted format for the mapping is as follows:

```xml
<map>
  <records>
    <record>
      <id>1</id> if given, module and value are ignored
      <module>ModuleName</module>
      <value>EntityCustomNumberValue</value> we only search on the uitype 4 field
      <action>include</action>  Include | Exclude | Group  The default action is Exclude
    </record>
    ...
  </records>
</map>
```

Within the `<records>` section, you can define multiple `<record>` elements, each representing a record in the mapping. For each record, you can provide the CRMID directly using the `<id>` tag. Alternatively, you can specify the module and the corresponding value to search for using the `<module>` and `<value>` tags, respectively. The `<action>` tag determines the action to be performed on the record, with options including "Include," "Exclude," or "Group" (the default action is "Exclude").

Using the Record ID Mapping, you can:

- Retrieve CRMIDs in each action group and module.
- Check if a given CRMID exists within the recordset.
- Obtain a list of module names that contain specific CRMIDs in the recordset.

<div class="notices blue">
Please note that only IDs that are not marked as "DELETED" will be returned.
</div>

<br>
------------------------------------------------------------------------

[Next](../20.module_set) | Chapter 8: Module Set Mapping.

------------------------------------------------------------------------