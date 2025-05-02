---
title: 'coreBOS Translation Module'
metadata:
    description: 'coreBOS Translation Module'
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
        - language
    tag:
        - i18n
---

### Pros

- **add strings to other modules with no code changes**
- **more control of labels: avoid duplicates**
- **Import/Export**
- **all module advantages: mass edit, deduplication**
- **modify any label easily**
- **easier to translate: external tools**
- **correct functionality of picklist search**
- **possibility to translate values on modules, not just labels**
- **Support for using Accept-Language header when fetching required language:** ***[getLanguage](https://github.com/tsolucio/corebos/blob/master/modules/cbtranslation/cbtranslation.php#L178)***
- **Support for contextual and plural translations with full sprintf syntax (see syntax below)**
-  **Full support for getting plural cases in 144 languages based on** ***[http://docs.translatehouse.org/projects/localization-guide/en/latest/l10n/pluralforms.html?id=l10n/pluralforms](http://docs.translatehouse.org/projects/localization-guide/en/latest/l10n/pluralforms.html?id=l10n/pluralforms)***
- **Full backward compatibility**

### Cons

- **harder to install new language file: could be fixed easily**
- **slower: about 2% (needs validation)**
- **modifying and adding strings is harder: cbupdater?**

### Accept-Language Header

[cbTranslation::getLanguage()](https://github.com/tsolucio/corebos/blob/master/modules/cbtranslation/cbtranslation.php#L178)

Will first try to find a user chosen locale in the user settings.

If none found, it will next try to use the Accept-Language header provided by the browser. This is especially useful in the login screen for multilingual users.

Finally, it will fallback to the global configuration

### Contextual and plural translations

### Context translation

The use of context string lets tuning translation in special cases, e.g. taking care of gender.

### Plural translations

Many languages have different ways of taking plurals into account, from none to 6 plural forms.

### cbtranslation::get()

The [cbtranslation::get()](https://github.com/tsolucio/corebos/blob/master/modules/cbtranslation/cbtranslation.php#L225) method has full support for context and plurals, among other features.

The basic usage is **cbtranslation::get('friend')** that will return the value of 'friend' taken from the module cbtranslation values (equivalent to the previous main translation file in include/language).

Next we can pass in the module as we did before with getTranslatedString, **cbtranslation::get('friend','Users')**, which will return the value of 'friend' taken from the Users module translations entries in the database.

The third parameter is an array with a set of options for the translation.

- language =&gt; &lt;String&gt; language to translate against, if not set $current\_language will be used
- context =&gt; &lt;String&gt; label modifier for specific translation contexts, like gender. The context is simply added after key name separated by an underscore.
- count =&gt; &lt;Integer&gt; label modifier for plurals. Plurals are written following gettext format. For a language with 2 plural forms, you keep KEY\_NAME for singular and KEY\_NAME\_PLURAL for plural. For a language with 3 or more plural forms, it will be KEY\_NAME\_0, KEY\_NAME\_1, ..., KEY\_NAME\_N for each case

Some examples would be:

- **cbtranslation::get('friend','Users',array('language'⇒'en_us'))** which will   search in english
- **cbtranslation::get('friend','Users',array('language'⇒'es_es'))** which will search in spanish
- **cbtranslation::get('friend','Users',array('language'⇒'en_us','count'⇒2))** which will search in english for the plural form of the label: 'friend_PLURAL'
- **cbtranslation::get('friend','Users',array('language'⇒'en_us','count'⇒1))** which will search in english for the singular form of the label: 'friend'
- **cbtranslation::get('friend','Users',array('language'⇒'en_us','count'⇒2, 'context'⇒'female'))** which will search in english for the plural form of the label with 'female' suffix: 'friend_female_PLURAL'

Finally, you can add more parameters to support sprintf formatting like this: **cbtranslation::get('friendcountry','Users',array('language'⇒'en_us','context'⇒'female','count'⇒2),2,'England')**

You can [find a set of examples in our unit test for this module](https://github.com/tsolucio/coreBOSTests/blob/master/modules/cbtranslation/cbtranslationTest.php).

#### Examples

Let's say that we have these values

    'LBL_USER' => 'User',
    'LBL_USER_PLURAL' => 'Users',
    'LBL_USER_MALE' => 'Male User',
    'LBL_USER_FEMALE' => 'Female User',
    'LBL_USER_FEMALE_PLURAL' => 'Many female users',
    'LBL_CONNECTED_USERS' => '%d user is connected',
    'LBL_CONNECTED_USERS_PLURAL' => '%d users are connected',

Calling **cbtranslation::get('LBL_USER', $MODULE)** will return 'User'

Calling **cbtranslation::get('LBL_USER', $MODULE, array('count'⇒$CONNECTED_USERS_COUNT))** will return 'Users' if $CONNECTED_USERS_COUNT > 1 and 'User' if $CONNECTED_USERS_COUNT = 1

Calling **cbtranslation::get('LBL_CONNECTED_USERS', $MODULE, array('count'⇒$CONNECTED_USERS_COUNT),$CONNECTED_USERS_COUNT)** will return for instance '10 users are connected'

Calling **cbtranslation::get('LBL_USER', $MODULE, array('context'⇒'FEMALE','count'⇒$CONNECTED_USERS_COUNT))** will return 'Female User' if $CONNECTED_USERS_COUNT = 1 and 'Many female users' if $CONNECTED_USERS_COUNT > 1

### cbtranslation webservice

There is currently no webservice interface to this module's translation services. We could enhance the webservice getTranslatedString method, which, I think, would be the correct way to proceed.

In the mean time, a normal query should get you the translation you need:

    select i18n from cbtranslation where translation_key = 'friend' and locale='es_es'
    select i18n,Products.productname from cbtranslation where Products.productname = 'Sexy Leggings';

### References

This enhancement to coreBOS is based on the [work of @bertrand.wattel](http://code.vtiger.com/vtiger/vtigercrm/merge_requests/238).

**Thank you very much!!** I'm sure vtiger will pay just as much attention to your effort as I did LOL

[http://code.vtiger.com/vtiger/vtigercrm/merge_requests/238](https://code.vtiger.com/vtiger/vtigercrm/merge_requests/238)<br>
[http://docs.translatehouse.org/projects/localization-guide/en/latest/guide/start.html](http://docs.translatehouse.org/projects/localization-guide/en/latest/guide/start.html)<br>
[http://docs.translatehouse.org/projects/localization-guide/en/latest/l10n/pluralforms.html?id=l10n/pluralforms](http://docs.translatehouse.org/projects/localization-guide/en/latest/l10n/pluralforms.html?id=l10n/pluralforms)<br>
[https://www.i18next.com/plurals.html](https://www.i18next.com/plurals.html)<br>
[https://www.i18next.com/context.html](https://www.i18next.com/context.html)<br>