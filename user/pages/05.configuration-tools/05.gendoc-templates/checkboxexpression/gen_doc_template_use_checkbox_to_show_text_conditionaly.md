---
title: 'GenDoc Template:: Use checkbox to show text conditionaly'
metadata:
    description: 'Use checkbox to show text conditionaly.'
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
        - integration
        - contribute
    tag:
        - gendoc
---

- [checkboxes on module template](../checkbox_expression_conditions.odt)
- [checkboxes on module example](../organization_chemex_labs_ltd.odt)

Example of using checkboxes to show different texts in the document

I created a block with 4 checkboxes in Accounts and Contacts.

![checkboxes on module](checkboxesonmodules.png?width=100%)

then I created the template above that uses the values of those checkboxes inside a FOREACH and a simple normal table to show different text.

![checkboxes gendoc example](gendoccheckboxesexampe.png?width=100%)

HTH
