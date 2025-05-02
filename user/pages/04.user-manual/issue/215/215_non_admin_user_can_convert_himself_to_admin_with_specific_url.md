---
title: '215: Non admin user can convert himself to admin with specific URL'
metadata:
    description: '215: Non admin user can convert himself to admin with specific URL'
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

[vtiger CRM Trac Ticket](http://trac.vtiger.com/cgi-bin/trac.cgi/ticket/7714)

## Detailed Explanation

A specifically crafted URL from a user logged in to the application permits the user to promote himself to admin role and also change the value of **ANY**field on other users profile.

The URL is basically calling the inline Detail View Ajax edit functionality

The patch committed solves both problems by limiting the editing to current user and admin users and also limiting the edition of the is_admin field only to users with administrative privileges.

Thank you *Muhammed Abdul Salim* for reporting this.