---
title: 'coreBOS Settings: Key-Value Store'
metadata:
    description: 'A generic, system-wide, Key-Value store available to all developers.'
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
        - development
        - keyvaluestore
    tag:
        - store
---

As of April 2017 coreBOS has a generic, system-wide, **Key-Value store** available to all developers.

coreBOS Settings permits any module or extension to easily save values persistently in the database without the need to create their own tables.

===

The typical scenario is where the new module or extension requires saving some small configuration settings or an install license key. Since there was no way of saving this information without your own table the database tends to fill up with small tables that just hold a few values.

Now, with coreBOS Settings these values can be saved and retrieved from one generic table.

The [coreBOS Settings object](https://github.com/tsolucio/corebos/blob/master/include/utils/cbSettings.php) is called **coreBOS\_Settings** and contains 4 static methods to manipulate the values:

## getSetting

Will retrieve a value by the name of the key if it exists or the given default value if the key does not exist.

This method implements an internal cache.

## setSetting

Saves the given Key-Value overwriting any existing value for that key.

 !! It is important to prefix your keys with some unique identifier in order to not enter in conflict with some other existing key.

## delSetting

Eliminates the Key-Value from the store.

## SettingExists

Checks if a value exists for the given key. Will return true if the key is found and false if not.

## Notes

- You can use the coreBOS\_Settings object from anywhere in the application
- Values are limited to 64K characters (text field)
- Values are always strings
- You can see some examples of usage in the [coreBOS Test Project](https://github.com/tsolucio/coreBOSTests/blob/master/include/utils/cbSettingsTest.php)
