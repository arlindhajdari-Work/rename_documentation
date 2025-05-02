---
title: 'Steps to take when changing your database'
metadata:
    description: 'Steps to take when changing your database'
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
        - database
---

From time to time it happens that you want to change the database you are using in your installation. This is a developer situation as it is very rare to want to do this in a production install, but the steps below would work correctly also for a production coreBOS.

===

The situation is that we have a completely functional coreBOS connected to some database. This database has been corrupted or simply contains some obsolete image that we want to eliminate in order to recover a different database to use with our code. Obviously, the database contains meta information about users, modules and similar settings that require synchronization with the code. That is why we must follow the next steps every time we change the database:

Once deleted and recovered the new database we must:

- set the config.inc.php or the config-dev.inc.php database access variables if their values have changed
- execute build/HelperScripts/updatetabdata.php
- execute build/HelperScripts/createuserfiles.php
- execute build/HelperScripts/resetadminpw (if necessary)
- login, go to the coreBOS updater module: load and apply all changesets
