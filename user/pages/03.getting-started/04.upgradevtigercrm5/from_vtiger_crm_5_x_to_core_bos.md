---
title: 'From vtiger CRM 5.x to coreBOS'
metadata:
    description: 'Upgrade from vtiger CRM 5.4.0 to coreBOS using coreBOS Updater'
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

Upgrade from vtiger CRM 5.4.0 and 5.x to coreBOS using coreBOS Updater

===

- make a copy of your database
- get a copy of the latest version of coreBOS and copy it into a subdirectory on your server
  - download the code from [the download button on github](https://github.com/tsolucio/corebos/archive/master.zip) or MUCH BETTER, clone the repository `git clone https://github.com/tsolucio/corebos`
- copy from your current install:
  - storage
  - test/logo
  - user\_privileges (overwrite any existing files)
  - config.inc.php
  - and any non standard modules that you may have:
    - for example, PDFMaker would require that you copy:
      - modules/PDFMaker
      - Smarty/templates/PDFMaker
      - if you have others, then you copy their directories
- edit config.inc.php
  - change the database access to point to the database copy and $site_url and $root_directory accordingly
- <s>edit vtigerversion.php and change the version to 5.4</s>
- copy build/HelperScripts/installupdater.php to the root of your install and execute it: `http://your_server/your_install/installupdater.php`
- now log in as admin to make sure you are working ok: you can log in and the initial home page appears
- go to coreBOS updater
- click on "Load Updates"
- click on "Apply All". Note that you may have to do this a few times to get all the changes applied as there are some dependencies. Also there will be some SQL errors because we have a set of changes that cover many different cases and your install is different for sure.

you are done! you should be on the latest version of coreBOS

## Upgrade from vtiger CRM 5.2/5.3 to coreBOS

- get a copy of the latest version of coreBOS and copy it into a subdirectory on your server
  - download the code from [the download button on github](https://github.com/tsolucio/corebos/archive/master.zip) or MUCH BETTER, clone the repository `git clone https://github.com/tsolucio/corebos`
- unzip the file build/migrate5.zip
- copy the file install/migratefromvtigercrm.php to the root of your install (where config.inc.php is)
- execute the migratefromvtigercrm.php script in your browser
- follow the instructions
- go to coreBOS updater
- click on "Load Updates"
- click on "Apply All". Note that you may have to do this a few times to get all the changes applied as there are some dependencies. Also, there will be some SQL errors because we have a set of changes that cover many different cases and your install is different for sure.
- delete modules/Migration directory

you are done! you should be on the latest version of coreBOS
