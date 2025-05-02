---
title: '200: Add support for translating from inside the application'
metadata:
    description: '200: Add support for translating from inside the application'
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
        - issue
---

## Detailed Explanation

### Translating

[Based on Produccing Open Source Software](https://producingoss.com/en/share-management.html#translation-manager)

### Translating Application
**Translating from within the application**

Thanks to the team at **OpenCubed** who have modified an abandoned project of many years ago, starting at **coreBOS 5.6**, we have the functionality to translate the labels from within the application.

This is specially important for custom fields, because we cannot use special characters that are so important in many language either in the labels or the picklist values. Due to that restriction we have to use plain text and then translate the values. Before having this functionality that translation had to be done directly editing the language files, now the admin user can easily do the change without needing access to the files.

To access the translator you must login as an admin user and go to the **Module Manager**. On the **Custom Modules** tab we will find the language files and next to each one the hammer icon will take us to the translation screen.

![](tag_task.png?width=100%)

The translator permits us to select from among the different modules and base language files to translate and shows us the full list of labels with their value in the base application language followed by the translation which you can modify accordingly.

![](tag_task.png?width=100%)

**Translating using version control system (GIT)**

Git/Subversion control all the file changes that occur in the project so it is very easy to ask them for the exact set of changes that have been applied to the language file of reference. Once we have that we can apply those changes to our translation.

First we need to know what revision we are on or which was the last revision we translated from. In the second case you will have to save that information somewhere, in the first case we can ask the code control system like this:

```
git show --oneline -s
```
the first number is the commit we are on

or
```
svn info
```
there will be a line that indicates the revision we are on.

Let's call this revision **rorg**

Now we can update our code:

```
git pull
```
or
```
svn up
```

Next we need a list of all the translation files that have changed. For that we can ask git to show us all the files that have changed since **rorg** and our current state and we pass that through a **grep** to get only the files we are interested in:

```
git log --name-only rorg.. | grep fr_fr
```
Now for each reference language file we have to see if it has had any changes. For example, for the file include/language/en_us.lang.php you would execute
```
git diff -r rorg.. include/language/en_us.lang.php
```
or
```
svn diff -r rorg:HEAD include/language/en_us.lang.php
```
Apply the changes, if any, to your translation files and translate.

**Test and verify**

**Starting a new language**

The high level steps are:

- choose your reference language. Make sure this language is **TOTALLY** translated and complete
- find all the files of your reference language and make a copy of each file in the exact same directory with the exact same name but changing the language prefix
- edit the manifest file in the include/language directory and adapt it accordingly
- install the language in the application
- select your language in Preferences
- edit each language file for your prefix
     - change the license accordingly
     - translate
     - test
- package and distribute

Let's get into some details. Let's suppose that I want to create an Italian translation starting from the Spanish es_es translation.

This linux command, executed from the root of a coreBOS installation obtains all the translation files that exist:

```
find . -name "*es_es*"
```
based on that the next script will find all these files and create the new language for you
```php
#/bin/bash
echo    
if [ $1. = "." -o $2. = "." ]
then
        echo "This script creates a new language from and existing one"
        echo "It requires two parameters:"
        echo " - reference language prefix: es_es for example"
        echo " - destination language prefix: it_it for example"
        echo
        echo "It must be executed from the root of the coreBOS installation"
        echo "You can read more about it here: http://corebos.org/documentation/doku.php?id=en:devel:translating&#starting_a_new_language"
else
        reffiles=`find . -name "*$1*"`
        if [ "$reffiles." = "." ]
        then
                echo "Reference language files cannot be found"
        else
                cnt=`find . -name "*$1*" | wc -l`
                if [ $cnt -lt 65 ]
                then
                        echo "Low number of reference files: $cnt. Your reference language is probably missing some translations!"
                else
                        for lng in $reffiles
                        do
                                dstfile=`echo $lng | sed s/$1/$2/`
                                cp $lng $dstfile
                        done
                fi
        fi
fi
echo  
```

You should be able to find this script in the build directory of coreBOS

Calling this script like this will create the Italian it_it language from the Spanish es_es translation:

```
build/createLanguage.sh es_es it_it
```
Now edit the manifest file in the include/language directory and adapt it accordingly. Basically change the license and the elements:

```php
<name>Spanish</name>
  <label>ES Spanish</label>
  <prefix>es_es</prefix>
```
<div class="notices red">
It is very important that you respect the exact structure of the file, everything has it's reason and must be respected. Only change the text contained inside the XML elements.</div>

With that done, we can now install the language in the application, which would be accomplished calling the **importManifest** method of the Package class, like this:

```php
<?php
// Turn on debugging level
$Vtiger_Utils_Log = true;

require_once('vtlib/Vtiger/Module.php');
require_once('vtlib/Vtiger/Package.php');

global $current_user,$adb;
set_time_limit(0);
ini_set('memory_limit','1024M');
$current_user = new Users();
$current_user->retrieveCurrentUserInfoFromFile(1); // admin
$package = new Vtiger_Package();
$rdo = $package->importManifest('include/language/it_it.manifest.xml');
?>
```

Log into the application, select your language in Preferences and proceed to edit and test the translation either directly in the files with your favorite editor (remember to use UTF8) or through the translation manager in Settings.

Finally, [package and distribute](../../../.../../../../../10.developer-guide/04.development_framework/11.develtutorials/05.packagemodules)
