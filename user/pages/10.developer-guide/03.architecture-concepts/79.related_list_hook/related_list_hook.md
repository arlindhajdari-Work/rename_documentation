---
title: 'Related List hook'
metadata:
    description: 'The need for this hook appears when a new module or functionality needs to add a related list on a module that is already installed or is a pure base module like Accounts or Contacts.'
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
        - event
    tag:
        - hooks
        - relatedlist
---

The need for this hook appears when a new module or functionality needs to add a related list on a module that is already installed or is a pure base module like Accounts or Contacts. To achieve this the method that will return the contents of the related list must be INSIDE the module's main class. So, for example, if we want to add a related list on Accounts, we need the method to be a native method of the Accounts class which is contained in the modules/Accounts/Accounts.php file. In other words: we need to modify a base code file.

===

To avoid having to do that we need a way to add the method without modifying the base code file.

Other examples are the base *get_dependents_list()* and *get_related_list()* methods. So that these methods can be executed against any module (as is currently the case) they are inside the CRMEntity class which is the base of all the entities in the system. This way, all the modules of the system inherit these methods and they can be attached easily from any other module.

We will be following the CRMEntity idea and permit adding the new method to this class. Although it would be ideal to add the new method only to the base class that needs it, that would require some additional code changes that are overly complicated and may break backward compatibility. So, in the end we will have a new method on the base CRMEntity class which all modules extend so any module will be able to use it.

The way this works is rather transparent. We [register our related list method exactly as we do with any normal related list method.](../../04.development_framework/11.develtutorials/07.relatedlists) In this case, the name of the function that defines the related list does not exist inside the function. For example, lets imagine we have this definition:

```php
$accounts->setRelatedList(Vtiger_Module::getInstance('Payslip'), 'header',Array('ADD'),'get_special_related_list');
```
So our Payslip module is adding a related list on Accounts and wants it to call a special method called *get_special_related_list()* to obtain the contents. Now we define this method in a file inside our Payslip module. The file must be named exactly as the function name and contain exactly one function definition with that name. So we will have a file named *modules/Payslip/get_special_related_list.php* with a contents like this:

```php
<?php
function get_special_related_list($param1, $param2, ..., $object) {
...
}
?>
```

The rest is transparent, the application know what to do. It will look for the method *get_special_related_list()*, if it isn't found it will look for the file *modules/Payslip/get_special_related_list.php*, if it is found it will load it and look for the function *get_special_related_list()*, if found it will add it as a method to the CRMEntity class and proceed with the code as usual.

There is only one small issue: due to the way PHP works adding a method dynamically at run time is really not supported. So we are forcing the code to some extent and in return we have to sacrifice that the new method will not be able to use the "$this" reference. This is why we add to the list of parameters the object reference, as can be seen in the above example.

You can find an [example function in the helpers directory.](https://github.com/tsolucio/corebos/blob/master/build/HelperScripts/CustomRelatedListFunction.php)

With this new functionality and the [special detailed view blocks enhancements,](../../04.development_framework/11.develtutorials/16.add_special_block) we can really personalize an existing module. For example, we could completely override the Project's Gantt related list with our own functionality and add a block to show the same information directly on the project's detail view, simply installing an extension module with no base code changes to the project module's code.

<div class="notices blue">
This enhancement is <a href="https://www.garfieldtech.com/blog/magical-php-call">based on this article.</a>
<br>

</br>
Thanks :-)
</div>


