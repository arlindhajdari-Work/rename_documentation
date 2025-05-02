---
title: '127: Enhance REST query language to support related entities'
metadata:
    description: '127: Enhance REST query language to support related entities'
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

## Detailed Explanation

### Related Entity Query Syntax

[plugin:youtube](https://youtu.be/5B0A6IPMnJM)


Constructing on top of the [getRelatedRecords](../../../../../../10.developer-guide/02.webservice-development/06.getrelatedcontrols) function we have extended the REST query syntax to benefit from that functionality, making it easy to query related entities and filter them also.

The new syntax enhances the where conditional statement to support module names preceded with the *"related"* string and followed by the id of the entity:
```
where related.modulename=id
```

Examples:
```
select * from projecttask where related.project=30x144
select * from projecttask where related.project=30x144 and projecttaskname='dsf'
select * from documents where related.accounts=3x12
select * from documents where filelocationtype='E' and related.contacts=4x22
Select * from Documents where (related.Contacts='4x22') AND (filelocationtype LIKE '%I%') LIMIT 5;
select * from modcomments where related.helpdesk=9x114
select * from modcomments where related.helpdesk=9x114 and commentcontent like 'hdcc%'
select * from products where related.products=6x58 // only product children are accessible with this syntax
select * from products where related.contacts=4x22  // only directly related products
select * from products where related.contacts=4x22 and productcategory='Software'  // only directly related products
Select * from Products where related.Contacts='4x22' LIMIT 5;
Select * from Products where related.Contacts='4x22' order by productname LIMIT 5;
```

- queryparameters support limit and offset for those sets of related records where the total count is very high or simply high enough to want to be able to page through.
- queryparameters support column definitions, reducing the size of information being returned
- **multiple entities, IDs or related modules** are **NOT** supported with this API. We have created the extended query language functionality, based on Query Generator for this.

There are a few restrictions we couldn't overcome:

- only one related entity may be used, as the getRelatedRecords function works with only one entity ID, we inherit this restriction. If more than one is put in the query, only the first is used and the rest are ignored and eliminated.
- the product relation is limited to directly related records, which means that on a contact we will only have access to the ones on his +info tab, or for a product we can only see it's bundle child products.
- advanced filtering (limited by current query syntax)

<div class="notices blue">
The Webservice extended query language functionality, based on Query GeneratorQuery overcomes some of these limitations.
</div>