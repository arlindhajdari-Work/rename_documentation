---
title: 'Web Service cbRule'
metadata:
    description: 'Menu Editor'
    author: 'Eleni Kullira'
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
        - adminmanual
    tag:
        - howto
---

---


### cbRule - Operation 

This operation allows you to execute a Condition Expression-BusiessMap. This mapping permits us to evaluate an expression in the context of the application and get the result to decide subsequent actions. It accepts two formats, one is a direct expression from the workflow expression engine and the other is a function expression that can be called from inside the system. The function parameters will be changed to the current record values if they exist.

 **GET URL Format :**
 ```
http://144.91.100.102:8880/corebos/webservice.php?operation=cbRule&sessionName={{sessionName}}&conditionid=34033&context=74
```

**Query parameters**
<div class="alpha right"></div>

|Key | Value | Description|
|--- | --- | ---|
|operation | cbRule | The operation you  need to execute a businessMap type Condition Expression or ConditionQuery|
|sessionName | {{sessionName}} | The value of a hashing value that you need to connect to coreBOS.|
|conditionid | 34033 | The id of the BusinessMap that you want to execute|
|context | module_rest_idx74 | The module id and the record_id where you want to execute the BusinessMap|
<br> 

**SessionName**
<br> 
```
var hash = CryptoJS.MD5(token+accesskey).toString();
```

**Condition Expression Map example**

![ce](ce1.PNG?classes=max)

**Response:**
```json
{
    "success": true,
    "result": "Chemex Labs Ltd"
}
```

### cbRule- coreBOS Webservice Development

**Request :**

```json
<?php
$context = array(
	'record_id' => '74',
);
$context = json_encode($context);
$mapid = '34032';
 
//sessionId is obtained from loginResult.
$params = "sessionName=$cbSessionID";
$params.= "&operation=cbRule";
$params.= "&conditionid=".urlencode($mapid);
$params.= "&context=".urlencode($context);
 
//Retrieve must be GET Request.
$response = $httpc->fetch_url("$cbURL?$params");
$dmsg.= debugmsg("Raw response (json)", $response);
 
//decode the json encode response from the server.
$jsonResponse = json_decode($response, true);
$dmsg.= debugmsg("Webservice response", $jsonResponse);
 
//operation was successful get the token from the response.
if($jsonResponse['success']==false) {
	$dmsg.= debugmsg('failed:'.$jsonResponse['error']['message']);
	echo 'rule failed!';
} else {
	echo $jsonResponse['result'];
}
?>
```

Condition Expression Map example

![ce2](ce2.png?classes=max)

**Response:**
```json
{"success":true,"result":141}
```



<head>
  <style type="text/css">
    div.alpha + table  { width: 600px; border: 1px solid black }
    div.alpha + table td { border: 1px solid black;border-bottom: 1px solid black; }
    div.alpha + table th { border: 1px solid black;border-bottom: 1px solid black;background-color:#f2f2f2 }
     div.alpha + table tr:nth-child(even) {background: #f2f2f2}

  .max {
  width: 600px ;
 }