---
title: 'Duplicate Records Business Mapping'
metadata:
    description: 'It permits you to define the related modules that will be duplicated when launching a Duplicate Records workflow task.'
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
        - duplicaterecords
---

The purpose of the duplicate map is to define which related modules should be duplicated when executing the Duplicate Records workflow task.

===

This is a workflow configuration map. It permits you to define the related modules that will be duplicated when launching a Duplicate Records workflow task.

The accepted format is

```xml
<map>
  <originmodule>
    <originname>ModuleName</originname> {optional}
  </originmodule>
  <relatedmodules>
    <relatedmodule>
      <module></module>
      <relation>m:m</relation> {optional}
    </relatedmodule>
    ...
    <relatedmodule>
      <module></module>
      <relation>1:1</relation>
    </relatedmodule>
  </relatedmodules>
  <DuplicateDirectRelations>false</DuplicateDirectRelations> Allowed values: true, false
  <LaunchWorkflows>
    <workflow>name or ID</workflow>
  </LaunchWorkflows>
</map>
```

The coreBOS application supports mass duplication of records by means of the **Duplicate Records** workflow task. The idea is that you can duplicate a record and all its related information in one step. The task will do the next set of steps when launched:

- duplicate the record launching the workflow
- relate the duplicated record with all the records the main record is related with by m:m
- create new related records for all the directly related records (1:n), which effectively mass creates many records, duplicates themselves of all the records related to the main record

This map permits us to tune the way we want this duplication to work.

By default, those records which are directly related to the one being duplicated are **NOT** duplicated. This means, for example, that if we are duplicating a Contact which is related to Account X, the new duplicated Contact will still be related to the same Account X. If we set the **DuplicateDirectRelations** directive to TRUE, then a new record will be created for each direct relation. In the previous example, the duplicated Contact would be related to a new Account Y which would be a duplicate of Account X.

Also, by default, the mass duplicate task will duplicate all relations of the record. If it is an m:m relation the records will end up being related to both records; the original and the duplicate. If the relation is 1:n, then new records will be created and related to the duplicate record.

<div class="notices blue">
Only standard vtlib relations are supported (get_dependents_list and get_related_list)
</div>

Using the **relatedmodule** directives we can limit the relations we want to be duplicated in order to avoid doing more work than necessary and duplicating information that does not need to be repeated.

Infinite loops
--------------

Workflows are not launched on the main record being duplicated, so we avoid getting into an infinite loop at this first stage.

Workflows are launched on all related records that are created, which opens the possibility of infinite loops. For example, if the **DuplicateDirectRelations** directive is set to true on the related records they will create a new record in the main module for sure.

So be very careful with the rules and configurations you set when duplicating.

Sometimes it is necessary to execute some workflows on the main record being duplicated. For this case, the map supports the `<LaunchWorkflows>` directive. This directive contains a list of workflow IDs or names that will be executed on the main duplicated record. Please be very careful as this can easily create infinite loops.

Duplicating second level records
--------------------------------

Only the first level of related records are duplicated.

If you need to duplicate also the relations on those records, or even go
lower in the relation tree, we need to do some additional work.

In order to completely duplicate a record, we must know the CRMID of the
record. This is the record that is launching the workflow.

If we define another workflow, with a duplicate record task, on one or
more of the related modules we may think that it will launch when the
parent duplicate tasks creates a record in this module. In other words,
let's suppose that we have a duplicate record task on Projects and we
want to duplicate all the Project Tasks with the relations it may have.
So we add another duplicate record task on the Project Tasks module.
What we end up with is two duplicate Project Tasks with none of the
related information the original one had. This is wrong but makes sense.
Let me try to explain.

The duplicate task on Project starts creating new duplicate Project
Tasks after duplicating the Project record that launched the workflow.
This process creates a new Project Task and relates it to the new
duplicated Project. This save process launches the duplicate record task
on the newly created Project Task record which is duplicated, NOT the
original Project Task which the first task duplicated but the SECOND,
duplicate Project Task is the one that launches the workflow. That is
why we end up with two records with no related records.

To fix this we must add a new field on the Project Task module (and on
all the related modules we want to duplicate correctly). This field must
be called ***isduplicatedfromrecordid***. It will hold the CRMID of the
original record the duplication started from and will be used to get the
relations and launch the workflow correctly.

This new field will also work correctly in the normal edit of the
application, getting filled in automatically when we duplicate, so it is
also a helpful field to have around. You can set it to displaytype 3 or
4 if you don't want to have it on the display.

This is the code to add the field:

```php
<?php

// Turn on debugging level
$Vtiger_Utils_Log = true;

include_once('vtlib/Vtiger/Module.php');

$modname = 'Potentials'; // Or whatever module you want to have this on.
$module = Vtiger_Module::getInstance($modname);

if ($module) {
    $blockInstances = Vtiger_Block::getAllForModule($module);
    $blockInstance = reset($blockInstances); // get first block
    if ($blockInstance) {
        $field = new Vtiger_Field();
        $field->name = 'isduplicatedfromrecordid';
        $field->label= 'isduplicatedfromrecordid';
        $field->table = $module->basetable;
        $field->column = 'isduplicatedfromrecordid';
        $field->columntype = 'INT(11)';
        $field->uitype = 10;
        $field->displaytype = 1;
        $field->typeofdata = 'I~O';
        $field->presence = 0;
        $blockInstance->addField($field);
        $field->setRelatedModules(Array($modname));
        echo "<br><b>Added Field to $modname module.</b><br>";
    } else {
        echo "<b>Failed to find $modname block</b><br>";
    }
} else {
    echo "<b>Failed to find $modname module.</b><br>";
}
?>
```

<br>
------------------------------------------------------------------------

[Next](../12.globalsearch) | Chapter 18: Global Search Autocomplete.

------------------------------------------------------------------------