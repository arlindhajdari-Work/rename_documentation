---
title: 'Configuring Autocomplete and MultiSelect Autocomplete Fields'
metadata:
    description: 'Configuring Autocomplete and MultiSelect Autocomplete Fields.'
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
        - autocomplete
---

To configure an autocomplete field, there are three options that can be customized:

- **Search Settings**: You can define the module or table where the system should search for values, specify whether to use "startswith" or "contains" for the search, and even utilize SQL queries within the cbMap to override the default search behavior in specific situations. Additionally, it is common to configure the minimum number of characters required to trigger the search.
- **Returned Information**: You can specify the main entity identifier that should be returned when a record is selected from the autocomplete suggestions. Additionally, you can include additional fields that support the decision-making process for selecting a record.
- **Field Population**: You have the ability to automatically populate fields in the current module with related fields from the source module. For example, copying address fields from Accounts to Contacts.

All these options can be defined using the Extended Field Information mapping.

Here is an example of a configuration map that activates the functionality for the "Potentials Name" and "RelatedTo" fields:

**Potentials_FieldInfo**

```xml
<map>
  <originmodule>
    <originname>Potentials</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>related_to</fieldname>
      <features>
        <feature>
          <name>searchmodule</name>
          <value>Contacts</value>
        </feature>
        <feature>
          <name>searchfields</name>
          <values>
            <value>
              <module>Accounts</module>
              <value>accountname</value>
            </value>
            <value>
              <module>Contacts</module>
              <value>firstname,lastname</value>
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
              <value>accountname</value>
            </value>
            <value>
              <module>Contacts</module>
              <value>firstname</value>
            </value>
          </values>
        </feature>
        <feature>
          <name>showfields</name>
          <values>
            <value>
              <module>Accounts</module>
              <value>accountname,phone,email1</value>
            </value>
            <value>
              <module>Contacts</module>
              <value>firstname,email,mailingstreet</value>
            </value>
          </values>
        </feature>
        <feature>
          <name>fillfields</name>
          <values>
            <value>
              <module>Accounts</module>
              <value>forecast_amount=annual_revenue</value>
            </value>
            <value>
              <module>Contacts</module>
              <value>leadsource=leadsource,assigned_user_id=assigned_user_id,closingdate=support_end_date</value>
            </value>
          </values>
        </feature>
      </features>
    </field>
    <field>
      <fieldname>potentialname</fieldname>
      <features>
        <feature>
          <name>searchmodule</name>
          <value>Contacts</value>
        </feature>
        <feature>
          <name>searchfields</name>
          <value>firstname,lastname</value>
        </feature>
        <feature>
          <name>searchcondition</name>
          <value>startswith</value>
        </feature>
        <feature>
          <name>entityfield</name>
          <value>firstname</value>
        </feature>
        <feature>
          <name>showfields</name>
          <value>firstname,email,mailingstreet</value>
        </feature>
        <feature>
          <name>fillfields</name>
          <value>leadsource=leadsource,assigned_user_id=assigned_user_id,closingdate=support_end_date</value>
        </feature>
      </features>
    </field>
  </fields>
</map>
```

There are three types of fields that support autocomplete: relation or capture fields (uitype 10), uitype 1 text fields, and uitype 2 text fields. Please note that uitype 2 text fields can only be created through programming.

Each of these field types has a different extended information structure, as shown in the example above. The "potentialname" field uses a flat value directive since it only searches within one module. On the other hand, the "related_to" field has a more complex syntax because it allows searching across multiple related modules.

To ensure the correct functionality, please apply the appropriate XML structure based on your field type.

## Product/Service Fields on Inventory Modules

Luke from MajorLabel has made remarkable progress in implementing the autocomplete search functionality for product/service capture in the inventory modules. Not only did he add the functionality, but he also extended it to meet specific requirements for those lines and introduced additional features.

If you're interested, Luke has provided extensive documentation on this topic, which you can find [here](https://gist.github.com/Luke1982/d886a67eb661db777d93e7e645076ecc) ([PDF](fine-tuning_the_products_services_autocomplete.pdf)).

**A big thanks to Luke for his contributions!**

## MultiSelect Autocomplete Fields

For MultiSelect Autocomplete Fields, the uitype is 1025, and the extended field information follows the same structure as a normal select autocomplete field.

This feature allows support for multiple selectable modules, but it's important to note that you can only choose records from one specific module at a time.

Here's an example of a test field definition for a uitype 1025 in the potentials module:

```XML
<field>
  <fieldname>ui1025</fieldname>
  <features>
<feature>
  <name>searchmodule</name>
  <value>Contacts</value>
</feature>
<feature>
  <name>searchfields</name>
  <values>
<value>
  <module>Accounts</module>
  <value>accountname</value>
</value>
<value>
  <module>Contacts</module>
  <value>firstname,lastname</value>
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
  <value>accountname</value>
</value>
<value>
  <module>Contacts</module>
  <value>firstname</value>
</value>
  </values>
</feature>
<feature>
  <name>showfields</name>
  <values>
<value>
  <module>Accounts</module>
  <value>accountname,phone,email1</value>
</value>
<value>
  <module>Contacts</module>
  <value>firstname,email,mailingstreet</value>
</value>
  </values>
</feature>
<feature>
  <name>fillfields</name>
  <values>
<value>
  <module>Accounts</module>
  <value>forecast_amount=annual_revenue</value>
</value>
<value>
  <module>Contacts</module>
  <value>leadsource=leadsource,assigned_user_id=assigned_user_id,closingdate=support_end_date</value>
</value>
  </values>
</feature>
<feature>
  <name>multiselect</name>
  <value>true</value>
</feature>
  </features>
</field>
```

Please make sure to use the correct XML structure for your specific field type to ensure the proper functionality.