---
title: 'coreBOS Rules'
metadata:
    description: 'coreBOS Rules'
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
        - businessrule
    tag:
        - rule
        - decision
---

coreBOS Rules are a step towards [BPM](https://en.wikipedia.org/wiki/Business_process_management) automation using the workflow infrastructure.

===

A **rule** is a [Condition Query](../../../../05.configuration-tools/02.business-maps/04.condition-query), a [Condition Expression](../../../../05.configuration-tools/02.business-maps/03.condition-expression) or [Decision Table](../../../../05.configuration-tools/02.business-maps/06.decisiontable)
Business Map that is launched in the context of a CRM record.

In BPM, a rule is defined as a string expression, written in some grammar, that is evaluated using a given context.

Using this definition, in coreBOS, we use either an SQL query, a workflow expression or a Decision Table and evaluate it in the context of any record in the application.

This will return a result, whose value depends exclusively on the rule being launched.

Let's see some examples.

Let's suppose we have this Condition Expression map named "THISSTRING":

```xml
<map>
    <expression>uppercase('this string')</expression>
</map>
```

This expression does not depend on any context, it is a fixed value always (rather useless in real life), so we can call it in any context and always get the same result. Let's suppose that we have a valid ID for an account with CRMID = 74, our call would look like this:

```php
$result = coreBOS_Rule::evaluate('THISSTRING', 74);
// $result == 'THIS STRING'
```

The profile of the rule looks like this:

```php
$result = coreBOS_Rule::evaluate($conditionid, $context);
```

where:

- **$conditionid** is either the CRMID or the NAME of the business map. If it is a name, it will get passed through the global variable module following the "BusinessMap\_" prefix convention
- **$context** can be either:
  - the CRMID of the record that will be the context of the rule
  - an array with context variables that will be merged before the evaluation ([read more below](../26.corebos_rules/item.md#array-context))

Now let's suppose we change the expression map above to:

```xml
<map>
    <expression>accountname</expression>
</map>
```

When we evaluate this rule against different account contexts we will get different account names.

A condition query could be:

```xml
<map>
    <module>Accounts</module>
    <sql>select vtiger_account.accountid
    from vtiger_account
    inner join vtiger_crmentity on vtiger_crmentity.crmid=vtiger_account.accountid
    inner join vtiger_invoice on vtiger_invoice.accountid=vtiger_account.accountid
    inner join vtiger_crmentity as crminv on crminv.crmid=vtiger_invoice.invoiceid
    where vtiger_crmentity.deleted=0 and crminv.deleted=0 and vtiger_account.accountid=?
    </sql>
    <return>count</return>
</map>
```

and the rule call would be:

```php
$result = coreBOS_Rule::evaluate($conditionid, 74);
// $result == the number of invoice of account with crmid 74
```

In the end, the goal is to give the developer a tool to make decisions that are defined by the implementor. In this last example above we get the number of invoices any given account has. So we can apply a discount if this number is non-zero, or bigger than 10, for example. Now the implementor can decide to change the SQL and count only paid invoices or invoices in the last 6 months.

Finally, since rules are based on business maps, and these on the existing workflow expression system all enhancements we make in either are directly inherited by the rule system.

There is one special case in the condition expression business map that is worth mentioning: **function execution**.

The [Condition Expression](../../../../05.configuration-tools/02.business-maps/03.condition-expression) Business Map permits the execution of any function that is loaded in the application. So we could also define our own functions to make some complex decision that cannot be made using the workflow expression or an SQL statement and load that into a business map so the implementor would have control over the parameters or, even the actual function. Imagine that we implement 4 or 5 functions to make different decisions, the implementor could pick which one to use at any given moment by simply editing the business map.

### Array context

Setting the $context variable to an array of values permits the developer to instantiate the business rule with a set of additional values that are not accessible by the application entity context.

The key values of the array will be directly substituted in the rule before evaluating it in the context of the record.

The **record CRMID MUST be one of the array values** and it must be in the key "record\_id". This value will also be changed in the rule if it is present.

The variables in the rule must be contained in brackets preceded by the dollar sign. For example, **$\[record\_id\]**

Let's suppose that we are incrementing a variable in a loop. In each iteration, we need to pass the current value of the variable to the rule so it can indicate which is the next increment value. The rule would be something like:

<div class="notices blue">Increment by 1 until 10 and then stop incrementing</div>

```xml
<map>
<expression>if $[counter] < 10 then 1 else 0 end</expression>
</map>
```

and the call looks like this:

```php
$result = coreBOS_Rule::evaluate(
    'IncrementUnitForMyImportantBusinessProcess',
    array('record_id' => 74, 'counter' => $count
);
```

### Decision Tables

Continue reading these resources to understand how Decision Tables work.

- [Decision Table Business Map](../../../../05.configuration-tools/02.business-maps/06.decisiontable/)
- [Decision Table Blog Post](http://blog.corebos.org/blog/decisiontable)

### Credits

<div class="notices blue"> Inspired by the exceptional work of <a href="https://hoa-project.net/En/Literature/Hack/Ruler.html">HOA\Ruler</a></div>
