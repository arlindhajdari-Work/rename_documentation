---
title: 'coreBOS Custom Permission Hooks'
---

## What is it for?

The coreBOS custom permission hooks serve the purpose of modifying the existing permission system with custom programming. Using these hooks we will be able to completely override the existing permission decision or construct upon them to enhance the decision of showing or editing a set of records without having to modify the base code to do it.

<div class="alert-danger">You will need to learn and understand how the current permission system works to be able to modify it!</div>

## Why not use Record Access Control?

coreBOS has a powerful configuration option through Business Mappings. Using these we can configure many parts of the application to adapt them to the exact requirements of each implementation. One of these options is [Record Access Control](../../../05.configuration-tools/02.business-maps/22.record_access_control/item.md). With this very powerful mapping, we can hide/show create, retrieve, edit and delete actions using advanced conditions based on the record upon which the action should take place.

RAC (Record Access Control) is ideal for additional logic upon the existing permission system. For example, we can hide the Add button on Project Task whose Project is closed or block editing of the existing project tasks of a closed project. In this scenario, the user already has access to the Project and the Project Tasks, but the business wants the application to stop any attempt to create/edit a project task related to a closed project.

Although a LOT of configuration can be done using RAC it falls short in a couple of situations.

One is when the decision to be made has to be done globally. RAC requires to have access to the record to make a decision, but when we are retrieving a whole set of records to list or report the decision is made directly in the database using SQL, in this case, we can't use record by record conditions that are executed in PHP. This scenario arises when the coreBOS permission system isn't enough to express the access rules. For example, if we want to give access to a record based on the value of a field or based on it's relation to another module, this can effectively change the set of records that the coreBOS permission system would return. In this case, we could eliminate from the set a record that coreBOS would include or, the reverse, add a record that the application would not include.

The other situations is when the decision requires a complex set of conditions and methods that would be hard to express using workflow or condition mappings.

For these two situations, more for the first, we need more power than the RAC system can offer and that is where these hooks come in.

### The hooks

<table>
<thead>
<tr class="header">
<th>event_name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>corebos.permissions.accessquery</td>
<td>Permits manipulation of the SQL that retrieves records that the user can access</td>
</tr>
<tr class="even">
<td>corebos.permissions.ispermitted</td>
<td>Permits intercepting and modifying the module/record access permission</td>
</tr>
</tbody>
</table>

How it works
------------

With the permission hooks we can override or manipulate the existing
permissions system with complex scenarios which can be easily expressed
in PHP using the whole infrastructure of the application and the
necessary SQL.

The **corebos.permissions.ispermitted** hook is easy to use. It permits
you to decide if a given user is authorized to execute an action against
a module or a record. First the coreBOS permission system will be
consulted. The result of what the application would do is given to the
hook but the result of the hook is what will be returned as the result.

The profile of the hook is like this:

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>$permission</td>
<td>Input/Output</td>
<td>Contains the decision that coreBOS has taken for the requested action in the form of 'yes' or 'no'</td>
</tr>
<tr class="even">
<td>$module</td>
<td>Input</td>
<td>The name of the module the requested action is to be executed</td>
</tr>
<tr class="odd">
<td>$actionname</td>
<td>Input</td>
<td>The action to be executed in the form of: EditView, Delete, DetailView, CreateView and Save (see vtiger_actionmapping for a full list)</td>
</tr>
<tr class="even">
<td>$record_id</td>
<td>Input</td>
<td>If the action is to be executed against one record you will get it's CRMID here, if not it will be empty (the action is against the whole module)</td>
</tr>
</tbody>
</table>

As with all hooks you **MUST** return the full set of parameters given
and, in this case only the first one, the permission, will be returned
as the result of the permission.

The code in this hook must determine if the given user has permission to
execute the given action against the module and/or record. It can use
any function in the application or do any database query it needs to do
to make that decision. It must return a 'yes' or 'no' string loaded into
the $permission parameter.

The **corebos.permissions.accessquery** hook is mostly SQL. It permits
you to change the set of records returned from the database, effectively
changing the set of records that the user can see/access.

The profile of the hook is like this:

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>$SpecialAccessQuery</td>
<td>Output</td>
<td>This is an SQL condition that will be added to the SQL that is retrieving the set of records to show. Exactly what SQL can be returned and how it will be mixed with the existing SQL depends on the value of the $typeOfPermissionOverride parameter.</td>
</tr>
<tr class="even">
<td>$typeOfPermissionOverride</td>
<td>Output</td>
<td>-<strong>none</strong>: no override, the default behavior will be taken<br />
-<strong>fullOverride</strong>: full control, whatever is returned by the hook will be mixed in<br />
-<strong>addToUserPermission</strong>: the SQL returned will be added (UNION) to the default behavior<br />
-<strong>SubstractFromUserPermission</strong>: the SQL returned will have these records substracted<br />
-<strong>showTheseRecords</strong>: will INNER JOIN with the set of records returned in this SQL</td>
</tr>
<tr class="odd">
<td>$module</td>
<td>Input</td>
<td>The module name for which we are retrieving the records</td>
</tr>
<tr class="even">
<td>$user</td>
<td>Input</td>
<td>The user who is requesting the records</td>
</tr>
</tbody>
</table>

The first two parameters are output variables that will determine how
the subsequent SQL is constructed and the other two are input parameters
so the code in the hook can decide what to return.

As with all hooks you MUST return the full set of parameters given.

This hook lives inside a function that constructs an INNER JOIN
condition to limit the records returned to those related to a given
user. So, by default, it will return a string that will look like this:

    INNER JOIN $tableName ON $tableName.id = vtiger_crmentity.smownerid

where $tableName is a dynamically created table that contains the set of
user and group IDs whose assigned records we want to retrieve.

This hook permits us to modify that condition in four ways:

### $typeOfPermissionOverride = none

**no modification**, it will return the exact same string condition the
application would have sent

### $typeOfPermissionOverride = fullOverride

**full modification**, whatever is returned from the hook will be
returned unmodified, you have full control over the condition.

It must be an INNER JOIN condition as that is what the application
expects from this method.

### $typeOfPermissionOverride = addToUserPermission

**add records to existing set**, the SQL condition returned must be a
full, correct syntax SQL statement that will return a set of record IDs
that the user can access. This set of records will be merged with the
existing set of user and group IDs. It must return a set of record IDs,
not user IDs.

The end result will be something like this:

    INNER JOIN $tsTableName on
     ($tsTableName.id=vtiger_crmentity.crmid or $tsTableName.id = vtiger_crmentity.smownerid)

where $tsTableName is the UNION of the default set of users and groups
and the set of CRMIDs returned from the SQL generated by the hook.

As can be seen the OR condition will retrieve all records assigned to
the user and all records included in the special query returned from the
hook. It mixes both users and CRMIDs making it easy to get all the
accounts in a certain status (for example).

### $typeOfPermissionOverride = SubstractFromUserPermission

It's a combination of 'none' and 'showTheseRecords'. We substract from
the normal user permission the records that are returned by the special
query

### $typeOfPermissionOverride = showTheseRecords

**retrieve an exact set of records**, the SQL generated by this type
must be a full, correct syntax SQL statement that should return the
exact set of record IDs that the user has right to access. The SQL
condition will be computed and an INNER JOIN similar to this will be
launched:

    INNER JOIN $tsTableName on $tsTableName.id=vtiger_crmentity.crmid

Example
-------

Loading the event handlers for the hooks is the same as with any other
event handler where you have to call the **registerHandler()** method as
[can be seen in the example
code](https://github.com/tsolucio/corebos/blob/master/build/HelperScripts/coreBOSEventsLoader.php#L46).

You can find the example code in the HelperScripts directory. Exactly in
the [coreBOSEventsPermission.php
file](https://github.com/tsolucio/corebos/blob/master/build/HelperScripts/coreBOSEventsPermission.php).

This file is prepared to run in the [coreBOS test suite
database](https://github.com/tsolucio/coreBOSTests). In that database
HelpDesk (Trouble Tickets) and Products are configured to be private, so
each user can only see Tickets and Products assigned to himself as per
the default permission system.

The hook in the code is an example for the four types of permission
override.

### Type none

Set the [$typeOfPermissionOverride property to
'none'](https://github.com/tsolucio/corebos/blob/master/build/HelperScripts/coreBOSEventsPermission.php#L22).
With this setting both hooks will simply return the default parameter
array given and the application will work normally. Accessing the
application with a non-admin user you will see the tickets and products
assigned to that user.

### Type fullOverride

Set the [$typeOfPermissionOverride property to
'fullOverride'](https://github.com/tsolucio/corebos/blob/master/build/HelperScripts/coreBOSEventsPermission.php#L23).
This will assign the returned query to the one [you can see on line
44](https://github.com/tsolucio/corebos/blob/master/build/HelperScripts/coreBOSEventsPermission.php#L44)
that establishes that the only tickets that can be seen are those
related to Account 74, Chemex.

[On line
77](https://github.com/tsolucio/corebos/blob/master/build/HelperScripts/coreBOSEventsPermission.php#L77)
we give access to the record if the related account is Chemex.

In short, we have modified the application to only show tickets of the
account Chemex. All other tickets are hidden.

We could enhance the conditions as needed.

### Type addToUserPermission

Set the [$typeOfPermissionOverride property to
'addToUserPermission'](https://github.com/tsolucio/corebos/blob/master/build/HelperScripts/coreBOSEventsPermission.php#L24).

In this case we add to the tickets that the user can see per the normal
permission system those tickets that are related to accounts or products
that the user has permission to see. In other words, if a ticket is
assigned to another user, thus the current user can not see it, if that
ticket is related to an account or product that the user CAN see, then
the ticket will also be accessible.

We accomplish this by returning a query that retrieves all ticket IDs
that fulfill the condition described above [as can be seen
here](https://github.com/tsolucio/corebos/blob/master/build/HelperScripts/coreBOSEventsPermission.php#L119)
and setting the $typeOfPermissionOverride to 'addToUserPermission' so
that our ticket IDs will be added to the default user permissions.

For individual record access [we set the isPermitted value depending on
the owner of the ticket or of the related account or
product](https://github.com/tsolucio/corebos/blob/master/build/HelperScripts/coreBOSEventsPermission.php#L87).

### Type showTheseRecords

Set the [$typeOfPermissionOverride property to
'showTheseRecords'](https://github.com/tsolucio/corebos/blob/master/build/HelperScripts/coreBOSEventsPermission.php#L25).

In this case we will return ONLY those tickets that we want the user to
see. These tickets will be those tickets that are related to accounts or
products that the user has permission to see. In other words, if a
ticket is assigned to another user, thus the current user can not see
it, if that ticket is related to an account or product that the user CAN
see, then the ticket will also be accessible, but ONLY those tickets,
not even the ones assigned to the user will be accessible.

We accomplish this by returning a query that retrieves all ticket IDs
that fulfill the condition described above [as can be seen
here](https://github.com/tsolucio/corebos/blob/master/build/HelperScripts/coreBOSEventsPermission.php#L119)
and setting the $typeOfPermissionOverride to 'showTheseRecords' so that
our ticket IDs will be the only ones shown.

For individual record access [we set the isPermitted value depending on
the owner of the related account or
product](https://github.com/tsolucio/corebos/blob/master/build/HelperScripts/coreBOSEventsPermission.php#L99).

Another Example
---------------

Starting on [line
128](https://github.com/tsolucio/corebos/blob/master/build/HelperScripts/coreBOSEventsPermission.php#L128)
you can find another example with two methods that implement the logic
of permitting users to see all information related to accounts or
contacts assigned to them. In other words, you can assign an account to
a user and he will automatically be able to access all the related
modules' records related to this account, no matter whom they are
assigned to.

Notes
-----

-   there is no hook to override **getListViewSecurityParameter()**
    method because this method is obsolete. It is deprecated by the
    **getNonAdminAccessControlQuery()** method. It is currently only
    used for Deduplication (and some modules like Assets and
    SMSNotifier) and we will get around to eliminating its use
    completely. In the mean time it is possible that users affected by
    custom permission rules with the existing hooks will see a different
    set of records when deduplicating.
