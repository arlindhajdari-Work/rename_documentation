---
title: 'Popup Filter'
metadata:
    description: 'The purpose of this mapping is to filter in the popup window by comparing fields from that module to a certain value or to another field from modules by navigating through infinite link fields when the relations exist.'
    author: 'Enea Dudija'
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
        - popupfilter
---

The purpose of the Popup Filter map is to enable record filtering within popup windows. When we open a popup from a uitype10 field, this map allows us to define conditions that the records must meet in order to be displayed in the popup.

===

One advantage of this method is that it enables us to compare a field with another field by accessing an infinite number of uitype10s. This means that if we want to retrieve a value from a field in a third or more relation, we can easily navigate through link fields between modules, as long as a relation exists.

Here's an example of a map built for the **AssetDetails** module to filter **ProductComponents** based on the condition where the **_frompdo_** field is equal to the **_product_** field in the **_related_assets_** field of the **AssetDetail**:

In a few words we are in the **AssetDetails** module, go to **$related_assets** which is the relation field to the **Assets** module and from there we take this **$product field**: 

```xml
<map>
  <modulename>AssetDetails</modulename> <!-- module where we open the popup -->
  <field>
    <fieldname>related_productcomponent</fieldname> <!-- the uitype10 field where we click to open the popup -->
    <modulename>ProductComponent</modulename> <!-- the module that appears in the popup -->
    <advft_criteria>[{"groupid":1,"columnname":"frompdo","comparator":"e","value":"$related_assets.$product","columncondition":""}]</advft_criteria>
    <advft_criteria_groups>[]</advft_criteria_groups>
  </field>
  <!-- after “columnname:” we specify a field from the module where we are trying to filter, ProductComponent in our case; meanwhile as value we specify the field that we want to compare with. We can navigate through uitype10 using ‘.’ to separate fields and the ‘$’ sign before names -->
  <field>
    <fieldname>related_ad_servicecontact</fieldname>
    <modulename>ServiceContracts</modulename>
    <advft_criteria>[{"groupid":1,"columnname":"sc_related_to","comparator":"e","value":"$related_assets.$account","columncondition":""}]</advft_criteria>
    <advft_criteria_groups>[]</advft_criteria_groups>
  </field>
</map>
```

The map name must always be named **{Module name}_PopupFilter**. 

The type of map must be: **Popup Filter**

If you need to specify additional filters for other uitype10 fields within the module, you can add <field> tags to define those filters in the map.

