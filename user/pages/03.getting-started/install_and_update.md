---
title: 'Install and Update'
metadata:
    description: 'How to install and update the application'
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
        - getting-started
---

How to install and update your coreBOS application.

===

## Download

[Download the code from github](https://github.com/tsolucio/corebos)

We make changes every day so you can apply the above procedure every day
to get the latest changes. Note that the application version numbers are
TOTALLY irrelevant, they have no meaning at all except for marketing.

The ideal situation is that you have your install under git control.
That means that instead of downloading the zip from github you executed
"`git clone`", if you did that, updating the code to the latest release is
just "git pull". Then you launch the updater and you are done

In other words, once you are on coreBOS there is no more migration
scripts nor version numbers there is just: update code and apply
changes, forever...

## Install

[Install coreBOS](02.installation)

## Update from vtiger CRM

- [Upgrade from vtiger CRM 5.4.0 and 5.x to coreBOS](04.upgradevtigercrm5)
- [Migrate from vtiger CRM 6.x to coreBOS](05.upgradevtigercrm67)
