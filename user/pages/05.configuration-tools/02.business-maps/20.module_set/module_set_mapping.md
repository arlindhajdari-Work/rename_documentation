---
title: 'Module Set Mapping'
metadata:
    description: 'This map defines a heterogeneous set of module names. Simply a bunch of modules.'
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
        - moduleset
---

The Module Set Mapping serves the purpose of defining a heterogeneous set of module names. It allows you to gather a collection of modules for various use cases, such as performing mass operations or excluding specific modules from a global process.

===

The accepted format for the mapping is as follows:

```xml
<map>
  <modules>
    <module>ModuleName1</module>
    <module>ModuleName2</module>
    ...
  </modules> 
</map>
```

Within the `<modules>` section, you can specify multiple `<module>` elements, each representing a module in the mapping. Simply list the names of the desired modules within the corresponding tags.

Once the mapping is defined, you can utilize the `getFullModuleSet()` method to retrieve the set of modules defined in the mapping. This method provides access to the complete module set, allowing you to perform operations or make decisions based on the modules included.

By utilizing the Module Set Mapping and the `getFullModuleSet()` method, you can conveniently manage and work with a defined set of modules within your coreBOS application.

<br>
------------------------------------------------------------------------

[Next](../10.field_set) | Chapter 9: Field Set Mapping.

------------------------------------------------------------------------