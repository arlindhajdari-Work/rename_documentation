---
title: 'Roundcube coreBOS CRM Integration'
metadata:
    description: 'Roundcube CRM Integration'
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
        - corebosmail
        - integration
    tag:
        - roundcube
---

<div class="notices blue">This project is fully documented and operative at <a href="https://corebosmail.tsolucio.com/">coreBOSMail website</a></div>

With this extensión to round cube you will be able to easily manage your email and synchronize it with your vtiger CRM application. You will be able to upload your emails to the CRM and create many entities from any email.

===

- Select Email &gt; Qualify.
  - Both automatic and manual options are available
  - Attachments respected

![](rcvt_menus.png?width=90%) 

![](rcvt_captureentity.png?width=90%) 

- Tag/Label Message
- Configure access information and functionality options

![](rcvt_config.png?width=90%)

- Auto-fill-in search when sending
  - search To/CC/BCC in Contact
  - search in account, contact and lead
  - search on name, email, secondary email

![](rcvt_autofillin.png?width=90%)

- Autocreate Contact/Account and upload email on send

## Creating entities

You can create various types of entities from an email. These are the ones that are currently supported:

- **Contacts**
  - Firstname, Lastname
  - Email

<!-- -->

- **Accounts**
  - Domain &gt; Accountname
  - Email
  - Firstname, Lastname &gt; Description

<!-- -->

- **Lead**
  - Domain &gt; Company
  - Dmail
  - Firstname, Lastname

<!-- -->

- **Potential**
  - Subject > Name
  - Related To
  - Body > Description

- **Todo**
  - Subject
  - Related To
  - Body &gt; Description

<!-- -->

- **HelpDesk**
  - Subject &gt; Title
  - Related To
  - Body &gt; Description

<!-- -->

- **Project**
  - Subject &gt; Name
  - Related To
  - Body &gt; Description

<!-- -->

- **Project Task**
  - Subject &gt; Name
  - Body &gt; Description

## Attach documents that are in vtiger CRM

**on todo list/wish list**

------------------------------------------------------------------------

[Next](../06.sendgrid) | Chapter 6: Sendgrid-coreBOS Integration

------------------------------------------------------------------------