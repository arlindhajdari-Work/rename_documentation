---
title: 'Application Menu Business Mapping'
metadata:
    description: 'Access any saved menu structure using this business map.'
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
        - application
        - menu
---

The purpose of the coreBOS Menu Layout Mapping is to retrieve and export the JSON layout of a specified menu from the coreBOS application. This feature allows you to define menus within coreBOS using the menu editor and then export them for use in external applications. By leveraging global variables, you can dynamically apply different menus to different users based on predefined conditions.

===

The accepted format for the mapping is as follows:

```xml
<map>
    <menuname>my_useful_menu</menuname> 
</map>
```

To retrieve the menu dynamically by passing the menu name as a parameter, you can use the special menuname value `get_name_from_menuname_parameter` in the mapping:

```xml
<map>
    <menuname>get_name_from_menuname_parameter</menuname> 
</map>
```

For example, if you have named your business map as `GenericMenuAccess`, you can use the following PHP code to retrieve a saved menu named `SomeSavedMenuName`:

```php
$mapid = 'convert GenericMenuAccess to a crmid';
$map = new cbMap();
$map->id = $mapid;
$map->retrieve_entity_info($mapid, 'cbMap');
$mapinfo = $map->ApplicationMenu(['menuname' => 'SomeSavedMenuName']);
```

If you prefer to use the coreBOS web service development tool, you can use the following code:

```php
$params = array(
	'sessionName' => $cbSessionID,
	'operation' => 'ProcessMap',
	'mapid' => 'GenericMenuAccess',
	'parameters' => '{"menuname":"SomeSavedMenuName"}',
);
$response = $httpc->doPost($params, false);
$dmsg.= debugmsg('Webservice response', $response);
var_dump($response);
```

These examples demonstrate how to retrieve and utilize the coreBOS menu layout mapping to export menus for external applications or integrate them into your custom development projects.

## Nested Array Menu JSON Representation

By configuring the nested property in the XML as illustrated below:

```xml
<map>
    <menuname>my_useful_menu</menuname>
    <nested>1</nested>
</map>
```

You will receive a JSON representation of the menu already organized in a nested structure. This facilitates readability for front-end developers, particularly when dealing with multiple levels of the menu.

Instead of obtaining a 1D menu array like this:

```json
[
  ["64", "menu", "", "Settings", 0, "8", "1", "", "main_menu", "Settings"],
  [ "2", "module", "Home", "Home", "1", "1", "1", "", "main_menu"],
  [ "3", "module", "Calendar4You", "Calendar4You", "1", "2", "1", "", "main_menu"],
]
```

You will receive a nested array:

```json
[
  {
    "evvtmenuid": 1,
    "mtype": "menu",
    "mvalue": "",
    "mlabel": "My Home Page",
    "mparent": 0,
    "mseq": 1,
    "mvisible": 1,
    "mpermission": "",
    "menu_name": "main_menu",
    "children": [
      {
        "evvtmenuid": 2,
        "mtype": "module",
        "mvalue": "Home",
        "mlabel": "Home",
        "mparent": 1,
        "mseq": 1,
        "mvisible": 1,
        "mpermission": "",
        "menu_name": "main_menu",
        "icon": {
          "library": "standard",
          "containerClass": "slds-icon_container slds-icon-standard-home",
          "class": "slds-icon",
          "icon": "home"
        },
        "children": []
      },
    ]
  },
  {
    "evvtmenuid": 39,
    "mtype": "menu",
    "mvalue": "",
    "mlabel": "Inventory",
    "mparent": 0,
    "mseq": 6,
    "mvisible": 1,
    "mpermission": "",
    "menu_name": "main_menu",
    "children": [
      {
        "evvtmenuid": 40,
        "mtype": "module",
        "mvalue": "Products",
        "mlabel": "Products",
        "mparent": 39,
        "mseq": 1,
        "mvisible": 1,
        "mpermission": "",
        "menu_name": "main_menu",
        "icon": {
          "library": "standard",
          "containerClass": "slds-icon_container slds-icon-standard-product",
          "class": "slds-icon",
          "icon": "product"
        },
        "children": []
      },
      {
        "evvtmenuid": 41,
        "mtype": "module",
        "mvalue": "Vendors",
        "mlabel": "Vendors",
        "mparent": 39,
        "mseq": 2,
        "mvisible": 1,
        "mpermission": "",
        "menu_name": "main_menu",
        "icon": {
          "library": "standard",
          "containerClass": "slds-icon_container slds-icon-standard-person-account",
          "class": "slds-icon",
          "icon": "person_account"
        },
        "children": []
      },
    ]
  },
  {
    "evvtmenuid": 51,
    "mtype": "menu",
    "mvalue": "",
    "mlabel": "Tools",
    "mparent": 0,
    "mseq": 7,
    "mvisible": 1,
    "mpermission": "",
    "menu_name": "main_menu",
    "children": [
      {
        "evvtmenuid": 52,
        "mtype": "module",
        "mvalue": "Rss",
        "mlabel": "RSS",
        "mparent": 51,
        "mseq": 1,
        "mvisible": 1,
        "mpermission": "",
        "menu_name": "main_menu",
        "icon": {
          "library": "standard",
          "containerClass": "slds-icon_container slds-icon-standard-account",
          "class": "slds-icon",
          "icon": "news"
        },
        "children": []
      },
    ]
  },
]
```

<br>
------------------------------------------------------------------------

[Next](../16.kanban) | Chapter 23: Kanban View.

------------------------------------------------------------------------