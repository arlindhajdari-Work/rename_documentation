---
title: 'Upgrade from coreBOS 5.4.0 to coreBOS 5.5.0'
metadata:
    description: 'Upgrade from coreBOS 5.4.0 to coreBOS 5.5.0'
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
        - documentation
    tag:
        - upgrade
---

This release is about updating and stabilizing our code base along with enhancements in two directions:

- open the application to third party projects through a much more powerful REST interface, so we can grow upon the core system creating incredible applications on top of it
- change the package distribution system, so it is much easier to distribute new modules and new changes without having to go through a traumatic process of patching and manually executing code

===

But we still slipped in a few interesting features on reporting and importing among others :-)

[You can find the full details of the changes made on this page.]()

Upgrading is *still* a work better suited for a developer who is comfortable playing with the code, but I will try to explain the process in detail to make it easier.

<div class="notices red">
<strong>Backup your files and database</strong>, there should be no problem, all the code is tested and the process is not invasive, if there is a problem <strong>we will help</strong>, this is just a precautionary step and another good reason to make a backup of your information</strong></div>

## You have a clean coreBOS 5.4

You can proceed in two ways, either use the fully patched zip upgrade package or apply the patch.

### Fully patched zip upgrade

1. backup your files and database, there should be no problem, all the code is tested, if there is a problem we will help, this is just a precautionary step and another good reason to make a backup of your information
2. [download the upgrade package from here](corebos54_to_corebos55.zip)
3. copy it to the root of your current coreBOS 5.4
4. unzip it overwriting all files
```
unzip -o corebos54_to_corebos55.zip
```
5.  you can also uncompress the files locally and upload them to your server via FTP

<div class="notices blue">
<strong>PLEASE</strong>, make sure your code base is totally clean, this step will overwrite your files and any change they may contain. Although you may not have done any changes to the files you know of, some extensions in the market do this and require those changes. If you have any code change at all, or some extension already installed that modify base files, use the patch upgrade procedure detailed below. If you are in doubt, <a href="http://discussions.corebos.org/">ask in the forum.</a></div>

6.  **execute the database changes**, this is done using the [coreBOS Updater](../../../10.developer-guide/04.development_framework/11.develtutorials/08.corebosupdater), which is a module that will take care of managing all the updates from now on. It will read the set of changes that need to be done and will permit you to apply them and undo some of them. In this first release of the module we must install it.<br>
a. Go to your browser<br>
b. login to your coreBOS 5.4 <br>
c. edit the URL box and eliminate all the text starting from index.php <br>
d. add installupdater.php <br>

!!! It should look like this: 
!!! ` http://your_server/your_crm/installupdater.php`
e. execute the script and you should get a green screen with some messages about the actions executed
f. edit the URL box again and go to your coreBOS: 
```
http://your_server/your_crm/index.php
```
g. open the menu and go to **coreBOS Updater**<br>
h. click on the **Get Updates** button<br>
i. go back to the list view and click on the **Apply All** button<br>
7. **manually change your config.inc.php**, for speed optimization we have require adding a line to your config.inc.php, **THIS IS VERY IMPORTANT** or some parts of the application may not work correctly.
a. edit config.inc.php and look for the lines <br>
```
// default charset default value = 'UTF-8' or 'ISO-8859-1'
$default_charset = 'UTF-8';
```
note that your value may be different from UTF-8, now add this line after the assignment
```
$default_charset = strtoupper($default_charset);  // DO NOT MODIFY THIS LINE, IT IS IMPORTANT
```
so it all ends up looking like this:
```
// default charset default value = 'UTF-8' or 'ISO-8859-1'
$default_charset = 'UTF-8';
$default_charset = strtoupper($default_charset);  // DO NOT MODIFY THIS LINE, IT IS IMPORTANT
```
b. save the file 

Your done. Enjoy!

## Apply patch file with changes upgrade

1. backup your files and database, there should be no problem, all the code is tested, if there is a problem we will help, this is just a precautionary step and another good reason to make a backup of your information
2. [download the upgrade patch from here]()
3. copy it to the root of your current coreBOS 5.4
4. apply the patch with the git apply command
```
git apply --reject corebos54_to_corebos55.patch
```
5. you can also do this locally on your file system and then upload the files to your server via FTP

<div class="notices blue">
The <i>git apply</i> command will give some errors and warnings. This is normal because in this release we are changing the distribution method of modules and extensions, now we have them all laid out in the code instead of packed in .zip files. This requires us to put all the files in place and we do this for all files, many of which you already have in place and those do not get overwritten, thus the error/warnings. What you do have to pay attention to is any message of <strong>REJECT</strong>, those are indicating a problem you need to attend.
</div>

6. **execute the database changes**, this is done using the [coreBOS Updater](../../../10.developer-guide/04.development_framework/11.develtutorials/08.corebosupdater), which is a module that will take care of managing all the updates from now on. It will read the set of changes that need to be done and will permit you to apply them and undo some of them. In this first release of the module we must install it.<br>
a. Go to your browser<br>
b. login to your coreBOS 5.4<br>
c. edit the URL box and eliminate all the text starting from index.php<br>
d. add installupdater.php<br>

It should look like this:
```
http://your_server/your_crm/installupdater.php
```
e. execute the script and you should get a green screen with some messages about the actions executed
f. edit the URL box again and go to your coreBOS:
```
http://your_server/your_crm/index.php
```
g. open the menu and go to **coreBOS Updater**<br>
h. click on the **Get Updates** button<br>
i. go back to the list view and click on the **Apply All** button<br>

7. manually change your config.inc.php, for speed optimization we have require adding a line to your config.inc.php, THIS IS VERY IMPORTANT or some parts of the application may not work correctly.<br>
a. edit config.inc.php and look for the lines <br>
```
// default charset default value = 'UTF-8' or 'ISO-8859-1'
$default_charset = 'UTF-8';
```
note that your value may be different from UTF-8, now add this line after the assignment
```
$default_charset = strtoupper($default_charset);  // DO NOT MODIFY THIS LINE, IT IS IMPORTANT
```
so it all ends up looking like this:
```
// default charset default value = 'UTF-8' or 'ISO-8859-1'
$default_charset = 'UTF-8';
$default_charset = strtoupper($default_charset);  // DO NOT MODIFY THIS LINE, IT IS IMPORTANT
```
b. save the file

Your done. Enjoy!

## You have a modified coreBOS 5.4
There is not much I can say here; you need a developer to weed through the changes and adapt your version with the new changes. We are tending towards making these updates less traumatic but, at this moment, we still have a little bit to go.

Your developer will have to evaluate which of the previous two scenarios is best for him and take it from there.

Remember to install the **coreBOS Updater** and apply all the changes to the database.

## You have your coreBOS 5.4 under GIT version control

This is ideal as you can add a remote to our [GitHub project (https://github.com/tsolucio/corebos)](https://github.com/tsolucio/corebos) and follow our development as we move along. You still have to play around with the code and apply patches but GIT is going to help you a lot.

So the steps here are identical to the three situations described before just that GIT will do the patching for you and help you along the way once you have added the remote link.

**REALLY** high level steps would be:

- git remote add corebos [https://github.com/tsolucio/corebos](https://github.com/tsolucio/corebos)
- git merge corebos/master
- fixes conflcts
- execute installupdater.php from the browser
- log in to application and go to the new coreBOS Updater module
- click on Get Updates
- click on Apply All

<div class="notices red">
Remember to apply the database changes using <strong>coreBOS Updater</strong> and to manually change your config.inc.php, for speed optimization we require adding a line to your config.inc.php, <strong>THIS IS VERY IMPORTANT</strong> or some parts of the application may not work correctly.<br></div>

1. edit config.inc.php and look for the lines 
```
// default charset default value = 'UTF-8' or 'ISO-8859-1'
$default_charset = 'UTF-8';
```
note that your value may be different from UTF-8, now add this line after the assignment
```
$default_charset = strtoupper($default_charset);  // DO NOT MODIFY THIS LINE, IT IS IMPORTANT
```
so it all ends up looking like this:
```
// default charset default value = 'UTF-8' or 'ISO-8859-1'
$default_charset = 'UTF-8';
$default_charset = strtoupper($default_charset);  // DO NOT MODIFY THIS LINE, IT IS IMPORTANT
```

2. save the file


</div>