---
title: 'Pivot View Mapping'
metadata:
    description: 'Define a pivot view report of the records of a module'
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
        - pivot
---

The purpose of this mapping is to define a pivot view report of the
records of a module. This map is in the "View Business Map" category as
it serves the purpose of showing the records of a module in a different
way than we usually see them in the list view.

===

With this map, we will be able to divide the records into columns based
on the distinct values in a field of the module as well as filter the
records based on a search or custom view settings.

As usual, the map to apply is selected using the name of the map which
must be **{ModuleName}_Pivot** and you can use the global variable
**BusinessMapping_{ModuleName}_Pivot** to define maps based on user
and roles (among other escalation rules) just like most of the other
maps.

The accepted format is:

```xml
<map>
    <module>Module name</module>
    <filter>filter name</filter>
        <aggregate>field name</aggregate>
    <rows>
        <row>
            <name>value of module field name</name>
            <label>label of field in the table</label>
        </row>
    </rows>
    <cols>
        <col>
            <name>value of module field name</name>
            <label>label of field in the table</label>
        </col>
    </cols>
</map>
```

This is a test map you can use to see it in action.

```xml
<map>
    <module>Accounts</module>
    <filter>All</filter>
    <aggregate>employees</aggregate>
    <rows>
        <row>
            <name>accounttype</name>
            <label>Account Type</label>
        </row>
        <row>
            <name>rating</name>
            <label>Rating</label>
        </row>
    </rows>
    <cols>
        <col>
            <name>industry</name>
            <label>industry</label>
        </col>
    </cols>
</map>
```

Which looks like this

![](preview-screenshot_at_2021-10-08_17-27-20.png?width=100%)

<br>
------------------------------------------------------------------------

[Next](../29.massupsertgrid) | Chapter 25: Mass Upsert Grid

------------------------------------------------------------------------