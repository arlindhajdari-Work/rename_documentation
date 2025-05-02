---
title: 'List Columns'
metadata:
    description: 'The purpose of this mapping is to override the predefined columns that appear on the related and popup lists for a module.'
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
        - listcolumns
---

The List Columns mapping feature allows you to customize the columns displayed in related and popup lists for a module in coreBOS. By overriding the default columns, you can adapt the lists to your specific requirements without the need for code modifications. This flexibility enables you to show relevant information or provide additional details for users who need them.

===

The purpose of this mapping is to override the predefined columns that appear on the related and popup lists for a module. Each module has two hard coded lists of columns, one defines the columns that are showed when the module is on a related lists (list_fields) and the other defines the columns that are shown in the module's popup capture screen (search_fields). Many times we want to be able to change these columns because the default ones aren't important for us or some users need more information in the popup screen. Using the List Columns mapping you can adapt these lists to your requirements without modifying the code.

The mapping follows the accepted XML format:

```xml
<map>
<originmodule>
<originname>{ModuleName}</originname>
</originmodule>
<relatedlists>
<relatedlist>
<module>{parentmodule}</module>
<linkfield></linkfield>
<columns>
    <field>
    <label></label>
    <name></name>
    <table></table>  {optional}
    <columnname></columnname>  {optional}
    </field>
    ...
</columns>
</relatedlist>
...
</relatedlists>
<popup>
<linkfield></linkfield>
<columns>
    <field>
    <label></label>
    <name></name>
    <table></table>  {optional}
    <columnname></columnname>  {optional}
    </field>
    ...
</columns>
<conditions>
    <condition>
        <forfield>fieldname</forfield>
        <value>JSON filter conditions</value>
    </condition>
</conditions>
</popup>
</map>
```

In the mapping, you can define different sets of columns for related lists and the popup screen. Each related list section specifies the parent module, the link field, and the columns to display. Similarly, the popup section defines the link field and the columns for the popup screen.

The name of the mapping should follow the format `{ModuleName}_ListColumns`, and if you need the mapping to be specific to individual users, you can use the global variable `BusinessMapping_{ModuleName}_ListColumns`.

To understand how the mapping works, consider the following example:

<div class="notices blue">
The Potentials_ListColumns map is intended for the Potentials module. When displaying a list of potential records in the Contacts module, show these columns. For the same list in the Accounts module, show these other columns. When opening a popup to select a potential record, display these fields. Ensure that all field references correspond to fields available in the Potentials module.
</div>

<div class="notices blue">
If you want to modify how contacts appear in their lists, you should create a `Contacts_ListColumns` map and open a related list section for Potentials.
</div>

<div class="notices blue">
To modify the columns appearing in the Global Search for the module, create a section with the parentmodule set to Utilities.
</div>

By leveraging the List Columns mapping feature, you can easily tailor the columns shown in related and popup lists to match your specific module and user requirements within coreBOS.

<br>

## Popup Query Conditions

The Popup Query Conditions feature in coreBOS allows you to filter the records displayed in the popup screen. Previously, achieving this required coding changes using the [Popup Query Hook](../../../10.developer-guide/03.architecture-concepts/77.popup_query_hook). However, with this feature, you can accomplish the same task by adding a simple mapping in the **Business Mapping** module.

Let's take a look at an example of the mapping in the **Products** module:

```xml
<map>
<originmodule>
    <originname>Products</originname>
</originmodule>
<popup>
    <linkfield>productcode</linkfield>
    <columns>
        <field>
            <name>productcode</name>
        </field>
        <field>
            <name>productname</name>
        </field>
        <field>
            <name>unit_price</name>
        </field>
    </columns>
    <conditions>
        <condition>
            <forfield>productid</forfield>
            <value>[{"fieldname":"unit_price","operation":"less than","value":"5","valuetype":"rawtext","joincondition":"and","groupid":"0","groupjoin":""}]</value>
        </condition>
    </conditions>
</popup>
</map>
```

In the mapping, we start by specifying the `originmodule`, which is the target module (in this case, **Products**). The `linkfield` specifies a field in the **Products** module that will be used to navigate to another module upon selection. Within the `columns` section, you define the fields that will be displayed in the popup screen.

The `conditions` section is where you define the filtering conditions. In the example, we use the `forfield` tag to specify the related field (uitype 10) in every module associated with **Products**. For example, if you try to link a specific product in the **InventoryDetails** module, the popup screen will only show records that satisfy the conditions specified within the `value` tags.

The value provided within the `value` tags is a JSON array that defines the conditions. In the example, we have the following condition:

`[{"fieldname":"unit_price","operation":"less than","value":"5","valuetype":"rawtext","joincondition":"and","groupid":"0","groupjoin":""}]`

This condition instructs the system to display only the products where the *unit_price* field has a value less than 5.

By applying these conditions, you will receive a list of products with a unit price less than 5.

> **_Last tip:_** If you need an easier way to write conditions, you can use the **cbQuestion** module. Access the "Builder" mode within the module by visiting the following link in your coreBOS installation: `index.php?action=Builder&module=cbQuestion`. This mode allows you to create specific conditions, which will be translated into code lines to assist you.

------------------------------------------------------------------------

[Next](../23.record_set/item.md) | Chapter 7: Record Set Mapping.

------------------------------------------------------------------------