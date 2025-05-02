---
title: 'Extended Field Information Mapping'
metadata:
    description: 'Define a set of additional features on fields.'
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
---

The purpose of this mapping is to provide additional features for fields in a structured way. Instead of modifying the vtiger_field table and creating various UI settings options, we use this mapping to configure extra information for each field.

===

The accepted format for the mapping is as follows:

```xml
<map>
  <originmodule>
    <originname>ModuleName</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>fieldname</fieldname>
      <features>
        <feature>
          <name>feature_name</name>
          <value>feature_value</value>
          <values>
             <value>
               <module>module_name</module>
               <value>value</value>
               ...
             </value>
             ...
           </values>
        </feature>
      </features>
    </field>
  </fields>
</map>
```

A **feature** can have a single unique value or an array of values. If both are provided, the unique value will take precedence.

For example, to define a Rich Text Editor (RTE) field, use the following mapping:

```xml
<map>
  <originmodule>
    <originname>SalesOrder</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>description</fieldname>
      <features>
        <feature>
          <name>RTE</name>
          <value>1</value>
        </feature>
      </features>
    </field>
  </fields>
</map>
```

The above mapping will enable the RTE feature for the "description" field in the SalesOrder module.

Similar to other Business Maps, the record's name determines whether it is used and in which module. In this case, the record must be named `{MODULENAME}_FieldInfo`. To make the example mapping above work, save it in a record named `SalesOrder_FieldInfo`.

The information in this mapping is directly available in the DetailViewUtils and EditViewUtils scripts, as well as in the Detail and Edit View Smarty templates. You can refer to this commit for an example of how we access this information to add generic support for RTE fields.

The information in this mapping is directly available in the DetailViewUtils and EditViewUtils scripts, as well as in the Detail and Edit View Smarty templates. You can refer to [this commit](https://github.com/tsolucio/corebos/commit/97d26c2a7d32a84fee4737e40f099a8166484e64) for an example of how we access this information to add generic support for RTE fields.

Another example involves configuring different settings for an autocomplete field. Here's the mapping structure:

```xml
<map>
  <originmodule>
    <originname>Potentials</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>autocompletefieldx</fieldname>
      <features>
        <feature>
          <name>searchfields</name>
          <value>field1,field2,...,fieldn</value>
        </feature>
        <feature>
          <name>searchcondition</name>
          <value>startswith</value>
        </feature>
        <feature>
          <name>entityfield</name>
          <value>field</value>
        </feature>
        <feature>
          <name>showfields</name>
          <value>field1,field2,...,fieldn</value>
        </feature>
        <feature>
          <name>fillfields</name>
          <value>field1=fillfield1,field2=fillfield2,...,fieldn=fillfieldn</value>
        </feature>
      </features>
    </field>
  </fields>
</map>
```

This map defines that the autocomplete field must show the "entityfield" followed by the list of "showfields" to the user, while permitting them to search on the list of "searchfields," and then filling in the "fillfields" with the values of the indicated record fields.

Alternatively, if we want to configure a multioptional autocomplete field, we could use a map like this one:

```xml
<map>
  <originmodule>
    <originname>Potentials</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>autocompletefieldx</fieldname>
      <features>
        <feature>
          <name>searchfields</name>
          <values>
            <value>
              <module>Accounts</module>
              <value>field1,field2,...,fieldn</value>
            </value>
            <value>
              <module>Contacts</module>
              <value>field1,field2,...,fieldn</value>
            </value>
          </values>
        </feature>
        <feature>
          <name>searchcondition</name>
          <value>startswith</value>
        </feature>
        <feature>
          <name>entityfield</name>
          <values>
            <value>
              <module>Accounts</module>
              <value>field</value>
            </value>
            <value>
              <module>Contacts</module>
              <value>field</value>
            </value>
          </values>
        </feature>
        <feature>
          <name>showfields</name>
          <values>
            <value>
              <module>Accounts</module>
              <value>field1,field2,...,fieldn</value>
            </value>
            <value>
              <module>Contacts</module>
              <value>field1,field2,...,fieldn</value>
            </value>
          </values>
        </feature>
        <feature>
          <name>fillfields</name>
          <values>
            <value>
              <module>Accounts</module>
              <value>field1=fillfield1,field2=fillfield2,...,fieldn=fillfieldn</value>
            </value>
            <value>
              <module>Contacts</module>
              <value>field1=fillfield1,field2=fillfield2,...,fieldn=fillfieldn</value>
            </value>
          </values>
        </feature>
      </features>
    </field>
  </fields>
</map>
```

## Configuring Autocomplete and MultiSelect Autocomplete Fields

[Continue reading here for more information on how to configure an autocomplete functionality on a field in coreBOS](autocomplete)

## Configuring Combobox with static values Fields

[Continue reading here for more information on how to configure a combobox functionality on a field in coreBOS](combobox)

## Configuring Multipicklists

```xml
<map>
  <originmodule>
    <originname>Accounts</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>cf_732</fieldname>
      <features>
        <feature>
          <name>columns</name>
          <value>10</value>
        </feature>
        <feature>
          <name>width</name>
          <value>350</value>
        </feature>
      </features>
    </field>
  </fields>
</map>
```

## Configuring Textarea Height

```xml
<map>
  <originmodule>
    <originname>Accounts</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>description</fieldname>
      <features>
        <feature>
          <name>height</name>
          <value>150</value>
        </feature>
      </features>
    </field>
  </fields>
</map>
```

<br>
------------------------------------------------------------------------

[Next](../22.record_access_control) | Chapter 5: Record Access Control.

------------------------------------------------------------------------