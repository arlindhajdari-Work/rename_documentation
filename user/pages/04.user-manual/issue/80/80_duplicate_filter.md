---
title: '80: Duplicate Filter'
metadata:
    description: '80: Duplicate Filter'
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
        - filter
    tag:
        - filter
---

## Detailed Explanation

Adds a **"New"** button to the filter configuration page. You can now edit any filter, change the name and any other coniguration you require and click the **"New"** button to create a new filter, effectively implementing the Duplicate Feature with ease.

![](duplicatefilter.png?width=100%)
