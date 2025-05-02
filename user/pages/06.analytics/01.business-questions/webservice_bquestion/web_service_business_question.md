---
title: 'Web Service BusinessQuestion'
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


### cbQuestionAnswer - Operation

This operation can trigger a [BusinessQuestion](../../01.business-questions) and get back the result . The BusinessQuestion can be of several different types such as: Global Search,File,Mermaid,Table,Grid,Number ,Area,RowChart,Scatter,Pie,Map or Funnel.


 **GET URL Format :**

```
http://144.91.100.102:8880/corebos/webservice.php?operation=cbQuestionAnswer&sessionName={{sessionName}}&qid=48x44081
```

**Mermaid BusinessQuestion**
**Query parameters**

<div class="alpha right"></div>

|Key | Value | Description|
|--- | --- | ---|
|operation | cbQuestionAnswer | The operation you  need to execute a businessQuestion|
|sessionName | {{sessionName}} | The value of a hashing value that you need to connect to coreBOS.|
|qid | 48x44081 | The id of the BusinessQuestion that you want to execute|
<br> 

**SessionName**
<br> 
```
var hash = CryptoJS.MD5(token+accesskey).toString();
```
```json
Response
{
    "success": true,
    "result": {
        "columns": "A(( )) -->|contrat| B\nB(( )) -->|Avenants| C(( ))\nC(( )) -->|en cours| H\nD(( )) -->|Terrain| E\nE(( )) -->|Etudes| C(( ))\nF(( )) -->|Plans| G\nG(( )) -->|Métrés| C(( ))\nH((VT)) -->|\"Control<br>Dossier\"| I(( ))\nI(( )) -->|\"Control<br>Prix\"| J\nJ((VA)) --> K\nK((LCS)) --> L\nL((OUV)) --> M\nM((PV)) -->|Solde| N(( ))\nlinkStyle 0 stroke:greenyellow,stroke-width:2px\nlinkStyle 1 stroke:greenyellow,stroke-width:2px\nlinkStyle 2 stroke:greenyellow,stroke-width:2px\nlinkStyle 7 stroke:greenyellow,stroke-width:2px\nlinkStyle 8 stroke:greenyellow,stroke-width:2px\nstyle H fill:greenyellow,stroke:green,stroke-width:4px\nstyle I fill:greenyellow,stroke:green",
        "title": "mermaid",
        "type": "Mermaid",
        "properties": "LR",
        "answer": "graph LR\n\nA(( )) -->|contrat| B\nB(( )) -->|Avenants| C(( ))\nC(( )) -->|en cours| H\nD(( )) -->|Terrain| E\nE(( )) -->|Etudes| C(( ))\nF(( )) -->|Plans| G\nG(( )) -->|Métrés| C(( ))\nH((VT)) -->|\"Control<br>Dossier\"| I(( ))\nI(( )) -->|\"Control<br>Prix\"| J\nJ((VA)) --> K\nK((LCS)) --> L\nL((OUV)) --> M\nM((PV)) -->|Solde| N(( ))\nlinkStyle 0 stroke:greenyellow,stroke-width:2px\nlinkStyle 1 stroke:greenyellow,stroke-width:2px\nlinkStyle 2 stroke:greenyellow,stroke-width:2px\nlinkStyle 7 stroke:greenyellow,stroke-width:2px\nlinkStyle 8 stroke:greenyellow,stroke-width:2px\nstyle H fill:greenyellow,stroke:green,stroke-width:4px\nstyle I fill:greenyellow,stroke:green\n\n"
    }
}
```

#### Pie BusinessQuestion- coreBOS Webservice Development

**Request :**

```json
<?php
//sessionId is obtained from login result.
$params = "sessionName=$cbSessionID&operation=cbQuestionAnswer&qid=44080";
//query must be GET Request.
$response = $httpc->fetch_url("$cbURL?$params");
$dmsg.= debugmsg("Raw response (json) Query",$response);

//decode the json encode response from the server.
$jsonResponse = json_decode($response, true);
$dmsg.= debugmsg("Webservice response Query",$jsonResponse);

if($jsonResponse['success']==false) {
    $dmsg.= debugmsg('query failed: '.$jsonResponse['message']);
	var_dump($jsonResponse['message']);
    echo 'query failed!';
} else {
    $dmsg.= debugmsg('query OK: '.$jsonResponse['result']);
	var_dump($jsonResponse['result']);
    echo 'query OK!';
}
?>
```

**Response :**

```json
array(6) { ["module"]=> string(8) "HelpDesk" ["columns"]=> string(263) "[{"fieldname":"countres","operation":"is","value":"count(ticket_title)","valuetype":"expression","joincondition":"and","groupid":"0"},{"fieldname":"ticketstatus","operation":"is","value":"ticketstatus","valuetype":"fieldname","joincondition":"and","groupid":"0"}]" ["title"]=> string(17) "Ticket per Status" ["type"]=> string(3) "Pie" ["properties"]=> string(51) "{"key_label":"ticketstatus","key_value":"countres"}" ["answer"]=> array(4) { [0]=> array(2) { ["countres"]=> string(1) "5" ["ticketstatus"]=> string(6) "Closed" } [1]=> array(2) { ["countres"]=> string(1) "2" ["ticketstatus"]=> string(11) "In Progress" } [2]=> array(2) { ["countres"]=> string(1) "1" ["ticketstatus"]=> string(4) "Open" } [3]=> array(2) { ["countres"]=> string(1) "1" ["ticketstatus"]=> string(17) "Wait For Response" } } } query OK!
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