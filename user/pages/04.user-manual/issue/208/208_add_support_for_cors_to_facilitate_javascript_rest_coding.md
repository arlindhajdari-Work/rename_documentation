---
title: '208: Add support for CORS to facilitate javascript REST coding'
metadata:
    description: '208: Add support for CORS to facilitate javascript REST coding'
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

[Cross origin resource sharing](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)

We have added a Global Variable which must contain the list of valid domains/IPs we will accept webservice requests from.

The variable is called *Webservice_CORS_Enabled_Domains*

The variable can have two types of values:

- asterisk * which means that all origin domains are accepted
- a space or comma separated list of domains that will be searched for inclusion