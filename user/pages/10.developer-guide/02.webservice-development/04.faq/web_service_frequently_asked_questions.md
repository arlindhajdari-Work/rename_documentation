---
title: 'Web service Frequently Asked Questions'
metadata:
    description: 'Web service Frequently Asked Questions'
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
        - development
        - webservice
    tag:
        - faq
---

## Using the count(*) operator in VQL, How do I get the number from the returned result?

<div class="notices blue">
The result returned is an array of one row, that contains an array with one element which is the count result. That result can be accessed as index 0 or with the key 'count':
</div>

```php
array(
   [0] => array(
       [count] => 12
   )
)
```
![](webservicecount.png?width=100%)

<br>
------------------------------------------------------------------------

[Next](../00.manual/04.addws)| Chapter 20: Add web service end points.


------------------------------------------------------------------------