---
title: 'Record Versioning'
metadata:
    description: 'There is a new feature in coreBOS that permits users to save different versions of one record.'
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
        - recordversioning
---

There is a new feature in coreBOS that permits users to save different versions of one record. Each version is a new record by itself but it is not shown as such. You can't see it in the ListView nor search for it, because of all the versions of a record, only the Active Version is shown. *But how can this new feature be enabled?*

It's easy. You have to go to the Integrations panel (CRM URL/index.php?action=integration&module=Utilities) and enable Record Versioning for one or more modules.

![](screenshot_from_2019-06-19_11-42-23.png?width=60%)

From a technical point of view enabling Record Versioning for a module, let's say Potentials becomes possible through :

-   the creation (if it does not already exist) of a Global Variable of type RecordVersioningModules. If the record is already present, it only edits the module list field adding the Potentials module.

![](screenshot_from_2019-06-19_11-48-11.png?width=70%)

-   the creation of a Business Action record (if it does not already exist). If the record is already present, it edits the module list field adding the Potentials module. This Business Action creates the Developers block in the DetailView of the module.

![](screenshot_from_2019-06-19_11-50-57.png?width=70%)

![](screenshot_from_2019-06-19_11-52-44.png?width=70%)

-   the creation of two new fields for the module: Version and Active Version in which we save respectively the Version Number of the current record and 1/0 for the version status (Active or not)

-   the creation of a new event handler in order to filter the ListView records based on the Active version field. As we stated at the beginning of the article, you can only see or search the active version of the record in the ListView.

![](screenshot_from_2019-06-19_12-44-36.png?width=70%)

![](screenshot_from_2019-06-19_12-45-09.png?width=70%)

-   the creation of a workflow and task that sets the Version and Active Version at 1 in the first save of the record.

![](screenshot_from_2019-06-19_12-05-14.png?width=70%)

*Disable Record Versioning*

If you want to disable the Record Versioning feature for a module you can go into the Integrations panel and just do it.

The module will be removed from the module list fields in the Global Variable and Business Actions modules.

The workflow will be deleted and the handler won't be used anymore for that module because it is based on the Global Variable module list.

*How to use the Record Versioning?*

That's even easier. Now you have the developers block in the DetailView of the module and you have two links: Create Version and Recover Version. The first is used to create a new version of the record and save it while the second recovers an older version. It means that it sets an older version of the record as the active one. You can double click on the version you want to recover too.

**Recover**

![](screenshot_from_2019-06-19_12-25-28.png?width=70%)

**Create**

![](screenshot_from_2019-06-19_12-25-07.png?width=70%)

Record Versioning uses the [duplication business map](../../02.business-maps/08.duplicaterecords) which permits us to fine-tune the related records that need to be versioned also.

Record versions will be respected also when using the Duplicate Records workflow task of the record can also be done by using a Duplication Map. You can find more information about this on the page below:

