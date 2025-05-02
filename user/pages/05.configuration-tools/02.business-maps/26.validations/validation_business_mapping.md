---
title: 'Validation Business Mapping'
metadata:
    description: 'Add different types of validations on the fields of a module.'
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
        - validations
---

The coreBOS Validation Business Mapping allows you to define custom validation rules for fields within the coreBOS CRM system. It enables you to specify conditions that must be met for a field's value to be considered valid, ensuring data integrity and enforcing business rules.

===

The mapping structure follows this format:

```xml
<map>
  <originmodule>
    <originname>Module_Name</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>Field_Name</fieldname>   {field to validate}
      <validations>  {if more than one is present they must all pass to accept the value}
        <validation>
          <rule>{rule_name}</rule>
          <restrictions>
          <restriction>{values depend on the rule}</restriction>
          </restrictions>
          <message>This is my custom msg for field: {field}</message>  {optional}
        </validation>
        ...
      </validations>
    </field>
    <field>
     ...
    </field>
  </fields>
</map>
```

Let's break down the structure:

- `<map>`: The root element that encapsulates the entire mapping.
- `<originmodule>`: Specifies the module where the validation rules originate.
- `<originname>`: Specifies the name of the module for which validation rules are being defined.
- `<fields>`: Contains the list of field validations within the module.
- `<field>`: Represents a specific field validation rule.
- `<fieldname>`: Specifies the name of the field for which the validation rule is being defined.
- `<validations>`: Contains the set of validations to apply on the field. If more than one is given they must all pass.
- `<validation>`: Defines a specific evaluation for the validation rule.
- `<message>`: Specifies the error message to display when the validation rule is violated.

Within the `<validations>` element, you can define one or more `<validation>` elements that specify the conditions for the validation rule. These conditions can include various comparisons, logical operators, and values.

The `<message>` element allows you to provide a custom error message that will be displayed when the validation rule is violated. This message can provide useful information to the user regarding the validation failure.

By using the coreBOS Validation Business Mapping, you can implement complex validation logic, such as checking for valid date ranges, enforcing unique values, validating input formats, and more. These validation rules help maintain data quality and consistency within the coreBOS CRM system and ensure that the entered data adheres to your organization's specific business requirements.

The supported set of validation rules ({rule_name}) can be:

* required - Required field
  * restrictions: none
* equals - Field must match another field (email/password confirmation)
  * restrictions: name of the other field
* different - Field must be different than another field
  * restrictions: name of the other field
* accepted - Checkbox or Radio must be accepted (yes, on, 1, true)
  * restrictions: none
* numeric - Must be numeric
  * restrictions: none
* integer - Must be integer number
  * restrictions: none
* array - Must be an array
  * restrictions: none
* length - String must be a certain length
  * restrictions: number
* lengthBetween - String must be between given lengths
  * restrictions: two restrictions of type number
* lengthMin - String must be greater than given length
  * restrictions: number
* lengthMax - String must be less than given length
  * restrictions: number
* min - Minimum
* greater - Minimum
* bigger - Minimum
  * restrictions: number
* max - Maximum
* smaller - Minimum
* lesser - Minimum
  * restrictions: number
* in - Performs in_array check on given array values
  * restrictions: list of values of the array
* notIn - Negation of in rule (not in the array of values)
  * restrictions: list of values of the array
* ip - Valid IP address
  * restrictions: IP number
* email - Valid email address
  * restrictions: none
* url - Valid URL
  * restrictions: none
* urlActive - Valid URL with active DNS record
  * restrictions: none
* alpha - Alphabetic characters only
  * restrictions: none
* alphaNum - Alphabetic and numeric characters only
  * restrictions: none
* slug - URL slug characters (a-z, 0-9, -, _)
  * restrictions: none
* regex - Field matches a given regex pattern
  * restrictions: regular expression. be careful you may have to put this inside a CDATA
* date - Field is a valid date
  * restrictions: none
* dateFormat - Field is a valid date in the given format
  * restrictions: date format
* dateBefore - Field is a valid date and is before the given date
  * restrictions: date in ISO format
* dateAfter - Field is a valid date and is after the given date
  * restrictions: date in ISO format
* dateEqualOrAfter - Field is a valid date and is equal or after the given date
  * restrictions: date in ISO format
* contains - Field is a string and contains the given string
  * restrictions: string
* creditCard - Field is a valid credit card number
  * restrictions: list of accepted credit cards, if none given all supported cards will be checked
    * supported cards: Visa visa, Mastercard mastercard, Dinersclub dinersclub, American Express amex or Discover discover
* requiredWith -  Field is required if any other fields are present
  * restrictions: list of fields
* requiredWithout - Field is required if any other fields are NOT present
  * restrictions: list of fields
* listcontains - Validate a field is contained within a list of values
* arrayhaskeys
* IBAN_BankAccount - validate IBAN Bank Account number
  * restrictions: none
* EU_VAT - validate EU VAT number: the EU VAT validation checks if the VAT no. is in use, which implicitly  checks the format
  * restrictions: none
* notDuplicate - checks that no other record with the same value exists on the given field name
  * restrictions: list of [other fields you want to combine](https://discussions.corebos.org/showthread.php?tid=1934&pid=8265#pid8265) with the main field to search all at once
* expression - accept a workflow expression map and evaluate it in the context of the new screen values
  * restrictions: map name or id
* validateRelatedModuleExists
  * retriction: related module name
* custom - launch custom function that can be found in the indicated file
  * restrictions: filename, validation test name, function name and label to show on error (will be translated)
  * parameters: parameters can be passed to custom functions using the parameters-parameter directives 

!!! The parameters directive permits us to send values to our custom validation method with a structure like this:
!!! 
!!! ```xml
!!! <parameters>
!!!   <parameter>
!!!     <name>name of variable</name>
!!!     <value>value of variable</value>
!!!   </parameter>
!!! </parameters>
!!! ```
!!! 
!!! these parameters will be sent as a name indexed array to the function

### Validation Message

All of the rules above accept an optional directive named `message` where you can set the error message you want the user to see when an error on that field happens. If this is not defined, a standard error message will be returned. Inside this custom message you can use the curly brace `field` tag to indicate where you want the field name to appear:

```xml
<message>This is my custom msg for field: {field}</message>
```

We also support asking the user for confirmation by prefixing the message with the special string `%%%CONFIRM%%%`. This will produce a screen that will ask for confirmation using the text following the CONFIRM prefix.

```xml
<message>%%%CONFIRM%%%This is my custom msg for field: {field}</message>
```

If the user clicks on the accept button the save will proceed as normal if all the other validations pass. If the user presses on the cancel button he will stay in the edit screen where he can change whatever he wants before saving again.

Besides this option, which covers almost all the use cases, we have run into an edge case where we needed the message to be dynamically set. The problem with this is that the way the valitron library works we need to give it all the rules and messages before we start but in this case, we didn't know the message until the validation was launched. So we added support for defining the message before validating the rule for custom functions.

To retrieve the message to be used, the validation map will look for a function with the same name as custom function concatenated with the string "GetMessage". So, if we have a custom rule named "validateFlowStep" and we define another function named "validateFlowStepGetMessage", then the validation map will execute this second function giving it the same parameters as the validation function plus the current validation message. This way your custom validation function can determine which message to return. This is almost like launching the validation twice, so it comes at a price.

You can see an example of this in the [BPM Process Flow Perspective](https://github.com/coreBOS/ProcessFlowPerspective). Look in
the Process Flow module for the validateFlowStep script.

### Activating the validation maps

The trigger for these maps is:

- they must be of type "Validations"
- the "Target Module" must be set correctly
- the name MUST end with "_Validations"

If more than one record is found, they will ALL be applied.

So, as with most business maps, what activates the map is the name, but
as a difference with other maps this type of map can have more than one
and they will all be merged and applied.

This type of map also supports the Global Variable configuration as all
the other business maps. In this case, the global variables will all be
obtained and evaluated, so you can have more than one global variable
and they will ALL be added to the Business Maps that are found by name.

The idea is that we can have global validations for all users using the
business map trigger name (ending with "_Validations") and then define
other business maps with any other name and activate these per-user or
role using the global variable "**BusinessMappings_Validations**". This
global variable MUST have the correct module selected (only one).

### Accessing other fields in the form

You can **use the values of other fields on the form** by putting the
field name inside two curly brackets. For example, the next map will
validate that the field dtstart is before the value in field dtend.

```xml
<map>
  <originmodule>
    <originname>cbCalendar</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>dtend</fieldname>
      <validations>
        <validation>
          <rule>dateAfter</rule>
          <restrictions>
          <restriction>{{dtstart}}</restriction>
          </restrictions>
        </validation>
      </validations>
    </field>
  </fields>
</map>
```

! There is an important limitation when using the values of other fields. These values will only be available when editing the whole record. If the user is doing inline individual field edit on the detail view, the value of the other fields will not be available. To overcome this limitation, you need to create a custom validation rule and access the values you need from the database.

### Other information available during validation

In order to enhance the set of possible validations that can be done, the validation system automatically adds some values that you can use freely.

### Current values

When editing a record it is possible to want to compare the value
introduced by the user with the value that is currently saved in that
same field or some other field with which it may have some dependency.

In this case you can access these values prefixing the string
"current_" to the variable name. For example, let's suppose that we are
editing an Account, the user has changed the Industry picklist value and
we want to check what the currently saved value is before accepting the
change. Let's imagine a rule that says:

!!! Any account who's industry is set to Banking, cannot be changed 

In this case, we can easily access the value that the user has selected
by putting the industry field and to access the value saved in the
application we would use: current_industry, something like this:

```xml
<map>
  <originmodule>
    <originname>Accounts</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>current_industry</fieldname>
      <validations>
        <validation>
          <rule>notIn</rule>
          <restrictions>
          <restriction>Banking</restriction>
          </restrictions>
        </validation>
      </validations>
    </field>
  </fields>
</map>
```

### Product lines

In inventory modules, the system will load all the information of the lines into the **pdoInformation** array which will look something like this:

```php
pdoInformation => array(
 array(
  'crmid' = {first line product/service ID},
  'qty' = {first line quantity (units)},
  'name' = {first line product/service name},
  'type' = {first line product/service type},
 ),
 ... all product/service lines ..
```

### Accessing via web service

Validation maps have their own web service end-point: **ValidateInformation**

Also, we have **CreateWithValidation**, **UpdateWithValidation**, and **ReviseWithValidation**

### Some other examples

Another example of how to limit the accepted values in a picklist, even making it mandatory if needed.

```xml
<map>
  <originmodule>
    <originname>cbCalendar</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>activitytype</fieldname>
      <validations>
        <validation>
          <rule>notIn</rule>
          <restrictions>
          <restriction>Call</restriction>
          <restriction>Meeting</restriction>
          </restrictions>
        </validation>
      </validations>
    </field>
  </fields>
</map>
```
This next example contains a REGEX expression that will not accept any
alphabetical letter in the accountname field and there must be at least
one character. Important things to notice in the REGEX expression are:

1. you must set the initial and end of line markers as the value is compared as a complete string
2. you may or may not need the CDATA depending on the regex (the one below does not need CDATA)
3. modifiers are not supported in the expression

```xml
<map>
  <originmodule>
    <originname>Accounts</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>accountname</fieldname>
      <validations>
        <validation>
          <rule>regex</rule>
          <restrictions>
          <restriction><![CDATA[/^[^A-Za-z]+$/]]></restriction>
          </restrictions>
        </validation>
      </validations>
    </field>
  </fields>
</map>
```

### Forum Post with a very advanced example of a custom validation

[Forum Post](https://discussions.corebos.org/showthread.php?tid=1017&pid=5472#pid5472)

!!! [Thanks Luke](https://github.com/Luke1982)

### Custom Validations

coreBOS has some custom validations that are not loaded by default but can be used if necessary:

- Brazilian ID Number: file include/validation/validateCPFCNPJ.php
 - validaCPF
 - validaCNPJ
 - validaCNPJ2
- Spanish ID Number: file include/validation/validatorESIDNumber.php
 - isValidDNI
 - isValidNIE
 - isValidNIF
 - isValidCIF
 - isValidPersonalESID = isValidDNI or isValidNIE or isValidNIF
 - isValidESID = isValidPersonalESID or isValidCIF
- Italian ID Number: file include/validation/validatePIVA.php
 - checkAccountPIVA

For example, a validation for a valid CIF on account siccode field looks like this:

```xml
<map>
  <originmodule>
    <originname>Accounts</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>siccode</fieldname>
      <validations>
        <validation>
          <rule>custom</rule>
          <restrictions>
          <restriction>include/validation/validatorESIDNumber.php</restriction>
          <restriction>isValidCIF</restriction>
          <restriction>isValidCIF</restriction>
          </restrictions>
        </validation>
      </validations>
    </field>
  </fields>
</map>
```

### Test Validation Business Mapping

These are the two validation maps I used while developing the integration of the mapping in the save process:

```xml
<map>
  <originmodule>
    <originname>Accounts</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>accountname</fieldname>
      <validations>
        <validation>
          <rule>required</rule>
        </validation>
        <validation>
          <rule>contains</rule>
          <restrictions>
          <restriction>mex</restriction>
          </restrictions>
        </validation>
      </validations>
    </field>
    <field>
      <fieldname>industry</fieldname>
      <validations>
        <validation>
          <rule>notDuplicate</rule>
        </validation>
      </validations>
    </field>
  </fields>
</map>
```

```xml
<map>
  <originmodule>
    <originname>Accounts</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>email1</fieldname>
      <validations>
        <validation>
          <rule>custom</rule>
          <restrictions>
          <restriction>modules/cbMap/Validation.php</restriction>
          <restriction>testemail</restriction>
          <restriction>validate_testacccemail</restriction>
          </restrictions>
        </validation>
      </validations>
    </field>
  </fields>
</map>
```

both are set for the Accounts module.

This is the custom validation script:

```js
function validate_testacccemail($field) {
  global $log;$log->fatal('validation for'.$field);
  return true;
}
```

### Expression Map

```xml
<map>
  <originmodule>
    <originname>Accounts</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>employees</fieldname>
      <validations>
        <validation>
          <rule>expression</rule>
          <restrictions>
          <restriction>AccountsEmployees_ConditionExpression</restriction>
          </restrictions>
        </validation>
      </validations>
    </field>
  </fields>
</map>
```

```xml
<map>
  <expression>if employees > 10 then 1 else 0 end</expression>
</map>
```

### Custom Message Test Map

```xml
<map>
  <originmodule>
    <originname>Accounts</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>industry</fieldname>
      <validations>
        <validation>
          <rule>notIn</rule>
          <restrictions>
          <restriction>Banking</restriction>
          </restrictions>
          <message>This is my custom msg for field: {field}</message>
        </validation>
        <validation>
          <rule>notIn</rule>
          <restrictions>
          <restriction>Energy</restriction>
          </restrictions>
          <message>Energy not supportted for: {field}</message>
        </validation>
        <validation>
          <rule>notIn</rule>
          <restrictions>
          <restriction>Apparel</restriction>
          </restrictions>
        </validation>
      </validations>
    </field>
  </fields>
</map>
```

<br>
------------------------------------------------------------------------

[Next](../24.relatedpanes) | Chapter 15: Related Panes.

------------------------------------------------------------------------