---
title: 'From vtiger CRM 6.x to coreBOS'
metadata:
    description: 'Upgrade from vtiger CRM 6.x and 7.x to coreBOS using coreBOS Updater'
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
        - installation
        - update
    tag:
        - install
        - vtigercrm
---

## Migrate from vtiger CRM 6.x and 7.x to coreBOS

===

 !!! Currently migrations from 6.0 to 6.5 are available.

The steps to migrate your vtiger CRM 6.x to coreBOS are:

- get a copy of coreBOS from github
- recover a dump of your vtiger CRM 6.x database
- copy your config.inc.php from VT6 and modify the database settings to point to your copy
- at this step your coreBOS install is pointing at the vtiger CRM 6.0 and does not work
- copy the migration script to the root of the coreBOS install. The script is in the build directory `build/migrate_from_vt6.php`
- execute the script`http://your_server/your_corebos/migrate_from_vt6.php`

 ! In some of the migrations we have done, we have found that the version is not correctly updated in the database. Although the code is on version 6.1 the database is incorrectly set to 6.0 (no idea how that can work!!). If this is your case you need to force the migration to apply the 6.1 changes bt adding the force parameter like this:`http://your_server/your_corebos/migrate_from_vt6.php?force=1`
- copy all your documents from the vtiger CRM install: directly copy all the files in the **storage** directory from one to the other
- copy logos and the like which are in the *test/logo* directory
- enter coreBOS and activate modules in module manager if necessary
- apply [coreBOS Updater changesets](../../10.developer-guide/04.development_framework/11.develtutorials/08.corebosupdater)
