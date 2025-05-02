---
title: 'Elastic Search/Kibana Integration'
metadata:
    description: 'coreBOS extension to synchronize information with ElasticSearch'
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
        - extension
    tag:
        - module
        - ELK
        - elasticsearch
---

## coreBOS Native Integration Elastic Search/Kibana Integration

This integration adds an event handler script to each module you enable in order to save records of the module in an Elasticsearch index. You choose the query in a Condition Query type map like this:

===

```php
  <map>
    <sql>
    SELECT contactid, contact_no,firstname,lastname from vtiger_contactdetails join vtiger_crmentity on crmid=contactid where vtiger_contactdetails.contactid =?
    </sql>
    <return>recordset</return>
  </map>
```

First, you create the elasticsearch new table by loading and applying the coreBOS updater changeset and applying the DefineGlobalVariable changeset for some new global variables. Then you create the Condition Query map.

After that you have to create 2 or 4 Global Variables based on Elasticsearch configuration of security. 2 are mandatory:

![](esgv1.png?width=100%)

2 are optional if it's Basic Auth enabled:

![](esgv2.png?width=100%)

and after that you configure it like this in Utilities:

![](essetting.png?width=100%)

by enabling the integration **AFTER** selecting the module and the fields.

This adds the event handler script and now if you save a contact record, you see it in an elasticsearch index with a standard name based on the elastic prefix chosen in the Global Variables + module name + index like this `myproject_contactsindex`

<div class="notices blue">For the moment it works with ES >=5 because mapping types (like text instead of string) have changed from version 5</div>

------------------------------------------------------------------------

[Next](../02.elasticsearchexternal) | Chapter 1.2: coreBOS External Integration.

------------------------------------------------------------------------