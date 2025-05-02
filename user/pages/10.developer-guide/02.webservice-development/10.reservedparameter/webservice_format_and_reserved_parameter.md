---
title: 'Webservice format and reserved parameter'
metadata:
    description: 'Webservice format and reserved parameter'
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
        - reserved parameter
---

The web service API returns responses in JSON format. This format can be changed on a per-call basis. To accomplish this we would need to implement the code to support the desired format [like this code which implements the JSON format](https://github.com/tsolucio/corebos/blob/master/include/Webservices/OperationManagerEnDecode.php), add the new format to [the array of supported formats](https://github.com/tsolucio/corebos/blob/master/include/Webservices/OperationManager.php#L13) and then indicate the format using the special reserved parameter **format** in the GET/POST call.

The current set of supported formats are:

- **JSON**: the default response format
- **stream** and **streamraw**: [read about them here](https://blog.corebos.org/blog/query-stream-format)
- **user**: return response based on user preferences settings

<div class="notices red"> Note that this implies that NO web service end point may use a parameter named **format** as this parameter is used for this sole purpose. </div>

<br>
------------------------------------------------------------------------

[Next](../04.faq)| Chapter 19: Frequently Asked Questions.

------------------------------------------------------------------------