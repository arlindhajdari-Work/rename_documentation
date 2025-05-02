---
title: 'Development Guidelines we try to adhere to'
metadata:
    description: 'On this page you will find a set of code rules and general development workflow we try to impose in the coreBOS project.'
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
        - contribute
    tag:
        - guidelines
---

On this page you will find a set of code rules and general development
workflow we try to impose in the coreBOS project. I strongly recommend
that all developers who want to contribute to the project read these
guidelines and try to apply them as much as possible. I will take them
into consideration at the moment of accepting code contributions.

In general I am paraphrasing the [PHP FIG -
RECTIFIED](https://github.com/php-fig-rectified/fig-rectified-standards),
[PHP-FIG Standards Recommendations](http://www.php-fig.org/psr/), and
[Produccing Open Source Software](http://producingoss.com/), but with
some minor adjustments to the reality of our code base. So anything you
read there is useful.

<div class="notices blue"> 
I am open to suggestions and comments and I know this is a living document that may change as we go forward, so don't hesitate to contact me. </div>

Where developers dwell
----------------------

The best place to contact the developer community is [on our gitter chat group](https://gitter.im/corebos/discuss).

The [blog](https://blog.corebos.org) is mostly developer oriented and there is a lot of information here on the documentation site.

You can [ask in the forum](http://discussions.corebos.org/) also, but don't hesitate to get in touch, we are a really **friendly and helpful community**.

How to Contribute
-----------------

The project lives on github and we recommend following the typical fork
and pull request procedure. [Read here for the exact steps.](../../../02.prologue/03.documentation)

Bug Reports
-----------

Use [the github issues section](https://github.com/tsolucio/corebos/issues) (prefered) or the
Mantis bug tracker. [Read here for some additional ideas.](../../../11.others/04.devel/08.bugreport)

Code Formatting and Structure
-----------------------------

In general the next sections apply both to PHP and Javascript code. Each
has their own particularities, but we should try to be as consistent as
possible.

### PSR-0/PSR-4: Autoloading Standard

We are currently not following this recommendation. We load the files we
need using require or include from wherever they have been added in the
project.

We will probably get to this in the future but it is not a high priority
right now.

### Basic Coding Standard

[PSR-2: Basic Coding Standard](http://www.php-fig.org/psr/psr-1/)

-   Files MUST use only &lt;?php tags, no short tags nor any others
-   Files MUST use only UTF-8 without BOM.
-   Files SHOULD either declare symbols (classes, functions, constants,
    etc.) or cause side-effects (e.g. generate output, change .ini
    settings, etc.) but SHOULD NOT do both. This is a good
    recommendation but it is not present at all in our code base, so if
    you follow it fine, if not it's ok.
-   <s>Namespaces and classes MUST follow an "autoloading" PSR: [PSR-0, PSR-4].</s>
-   Class names MUST be declared in *StudlyCaps*.
-   Class constants MUST be declared in all upper case with underscore separators.
-   Method names MUST be declared in *camelCase*.

### Coding Style Guide

[PSR-2: Coding Style Guide](http://www.php-fig.org/psr/psr-2/)

-   Code MUST use 1 tab for indenting, not spaces. [Reasoning behind it and a Spaces-vs-Tabs and Brace-Styles evaluation](https://github.com/php-fig-rectified/fig-rectified-standards/blob/master/Reasoning.md)
-   There is a recommended hard limit on line length set to 180; the
    soft limit MUST be 170 characters; lines SHOULD be 80 characters or less.
-   There MUST NOT be trailing whitespace at the end of non-blank lines.
-   There MUST be one blank line after the namespace declaration, and
    there MUST be one blank line after the block of use declarations.
-   Visibility MUST be declared on all properties and methods; abstract
    and final MUST be declared before the visibility; static MUST be
    declared after the visibility.
-   Control structure keywords MUST have one space after them; method
    and function calls MUST NOT.
-   Opening braces for classes, methods, functions, and control
    structures MUST go on the same line, and closing braces MUST go on
    the next line after the body.
-   Opening parentheses for control structures MUST NOT have a space
    after them, and closing parentheses for control structures MUST NOT
    have a space before.
-   Strings should be enclosed in SINGLE QUOTES where possible.

The [Nextcloud coding style is a very sane set of rules also](https://docs.nextcloud.com/server/14/developer_manual/general/codingguidelines.html)

Error Reporting
---------------

All development MUST be done using **error_reporting set to E_ALL**
and we should not leave any warning nor notice in the code. They must
all be eliminated.

If you run into a part of the code that emits a lot of warnings, either
dedicate some time to eliminating them or send me the details and I will
take care of it.

MySQL Strict
------------

All development MUST be done using **MySQL Strict Mode** and we should
fix any SQL commands that we create.

If you run into a part of the code that has some SQL Strict error,
either dedicate some time to eliminating it or send me the details and I
will take care of it.

Security
--------

Security is a very complex **and important** issue which requires a lot
of dedication and time. In other words, **dedicate time to studying and
understanding security issues**.

- use vtlib_purify on all incoming and outgoing information
- user Vtiger_Request to construct URLs

[Read the Nextcloud recommendations](https://docs.nextcloud.com/server/14/developer_manual/general/codingguidelines.html)

Commit Guidelines
-----------------

### BEFORE Committing

This is a [list of things that you MUST do before executing a commit](https://github.com/tsolucio/corebos/issues/911#issue-719191770):

- *git diff* check all the files that have been modified, read the diff, and mentally review the change. eliminate debug messages and passwords.
- Check for debug messages you may have left behind. Before I launch a commit I usually execute these commands:

```
git diff {files} | grep dump
git diff {files} | grep fatal
git diff {files} | grep log
```

- Check for php errors

```
for f in {diff file list}; do php -l $f; done;
```

- *git status* any new/untracked files to add?
- Any strings that should be translated?
- If you alter an existing function, did you check if all the existing references to that function will still behave the same way?
- If you created new code, did you try and use existing functionality as much as possible?
- [code formatting](item.md#code-formatting-and-validation-tools)
- Ideally you should run a lint process on both PHP and javascript. Please look below for the tools we use and how to execute them. I will add it to the Pull Request acceptance process at some point.
- see the checkfile executable below
- Did you execute the unit tests and/or e2e tests?
- **git add -p** to separate commits into semantically meaningful chunks. Check if you must separate the code changes in various commits. When I program I usually make some cosmetic changes or modifications that are not related to the requirement I am implementing. You can use the "-p" directive to split unrelated changes creating concise and cohesive commit changes.
- dedicate a moment to [think about the commit message](item.md#commit-guidelines)
- Any documentation that should be added to the wiki?

### Commit Guidelines we try to adhere to

[AngularJS Git Commit Message Conventions](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/mobilebasic?pli=1)

```
<type>(<scope>) <subject>
```

another way of reading that is:

```
what(where) how
```

in this second form, the when and who are controlled by git itself, so sign your commits.

Some additional clarifications:

- Any line of the commit message cannot be longer 100 characters! This allows the message to be easier to read on GitHub as well as in various git tools.
- Allowed **< type>**
  - **feat**: feature
  - **adapt**: this is a feature, but it only affects a particular install, not the whole coreBOS project
  - **fix**: bug fix
  - **security**
  - **i18n**: translation strings and enhancements
  - **docs**: documentation
  - **style**: formatting, missing semi colons, ...
  - **refactor**: code refactor
  - **test**: when adding missing tests
  - **chore**: maintenance tasks
- Allowed **< scope>** could be anything specifying place of the commit change. For example a module name, webservice or functional feature
- **< subject>** line contains succinct description of the change. Use imperative, present tense: "change" not "changed" nor "changes".
  - If the commit fixes or is related to a ticket put the title or a summary of it, the actual ticket number is rather useless as time has taught me that ticket systems come and go while code and commit messages persist.

### Special Committs

#### Service Worker Commit

These are the steps to update the service worker:

```shell
fold service-worker.js > sold
include/sw-precache/regen_swprecache
fold service-worker.js > snew
meld sold snew
# make sure the update is about the files you know have changed
# the typical error here is for the update to include some javascript or css code you have not committed yet
rm sold snew
```

**Always** commit the service worker update in it's own commit. Do not
mix it with any other changes. This way we can safely ignore all those
commits when searching, or easily locate changes when needed.

Code Formatting and Validation tools
------------------------------------

We recommend and use these tools to help validating the formatting issues in PHP and Javascript files.

- [PHP Code Sniffer](https://github.com/squizlabs/PHP_CodeSniffer) for PHP
- [ESLint](https://eslint.org) for Javascript
- [PHP Mess Detector](https://phpmd.org/)
- [PHP Doctor](https://github.com/voku/PHPDoctor) We must start seriously using this and applying type definitions to our code as we move towards PHP 8 and above

You can find rulesets for the above guidelines in the build/cbSR directory.

For example, to validate a PHP file you can execute:

```shell
./phpcs.phar --standard=build/cbSR file_to_validate
```

You could also execute this command on javascript files, but eslint is better:

```shell
eslint -c build/cbSR/eslintrc.js file_to_validate
```

<div class="notices blue"> You can use phpcbf and the `eslint --fix` to get changes applied automatically </div>

I actually bundle phpcs and phpmd in one file (checkfile) that I use to validate my php files:

```shell
echo ======
echo $1
echo ======
phpcs.phar --standard=/var/www/coreBOSwork/build/cbSR $1
phpmd.phar $1 text unusedcode
php -l $1
```

Some important management recommendations
-----------------------------------------

- Custom modules:
  - Each module must have it's own repository
  - You must try to keep the modules' repository in sync with the installs where it is in production
  - Since that is a bit difficult what I do is update them when I need to install them somewhere
  - [Register your module in the extensions section](../../../08.extensions-integrations/01.corebosmodules/) so it can be found in the future. You can [use the helper scripts](../../../10.developer-guide/04.development_framework/06.helperscripts/item.md#composer2readme-and-module2wiki).
- There **MUST NOT** be any unversioned changes in production. This is MANDATORY
- For EVERY change or customization that you have to do in coreBOS, challenge yourself to find a way to make that change without modifying one line of base code that you can find in the github repository. You will be surprised how much can be done, you will learn a lot and have much more fun :-)

References and further reading
------------------------------

- [Debugging](../14.commitguidelines)
- [How to Contribute](../../../02.prologue/03.documentation)
- [Bug Reports](../../../11.others/04.devel/08.bugreport)
- [PHP Framework Interop Group](http://www.php-fig.org/)
- [PHP Framework Interoperability Group - RECTIFIED](https://github.com/php-fig-rectified/fig-rectified-standards)
- [Produccing Open Source Software](http://producingoss.com/)
- [AngularJS Git Commit Message Conventions](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/mobilebasic?pli=1)
- [PHP Code Sniffer](https://github.com/squizlabs/PHP_CodeSniffer)
- [ESLint](https://eslint.org/)
- [Writing Consistent, Idiomatic JavaScript](https://github.com/rwaldron/idiomatic.js)
- [JavaScript, The Right Way](http://jstherightway.org/)
