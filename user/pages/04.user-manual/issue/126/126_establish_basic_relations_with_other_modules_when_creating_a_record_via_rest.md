---
title: '126: Establish basic relations with other modules when creating a record via REST'
metadata:
    description: '126: Establish basic relations with other modules when creating a record via REST'
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

[plugin:youtube](https://youtu.be/yGpzPTmvyhA)

Simply passing a new parameter called **relations** which can be a comma separated list of REST IDs of the records you want to relate.
