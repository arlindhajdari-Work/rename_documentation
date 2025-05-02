---
title: '210: eliminate 100 record limit on select queries'
metadata:
    description: '210: eliminate 100 record limit on select queries'
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

### Query return limit

The select statement only returns 100 records. This is due to timeout and resource restrictions. If you want to obtain more records you must use the limit modifier. Any select statement with a limit modifier will try to return all the records indicated in the limit. So, if we have a contacts table with 150 records, this query:
```
select * from contacts;
```
will return 100 records, while this query:
```
select * from contacts limit 200;
```

will return the 150 records.

```
select firstname,contact_no,phone from contacts order by firstname limit 4;
```

Only four records starting from the first

```
select firstname,contact_no,phone from contacts order by firstname limit 3, 4
```

Only four records starting from the third

<div class="notices blue">
If you are receiving timeouts you can increment the default timeout by modifying the code: <br>
<a href="https://github.com/tsolucio/coreBOSwsLibrary/blob/master/php/Net/HTTP_Client.php#L22">PHP</a><br>

<a href="https://github.com/tsolucio/coreBOSwsLibrary/blob/master/php/Net/HTTP_Client.php#L29">PHP</a><br>

<a href="https://github.com/tsolucio/coreBOSwsLibrary/blob/master/php/Net/curl_http_client.php#L162">cURL</a><br>

<a href="https://github.com/tsolucio/coreBOSwsLibrary/blob/master/php/Net/curl_http_client.php#L206">cURL</a>
</div>