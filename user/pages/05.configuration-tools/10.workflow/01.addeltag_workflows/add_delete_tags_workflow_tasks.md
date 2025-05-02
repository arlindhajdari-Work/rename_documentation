---
title: 'Add/Delete Tags Workflow Tasks'
metadata:
    description: 'This workflow task permits you to add or delete tags on the object being saved.'
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
        - adminmanuals
        - workflows
    tag:
        - add
        - delete
        - workflow
---

This workflow task permits you to add or delete tags on the object being saved. Either associated to the current user doing the operation or massively to all users.

This is very useful for filtering and segmenting your clients that are coming in through the webform, for example.

The workflow task in itself is simple; you select:

- the action to do: **add or delete**
- for whom to do it: **all users or only current user**
- list of **space-separated tags** to work with

![](tag_task.png?width=100%)

<br>
------------------------------------------------------------------------

[Next](../04.relateproductservice_workflows) | Chapter 7: Related Product/Service Workflow Task.

------------------------------------------------------------------------