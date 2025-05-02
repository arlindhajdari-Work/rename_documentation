---
title: 'Lead Conversion Options Explanation'
metadata:
    description: 'Lead Conversion Options Explanation'
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
        - faq
    tag:
        - lead
---

<div class="notices blue">
<h2>I define a profile where I deactivate the top options of see and use all and then all the modules except Accounts, Contacts and Leads.</h2>

Then I go to any Lead but the Convert Lead action is not there. Why?

I can only see the link if I activate see and use all, but then I also see al the modules, which I do not want.</div>

===

!!! I just tried and it worked correctly for me.

!!! [plugin:youtube](https://youtu.be/wFnoEiOtNDU)

!!! The problem must be with some field the conversion needs. I had a look at the code and it says that the "Convert Lead" action will be visible when all these conditions are met:

- the user has edit permission on Accounts, Contacts and Leads
- the user must have conversion tool permission in his profile (see image below)
- Accounts and Contacts modules are active
- the Lead hasn't been converted previously
- the field "Company" on the lead is not empty

![](convertleadtoolpermission.png?width=100%)