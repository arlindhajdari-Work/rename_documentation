---
title: 'Decision Table Mapping'
metadata:
    description: 'This map defines a set of rules that must be evaluated to make a decision.'
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
        - decisiontable
---

The coreBOS Decision Table Mapping is a powerful feature that allows you to define complex business rules and automate decision-making processes within the coreBOS application. The mapping provides a structured and configurable way to define conditions, actions, and outcomes based on specific criteria.

===

The general idea comes from the Decision Model and Notation (DMN)
structure used in BPM but very adapted to the specific coreBOS
environment and infrastructure.

You can find a few useful links about DMN here:

-   [DMN Tutorial](https://camunda.com/dmn/)
-   [DMN Tutorial PDF](http://corebos.com/documentation/lib/exe/fetch.php?media=en:adminmanual:businessmappings:dmn_tutorial_-_dmn_1.1_tutorial_for_beginners_-_learn_dmn_camunda_bpm.pdf)
-   [Decision Table
    Reference](https://docs.camunda.org/manual/latest/reference/dmn11/decision-table/)
-   [Decision Table Constructor](http://corebos.com/documentation/lib/exe/fetch.php?media=en:adminmanual:businessmappings:dmndecisiontablereference.pdf)
-   [Decision Table
    Constructor](https://github.com/steffenbrand/dmn-decision-tables)
-   <https://www.omg.org/spec/DMN/>

By defining decision rules using the Decision Table Mapping, you can automate various processes within coreBOS based on specific conditions. For example, you can define rules to automatically update field values, assign records to specific users, trigger notifications, or perform custom actions.

The flexibility of the Decision Table Mapping allows you to create complex decision-making logic with multiple conditions, actions, and outcomes. This feature empowers you to streamline and automate your business processes, reducing manual intervention and ensuring consistent and efficient decision-making within the coreBOS application.

Decision Table Map Format
=========================

The accepted format for this map is basically a set of rules which can be of three types:

- Expressions
- [Condition Expression](../03.condition-expression) or [Condition Query](../04.condition-query) business map names/IDs
- Decision Tables

Expressions
-----------

Expressions contain any workflow expression that can be evaluated in the
context of the Decision Map. These are exactly like [Condition Expression](../03.condition-expression) maps
but written directly inside this business map.

<div class="notices blue">
Since an expression can return any type of value, in order to know if an expression has failed it must return the reserved string <strong>__DoesNotPass__</strong>
</div>

Business Map Name/ID
--------------------

This type is simply the name or CRMID of any existing [Condition Expression](../03.condition-expression) or [Condition Query](../04.condition-query) business map, they will be loaded and evaluated in the context of the Decision Map

<div class="notices blue">
Since an expression can return any type of value, in order to know if an expression has failed it must return the reserved string <strong>__DoesNotPass__</strong>
</div>

Decision Tables
---------------

This type expects to have the values to search on inside a coreBOS module.

We will be able to define the conditions to filter the records in the module and then a set of search conditions to look for records.

Full Map Structure
------------------

```xml
<decision>
  <hitPolicy></hitPolicy>  <!-- U F C A R G -->
  <aggregate></aggregate>  <!-- only available if hitPolicy=G: sum,min,max,count -->
  <rules>
    <rule>
      <sequence></sequence>
      <expression></expression>
      <output></output>  <!-- ExpressionResult, FieldValue, crmObject, Row -->
    </rule>
    <rule>
      <sequence></sequence>
      <mapid></mapid>
      <output></output>  <!-- ExpressionResult, FieldValue, crmObject, Row -->
    </rule>
    <rule>
      <sequence></sequence>
      <decisionTable>
        <module></module>
        <conditions>  <!-- QueryGenerator conditions -->
            <condition>
              <input></input>  <!-- context variable name -->
              <operation></operation>  <!-- QueryGenerator operators -->
              <field></field>  <!-- fieldname of module -->
            </condition>
        </conditions>
        <orderby></orderby>  <!-- column to order the records by -->
        <searches>
          <search>
            <condition>
              <input></input>  <!-- context variable name -->
              <preprocess></preprocess>  <!-- optional: if present, the result of the expression it contains will be used as the input -->
              <operation></operation>  <!-- QueryGenerator operators -->
              <field></field>  <!-- fieldname of module -->
            </condition>
          </search>
        </searches>
        <output></output>  <!-- fieldname or fieldnames separated by commas or star (*) for all fields -->
      </decisionTable>
      <output></output>  <!-- ExpressionResult, FieldValue, crmObject, Row -->
    </rule>
  </rules>
</decision>
```

<div class="notices blue">
To make this type of map easier to construct when we have a large number of input variables, the input variables accept the special value <strong>__IGNORE__</strong>. When an input variable is set to this value the whole search on that column will be ignored. This permits us to establish rules that are more generic reducing the repetition of very similar rules. 
</div>

Hit Policy
----------

- **U**nique: Only a single rule can be satisfied. The decision table result contains the output entries of the satisfied rule. If more than one rule is satisfied, the Unique hit policy is violated.
- **F**irst: Multiple rules can be satisfied. The decision table result contains only the output of the first satisfied rule.
- **C**ollect: Multiple rules can be satisfied. The decision table result contains the output of all satisfied rules in an arbitrary order as a list.
- **A**ny: Multiple rules can be satisfied. However, all satisfied rules must generate the same output. The decision table result contains only the output of one of the satisfied rules. If multiple rules are satisfied which generate different outputs, the hit policy is violated.
- **R**uleOrder: Multiple rules can be satisfied. The decision table result contains the output of all satisfied rules in the order of the rules in the decision table.
- a**G**gregate:
  - The SUM aggregator sums up all outputs from the satisfied rules.
  - The MIN aggregator can be used to return the smallest output value of all satisfied rules.
  - The MAX aggregator can be used to return the largest output value of all satisfied rules.
  - The COUNT aggregator can be used to return the count of satisfied rules.

[Read the DMN Hit Policy reference](https://docs.camunda.org/manual/latest/reference/dmn/decision-table/hit-policy/)

Output Options
--------------

- **ExpressionResult:** whatever the expression returns will be returned
- **FieldValue:** we understand that the expression returns a field name which we will evaluate in the given context
- **crmObject:** we understand that the expression returns a CRM ID so we instantiate the module and return the fully-loaded object
- **Row:** will return the full row of fields indicated in the "output" directive

Execution
=========

To execute a decision map and get the result we use the [coreBOS Rules service](../../../10.developer-guide/04.development_framework/11.develtutorials/26.corebos_rules). coreBOS Rule will see that the given map is actually a decision table and will evaluate the map with the given context.

`$result = coreBOS_Rule::evaluate(put your decision map ID or name here, $context);`

Web service execution
---------------------

You can evaluate Decision Maps via the web service endpoint: **cbRule**
```php
  $context = array(
      'guestcount' => '4',
      'season' => 'Winter',
  );
  $context = json_encode($context);
  $mapid = 'SeasonDish twocolumns';

  //sessionId is obtained from loginResult.
  $params = "sessionName=$cbSessionID";
  $params.= "&operation=cbRule";
  $params.= "&conditionid=".urlencode($mapid);
  $params.= "&context=".urlencode($context);

  //Retrieve must be GET Request.
  $response = $httpc->fetch_url("$cbURL?$params");
  $dmsg.= debugmsg("Raw response (json)", $response);

  //decode the json encode response from the server.
  $jsonResponse = json_decode($response, true);
  $dmsg.= debugmsg("Webservice response", $jsonResponse);

  //operation was successful get the token from the response.
  if($jsonResponse['success']==false) {
      $dmsg.= debugmsg('failed:'.$jsonResponse['error']['message']);
      echo 'rule failed!';
  } else {
      echo $jsonResponse['result'];
  }
```

Examples
========

Select Dish with Expressions
----------------------------

![](dish-feel.png?width=100%)

```xml
<decision>
  <hitPolicy>U</hitPolicy>
  <rules>
    <rule>
      <sequence>1</sequence>
      <expression><![CDATA[if AND('$[season]'=='Fall', $[guestcount]<=8) then 'Spareribs' else '__DoesNotPass__' end]]></expression>
      <output>ExpressionResult</output>
    </rule>
    <rule>
      <sequence>2</sequence>
      <expression><![CDATA[if AND('$[season]'=='Winter', $[guestcount]<=8) then 'Roastbeef' else '__DoesNotPass__' end]]></expression>
      <output>ExpressionResult</output>
    </rule>
    <rule>
      <sequence>3</sequence>
      <expression><![CDATA[if AND('$[season]'=='Spring', $[guestcount]<=4) then 'Dry Aged Gourmet Steak' else '__DoesNotPass__' end]]></expression>
      <output>ExpressionResult</output>
    </rule>
    <rule>
      <sequence>4</sequence>
      <expression><![CDATA[if AND('$[season]'=='Spring', AND($[guestcount]>=5, $[guestCount]<=8)) then 'Steak' else '__DoesNotPass__' end]]></expression>
      <output>ExpressionResult</output>
    </rule>
    <rule>
      <sequence>5</sequence>
      <expression><![CDATA[if AND(OR('$[season]'=='Fall', OR('$[season]'=='Winter', '$[season]'=='Spring')), $[guestcount]>8) then 'Stew' else '__DoesNotPass__' end]]></expression>
      <output>ExpressionResult</output>
    </rule>
    <rule>
      <sequence>6</sequence>
      <expression><![CDATA[if '$[season]'=='Summer' then 'Light Salad and a nice Steak' else '__DoesNotPass__' end]]></expression>
      <output>ExpressionResult</output>
    </rule>
  </rules>
</decision>
```

Select Dish with Module
-----------------------

![](tag_task.png?width=100%)

Let's suppose we have a module called DecisionConditions with these fields:

- sequence
- season
- guestcountmin
- guestcountmax
- desireddish

and these records

<table class="table table-striped">
<thead>
<tr class="header">
<th>sequence</th>
<th>season</th>
<th>guestcountmin</th>
<th>guestcountmax</th>
<th>desireddish</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Fall</td>
<td>0</td>
<td>8</td>
<td>Spareribs</td>
</tr>
<tr class="even">
<td>2</td>
<td>Winter</td>
<td>0</td>
<td>8</td>
<td>Roastbeef</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Spring</td>
<td>0</td>
<td>4</td>
<td>Dry Aged Gourmet Steak</td>
</tr>
<tr class="even">
<td>4</td>
<td>Spring</td>
<td>5</td>
<td>8</td>
<td>Steak</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Fall</td>
<td>9</td>
<td>10000</td>
<td>Stew</td>
</tr>
<tr class="even">
<td>6</td>
<td>Winter</td>
<td>9</td>
<td>10000</td>
<td>Stew</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Spring</td>
<td>9</td>
<td>10000</td>
<td>Stew</td>
</tr>
<tr class="even">
<td>8</td>
<td>Summer</td>
<td>0</td>
<td>10000</td>
<td>Light Salad and a nice Steak</td>
</tr>
</tbody>
</table>

<br>

```xml
<decision>
  <hitPolicy>U</hitPolicy>
  <rules>
    <rule>
      <sequence>1</sequence>
      <decisionTable>
        <module>DecisionConditions</module>
        <orderby>sequence</orderby>  <!-- column to order the records by -->
        <searches>
          <search>
            <condition>
              <input>season</input>  <!-- context variable name -->
              <operation>e</operation>  <!-- QueryGenerator operators -->
              <field>season</field>  <!-- fieldname of module -->
            </condition>
            <condition>
              <input>guestcount</input>  <!-- context variable name -->
              <operation>ge</operation>  <!-- QueryGenerator operators -->
              <field>guestcountmin</field>  <!-- fieldname of module -->
            </condition>
            <condition>
              <input>guestcount</input>  <!-- context variable name -->
              <operation>le</operation>  <!-- QueryGenerator operators -->
              <field>guestcountmax</field>  <!-- fieldname of module -->
            </condition>
          </search>
        </searches>
        <output>desireddish</output>  <!-- fieldname -->
      </decisionTable>
      <output>FieldValue</output>
    </rule>
  </rules>
</decision>
```

In the example above I decided to add two columns for the Guest Count, in order to convert the range \[5..8\] into two records. In this mindset, I also use the value 10000 as an "infinite" value.

But the truth is that as the implementor of both the decision table map and module I have full control of how I want my users to define the conditions. Let's suppose that I want the users of the module to be able to define the condition with only one column for guest count like is reflected in the image. In this case, I would have implemented a module with these fields:

- sequence
- season
- guestcount
- desireddish

these records
<table class="table table-striped">
<thead>
<tr class="header">
<th>sequence</th>
<th>season</th>
<th>guestcount</th>
<th>desireddish</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Fall</td>
<td>8</td>
<td>Spareribs</td>
</tr>
<tr class="even">
<td>2</td>
<td>Fall</td>
<td>10000</td>
<td>Stew</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Spring</td>
<td>4</td>
<td>Dry Aged Gourmet Steak</td>
</tr>
<tr class="even">
<td>4</td>
<td>Spring</td>
<td>8</td>
<td>Steak</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Spring</td>
<td>10000</td>
<td>Stew</td>
</tr>
<tr class="even">
<td>5</td>
<td>Winter</td>
<td>8</td>
<td>Roastbeef</td>
</tr>
<tr class="odd">
<td>6</td>
<td>Winter</td>
<td>10000</td>
<td>Stew</td>
</tr>
<tr class="even">
<td>7</td>
<td>Summer</td>
<td>10000</td>
<td>Light Salad and a nice Steak</td>
</tr>
</tbody>
</table>

and this map

```xml
<decision>
  <hitPolicy>F</hitPolicy>
  <rules>
    <rule>
      <sequence>1</sequence>
      <decisionTable>
        <module>DecisionConditions</module>
        <orderby>sequence</orderby>  <!-- column to order the records by -->
        <searches>
          <search>
            <condition>
              <input>season</input>  <!-- context variable name -->
              <operation>e</operation>  <!-- QueryGenerator operators -->
              <field>season</field>  <!-- fieldname of module -->
            </condition>
            <condition>
              <input>guestcount</input>  <!-- context variable name -->
              <operation>le</operation>  <!-- QueryGenerator operators -->
              <field>guestcount</field>  <!-- fieldname of module -->
            </condition>
          </search>
        </searches>
        <output>desireddish</output>  <!-- fieldname -->
      </decisionTable>
      <output>FieldValue</output>
    </rule>
  </rules>
</decision>
```

In this case, I am playing with the **Hit Policy** which has changed to **F**irst, so now my users must understand that the ranges are defined from the previous value to the one defined in each record and that sequence is VERY important.

Since, in the end, the supported operations are those of the Query Generator, which even supports ranges:

    QueryGenerator->addConditions(column, operator, values) 

    where operator can be '[]', '[[', ']]', '][' among many others

the possibilities that the implementor has are very big.

IGNORE Reserved Word
--------------------

Finally, comment on a very important option where you can set the value
of any variable in the context to **\_\_IGNORE\_\_** to have that
variable eliminated from the decision. This permits us to create complex
rules with many variables where we search on only a few of them at a
time.

We can also use this special reserved word in the rules table itself to
create rules which cover many cases. For example, we could have a table
of rules like this:

<table class="table table-striped">
<thead>
<tr class="header">
<th>input1</th>
<th>input2</th>
<th>output</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>e1</td>
<td>c1</td>
<td>r1</td>
</tr>
<tr class="even">
<td>__IGNORE__</td>
<td>c2</td>
<td>r2</td>
</tr>
<tr class="odd">
<td>e3</td>
<td>c3</td>
<td>r3</td>
</tr>
</tbody>
</table>

With these rules in place, any decision that has input2==c2 will pass no
matter what value is passed in as input1. Note that this can easily
cause that more than one rule to pass. If we add a rule to the table
above, like this:

<table class="table table-striped">
<thead>
<tr class="header">
<th>input1</th>
<th>input2</th>
<th>output</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>e1</td>
<td>c1</td>
<td>r1</td>
</tr>
<tr class="even">
<td>__IGNORE__</td>
<td>c2</td>
<td>r2</td>
</tr>
<tr class="odd">
<td>e2</td>
<td>c2</td>
<td>r2b</td>
</tr>
<tr class="even">
<td>e3</td>
<td>c3</td>
<td>r3</td>
</tr>
</tbody>
</table>

and we pass in the values

1. input1=e2
2. input2=c2

**both r2 and r2b will pass** and be returned, so if we have a hit policy of Unique it will fail and if we have a hit policy of First then the sequence is of utmost importance to get the correct result.

Default Value
-------------

Using the \_\_IGNORE\_\_ reserved word we can implement a default value
for our rules. If we define a rule where all the input values are set to
\_\_IGNORE\_\_, this rule will pass for all input values. If we set the
hit policy of the decision map to First and order the rules in a way
that the all \_\_IGNORE\_\_ rule is always the last to be evaluated we
accomplish a decision table where any combination of input values that
is not explicitly defined will return the values in the all
\_\_IGNORE\_\_ rule instead of \_\_DoesNotPass\_\_

Preprocess Directive
--------------------

Following the new enhancements, we don't have to valorize context
variables on the Decision Table map using the Execute Expression
Workflow before evaluating the Decision table map. The map will be
evaluated on the context of the values that are present on the screen.

But there may be cases where we don’t want the context variable to hold
the entire value of the field. Here comes in play the preprocess
directive. The preprocess directive is optional. That being said, if it
is present it will send its value to the workflow expression system, get
back the result and use that result to search the Decision Table Module.
If you think about it the preprocess directive carries the work of the
Execute Expression workflow task. You don’t need to explicitly use the
workflow system because the preprocess directive will "call" it for you.

**Example:**

Let's change the logic we had in the last example above.

Remove all the records with the season of Spring and add this new rule
on the decision table module: *If the season is Spring then regardless
of how many guests there are I want the desired dish to be Beef*.

That would be a record like this in the decision table module.

<table class="table table-striped">
<thead>
<tr class="header">
<th>sequence</th>
<th>season</th>
<th>guestcount</th>
<th>desireddish</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Fall</td>
<td>8</td>
<td>Spareribs</td>
</tr>
<tr class="even">
<td>2</td>
<td>Fall</td>
<td>10000</td>
<td>Stew</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Spring</td>
<td>*</td>
<td>Beef</td>
</tr>
<tr class="even">
<td>5</td>
<td>Winter</td>
<td>8</td>
<td>Roastbeef</td>
</tr>
<tr class="odd">
<td>6</td>
<td>Winter</td>
<td>10000</td>
<td>Stew</td>
</tr>
<tr class="even">
<td>7</td>
<td>Summer</td>
<td>10000</td>
<td>Light Salad and a nice Steak</td>
</tr>
</tbody>
</table>

Lets see how that will look on our Decision Table map:

```xml
  <condition>
    <input>guestcount</input> <!-- context variable name -->
    <preprocess>if '$[season]' == 'Spring' then '*' else '$[guestcount]' end</preprocess>  <!-- if present sends the expression to the workflow expression system-->
    <operation>e</operation> <!-- QueryGenerator operators -->
    <field>guestcount</field> <!-- fieldname of module -->
  </condition>
```

As you can see we are using the preprocess directive. What is inside the
preprocess directive will be sent to the workflow system.

So if the season is Spring that valorizes the context variable with the
value \* and then searches the decision table module for a match. Now,
whenever the decision map gets evaluated on a record whose value of the
Season field is Spring it will consider the value of Guest Number as \*
and for our Decision Table module that means that the desired dish is
Beef.

Select Global Variable Escalation
---------------------------------

A decision map that would return the value of a global variable would
look something like the map below. The context would have to send in all
the role and group of the current user and I'm not totally sure if the
"module list" would work as it is below, but it will be VERY close and
enough for you to get an idea of how this map works.

```xml
<decision>
  <hitPolicy>F</hitPolicy>
  <rules>
    <rule>
      <sequence>1</sequence>
      <decisionTable>
        <module>GlobalVariable</module>
        <searches>
          <search> <!-- Mandatory GV -->
            <condition>
              <input>gvname</input>
              <operation>e</operation>
              <field>gvname</field>
            </condition>
            <condition>
              <input>checkboxtrue</input>  <!-- checkboxtrue == 1 in context -->
              <operation>e</operation>
              <field>mandatory</field>
            </condition>
          </search>
          <search> <!-- In module for user -->
            <condition>
              <input>gvname</input>
              <operation>e</operation>
              <field>gvname</field>
            </condition>
            <condition>
              <input>userid</input>
              <operation>e</operation>
              <field>assigned_user_id</field>
            </condition>
            <condition>
              <input>checkboxtrue</input>  <!-- checkboxtrue == 1 in context -->
              <operation>e</operation>
              <field>inmodulelist</field>
            </condition>
            <condition>
              <input>gvmodule</input>
              <operation>c</operation>
              <field>gvmodule</field>
            </condition>
          </search>
          <search> <!-- In module for group -->
            <condition>
              <input>gvname</input>
              <operation>e</operation>
              <field>gvname</field>
            </condition>
            <condition>
              <input>groupid</input>
              <operation>e</operation>
              <field>assigned_user_id</field>
            </condition>
            <condition>
              <input>checkboxtrue</input>  <!-- checkboxtrue == 1 in context -->
              <operation>e</operation>
              <field>inmodulelist</field>
            </condition>
            <condition>
              <input>gvmodule</input>
              <operation>c</operation>
              <field>gvmodule</field>
            </condition>
          </search>
          <search> <!-- In module for role -->
            <condition>
              <input>gvname</input>
              <operation>e</operation>
              <field>gvname</field>
            </condition>
            <condition>
              <input>userrole</input>
              <operation>c</operation>
              <field>gvrole</field>
            </condition>
            <condition>
              <input>checkboxtrue</input>  <!-- checkboxtrue == 1 in context -->
              <operation>e</operation>
              <field>inmodulelist</field>
            </condition>
            <condition>
              <input>gvmodule</input>
              <operation>c</operation>
              <field>gvmodule</field>
            </condition>
          </search>
          <search> <!-- without module for user -->
            <condition>
              <input>gvname</input>
              <operation>e</operation>
              <field>gvname</field>
            </condition>
            <condition>
              <input>userid</input>
              <operation>e</operation>
              <field>assigned_user_id</field>
            </condition>
            <condition>
              <input>checkboxfalse</input>  <!-- checkboxfalse == 0 in context -->
              <operation>e</operation>
              <field>inmodulelist</field>
            </condition>
          </search>
          <search> <!-- without module for group -->
            <condition>
              <input>gvname</input>
              <operation>e</operation>
              <field>gvname</field>
            </condition>
            <condition>
              <input>groupid</input>
              <operation>e</operation>
              <field>assigned_user_id</field>
            </condition>
            <condition>
              <input>checkboxfalse</input>  <!-- checkboxfalse == 1 in context -->
              <operation>e</operation>
              <field>inmodulelist</field>
            </condition>
          </search>
          <search> <!-- without module for role -->
            <condition>
              <input>gvname</input>
              <operation>e</operation>
              <field>gvname</field>
            </condition>
            <condition>
              <input>userrole</input>
              <operation>c</operation>
              <field>gvrole</field>
            </condition>
            <condition>
              <input>checkboxfalse</input>  <!-- checkboxfalse == 1 in context -->
              <operation>e</operation>
              <field>inmodulelist</field>
            </condition>
          </search>
          <search> <!-- Default GV -->
            <condition>
              <input>gvname</input>
              <operation>e</operation>
              <field>gvname</field>
            </condition>
            <condition>
              <input>checkboxtrue</input>  <!-- checkboxtrue == 1 in context -->
              <operation>e</operation>
              <field>default</field>
            </condition>
          </search>
        </searches>
        <output>value</output>  <!-- fieldname -->
      </decisionTable>
      <output>FieldValue</output>
    </rule>
  </rules>
</decision>
```

<br>
------------------------------------------------------------------------

[Next](../27.webservicecall) | Chapter 21: REST/SOAP call and retrieval.

------------------------------------------------------------------------