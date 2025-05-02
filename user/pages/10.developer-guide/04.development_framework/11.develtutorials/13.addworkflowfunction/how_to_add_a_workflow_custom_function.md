---
title: 'How to add a workflow custom function'
metadata:
    description: 'How to add a workflow custom function'
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
        - workflow
    tag:
        - workflow
---

There are two types of workflow tasks that can be added to the system: **custom workflow functions** and full-blown **workflow tasks**. The difference is the configuration screen. A **custom function** is just a set of instructions and code that do not need any configuration options, it's task is clearly defined and it just needs to be launched on the given event. For example, a routine that relates the products and services of an invoice with the account of the invoice is a custom function. This custom function does not need anything more than what it receives to get its work done, but it could get a little complicated and we could require an option to indicate if we want to have only products and not services related or the reverse, or both. Now that we need to know which elements to relate the custom function needs a configuration screen and must be converted into a **workflow task with configuration screen**.

===

Here we explain how to create the first type of workflows, [for the second type go here](../14.addworkflowtask).

A **workflow method or custom function** needs a name to show in the configuration section, a class that will extend VTTask and does the work, and it will be associated to certain modules and not to others. Finally, it may be active or not depending on a certain module is installed or not.

-   **Add new task definition to the application.** This is done by
    inserting a record with the details in the
    *com\_vtiger\_workflowtasks\_entitymethod* table.
    -   **method\_name**: external name, visible when configuring
        workflow: **available through the Invoke Custom Function**
        workflow task
    -   **function\_name**: the name of the function to be called, a
        normal PHP function
    -   **function\_path**: the script on the file system that contains
        our new function
    -   **module\_name**: the name of the module that the method is
        available for
    -   An example would be:
        -   "method\_name"=&gt;"Update Contact Assigned To": label to
            show on screen
        -   "function\_name"=&gt;"updateContactAssignedTo": name of the
            function to invoke to do the work
        -   "function\_path"=&gt;"include/wfMethods/updateContactAssignedTo.php":
            path to script that contains the function
        -   "module\_name"=&gt;'Accounts': will be available only for
            this module, if more modules can use this function you must
            insert a new record for each module.
    -   coreBOS has a helper method that can insert this record for you:
        *VTEntityMethodManager::addEntityMethod()*, an example call
        would be like this:
        ```php 
        <?php
        // Turn on debugging level
        $Vtiger_Utils_Log = true;

        require_once 'include/utils/utils.php';
        include_once('vtlib/Vtiger/Module.php');
        require 'modules/com_vtiger_workflow/VTEntityMethodManager.inc';
        global $adb;

        $emm = new VTEntityMethodManager($adb);
        $emm->addEntityMethod("Accounts", "Update Contact Assigned To", "include/wfMethods/updateContactAssignedTo.php", "updateContactAssignedTo");
        echo 'add Workflow Custom Function complete!';
        ?>
        ```
        or [like this using coreBOS Updater](https://github.com/tsolucio/corebos/blob/master/build/changeSets/workflow_contactassignedto.php)

<!-- -->

-   Add new workflow function file:
    *include/wfMethods/updateContactAssignedTo.php*, which contains the
    function that will do the work. You can put the script anywhere you
    want in the application file system, but it has to be the same place
    indicated in the database record.

<!-- -->

-   The script *include/wfMethods/updateContactAssignedTo.php* defines
    the function indicated in the database record.
    -   The name of the function has to be the same we added in the
        database record in the first step
    -   The function will receive **one parameter**: a **VTEntityData
        object of the record** being saved. This object can be found in
        *include/events/VTEntityData.inc* and contains a variable called
        *focus* which contains the full CRMEntity record. It also has an
        array with all the values being saved in *data*.
    -   We also have access to all of the coreBOS programming
        infrastructure

[You can see a full example of how we add a new workflow method to assign contacts to the same account user](https://github.com/tsolucio/corebos/commit/9a200854ba38cef0f8c3b7284d37b0edf13d5f12)
