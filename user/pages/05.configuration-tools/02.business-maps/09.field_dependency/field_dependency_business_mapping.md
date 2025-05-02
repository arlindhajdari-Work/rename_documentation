---
title: 'Field Dependency Business Mapping'
metadata:
    description: 'This map permits you to define dependencies between fields in edit mode.'
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
        - fielddependency
---

The CoreBOS Field Dependency Business Mapping is a mechanism that allows you to define dependencies between fields in different modules within the CoreBOS CRM system. It enables you to establish relationships and dependencies among fields, which determine their visibility and availability based on the values of other fields.

===

By defining field dependencies using the coreBOS Field Dependency Business Mapping, you can configure complex relationships between fields in different modules. This helps to enforce data integrity, streamline user interactions, and ensure that the right fields are available at the right time based on specific conditions.

The mapping is typically used in customizations and extensions of the CoreBOS CRM system to tailor the behavior of fields and modules according to specific business requirements and workflows.

The mapping is defined using an XML format. Here's an abstraction of the structure:

```xml
<map>
  <originmodule>
    <originname>Module_Name</originname>
  </originmodule>
  <dependencies>
    <dependency>
      <mode></mode> <!-- optional -->
      <field>Field_Name</field>
      <conditions>
        <!-- Define the conditions for the field dependency -->
        <condition>[...]</condition>
        ...
      </conditions>
      <actions>
        <!-- Define the actions to be performed when the conditions are met -->
        <mode></mode> <!-- optional -->
        ...
      </actions>
    </dependency>
    ...
  </dependencies>
</map>
```

Now let's break down the structure:

- **`<map>`**: The root element that encapsulates the entire mapping.
- **`<originmodule>`**: Specifies the module where the field dependencies originate.
- **`<originname>`**: Specifies the name of the module for which field dependencies are being defined.
- **`<dependencies>`**: Contains the list of field dependencies within the module.
- **`<dependency>`**: Represents a specific field dependency.
- **`<field>`**: Specifies the name of the field for which the dependency is being defined.
- **`<conditions>`**: Contains the conditions that determine when the field dependency is triggered.
- **`<condition>`**: Defines a specific condition for the field dependency.
- **`<actions>`**: Contains the actions to be performed when the conditions are met.

Within the `<conditions>` element, you can define one or more `<condition>` elements that specify the conditions for the field dependency. These conditions can include various comparisons, logical operators, and values.

Similarly, within the `<actions>` element, you can define the actions to be performed when the conditions are met. These actions can include showing or hiding fields, setting field values, executing workflows, invoking custom functions, and more.

This type of map works both in edit and details view, permiting you to define dependencies between fields. For example, it will permit you to make a field read-only (not editable) or not depending on the value selected in a given field or to change the available values in a picklist depending on the value.

The goal of this mapping is to define a set of rules/conditions and actions to be applied while editing a field in a coreBOS form.

The trigger event will be the `onChange` HTML event. Whenever a field changes its’ value in a form we will evaluate a given set of conditions and if they are true we will apply a set of actions.

Since we will be evaluating the field on a per-module basis and to avoid additional time looking for related values via AJAX, the conditions will be evaluated using only information located on the form.

The supported condition operators are the same ones we support in the custom view filter system (see [Conditional Popup](../../../10.developer-guide/04.development_framework/11.develtutorials/19.conditional_popup) and [Popup Open Hook](../../../10.developer-guide/04.development_framework/11.develtutorials/19.conditional_popup):

- e: igual | equal | "="
- n: distinto | not equal | "&lt;&gt;"
- s: empieza con | begins with | "LIKE" ("$value%")
- Ns: | does not begin with | "LIKE" !("$value%")
- ew: termina con | ends with | "LIKE" ("%$value")
- New: | does not end with | "LIKE" !("$value%")
- c: contiene | like | "LIKE" ("%$value%")
- k: no contiene | not like | "NOT LIKE" ("%$value")
- l: menor que | less than | "&lt;"
- b: menor que | less than | "&lt;"
- g: mayor que | greater than | "&gt;"
- a: mayor que | greater than | "&gt;"
- m: menor o igual | less or equal | "&lt;="
- h: mayor o igual | greater or equal | "&gt;="

Group conditions can be created concatenating with the typical AND/OR operators. We will be using a similar concept to the one used for filters:

```
"groupid":"number that identifies the group of conditions",
"columnname":"coreBOS column identifier or simply the column/field name"
"comparator":"comparison operator"
"value":"text to look"
"columncondition":"and|or" (logical operator to join with the next condition)
 ```

The actions supported are:

- **change**: will assign a value or set of values to another field
- **setoptions**: will add selectable options in a picklist
- **deloptions**: will eliminate selectable options from a picklist
- **hide**: hide a field and its label
- **show**: show a field and its label
- **collapse**: will collapse a block
- **open**: will open a block
- **disappear**: will hide a block
- **appear**: will show a block
- **readonly**: will make a field read-only
- **editable**: will make a field not read-only
- **enable**: will enable a field
- **disable**: will disable a field
- **setclass**: set CSS class
- **function**: will call the given function with the parameters:
  - change\_field, action\_field, new\_value, old\_value, any additional parameters in XML
  - this option leaves the door open to all sorts of options, giving total control to the programmer
  -  There are a set of common functions that can be used:
    - **fieldDep\_AssignNewValue**: return new value in the action\_field
    - **fieldDep\_CopyFieldValue**: copies the value in the field defined by the first parameter into the action field
    - **fieldDep\_AddDays**: add the given number of days to new\_value and return the result
    - **fieldDep\_SubDays**: subtract the given number of days from new\_value and return the result
    - **fieldDep\_OnlyNumbers**: return all numbers in new\_value
    - **fieldDep\_OnlyLetters**: return all letters in new\_value
    - **fieldDep\_GetField**: will use getFieldValuesFromRecord to retrieve the value of the given field from a related record. In other words, this works on related capture fields in the record and retrieves information from the selected related record
    - **fieldDep\_AssignUser**: set the assigned user to the given (user) ID parameter
    - **fieldDep\_AssignGroup**: set the assigned user to the given (group) ID parameter
    - **fieldDep\_AssignUserSelect**: set the assigned user to the given user ID parameter for uitype 101 fields
    - **fieldDep\_GetFieldSearch**: searches for a field as reference in order to map other fields
    - **fieldDep\_LaunchWorkflow**: launch the workflow ID given as a parameter with the record triggering the dependency
    - **fieldDep\_doJS**: [launch any generic javascript code](#fielddep-dojs)
    - **fieldDep\_ChangeLabel**: will permit changing the label of a field **NOT IMPLEMENTED YET**
    - **fieldDep\_Format**: return sprintf formatting of new\_value (use sprintf javascript library: <https://github.com/alexei/sprintf.js>) **NOT IMPLEMENTED YET**

This looks something like this:

```xml
<map>
  <originmodule>
    <originname>SalesOrder</originname>
  </originmodule>
  <dependencies>
    <dependency>
      <field>campaignname</field>
      <condition>[{...}]</condition>
      <actions>
        <change>
          <field>sponsor</field>
          <value>Sponzori</value>
        </change>
        <change>
          <field>campaignname</field>
          <value>2323232</value>
        </change>
        <hide>
          <field>targetaudience</field>
        </hide>
        <readonly>
          <field>campaignname</field>
        </readonly>
        <setclass>
          <field>somefield</field>
          <fieldclass>someCSSclass</fieldclass>
          <labelclass>someOtherCSSclass</labelclass>
        </setclass>
        <collapse>
          <block>sponsor</block>
        </collapse>
      </actions>
    </dependency>
    <dependency>
    …
    </dependency>
  </dependencies>
</map>
```

**Notes**

- This functionality overlaps with the native Picklist dependency, so we have moved that functionality to the map and eliminated the code that manages picklist dependency in javascript. The picklist dependency graphical editor in settings is still valid.
- When we manually assign a value to a field we have to launch the change event against that field so the dependencies get calculated again, but we have to make sure that we don’t enter an infinite loop by not launching the event against the same field we just modified.
- The mappings will be named **{modulename}\_FieldDependency** (to follow the logic of all the others)
- In EditView script we will search and load a mapping called `$current_module.'_FieldDependency'`. This will be done using the Global Variable module (like the others)
- If more than one is found we will load the first one found with no special preference. There should be only one.
- The mapping interface will have a method called getJSON (or similar). This method will return the conditions, fields and any other information the browser needs to implement the dependencies. We will load one or more variables into Smarty and modify the templates to load those values in javascript variables
- We will add a javascript library to process the mapping on the onChange events
- In MassEdit we have to do the same as in EditView
- In DetailView we will load the mapping and use another method called getFieldsWithDependency (or similar) to modify those fields in the detail view so they are not editable (as we do now with picklist fields that have dependencies). This is because we can’t guarantee their dependencies when editing one field individually. Note: it is very possible that this can be done directly in the getBlocks function.
- It is very possible that we have to modify the fields edit templates to add the onchange events. I would like that to be generic. I mean, we call a generic onChange event and add some hooks so anyone can add their own functionality. We use this hook to add the Field Dependency functionality.

Examples
--------

<div class="notices blue">
If payment is negative then set the category to `Infrastructure`
</div>

```xml
    <map>
      <originmodule>
        <originname>CobroPago</originname>
      </originmodule>
    <dependencies>
    <dependency>
        <field>amount</field>
        <condition>[{"groupid":"",
         "columnname":"vtiger_cobropago:amount:amount:CobroPago_Amount:N",
         "comparator":"m",
         "value":"0",
         "columncondition":""}]
        </condition>
        <actions>
            <change>
                <field>paymentcategory</field>
                <value>Infrastructure</value>
            </change>
        </actions>
    </dependency>
    </dependencies>
    </map>
```

<div class="notices blue">
If payment is negative then the category field must be `Infrastructure`
</div>

```xml
    <map>
      <originmodule>  <originname>CobroPago</originname> </originmodule>
    <dependencies>
    <dependency>
        <field>amount</field>
        <condition>[{"groupid":"",
         "columnname":"vtiger_cobropago:amount:amount:CobroPago_Amount:N",
         "comparator":"m",
         "value":"0",
         "columncondition":""}]
        </condition>
        <actions>
            <change>
                <field>paymentcategory</field>
                <value>Infrastructure</value>
            </change>
            <readonly>
                <field>paymentcategory</field>
            </readonly>
        </actions>
    </dependency>
    </dependencies>
    </map>
```

<div class="notices blue">
Or this one can also be done like this:
</div>

```xml
    <map>
      <originmodule>   <originname>CobroPago</originname> </originmodule>
    <dependencies>
    <dependency>
        <field>amount</field>
        <condition>[{"groupid":"",
         "columnname":"vtiger_cobropago:amount:amount:CobroPago_Amount:N",
         "comparator":"m",
         "value":"0",
         "columncondition":""}]
        </condition>
        <actions>
            <setoptions>
                <field>paymentcategory</field>
                <option>Infrastructure</option>
            </setoptions>

            <deloptions>
                <field>paymentcategory</field>
                <option>Taxes</option>
                <option>Travel</option>
                <option>Stock</option>
                <option>Sale</option>
            </deloptions>
            <change>
                <field>paymentcategory</field>
                <value>Infrastructure</value>
            </change>
        </actions>
    </dependency>
    </dependencies>
    </map>
```

<div class="notices blue">
if (employees &lt; 100 and bill_country is Spain) or (employees &gt; 100 and bill_country is Albania) then hide ownership collapse address block
</div>

```xml
    <map>
      <originmodule>  <originname>Accounts</originname> </originmodule>
    <dependencies>
    <dependency>
        <field>employees</field>
        <condition>[{"groupid":"1",
         "columnname":"vtiger_accounts:employees:employess:Accounts_Employees:N",
         "comparator":"l",
         "value":"100",
         "columncondition":"and"},
           {"groupid":"1",
         "columnname":"vtiger_accountbillads:bill_country:bill_country:Accounts_Bill_County:V",
         "comparator":"e",
         "value":"Spain",
         "columncondition":"or"},
    {"groupid":"2",
         "columnname":"vtiger_accounts:employees:employess:Accounts_Employees:N",
         "comparator":"g",
         "value":"100",
         "columncondition":"and"},
           {"groupid":"2",
         "columnname":"vtiger_accountbillads:bill_country:bill_country:Accounts_Bill_County:V",
         "comparator":"e",
         "value":"Albania",
         "columncondition":""}]
        </condition>
        <actions>
            <hide>
           <br>
     <field>ownership</field>
            </hide>
            <collapse>
                <block>LBL_ADDRESS_INFORMATION</block>
            </collapse>
        </actions>
    </dependency>
    <dependency>
        <field>bill_country</field>
        <condition>[{"groupid":"1",
         "columnname":"vtiger_accounts:employees:employess:Accounts_Employees:N",
         "comparator":"l",
         "value":"100",
         "columncondition":"and"},
           {"groupid":"1",
         "columnname":"vtiger_accountbillads:bill_country:bill_country:Accounts_Bill_County:V",
         "comparator":"e",
         "value":"Spain",
         "columncondition":"or"},
    {"groupid":"2",
         "columnname":"vtiger_accounts:employees:employess:Accounts_Employees:N",
         "comparator":"g",
         "value":"100",
         "columncondition":"and"},
           {"groupid":"2",
         "columnname":"vtiger_accountbillads:bill_country:bill_country:Accounts_Bill_County:V",
         "comparator":"e",
         "value":"Albania",
         "columncondition":""}]
        </condition>
        <actions>
            <hide>
                <field>ownership</field>
            </hide>
            <collapse>
                <block>LBL_ADDRESS_INFORMATION</block>
            </collapse>
        </actions>
    </dependency>
    </dependencies>
    </map>
```

<div class="notices blue">
On the invoice, set the due date field to 30 days more than the invoice date field
</div>

```xml
    <map>
      <originmodule>  <originname>Invoice</originname> </originmodule>
    <dependencies>
    <dependency>
        <field>invoicedate</field>
        <actions>
            <function>
                <field>duedate</field>
                <name>fieldDep_AddDays</name>
                <parameters>
                  <parameter>30</parameter>
                </parameters>
            </function>
        </actions>
    </dependency>
    </dependencies>
    </map>
```
<div class="notices blue">
On Contact change the phone field to contain only numbers 
</div>

```xml
    <map>
      <originmodule>  <originname>Contacts</originname> </originmodule>
    <dependencies>
    <dependency>
        <field>phone</field>
        <actions>
            <function>
                <field>phone</field>
                <name>fieldDep_OnlyNumbers</name>
            </function>
        </actions>
    </dependency>
    </dependencies>
    </map>
```

<div class="notices blue">
On Contact, set the description field to the value of the description field of the selected account
</div>

```xml
    <map>
      <originmodule>
        <originname>Contacts</originname>
      </originmodule>
    <dependencies>
    <dependency>
        <field>firstname</field>
        <actions>
            <function>
                <field>description</field>
                <name>fieldDep_GetField</name>
                <parameters>
                  <parameter>Accounts.description</parameter>
                  <parameter>description</parameter>
                </parameters>
            </function>
        </actions>
    </dependency>
    </dependencies>
    </map>
```

<div class="notices blue">
On Potential, set the potential name field to the industry of the related account and the next step field to the email of the related account
</div>

```xml
    <map>
      <originmodule>
        <originname>Potentials</originname>
      </originmodule>
    <dependencies>
    <dependency>
        <field>related_to</field>
        <actions>
            <function>
                <field>title</field>
                <name>fieldDep_GetField</name>
                <parameters>
                  <parameter>Accounts.industry,Accounts.email1</parameter>
                  <parameter>potentialname,nextstep</parameter>
                </parameters>
            </function>
        </actions>
    </dependency>
    </dependencies>
    </map>
```

<div class="notices blue">
IF (bill country starts with "A") SET the paymentcategory field to `infrastructure` and make it read-only ELSE make the paymentcategory field editable
</div>

```xml
    <map>
      <originmodule>  <originname>Accounts</originname> </originmodule>
    <dependencies>
    <dependency>
        <field>bill_country</field>
        <condition>
    [
        {"groupid":"1",
         "columnname":"bill_country",
         "comparator":"s",
         "value":"A",
         "columncondition":""}
    ]
        </condition>
        <actions>
            <change>
                <field>paymentcategory</field>
                <value>Infrastructure</value>
            </change>
            <readonly>
                <field>paymentcategory</field>
            </readonly>
        </actions>
    </dependency>

    <dependency>
        <field>bill_country</field>
        <condition>
    [
        {"groupid":"1",
         "columnname":"bill_country",
         "comparator":"ns",
         "value":"A",
         "columncondition":""}
    ]
        </condition>
        <actions>
            <editable>
                <field>paymentcategory</field>
            </editable>
        </actions>
    </dependency>
    </dependencies>
    </map>
```

Another Example:

```xml
    <map>
      <originmodule>
        <originname>Accounts</originname>
      </originmodule>
    <dependencies>
    <dependency>
        <field>accountname</field>
            <condition>
              [
            {"groupid":"1",
         "columnname":"vtiger_contacts:lastname:lastname:Contacts_Contact_Lastname:V",
         "comparator":"c",
         "value":"sel",
         "columncondition":"AND"},
     {"groupid":"1",
         "columnname":"vtiger_contacts:email:email:Contacts_Contact_Email:V",
         "comparator":"c",
         "value":"gmail",
         "columncondition":"OR"},
     {"groupid":"2",
         "columnname":"vtiger_contacts:firstname:firstname:Contacts_Contact_Firstname:V",
         "comparator":"e",
         "value":"albana",
         "columncondition":""}
    ]

            </condition>
        <actions>
            <change>
                <field>phone</field>
                <value>12345</value>
            </change>
            <change>
                <field>email1</field>
                <value>a@gmail.com</value>
            </change>
            <hide>
                <field>otherphone</field>
            </hide>
            <hide>
                <field>assigned_user_id</field>
            </hide>
            <readonly>
                <field>fax</field>
            </readonly>
            <readonly>
                <field>notify_owner</field>
            </readonly>
    <deloptions>
                <field>rating</field>
    <option>Acquired</option>
                <option>Active</option>
                <option>Shutdown</option>
     </deloptions>
            <collapse>
                <block>CustomerPortalInformation</block>
            </collapse>
        </actions>
    </dependency>
    <dependency>
        <field>accountname</field>
            <condition>
              [
        {"groupid":"1",
         "columnname":"vtiger_account:accountname:accountname:Accounts_Account_Name:V",
         "comparator":"c",
         "value":"corebos",
         "columncondition":""}
    ]
            </condition>
        <actions>
            <change>
                <field>phone</field>
                <value>54321</value>
            </change>
           <show>
                <block>assigned_user_id</block>
            </show>
            <setoptions>
                <field>rating</field>
                <option>Market Failed</option>
            </setoptions>
            <disappear>
                <block>AddressInformation</block>
            </disappear>
        </actions>
    </dependency>
    </dependencies>
    </map>
```

<div class="notices blue">
Change tax percentage when picklist with tax type changes
</div>

```xml
    <map>
      <originmodule>  <originname>Invoice</originname> </originmodule>
    <dependencies>
    <dependency>
        <field>cf_879</field>
        <actions>
            <function>
                <field>cf_879</field>
                <name>changeTaxDetails</name>
                <parameters>
                </parameters>
            </function>
        </actions>
    </dependency>
    </dependencies>
    </map>
```

```js
function changeTaxDetails(change_field, action_field, new_value, old_value) {
    if (action_field == 'cf_879') {
        if (new_value != 'Guardias') {
            document.getElementsByName('tax2_group_percentage')[0].value = 0.00;
        } else {
            document.getElementsByName('tax2_group_percentage')[0].value = -6.00;
        }
        calcTotal();
    }
}
```

you can load the JS from a file in the footer with:

```js
BusinessActions::addLink(getTabid("Invoice"), 'FOOTERSCRIPT', 'corebosjshookinvoice', 'modules/Invoice/corebosjshookinvoice.js', '', 0, null, false);
```

<div class="notices blue">
Force execution of functions on the load of the edit screen.
</div>

NOTE: The application is constructed to not permit this so we have to use a trick to consciously force this.

```xml
    <map>
      <originmodule>
        <originname>CobroPago</originname>
      </originmodule>
    <dependencies>
    <dependency>
        <field>cyp_no</field>
        <actions>
            <function>
                <field>cyp_no</field>
                <name>doNothing</name>
                <parameters>
                  <parameter>this is a stub to force the next two functions to work. this is a conscious execution of functions on load</parameter>
                </parameters>
            </function>
            <function>
                <field>assigned_user_id</field>
                <name>fieldDep_AssignUser</name>
                <parameters>
                  <parameter>12</parameter>
                </parameters>
            </function>
            <function>
                <field>reports_to_id</field>
                <name>fieldDep_AssignUserSelect</name>
                <parameters>
                  <parameter>5</parameter>
                </parameters>
            </function>
        </actions>
    </dependency>
    </dependencies>
    </map>
```

<div class="notices blue">
example using the fieldDep_GetFieldSearch functionality. Here we want to map some fields in AssetDetails whose values will be copied from Assets using a reference field to make the search:
</div>

```xml
<map>
  <originmodule>
    <originname>AssetDetails</originname> {the target module}
  </originmodule>
<dependencies>
  <dependency>
    <field>related_assets</field>  {reference field, so filling this field we will trigger the search for the other ones}
    <actions>
        <function>
            <name>fieldDep_GetFieldSearch</name>
            <parameters>
              <parameter>Assets</parameter>  {the module where we take the desired fields}
              <parameter>related_assets_sc,account</parameter> {fields we want to take the value from, in this case Assets}   
              <parameter>id</parameter> 
              <parameter>new value</parameter>   {default parameter; to set new values to the fields}
              <parameter>e</parameter> {operator; in this case means: equal}
              <parameter>related_ad_servicecontact,account_name</parameter> {fields where we will copy the values,in this case AssetDetils; the fields must be separated by coma in respective order with the above fields from Assets}
            </parameters>
        </function>
    </actions>
  </dependency>
  <dependency>
    <field>related_productcomponent</field>
    <actions>
        <function>
            <name>fieldDep_GetFieldSearch</name>
            <parameters>
              <parameter>ProductComponent</parameter> 
              <parameter>maintenance_buyingprice,maintenance_sellingprice</parameter>      
              <parameter>id</parameter>
              <parameter>new value</parameter>   
              <parameter>e</parameter>
              <parameter>vendor_maintenance_purchasevalue,customer_maintenance_salesvalue</parameter>
            </parameters>
        </function>
    </actions>
  </dependency>
</dependencies>
</map>
```

You can add as many dependencies to copy-paste field values from different modules. As you see above we have used two `<dependency>` tags in order to take values from **Assets** when we fill the `related_assets` and to take from **ProductComponent** filling the `related_productcomponent` between `<field>` tags.

### Example of conditions on read-only fields

When we set a field to display type 2 or 4, that field will not be present in the edit view of the record because they are fields that will be automatically filled in the background when saved. This is a problem for Field Dependencies because these happen completely in the browser. The change and the evaluation of the conditions are done in the browser when editing, where the read-only value is not present. If we need to add a dependency with a condition based on a read-only value we have to get the value into the browser. To achieve that we have to add an `EDITVIEWHTML` business action with this structure:

`<input type="hidden" id="cf_1329" name="cf_1329" value="{$FIELDS['cf_1329']}">`

This will add the input with the read-only field value to the browser where the field dependency code can read it and evaluate the conditions.

### Mode functionality

Both the `<dependency>` and the `<action>` directives accept an optional directive named `<mode>`. If given, this directive indicates if the dependency/action will be applied or not depending on the current mode of the record.

Valid mode values are:

- 'create', '1': only applied in create view
- 'edit', '2': only applied in edit view
- 'detail', '3': only applied in detail view
- a CSV string with the values above
- anything else which will be evaluated to ALL modes

### Include maps functionality

This type of map tends to get very complicated, with a lot of different options and conditions. It can also happen that we may have different variations of the map for the same module depending on the `mode`.

To help manage this complexity, the field dependency map permits including sections from other records.

The `<dependencies>`, the `<dependency>`, and the `<action>` directives can be imported from another Business map record.

**Invoice_FieldDependency Business Map**

```xml
<map>
  <originmodule>  <originname>Invoice</originname> </originmodule>
<dependencies>
<dependency>
<loadfrom>InvoiceDependency</loadfrom>
</dependency>
</dependencies>
</map>
```

**InvoiceDependency Business Map**

```xml
<dependency>
<field>invoicedate</field>
    <actions>
<loadfrom>InvoiceActions</loadfrom>
    </actions>
</dependency>
```

**InvoiceActions Business Map**

```xml
<action>
  <function>
    <field>duedate</field>
    <name>fieldDep_AddDays</name>
    <parameters>
        <parameter>30</parameter>
    </parameters>
  </function>
</action>
```

```xml
<map>
  <originmodule>
    <originname>LandlordInfo</originname>
  </originmodule>
  <dependencies>
    <loadfrom>Test</loadfrom>
  </dependencies>
</map>
```

### fieldDep\_doJS

`fieldDep_doJS` is a powerful function that basically executes any javascript code inside of the application. The structure of the map is as below, where `return '{{$committente}}' + '{{$insp_type}}'` is the javascript code that is going to be executed:

```xml
<dependency>
  <field>committente</field>
  <actions>
    <function>
      <field>accountname</field>
      <name>fieldDep_doJS</name>
      <parameters>
        <parameter>return '{{$firstname}}' + '{{$lastname}}'</parameter>
      </parameters>
    </function>
  </actions>
</dependency>
```

- `{{$fieldname}}` is a field in the application (Detailview/Editview) that you want to get the value of
- keyword `return` is a ''must'' for every code that you have to add it represents the value the Field Dependency will use to update the target field
- make sure to validate all datatypes when you create a new code for using it (this can break your code). this is powerful and dangerous
- **NOTE: DO NOT USE NEWLINES.** add all the code inline `<parameter>you code here without new lines</parameters>`

#### Some examples that you can use

- concat
```js
return '{{$firstname}}' + '{{$lastname}}'
```
- date (today)
```js
return new Date().toJSON().slice(0, 10);
```
- date (+30 days)
```js
const inputDate = '{{$datarichiestaintegrinsp}}';const parts = inputDate.split('-');const formattedDate = `${parts[2]}-${parts[1]}-${parts[0]}`;const givenDate = new Date(formattedDate);givenDate.setDate(givenDate.getDate() + 30); return givenDate.toISOString().slice(0, 10);
```

------------------------------------------------------------------------

[Next](../26.validations) | Chapter 14: Validations.

------------------------------------------------------------------------