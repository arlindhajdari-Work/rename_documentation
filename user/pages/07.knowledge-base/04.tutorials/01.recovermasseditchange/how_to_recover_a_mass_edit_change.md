---
title: 'How to recover a mass edit change'
metadata:
    description: 'How to recover a mass edit change'
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
    tag:
        - howto
---

The global steps are:

1. dump the affected table from your backup to a file
2. change the name of the table in the file
3. read the table into your database
4. execute an update SQL to recover the field values
5. delete the backup table

Let's see these steps with a real example.

## Use case

In February 2022 we introduced a changeset that had an error and overwrote the smcreatorid field in the vtiger_crmentity table. The next steps will detail how to recover this field from a database backup.

## Dump backup table

We need a copy of the smcreatorid field before the changeset. We only need that column as, in this case, only that field was lost. If you are here due to a Mass Edit change you will need to recover all those tables that have values that you want to recover.

Let's suppose that we have a copy of our backup database in MySQL named MassEditBackupRecovery. We want to extract from there just the vtiger_crmentity table, so we launch this command.

```
mysqldump -u root -p MassEditBackupRecovery vtiger_crmentity > crmentity.sql
```
now we have a file with the table we need

## Change the name of the table

Edit the crmentity.sql file and change all the **vtiger_crmentity to backup_crmentity**

I did this using Linux command line vi editor and launching this substitution **:s%/vtiger_crmentity/backup_crmentity/g**

We do this so we can load the backup table into our production database without overwriting the production table.

## read the table into your database

```
mysql -u root -p MassEditBackupRecovery < crmentity.sql
```

## execute an update SQL to recover the field values

Now that we have both tables in the same database we can recover the field values with an update SQL command like this

```
update vtiger_crmentity inner join backup_crmentity on vtiger_crmentity.crmid=backup_crmentity.crmid set vtiger_crmentity.smcreatorid=backup_crmentity.smcreatorid
```

If you are doing a Mass Edit recovery this query needs to be adapted to each case and consider all the fields you want to recover.

## delete the backup table

We drop the backup table as it is not needed anymore.

```
drop table backup_crmentity
```

# CAUTION

<div class="notices red">
These steps are not difficult but there are a lot of places where things can go wrong and you can mess up. So please, use your brain. Read the steps and read the commands you are executing. Make sure you know what you are doing in each case, and make backups before starting. </div>