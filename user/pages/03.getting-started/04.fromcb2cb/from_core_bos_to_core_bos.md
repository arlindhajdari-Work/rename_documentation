---
title: 'From coreBOS to coreBOS'
metadata:
    description: 'Copy a coreBOS install from one server to another'
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
---

Steps to copy a working coreBOS install from one server or directory to another

===

- copying files in the folder to the new destination on the server
- seting up the right permissions on folders / files
- removing all folders on /stroge/20\*, and removing all files on the folder users\_priviliege/ starting with sharing\_\* and user\_\*
- create new database from the corebos_justinstalled_empty.sql
- copying data on the tables containing names: users, tab, field, modules, menu, map, home, view, business
- edit config.inc.php
  - change the database access to point to the database copy and `$site_url` and `$root_directory` accordingly
- now log in as admin to make sure you are working ok: you can log in and the initial home page appears
- go to coreBOS updater
- click on "Load Updates"
- click on "Apply All". Note that you may have to do this a few times to get all the changes applied as there are some dependencies. Also there will be some SQL errors because we have a set of changes that cover many different cases and your install is different for sure.
