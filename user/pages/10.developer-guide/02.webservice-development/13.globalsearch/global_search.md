---
title: 'Global Search'
metadata:
    description: 'Web service Global Search end point'
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
        - search
---

Global search, unlike the search button located on each module, searches all modules in coreBOS. By default, Global Search will search the entire system. Currently, Global Search is able to search for accounts, potentials, leads, documents and other modules within the system.

===

#### getSearchResults -Operation

The operation you need for the simple global search

GET URL Format :

```
http://144.91.100.102:8880/corebos/webservice.php?operation=getSearchResults&sessionName={{sessionName}}&query=lin&serch_onlyin=&restrictionids={"userId":"module_rest_idxrecordid","accountId":"module_rest_idxrecordid","contactId":"module_rest_idxrecordid"}
```

**Query parameters**
<div class="alpha right"></div>
|Key | Value | Description|
|--- | --- | ---|
|operation | getSearchResults | The operation you need for the simple global search|
|sessionName | {{sessionName}} | The value of a hashing value that you need to connect to coreBOS.|
|query | lind | The word that you are searching for|
|serch_onlyin | Comma-separated list of module names | The module(s) that you want to search in. If the field is empty you are searching at all modules|
|restrictionids | {"userId":"module_rest_idx0", "accountId":"module_rest_idx0" "contactId":"module_rest_idx0"} | The id of the user and the id of the the records in some modules. If userid is given, the search will be executed as that user, with that user’s permissions. If accountid and/or contactid are given, the records returned must be related to those records.|
<br> 

**SessionName**
<br> 
```
var hash = CryptoJS.MD5(token+accesskey).toString();
```

**Response: This is a PHP Serialized object.**

```json
{
    "success": true,
    "result": "a:7:{i:0;a:10:{s:7:\"Lead No\";s:5:\"LEA74\";s:9:\"Last Name\";s:7:\"Lindall\";s:10:\"First Name\";s:9:\"Carmelina\";s:7:\"Company\" ;s:29:\"George Jessop Carter Jewelers\";s:5:\"Phone\";s:12:\"303-724-7371\";s:7:\"Website\ ";s:43:\"http://www.georgejessopcarterjewelers.co...\";s:5:\"Email\";s:29:\"carmelina_lindall@lindall.com\" ;s:11:\"Assigned To\";s:9:\"Var Group\";s:2:\"id\";s:7:\"10x4242\";s:18:\"search_module_name\";s:5: \"Leads\";}i:1;a:10:{s:7:\"Lead No\";s:6:\"LEA133\";s:9:\"Last Name\";s:7:\"Dilello\";s:10: \"First Name\";s:7:\"Lindsey\";s:7:\"Company\";s:23:\"Biltmore Investors Bank\";s:5: \"Phone\";s:12:\"909-639-9887\";s:7:\"Website\";s:36:\"http://www.biltmoreinvestorsbank.com\";s:5:\"Email\";s:27:\"lindsey.dilello@hotmail.com\";s:11:\"Assigned To\";s:9: \"Var Group\";s:2:\"id\";s:7:\"10x4301\";s:18:\"search_module_name\";s:5: \"Leads\";}i:2;a:10:{s:7:\"Lead No\";s:6:\"LEA107\";s:9:\"Last Name\";s:7:\"Hochard\";s:10:\"First Name\";s:7: \"Malinda\";s:7:\"Company\";s:23:\"Logan Memorial Hospital\";s:5:\"Phone\";s:12:\"317-722-5066\";s:7:\"Website\";s:36: \"http://www.loganmemorialhospital.com\";s:5:\"Email\";s:25: \"malinda.hochard@yahoo.com\";s:11:\"Assigned To\";s:9:\"Var Group\";s:2:\"id\";s:7:\"10x4275\";s:18: \"search_module_name\";s:5:\"Leads\";}i:3;a:7:{s:9:\"Vendor No\";s:5:\"VEN66\";s:11: \"Vendor Name\";s:29:\"George Jessop Carter Jewelers\";s:5:\"Phone\";s:12:\"303-724-7371\";s:5: \"Email\";s:29:\"carmelina_lindall@lindall.com\";s:8:\"Category\";s:0:\"\";s:2:\"id\";s:6: \"2x2281\";s:18:\"search_module_name\";s:7:\"Vendors\";}i:4;a:7:{s:9:\"Vendor No\";s:6:\"VEN259\";s:11: \"Vendor Name\";s:20:\"Bogart, Edward J Esq\";s:5:\"Phone\";s:12:\"604-458-2387\";s:5: \"Email\";s:18:\"bkazar@hotmail.com\";s:8:\"Category\";s:0:\"\";s:2:\"id\";s:6:\"2x2474\";s:18: "search_module_name\";s:7:\"Vendors\";}i:5;a:7:{s:22:\"Project Milestone Name\";s:15: \"Belinda Mathius\";s:14:\"Milestone Date\";s:10:\"2016-04-13\";s:11:\"description\";s:43: \"fringilla ornare placerat, orci lacus ve...\";s:12:\"Created Time\";s:19:\"2015-06-09 10:57:17\";s:13: \"Modified Time\";s:19:\"2016-05-16 15:48:10\";s:2:\"id\";s:7:\"31x8826\";s:18: \"search_module_name\";s:16:\"ProjectMilestone\";}i:6;a:7:{s:22:\"Project Milestone Name\";s:14: \"Howard Lindley\";s:14:\"Milestone Date\";s:10:\"2016-04-25\";s:11:\"description\";s:43: \"In mi pede, nonummy ut, molestie in, tem...\";s:12:\"Created Time\";s:19: \"2015-06-15 09:22:55\";s:13:\"Modified Time\";s:19:\"2015-07-10 13:41:29\";s:2:\"id\";s:7:\"31x9385\";s:18: \"search_module_name\";s:16:\"ProjectMilestone\";}}"
}
```


#### getSearchResultsArray-Operation

The operation you  need for the global search where the response is in the form of an array.

**GET URL Format :**

```
http://144.91.100.102:8880/corebos/webservice.php?operation=getSearchResultsArray&sessionName={{sessionName}}&query=lin&serch_onlyin= &restrictionids={"userId":"module_rest_idxrecordid","accountId":"module_rest_idxrecordid","contactId":"module_rest_idxrecordid"}
```

**Query parameters**

<div class="alpha right"></div>

|Key | Value | Description|
|--- | --- | ---|
|operation | getSearchResultsArray | The operation you  need for the global search where the response is in the form of an array.|
|sessionName | {{sessionName}} | The value of a hashing value that you need to connect to coreBOS.|
|query | lind | The word that you are searching for|
|serch_onlyin |  | The module that you want to search in. If the field is empty you are searching at all modules|
|restrictionids | {"userId":"module_rest_idx0", "accountId":"module_rest_idx0", "contactId":"module_rest_idx0"} | The id of the user and the id of the the records in some modules|

<br> 

**SessionName**
<br> 
```
var hash = CryptoJS.MD5(token+accesskey).toString();
```

**Response**

```json
{
    "success": true,
    "result": [
        {
            "Lead No": "LEA74",
            "Last Name": "Lindall",
            "First Name": "Carmelina",
            "Company": "George Jessop Carter Jewelers",
            "Phone": "303-724-7371",
            "Website": "http://www.georgejessopcarterjewelers.co...",
            "Email": "carmelina_lindall@lindall.com",
            "Assigned To": "Var Group",
            "id": "10x4242",
            "search_module_name": "Leads"
        },
        {
            "Lead No": "LEA133",
            "Last Name": "Dilello",
            "First Name": "Lindsey",
            "Company": "Biltmore Investors Bank",
            "Phone": "909-639-9887",
            "Website": "http://www.biltmoreinvestorsbank.com",
            "Email": "lindsey.dilello@hotmail.com",
            "Assigned To": "Var Group",
            "id": "10x4301",
            "search_module_name": "Leads"
        },
        {
            "Lead No": "LEA107",
            "Last Name": "Hochard",
            "First Name": "Malinda",
            "Company": "Logan Memorial Hospital",
            "Phone": "317-722-5066",
            "Website": "http://www.loganmemorialhospital.com",
            "Email": "malinda.hochard@yahoo.com",
            "Assigned To": "Var Group",
            "id": "10x4275",
            "search_module_name": "Leads"
        },
        {
            "Vendor No": "VEN66",
            "Vendor Name": "George Jessop Carter Jewelers",
            "Phone": "303-724-7371",
            "Email": "carmelina_lindall@lindall.com",
            "Category": "",
            "id": "2x2281",
            "search_module_name": "Vendors"
        },
        {
            "Vendor No": "VEN259",
            "Vendor Name": "Bogart, Edward J Esq",
            "Phone": "604-458-2387",
            "Email": "bkazar@hotmail.com",
            "Category": "",
            "id": "2x2474",
            "search_module_name": "Vendors"
        },
        {
            "Project Milestone Name": "Belinda Mathius",
            "Milestone Date": "2016-04-13",
            "description": "fringilla ornare placerat, orci lacus ve...",
            "Created Time": "2015-06-09 10:57:17",
            "Modified Time": "2016-05-16 15:48:10",
            "id": "31x8826",
            "search_module_name": "ProjectMilestone"
        },
        {
            "Project Milestone Name": "Howard Lindley",
            "Milestone Date": "2016-04-25",
            "description": "In mi pede, nonummy ut, molestie in, tem...",
            "Created Time": "2015-06-15 09:22:55",
            "Modified Time": "2015-07-10 13:41:29",
            "id": "31x9385",
            "search_module_name": "ProjectMilestone"
        }
    ]
}
```

#### getSearchResultsArrayWithTotals-Operation

The operation you need for global search where the response is in the form of an array, with the total count that the word appears in each module.

**GET URL Format :**

```
http://144.91.100.102:8880/corebos/webservice.php?operation=getSearchResultsArrayWithTotals&sessionName={{sessionName}}&query=lin&serch_onlyin= &restrictionids={"userId":"module_rest_idxrecordid","accountId":"module_rest_idxrecordid","contactId":"module_rest_idxrecordid"}
```

**Query parameters**

<div class="alpha right"></div>

|Key | Value | Description|
|--- | --- | ---|
|operation | getSearchResultsArrayWithTotals | The operation you need for global search where the response is in the form of an array, with the total count that the word appears in each module.|
|sessionName | {{sessionName}} | The value of a hashing value that you need to connect to coreBOS.|
|query | lind | The word that you are searching for|
|serch_onlyin |  | The module that you want to search in. If the field is empty you are searching at all modules|
|restrictionids | {"userId":"module_rest_idx0", "accountId" :"module_rest_idx0", "contactId":"module_rest_idx0"} | The id of the user and the id of the the records in some modules|
<br> 

**SessionName** 
<br> 
```
var hash = CryptoJS.MD5(token+accesskey).toString();
```


**Response**

```json
{
    "success": true,
    "result": {
        "records": [
            {
                "Lead No": "LEA74",
                "Last Name": "Lindall",
                "First Name": "Carmelina",
                "Company": "George Jessop Carter Jewelers",
                "Phone": "303-724-7371",
                "Website": "http://www.georgejessopcarterjewelers.co...",
                "Email": "carmelina_lindall@lindall.com",
                "Assigned To": "Var Group",
                "id": "10x4242",
                "search_module_name": "Leads"
            },
            {
                "Lead No": "LEA133",
                "Last Name": "Dilello",
                "First Name": "Lindsey",
                "Company": "Biltmore Investors Bank",
                "Phone": "909-639-9887",
                "Website": "http://www.biltmoreinvestorsbank.com",
                "Email": "lindsey.dilello@hotmail.com",
                "Assigned To": "Var Group",
                "id": "10x4301",
                "search_module_name": "Leads"
            },
            {
                "Lead No": "LEA107",
                "Last Name": "Hochard",
                "First Name": "Malinda",
                "Company": "Logan Memorial Hospital",
                "Phone": "317-722-5066",
                "Website": "http://www.loganmemorialhospital.com",
                "Email": "malinda.hochard@yahoo.com",
                "Assigned To": "Var Group",
                "id": "10x4275",
                "search_module_name": "Leads"
            },
            {
                "Vendor No": "VEN66",
                "Vendor Name": "George Jessop Carter Jewelers",
                "Phone": "303-724-7371",
                "Email": "carmelina_lindall@lindall.com",
                "Category": "",
                "id": "2x2281",
                "search_module_name": "Vendors"
            },
            {
                "Vendor No": "VEN259",
                "Vendor Name": "Bogart, Edward J Esq",
                "Phone": "604-458-2387",
                "Email": "bkazar@hotmail.com",
                "Category": "",
                "id": "2x2474",
                "search_module_name": "Vendors"
            },
            {
                "Project Milestone Name": "Belinda Mathius",
                "Milestone Date": "2016-04-13",
                "description": "fringilla ornare placerat, orci lacus ve...",
                "Created Time": "2015-06-09 10:57:17",
                "Modified Time": "2016-05-16 15:48:10",
                "id": "31x8826",
                "search_module_name": "ProjectMilestone"
            },
            {
                "Project Milestone Name": "Howard Lindley",
                "Milestone Date": "2016-04-25",
                "description": "In mi pede, nonummy ut, molestie in, tem...",
                "Created Time": "2015-06-15 09:22:55",
                "Modified Time": "2015-07-10 13:41:29",
                "id": "31x9385",
                "search_module_name": "ProjectMilestone"
            }
        ],
        "totals": {
            "Accounts": 0,
            "Leads": 3,
            "Contacts": 0,
            "Potentials": 0,
            "Campaigns": 0,
            "HelpDesk": 0,
            "Products": 0,
            "Documents": 0,
            "Emails": 0,
            "Faq": 0,
            "Vendors": 2,
            "PriceBooks": 0,
            "Quotes": 0,
            "PurchaseOrder": 0,
            "SalesOrder": 0,
            "Invoice": 0,
            "ServiceContracts": 0,
            "Services": 0,
            "CobroPago": 0,
            "Assets": 0,
            "ModComments": 0,
            "ProjectMilestone": 2,
            "ProjectTask": 0,
            "Project": 0,
            "InventoryDetails": 0,
            "cbTermConditions": 0,
            "cbCalendar": 0,
            "cbSurvey": 0,
            "cbSurveyQuestion": 0,
            "cbSurveyDone": 0,
            "cbSurveyAnswer": 0,
            "cbCompany": 0,
            "cbQuestion": 0,
            "ProductComponent": 0,
            "Messages": 0,
            "cbPulse": 0,
            "MsgTemplate": 0,
            "cbCredentials": 0,
            "Timecontrol": 0,
            "cbBCase": 0,
            "DocumentFolders": 0,
            "pricebookproductrel": 0,
            "AutoNumberPrefix": 0,
            "ProcessLog": 0,
            "cbProcessAlert": 0,
            "cbProcessFlow": 0,
            "cbProcessStep": 0
        }
    }
}
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
 
[Next](../00.manual/03.autocomplete)| Chapter 10: Autocomplete.

------------------------------------------------------------------------