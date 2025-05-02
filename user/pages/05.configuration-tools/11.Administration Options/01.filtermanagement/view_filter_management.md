---
title: 'View/Filter Management'
metadata:
    description: 'The View Management module permits us to fine tune the sharing rules of filters on each module and a view itself.'
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
        - adminmanual
    tag:
        - filter
---

The View Management module permits us to fine-tune the sharing rules of filters on each module and a view itself.

===

The record has **two "modes"**, one for the settings of a filter and another for the default permissions of the module. This dual mode is defined by the value of the "Default Setting" checkbox.

To set the permission for a view, we uncheck the "Default Setting" checkbox which puts the record in View permission mode. Then we can select the User, Group, or Role for which we want to set the permissions. Finally, we set the CRUD-A permissions and the Default status. We can make this the mandatory setting for the selected User/Group/Role.

If the "Default Setting" is checked then you must select the module for which you want to set the permissions and mark the permission set you want. This will define the default permissions on all views for the selected modules if no other record with specific settings is found.

So, for any view, we can select that view in the initial picklist and then select the user and set the Retrieve, Update, Delete, and Approve permissions that user will have over the filter.

With the "Default Setting" set to true, we can define the **C**reate, **R**etrieve, **U**pdate, **D**elete, and **A**pprove permissions that all users will have over in the module.

## Sync with List View Filters

When a new filter is created on a module, the application will automatically create a cbCVManagement record with these settings:

- User set to the user creating the filter
- SubRoles of the user will be set
- C = F
- R = T
- U = T
- D = T
- A = F
- Default View = F
- Mandatory = F
- Default Setting = F
- Module List = Empty
- Set Public = T

This will permit you to create a workflow that detects the "Set Public" checkbox and send an email to any user who needs to **Approve** the filter for other users.

When a filter is updated, the shared fields are updated.

## Escalation Rules

The escalation process followed to decide if a view is accessible or not is

- search for a mandatory default record
- search for a non-mandatory record that belongs to the role of the user
- search for a non-mandatory record assigned to the user
- search for a non-mandatory record assigned to any group of the user
- search for a non-mandatory record as the default setting for the module
- if no record is found then the ALL view for the module will be returned
- if no record is found then an empty array will be returned

## Set as private

The **set as private** checkbox in filters is a quick way to set a filter as private. This can be achieved by defining specific records in the View Permission module as described above but this makes it easier to override the default "permissive" sharing options of the application.

## Some examples

Watch a quick explanation of the View Permission module showing how it works with some examples.

[plugin:youtube](https://youtu.be/1YNP-6vK1Sc)

## Development

From a developer's point of view, the module gives a set of services:

- **getDefaultView(module, user):** which returns the default view for a module and user
- **getAllViews(module, user):** will return all the views a user has access to on the module
- **getPermission(CustomViewID, user):** CRUD-A permissions on the filter or Module if the filter is ALL

The getAllViews service can be retrieved via the **getAllViewsByModule** web service method.