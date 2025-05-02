---
title: 'Condition Expression Business Mapping'
metadata:
    description: 'evaluate an expression in the context of the application and get the result to decide subsequent actions'
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
        - condition
        - expression
---

The Condition Expression Business Mapping allows us to evaluate expressions and obtain results to make informed decisions for subsequent actions. It supports two formats: direct expressions from the workflow expression engine and function expressions that can be called from within the system. Furthermore, if applicable, the function parameters will be dynamically changed to match the current record values.

===

To illustrate the versatility of Condition Expression Business Mapping, let's examine a few examples:

Example 1:

```XML
<map>
  <expression>uppercase('this string')</expression>
</map>
```

In this example, the mapping evaluates the expression `uppercase('this string')`, which converts the provided string to uppercase. The result of this expression can be utilized for various purposes, such as data formatting, consistency, or further processing.

Example 2:

```XML
<map>
  <expression>accountname</expression>
</map>
```

Here, the mapping evaluates the expression `accountname`, which directly refers to a field in the current record. The result will be the value stored in the `accountname` field of the corresponding record. This approach allows for dynamic retrieval of field values based on the record context.

Example 3:

```XML
<map>
  <expression>employees + 10</expression>
</map>
```

In this case, the mapping evaluates the expression `employees + 10`, where `employees` represents a field in the current record. By adding 10 to the value of the `employees` field, the mapping enables dynamic calculation or modification of field values based on specific conditions or requirements.

Example 4:

```XML
<map>
  <expression>if employees > 10 then 'true' else 'false' end</expression>
</map>
```

Here, the mapping utilizes a conditional expression to evaluate whether the value of the `employees` field is greater than 10. If the condition is true, the result will be the string `'true'`; otherwise, it will be `'false'`. This kind of mapping enables decision-making and subsequent actions based on specific conditions within the application.

Example 5:

```XML
<map>
  <function>
   <name>isPermitted</name>
   <parameters>
     <parameter>Accounts</parameter>
     <parameter>CreateView</parameter>
     <parameter>record_id</parameter>
   </parameters>
  </function>
</map>
```

In this example, the mapping employs a function expression called `isPermitted` to check if a user has permission to perform a specific action. The function takes three parameters: `Accounts` (representing the module), `CreateView` (representing the action), and `record_id` (representing the specific record). The values of these parameters will be dynamically changed to match the current record's values during execution. Consequently, the mapping allows for permission-based access control and enforcement.

The `isPermitted` mapping above will be converted into:

```php
isPermitted('Accounts', 'CreateView', '74');
```

This transformation enables the execution of the function `isPermitted` with the provided arguments, thus checking the permission for the given module, action, and record ID.

Using this format of the map we have access to **all the functions** in the application.

By utilizing Condition Expression Business Mapping, you can perform dynamic evaluations, calculations, and decision-making within the application's context. The examples presented demonstrate its flexibility and applicability across various scenarios, empowering you to create intelligent workflows, automate processes, and make data-driven decisions.

## Additional Information

* [Forum thread](http://discussions.corebos.org/thread-642.html)


<br>
------------------------------------------------------------------------

[Next](../18.mapping ) | Chapter 3: (Field) Mapping.

------------------------------------------------------------------------