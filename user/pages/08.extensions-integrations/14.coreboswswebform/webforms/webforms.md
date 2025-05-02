---
title: 'Webforms'
metadata:
    description: 'coreBOS Webservice Webform'
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
        - webform
---

## Webservice Webforms

[coreBOS Webservice Webform](../../14.coreboswswebform)

### Relaying a Webform

<div class="notices blue">
postby jtrombley80 » Thu Nov 01, 2012 10:37 pm THANK YOU
</div>

Ran into a situation recently where I needed a Webform sitting out on the internet to hit a server in a DMZ and then be relayed from that server to a coreBOS server behind a firewall. The DMZ server was the only one allowed to talk to the coreBOS instance and it wasn't the server hosting the webform. Here's what I did in case anyone has a similar need.

Set the form post on the internet webform to go to "themiddlemanserver/relay.php"

Enabled cURL in PHP on the DMZ server. Contents of relay.php is:

```php
<?php
    $postParams = file_get_contents("php://input");
    $ch = curl_init('http://vtigerbehindfirewall/modules/Webforms/capture.php');
    curl_setopt ($ch, CURLOPT_POST, 1);
    curl_setopt ($ch, CURLOPT_POSTFIELDS, $postParams);
    curl_exec ($ch);
    curl_close ($ch);
?>
```
Webform hits the DMZ relay and is sent on to the coreBOS instance behind the firewall. Passes all values correctly.


