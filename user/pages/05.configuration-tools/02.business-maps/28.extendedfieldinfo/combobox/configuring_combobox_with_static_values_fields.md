---
title: 'Configuring Combobox with static values Fields'
metadata:
    description: 'Configuring Combobox with static values Fields.'
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
        - fieldinfo
        - combobox
---

The functionality of a Combobox with static values is useful for input fields where users can enter any text they want, but you want to suggest a predefined set of standard or accepted values.

To implement this functionality, you can refer to the [definition here](https://www.lightningdesignsystem.com/components/combobox/#Autocomplete-Combobox).

The map for configuring a Combobox with static values looks like this:

```XML
<field>
  <fieldname>potentialname</fieldname>
  <features>
   <feature>
    <name>combobox</name>
    <values>
      <value>value1</value>
      <value>value2</value>
      <value>...</value>
      <value>valueN</value>
    </values>
   </feature>
  </features>
</field>
```

In this map, the `<fieldname>` element specifies the name of the field you want to configure as a Combobox. The `<values>` element contains a list of static values that will be suggested to the user when they interact with the field. You can add as many `<value>` elements as needed to define the desired set of values.

By using this configuration, the Combobox will present the predefined values as suggestions to the user, enhancing the user experience and ensuring consistent data entry.