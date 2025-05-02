---
title: '123: Enhance field information returned from REST interface'
metadata:
    description: '123: Enhance field information returned from REST interface'
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

### Detailed Explanation

For certain external applications the information given by the REST interface referent to the fields is insufficient to be able to order them on screen by their order defined in the application and also about complete information about their type.

Before this patch the information returned looked like this:

```
{"name":"firstname",
"label":"First Name",
"mandatory":false,
"type":{"name":"string"},
"nullable":true,
"editable":true,
"default":""}
```

After the patch we get this structure: 

```
{"name":"firstname",
"label":"First Name",
"mandatory":false,
"type":{"name":"string"},
"nullable":true,
"editable":true,
"uitype":"55",
"typeofdata":"V~O",
"sequence":"2",
"block":{
   "blockid":"4",
   "blocksequence":"1",
   "blocklabel":"LBL_CONTACT_INFORMATION",
   "blockname":"Contact Information"
},
"default":""}
```

Using the [coreBOSwsBrowser](https://github.com/tsolucio/coreBOSwsDevelopment) this change looks like this:

![](coreboswsfieldinfonormal.png?width=100%)
![](coreboswsfieldinfoextended.png?width=100%)
