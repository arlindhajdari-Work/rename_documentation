---
title: 'How to change entity identifier'
metadata:
    description: 'How to change entity identifier'
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
    tag:
        - howto
---

Sometimes, when the default entity identifier field is not significant for us and we want to change it for some other field that is more relevant.

For example. In Opportunity module the default identifier is "Opportunity Name", but we want may want to use the "Opportunity No".

===

For this, we have to create this script:

```php
// Turn on debugging level
$Vtiger_Utils_Log = true;

require_once 'include/utils/utils.php';
include_once('vtlib/Vtiger/Module.php');
require_once('config.inc.php');

$module = Vtiger_Module::getInstance('Potentials');

$module->unsetEntityIdentifier(); // this unset the potentialname like a entity identifeir

$field = VTiger_Field::getInstance('potential_no', $module); // now you get the field that you want to entity identifier

$module->setEntityIdentifier($field); // set this field.
```

and then modify the main class of the module. In the header change some references to the previous entity field, at least **list_link_field.**.
