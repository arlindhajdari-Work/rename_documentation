---
title: '(Field) Mapping Business Mapping'
metadata:
    description: 'filling in fields of a new record when coming from another module record or setting default values for the module you are creating.'
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
        - mapping
        - field
---

Field Mapping Business Mapping is a powerful tool that allows users to define field mappings and set default values when creating new records in different modules. It provides flexibility and efficiency by automatically populating fields based on predefined rules and conditions. In this article, we will explore the structure and functionality of Field Mapping Business Mapping and how it can be used to streamline record creation processes.

===

The format of the Field Mapping Business Mapping is based on XML. It consists of several elements that define the origin module, target module, and the fields to be mapped. Let's break down the structure of the XML file:

1. **Origin Module**: This element specifies the module from which the record is originating. It contains the `<originname>` tag, which identifies the name of the origin module.

2. **Target Module**: This element defines the module in which the new record will be created. It includes the `<targetname>` tag, which indicates the name of the target module.

3. **Fields**: This section contains the mappings for individual fields. Each `<field>` element represents a field to be mapped. Within the `<field>` element, the following sub-elements are defined:

4. **Field Name**: This element, denoted by `<fieldname>`, specifies the name of the field in the target module.

5. **Origin Fields**: This element, denoted by `<Orgfields>`, defines the origin fields that provide values for the target field. Multiple origin fields can be specified, and their values can be concatenated using a delimiter.
    * **Origin Field**: Each origin field is enclosed within the `<Orgfield>` element. It consists of the following sub-elements:
      * **Origin Field Name**: This element, denoted by `<OrgfieldName>`, specifies the name of the origin field.
      * **Origin Field ID**: This element, denoted by `<OrgfieldID>`, indicates the type of the origin field. It can have values like FIELD, CONST, TEMPLATE, EXPRESSION, or RULE.

    * **Delimiter**: This element, denoted by `<delimiter>`, defines the delimiter used to concatenate multiple origin fields.

    * **Master**: This element, denoted by `<master>`, is an optional field used for integration mapping between two systems.

4. **OrgfieldID Directives**: The `<OrgfieldID>` element within each `<Orgfield>` element specifies the type of the origin field. Depending on the type, different actions can be performed. The available types are:

   * **FIELD**: The origin field contains a field or field expression.
   * **CONST**: The origin field is used as is, without any transformation.
   * **TEMPLATE**: The origin field is treated as a string template parsed by the Message engine.
   * **EXPRESSION**: The origin field contains a workflow expression to be parsed by the workflow engine.
   * **RULE**: The origin field contains the ID or name of a business rule. See below.

Each `<OrgfieldID>` directive can also have a `<postProcess>` directive, which allows additional processing of the field value.

**Mapping Name**: To apply the mapping, the name of the mapping must follow a specific format:

`{OriginModule}2{TargetModule}`

The mapping must be created with this name, and the module names must match their internal module names. If multiple mappings are required based on the user, a new entry in the Global Variable name picklist called

`BusinessMapping_{OriginModule}2{TargetModule}`

must be created, and a corresponding Global Variable of this type should be defined.

This map will permit you to define what values you want to copy from the origin module or simply what values you want to set by default when creating a new record.

 !!! When creating a new record you always have access to all the fields of the current user using the FIELD or TEMPLATE types. For example: `$(assigned_user_id : (Users) first_name)`

A commented example of the accepted format is:

```xml
<map>
  <originmodule>
    <originname>SalesOrder</originname>
  </originmodule>
  <targetmodule>
    <targetname>Invoice</targetname>
  </targetmodule>
  <fields>
    <field>
      <fieldname>subject</fieldname>   {destination field on invoice}
      <Orgfields>  {if more than one is present they will be concatenated with the delimiter}
        <Orgfield>
          <OrgfieldName>subject</OrgfieldName>
          <OrgfieldID>FIELD</OrgfieldID>
        </Orgfield>
        <Orgfield>
          <OrgfieldName>sostatus</OrgfieldName>
          <OrgfieldID>FIELD</OrgfieldID>
        </Orgfield>
        <Orgfield>
          <OrgfieldName>_FromSO</OrgfieldName>  {this is a constant string}
          <OrgfieldID>CONST</OrgfieldID>
        </Orgfield>
        <delimiter>;</delimiter>
      </Orgfields>
      <master>true|false</master> {optional: used for integration mapping between two systems}
    </field>
      <field>
      <fieldname>description</fieldname>   {destination field on invoice}
      <Orgfields>  {if more than one is present they will be concatenated with the delimiter}
        <Orgfield>
          <OrgfieldName>$(assigned_user_id : (Users) first_name)</OrgfieldName>
          <OrgfieldID>FIELD</OrgfieldID>
        </Orgfield>
        <Orgfield>
          <OrgfieldName>$(assigned_user_id : (Users) last_name)</OrgfieldName>
          <OrgfieldID>FIELD</OrgfieldID>
        </Orgfield>
        <Orgfield>
          <OrgfieldName>The user assigned to the Sales Order is: $(assigned_user_id : (Users) first_name) $(assigned_user_id : (Users) last_name)</OrgfieldName>
          <OrgfieldID>TEMPLATE</OrgfieldID>
        </Orgfield>
        <Orgfield>
          <OrgfieldName>account_id</OrgfieldName>
          <OrgfieldID>RULE</OrgfieldID>
          <Rule>business rule name or ID</Rule>
        </Orgfield>
        <delimiter> - </delimiter>
      </Orgfields>
    </field>
    <field>
      <fieldname>due_date</fieldname>   {destination field on invoice}
      <Orgfields>
        <Orgfield>
          <OrgfieldName>add_days(get_date('today'), 30)</OrgfieldName>
          <OrgfieldID>EXPRESSION</OrgfieldID>
          <postProcess>intval</postProcess>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      ...
    </field>
  </fields>
</map>
```

Each `OrgfieldID` directive may have a `postProcess` directive. This permits us to do some additional processing in cases where the `OrgfieldID` directive is not expressive enough. Usually this is used to specify the format of the result to be used in the mapping. For example, in general, coreBOS uses strings for all its' results but we may need to use an integer or float or strip slashes that are returned from the expression before inserting it into the resulting array. Some of the methods that can be used are:

- intval - Get the integer value of a variable
- boolval - Get the boolean value of a variable
- floatval - Get float value of a variable
- addslashes Quote string with slashes
- stripslashes - Un-quotes a quoted string
- htmlspecialchars - Convert special characters to HTML entities
- quotemeta - Quote meta characters
- json_encode
- json_decode

For example, if you create a Mapping called *Contacts2Potentials* and set it's mapping to the one below, you will get the name set to the contact's name, the closing date set to 30 days from now and the sales stage set to `Qualifying`.

Then call the create page of Potentials from a link passing in the variable **cbfromid** or from a related list, which already has this variable.

```xml
<map>
  <originmodule>
    <originname>Contacts</originname>
  </originmodule>
  <targetmodule>
    <targetname>Potentials</targetname>
  </targetmodule>
  <fields>
    <field>
      <fieldname>potentialname</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>firstname</OrgfieldName>
          <OrgfieldID>field</OrgfieldID>
        </Orgfield>
        <Orgfield>
          <OrgfieldName>lastname</OrgfieldName>
          <OrgfieldID>field</OrgfieldID>
        </Orgfield>
        <delimiter> </delimiter>
      </Orgfields>
    </field>
    <field>
      <fieldname>closingdate</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>add_days(get_date('today'), 30)</OrgfieldName>
          <OrgfieldID>expression</OrgfieldID>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
        <fieldname>sales_stage</fieldname>
        <Orgfields>
            <Orgfield>
                <OrgfieldName>Qualification</OrgfieldName>
                <OrgfieldID>CONST</OrgfieldID>
            </Orgfield>
        </Orgfields>
    </field>
  </fields>
</map>
```

Another example for User default values:

```xml
<map>
  <originmodule>
    <originname>Users</originname>
  </originmodule>
  <targetmodule>
    <targetname>Users</targetname>
  </targetmodule>
  <fields>
    <field>
      <fieldname>currency_grouping_pattern</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>123456789</OrgfieldName>
          <OrgfieldID>CONST</OrgfieldID>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>currency_decimal_separator</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>.</OrgfieldName>
          <OrgfieldID>CONST</OrgfieldID>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>QLTQ</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>QLTQ</OrgfieldName>
          <OrgfieldID>CONST</OrgfieldID>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>ALVT</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>ALVT</OrgfieldName>
          <OrgfieldID>CONST</OrgfieldID>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>tagcloudview</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>false</OrgfieldName>
          <OrgfieldID>CONST</OrgfieldID>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>showtagas</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>vring</OrgfieldName>
          <OrgfieldID>CONST</OrgfieldID>
        </Orgfield>
      </Orgfields>
    </field>
  </fields>
</map>
```

You can [see an example of converting a Contact into an Account in the Business Mapping Store](/en/adminmanual/businessmappings/store/contact2accounts).

And there is an explanation and [small example of Invoice default values here.](http://discussions.corebos.org/thread-338-post-1723.html#pid1723)

Another [example with Help Desk default values in the forum.](http://discussions.corebos.org/thread-346-post-1772.html#pid1772)

## Rule Directive

The rule directive will permit us to launch a [coreBOS Business Rule](/en/devel/corebos_rules) and save the result in the field. This opens the possibilities to launch a query, a workflow expression or a decision table.

You can accomplish the expression and template features with the Rule as it can do that and more.

For example, we may be given a code that we have to search in another module to save a value that comes from there. In this case, we need to launch a query so we would set up a Business Map (Rule) of type [Condition Query](../04.condition-query/) with something like this:

```sql
SELECT contactid
FROM vtiger_contactdetails
JOIN vtiger_contactscf on vtiger_contactdetails.contactid=vtiger_contactscf.contactid
where cf_1518=?
```

Let's suppose we called this business map "getContactFromSeller", then we would add the directive:

```xml
<Orgfield>
  <OrgfieldName>contact_id</OrgfieldName>
  <OrgfieldID>RULE</OrgfieldID>
  <Rule>getContactFromSeller</Rule>
</Orgfield>
```

## Accessing via web service

Field Mapping Business Mapping can be processed using the **ProcessMap** endpoint in the web service. This allows seamless integration with other systems and enables automated record creation with predefined field

<br>
------------------------------------------------------------------------

[Next](../28.extendedfieldinfo) | Chapter 4: Extended Field Information Mapping.

------------------------------------------------------------------------