---
title: 'Global Search Autocomplete Mapping'
metadata:
    description: 'This map defines the set of modules and fields you want to launch a reduced global search on.'
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
        - globalsearch
---

The coreBOS Global Search Autocomplete Mapping allows you to configure the modules and fields for a reduced global search with autocomplete functionality. This mapping serves the specific purpose of defining the set of modules and fields that should be included in the autocomplete dropdown when typing in the global search text box.

===

This business map is really a configuration setting. Most business maps are generic, whereas you can use them on many modules or for various purposes. This mapping is, specifically, to define the set of modules and fields you want to launch a reduced global search on.

As of the creation and implementation of this map, if it exists, you will be able to start writing in the global search text box to get an autocomplete dropdown with values that it finds in the modules and fields defined in the mapping.

```xml
<map>
  <mincharstosearch>3</mincharstosearch>
  <maxresults>10</maxresults>
  <searchin>
    <module>
      <name>Potentials</name>
      <searchfields>field1,field2,...,fieldn</searchfields>
      <searchcondition>startswith|contains</searchcondition>
      <showfields>field1,field2,...,fieldn</showfields>
    </module>
    ...
  </searchin>
</map>
```

Key elements in the mapping include:

- **`<mincharstosearch>`**: Specifies the minimum number of characters required to initiate the autocomplete search.
- **`<maxresults>`**: Defines the maximum number of results to display in the autocomplete dropdown.
- **`<searchin>`**: Contains the list of modules to be included in the autocomplete search.`

For each module, you define:

- **`<name>`**: Specifies the name of the module.
- **`<searchfields>`**: Lists the fields within the module that will be searched.
- **`<searchcondition>`**: Defines the search condition, which can be "startswith" or "contains".
- **`<showfields>`**: Specifies the fields that will be displayed in the autocomplete dropdown.

As usual, the mere existence of the mapping with the name **GlobalSearchAutocomplete** will activate the functionality and, as with all business maps you can define it using the global variable **BusinessMap\_GlobalSearchAutocomplete** to apply it only to certain users.

This feature was implemented by [Albana](https://github.com/AlbanaCelepija): Thank you!!

For example, the following map configuration can be used as a reference:

```xml
<map>
  <mincharstosearch>2</mincharstosearch>
  <maxresults>10</maxresults>
  <searchin>
    <module>
      <name>Potentials</name>
      <searchfields>potentialname,sales_stage,amount</searchfields>
      <searchcondition>startswith</searchcondition>
      <showfields>potentialname,sales_stage,amount,forecast_amount</showfields>
    </module>
    <module>
      <name>Accounts</name>
      <searchfields>accountname,industry,employees</searchfields>
      <searchcondition>startswith</searchcondition>
      <showfields>accountname,industry,employees,email1</showfields>
    </module>
  </searchin>
</map>
```

In the above example, the autocomplete search will include the "Potentials" module with search fields "potentialname", "sales_stage", and "amount". The search condition is set to "startswith", and the displayed fields in the autocomplete dropdown include "potentialname", "sales_stage", "amount", and "forecast_amount". Similarly, the "Accounts" module is configured with its respective search and display fields.

By customizing the Global Search Autocomplete Mapping, you can enhance the search experience by narrowing down the search scope and providing relevant autocomplete suggestions to users.

<br>
------------------------------------------------------------------------

[Next](../07.detailviewlayout) | Chapter 19: Detail View Layout.

------------------------------------------------------------------------