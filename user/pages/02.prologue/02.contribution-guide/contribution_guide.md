---
title: 'Contribution Guide'
metadata:
    description: 'How to contribute to the coreBOS Open Source project.'
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
        - howto
---

## Contribute to the coreBOS Open Source project

**coreBOS** is a git based open source project. That means that contributing to the project is basically the same as for any other git based project. The workflow applied is the typical [Forking Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow).

There are a dozen concepts you need to know to get your head around the initial learning curve. Those are explained in detail in the [developer getting started guide](../../03.getting-started/03.develinstall/item.md).

For every change you want to implement you start from the master branch, which is the default branch, you create a new branch, develop what you need, with as many commits and time as you need, when you have it finished, tested and all committed you push it to Github.

Now go to GitHub and you will see the option to create a Pull Request from your branch. I will get notified, I will study your changes, comment, and maybe ask you to make some more changes for which you will need to checkout your branch again and add them there, when you push them, GitHub will update the PR. I will finally accept your changes and incorporate them into the main master branch.

Once that happens you update your fork and your master branch gets the changes so your branch is not needed anymore and you can delete it.

Then you start all over again.

 ! Remember: the above is the normal [Git Pull Request Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow).

Let's see that explanation in git commands. Let's suppose I have a coreBOS fork on https://github.com/joebordes/corebos and I want to develop a new feature. That would look something like this

```shell
cd /var/www
git clone https://github.com/joebordes/corebos cbjoebordes
chgrp -R www-data cbjoebordes
> Install coreBOS
mv 123456789.install install
mv 123456789.install.php install.php
git checkout -b new_feature
> Develop and test here
git push
git checkout master
> Wait for approval
> I ask for some additional adjustments
git checkout new_feature
> Make change, test and commit
git push
git checkout master
> I accept your change
git pull upstream master
git branch -d new_feature
> Start all over again
```

Obviously you can have as many branches as you need at the same time, developing many features in parallel.

If you need to update your branch with the latest changes from the main stream master branch you would launch a **merge** command. When you launch the _git branch -b_ command to create a new branch that branch starts from the state the master branch is in at that moment. Let's suppose that it takes you a few days to finish your feature and in that time coreBOS has added a few more commits and you need to add these changes to your branch before pushing, to do that we would execute:

```shell
git checkout master (just to make sure)
git pull upstream master  (we get the new changes)
git checkout new_feature
git merge master
> Fix conflicts if any appear
```

The new commits are now also in your branch

 ! Thank you for contributing to coreBOS Open Source project!

### Some last comments

#### Conflicts: Mergetool

When doing the pull and merge it is possible that you run into some
conflicts. That means that you are changing a file that has changed in
the main repository. It is your responsibility to fix that, because you
are the one who knows what your changes are about. To make this process
easier git has a syntax that helps you, but I usually configure merge
tool with [meld merge](https://meldmerge.org/) like this

`git config --global merge.tool meld`

which gives me a nice graphical interface to resolve conflicts.

#### All installs under git control

I would recommend you put all your installs under git control, that way
moving changes around and keeping them all up to date is extremely easy.
For example, let's suppose that I get a new project, a client that wants
to make some changes to coreBOS for their particular needs. I Will
create a new git repository for them, I will merge in the latest version
of coreBOS, at that point my local clone of their repository has two
remote repositories, their private repository, and the GitHub upstream
open source project. I start developing and find an error in coreBOS or
I see a feature that should be available for everybody, I can
cherry-pick the relevant commits or simply develop the changes directly
in the open source project and then pull them in to the private
repository, this is all just as simple as the workflow I explained above
about branching and pull request.

But even more, when this client starts working with coreBOS, after a few
weeks he runs into an error that we have already fixed in the
mainstream, it is just as easy to upgrade their private repository with
a pull as we did above to update the master branch. Incredibly powerful!

#### config.inc.php: config-dev.inc.php

 !! The config.inc.php file must NEVER be in any commit you make on the main project. I will not accept any pull request that contains any modifications to this file.

This file is different on all coreBOS installs. It starts empty on the main repository and gets modified when you install the application. These changes are specific to each install, so if we make any modification to them we will be causing git merge conflicts for everyone and those conflicts will mostly be resolved by keeping their particular version.

The recommended procedure to manage these files is to version them in
the main repository of the install. As recommended above, each coreBOS
install should have its own repository and pull in changes from the main
coreBOS repository. So you will version the config.inc.php file in the repository of the install. This way you have
this important file controlled for each install and coreBOS main repository will not modify them. Obviously, your repository should not be publically accessible as this file contains passwords.

Now this brings us to one problem. When a developer who needs to work on the project clones the install locally they need to modify config.inc.php to adapt it to their development environment, this requires modifying config.inc.php and could lead to a mistake where you commit the file and break the production installation. To avoid this, config.inc.php includes the file **config-dev.inc.php** at the end of the script. This file is ignored by the .gitignore file so it will never be committed and will only be on each local development machine that needs it. This file will permit us to override any settings in config.inc.php without having to modify that file.

The **config-dev.inc.php** template I use is this one:

```php
<?php
error_reporting(-1);
ini_set('display_errors', 'on');
$site_URL = 'http://localhost/coreBOSwork';

// root directory path
$root_directory = __DIR__.'/';

$dbconfig['db_name'] = 'database name';
$dbconfig['db_username'] = 'database user';
$dbconfig['db_password'] = 'database password';

$dbconfig['db_server'] = 'localhost';
$dbconfig['db_hostname'] = $dbconfig['db_server'].$dbconfig['db_port'];
$hostname=$dbconfig['db_hostname'];
$LOG4PHP_DEBUG = true;
//$default_language = 'en_us';
?>
```

#### No private repository

Another situation that appears from time to time is when you don't have a private repository for your install, you just clone the main repository from GitHub, install it, and work there. In this case, both config.inc.php and tabdata.php appear in the "git status" commands and are always there as you can't commit them. You have two alternatives:

* one is just ignoring them, it really isn't that much noise and you get used to seeing them there
* the other is to [tell git to not show them to you](https://stackoverflow.com/questions/13630849/git-difference-between-assume-unchanged-and-skip-worktree/13631525#13631525) with the command: `git update-index --skip-worktree config.inc.php tabdata.php`

## Study git

Git is much more complex and flexible than what I explain here, but in the end you usually use the same commands over and over. I still recommend dedicating time to studying git but take your time one step at a time, let the concepts sink in, it is really a very powerful tool and a great investment in your knowledge.

There is a lot of documentation and examples on the internet so look there for guidance and also join our [gitter group](https://gitter.im/corebos/discuss) where we have close and quick chats about development.

## Contributor License Agreement (CLA)

 !!! We aren't doing this due to the small amount of contributors we have. We SHOULD be doing it though.

* Fill out a [Contributor License Agreement](../cla). If your contribution is happening on behalf of a company, they should sign a [Corporate Contributor License Agreement](../cla)
* Please complete, sign the form, scan it and [send it to us via email](mailto:corebos@tsolucio.com)
* We'll process it, and send you an introduction email
* You'll then appear as a approved contributor

## Contribute to any of the coreBOS Open Source modules

This is mostly the same exact process as explained above and that you would do with any other open source project.

* find the repository of the module
* clone it in some directory
* zip the contents and install the module using the module manager
* that will copy the modules/{modulename} directory to modules in your coreBOS development install
* that will copy the templates directory into Smarty/templates/modules/{modulename} (if it exists)
* develop the changes you need
* copy the modified files to your clone, branch, commit, push, and create the pull request
* **note:** if you modify the manifest.xml file you must update both the one inside modules/{modulename} and the one at the root of the repository. Both should always be the same.

## Contribute to the coreBOS Open Source Documentation project

Read all about our documentation project on the [documenation page](../03.documentation/item.md)

## Additional Reading

* [I thought I understood Open Source. I was wrong](https://hackernoon.com/i-thought-i-understood-open-source-i-was-wrong-cf54999c097b)
* [Effective Ways to Get Help from Maintainers](https://www.snoyman.com/blog/2017/10/effective-ways-help-from-maintainers)

