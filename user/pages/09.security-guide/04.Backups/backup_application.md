---
title: 'Backup Application'
metadata:
    description: 'Menu Editor'
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
        - adminmanual
        - security
    tag:
        - backup
---

The application has an extension that can be used to configure regular backups and create ad hoc backups.

You can use the Menu Editor to create an access point to this URL:

```
index.php?module=VtigerBackup&action=index
```
or directly use the Module name like this:

![](backup.png?width=100%)

When we access the extension we will be able to activate the local backups and the offsite (FTP) backups.

![](backupconfig.png?width=100%)

<div class="notices blue">
The "backup" default directory exists and is protected from access through the web.
</div>

Once configured the backups you can manually execute backups clicking on the **Backup Now** button and/or activate the **scheduled tasks** to make them regularly in Settings > Scheduled Tasks

![](backupschedule.png?width=100%)

There are two different types:

Backup with no external tools. Can easily run into memory limitations and really slow down the server. Good for smaller sets of information.
Backup with external tools. mysqldump and zip must be available on the server. Fast and good for big sets of information.
You can find some more information on our youtube channel and in the coreBOS Manual.

## Recovering from a Backup

-   Once you have made a backup you will have a .zip file with the information
-   Download a copy of your code as it is being used into a webserver directory and give it the correct permissions
-   Unzip the backup file into the downloaded code from the top directory of the application overwriting any existing files.
-   You will see a new .sql file which contains the backup database
-   Create a new empty database
```
mysqladmin -u dbuser -ppassword CREATE DBname
```

-   Import the information (database.sql)
```
mysql -u dbuser -ppassword DBname < database.sql
```
-   Configure config.inc.php (database name, user, password, application path, etc.)