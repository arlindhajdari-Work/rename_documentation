---
title: 'Summarized Rules'
metadata:
    description: 'Security Guide Summarized Rules'
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
        - security
        - manual
        - securityguide
    tag:
        - guide
        - rule
---

You should configure your system in the following order:

1. **Settings &gt; Users &gt; Admin: On/Off** With marking the Admin checkbox any user will be assigned administration privileges and become an administrator user. Administrator users have unlimited privileges for the CRM. `**Never use a user login with administrator privileges for your daily work with CRM system.**`
2. Except for the case of "Admin: On": `revoked privileges always override granted privileges.`
3. **Settings &gt; Fields Access**: the default organization-wide (or global) field access. It is used to control the visibility of fields in various modules for the entire organization and it `overrides the profile level field access` (see later).
4. Regardless of the organization-wide defaults, users can always view and edit all data (`except` the fields globally disabled in global Fields Access):
  - owned by or
  - shared with users below them in the role hierarchy
  - `if not prohibited by the profile.`
5. By default, **a specific user can view, edit and delete `only` the data sets that are:**
  - owned by the user
  - owned by a group where the user is a member
  - owned by subordinate users
  - or shared to the user
6. **Settings &gt; Sharing Access**
  - **Sharing Access Rules** define default privileges that are valid organization-wide, we have: **Global Sharing Access Rules** and **Custom Sharing Access Rules**.
  - Sharing access rules define the default user access levels to entity records (private or public), but only `if they are not limited by profiles`. This means `privileges revoked by profiles always override` the organization-wide sharing access rules!
  - Sharing rules apply to all existing data and the data which will be added in the future.
  - If you make changes, you must hit the `\[Recalculate\]` button!
  - Sharing Access Rules can be created for the modules we can see on the settings page. There is one special case: Rules created for the Organizations will apply to the Contacts module.

    1.  **Private:** `Only` the record `owner and` users `with a role which is above` that of the record owner's role in the hierarchy can `browse, edit, delete and report` on those records. If an **organization's access has been set to Private, the access to related** opportunities, tickets, quotes, sales orders, purchase orders, and invoices `is also set to private`. You must have at least read access to a record to be able to add activities or other associated records to it.
    2. **Public Read Only:** All users can `view and report on records` but not edit them.
    3. **Public Read/Create:** All users can `view, edit` all records, but they `can not delete` them. Only those given special rights can delete records.
    4. **Public Read/Create and Delete:** All users can `view, edit and delete` all records.
7. **Custom Sharing Access Rules (User defined Sharing Rules):** can be used to selectively grant data access to a set of users (Roles or Groups, but not directly users). This means sharing module related data between Roles and Groups.
  - Custom Sharing Rules can only extend the visibility, but they cannot hide it.
  - Custom Sharing Rules cannot be specified to share data between two users directly.
  - The number of rules defined for a single Role, Role Subordinates or Group is not limited.
8. **Settings &gt; Profile Privileges &gt; "given profile" &gt; Global Privileges: View All and Edit All** Global Privileges are checked next. `If they are enabled, no other security check will be done.` Depending on the settings, any user may view and edit all the data of the CRM System, `except the Settings module`.
9. **Settings &gt; Profile Privileges &gt; "given profile" &gt; Set Privileges for each Module** Revoked Module Privileges in Profiles `override the sharing rules` because the CRM system will not take any sharing rules into consideration.
10. **Settings &gt; Profile Privileges &gt; "given profile" &gt; Set Privileges for each Module** `If` a module privilege `is disabled`, a user cannot view or edit that particular module or cannot delete records of that module.
11. **Roles:** Roles are based on profiles and linked with the hierarchical order of the company. They define the overall privileges for each individual user. Users in any given role can always view, edit and delete all data owned by users below in the hierarchy.
12. **The group system is not a tool for defining security settings.** Rather, user groups are `used to manage the data access, that is, to share records`.
13. **Assigning a Group** to a given entity record **NEVER** `overrides access defined by the profile settings`. If you assign a group to a given CRM data entry all users defined by the group will become the owners of this entry `with all privileges that are defined by the appropriate profile`.
14. Group privileges `may become` restricted by custom (`default`) organization sharing privileges.
15. **Calendar Sharing:** By default, every user's calendar is set to **private**. Other users may see that you have an event scheduled but do not get access to detailed information. You may `share your calendar or specific event entries` with other CRM system users by inviting them.
16. Other users in the role-based hierarchy can also view specific events at another user's calendar if these events have been made public. To make a particular event public, mark the \[Public\] checkbox when you create a new event. A user with a role above in the hierarchy can always see the calendar of subordinates.
17. In addition, you may set up your calendar settings so that your calendar is shared with other users in the hierarchy

------------------------------------------------------------------------

[Next](../LicenseUsageAcknowledgements/) | License and Usage

------------------------------------------------------------------------
