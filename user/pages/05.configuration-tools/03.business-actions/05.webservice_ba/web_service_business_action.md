---
title: 'Web Service BusinessAction'
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

## Web Service BusinessActions


#### getBusinessActions-Operation

[Business Actions](../../03.business-actions) are things that can happen inside the application. They enhance the vtiger CRM link system and they can affect any part of the application

**GET URL Format :**

```
http://144.91.100.102:8880/corebos/webservice.php?operation=getBusinessActions&sessionName={{sessionName}}&view=ListView&module=Accounts&id=accounts_id&linktype=LISTVIEWBASIC
```

**Query parameters**
<div class="alpha right"></div>

|Key | Value | Description|
|--- | --- | ---|
|operation | getBusinessActions | The operation you  need to get the businessAction|
|sessionName | {{sessionName}} | The value of a hashing value that you need to connect to coreBOS.|
|view | ListView | The view that you want to show the result you get from the businessAction. The view can be : listview,detailsview, related module|
|module | Accounts | The module that you want to trigger the businessAction|
|id | e.g. 74 | The id of an account contact|
|linktype | LISTVIEWBASIC | The linktype you will use. You can use one of these linktypes: LISTVIEWBASIC, DETAILVIEWBASIC, HEADERSCRIPT, DETAILVIEWWIDGET|
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
        "LISTVIEWBASIC": [
            {
                "tabid": "6",
                "linkid": "43076",
                "linktype": "LISTVIEWBASIC",
                "linklabel": "Send SMS",
                "linkurl": "SMSNotifierCommon.displaySelectWizard(this, 'Accounts');",
                "linkicon": "",
                "sequence": "0",
                "status": false,
                "handler_path": "",
                "handler_class": "",
                "handler": "",
                "onlyonmymodule": "0"
            },
            {
                "tabid": "6",
                "linkid": "244610",
                "linktype": "LISTVIEWBASIC",
                "linklabel": "Generate Document",
                "linkurl": "javascript:showgendoctemplates('Accounts');",
                "linkicon": "",
                "sequence": "0",
                "status": false,
                "handler_path": "",
                "handler_class": "",
                "handler": "",
                "onlyonmymodule": "1"
            },
            {
                "tabid": "6",
                "linkid": "43152",
                "linktype": "LISTVIEWBASIC",
                "linklabel": "LBL_SEND_MAIL_BUTTON",
                "linkurl": "return eMail('Accounts',this);",
                "linkicon": "",
                "sequence": "0",
                "status": false,
                "handler_path": "",
                "handler_class": "",
                "handler": "",
                "onlyonmymodule": "0"
            },
            {
                "tabid": "6",
                "linkid": "43155",
                "linktype": "LISTVIEWBASIC",
                "linklabel": "LBL_MAILER_EXPORT",
                "linkurl": "return mailer_export();",
                "linkicon": "",
                "sequence": "0",
                "status": false,
                "handler_path": "",
                "handler_class": "",
                "handler": "",
                "onlyonmymodule": "0"
            }
        ]
    }
}
```

#### getBusinessAction - coreBOS Webservice Development
```json
<?php

//parameters
$params = "sessionName=$cbSessionID";
$params.= "&operation=getBusinessActions";
$params.= "&view=ListView";
$params.= "&module=Accounts";
$params.= "&id=74";
$params.= "&linktype=LISTVIEWBASIC";

//Retrieve must be GET Request.
$response = $httpc->fetch_url("$cbURL?$params");
$dmsg.= debugmsg("Raw response (json)", $response);

//decode the json encode response from the server.
$jsonResponse = json_decode($response, true);
$dmsg.= debugmsg("Webservice response", $jsonResponse);

//operation was successful get the token from the response.
if ($jsonResponse['success']==false) {
	$dmsg.= debugmsg('failed:'.$jsonResponse['error']['message']);
	echo 'rule failed!';
} else {
	echo $jsonResponse['result'];
}
?>
```

**Response:** 

```json
{
  "success":true,
  "result":{
     "LISTVIEWBASIC":[
        {
           "tabid":"6",
           "linkid":"43076",
           "linktype":"LISTVIEWBASIC",
           "linklabel":"Send SMS",
           "linkurl":"SMSNotifierCommon.displaySelectWizard(this, \\'Accounts\\');",
           "linkicon":"",
           "sequence":"0",
           "status":false,
           "handler_path":"",
           "handler_class":"",
           "handler":"",
           "onlyonmymodule":"0"
        },
        {
           "tabid":"6",
           "linkid":"244610",
           "linktype":"LISTVIEWBASIC",
           "linklabel":"Generate Document",
           "linkurl":"javascript:showgendoctemplates(\\'Accounts\\');",
           "linkicon":"",
           "sequence":"0",
           "status":false,
           "handler_path":"",
           "handler_class":"",
           "handler":"",
           "onlyonmymodule":"1"
        },
        {
           "tabid":"6",
           "linkid":"43152",
           "linktype":"LISTVIEWBASIC",
           "linklabel":"LBL_SEND_MAIL_BUTTON",
           "linkurl":"return eMail(\\'Accounts\\',this);",
           "linkicon":"",
           "sequence":"0",
           "status":false,
           "handler_path":"",
           "handler_class":"",
           "handler":"",
           "onlyonmymodule":"0"
        },
        {
           "tabid":"6",
           "linkid":"43155",
           "linktype":"LISTVIEWBASIC",
           "linklabel":"LBL_MAILER_EXPORT",
           "linkurl":"return mailer_export();",
           "linkicon":"",
           "sequence":"0",
           "status":false,
           "handler_path":"",
           "handler_class":"",
           "handler":"",
           "onlyonmymodule":"0"
        }
     ]
  }
}
```

#### executeBusinessAction-Operation

The operation that you need to execute a BusinessAction.

**GET URL Format :**
```
http://144.91.100.102:8880/corebos/webservice.php?operation=executeBusinessAction&sessionName={{sessionName}}&businessactionid=43063&context={"ID":"module_rest_idx74"}
```

**Query parameters**
<div class="alpha right"></div>

|Key | Value | Description|
|--- | --- | ---|
|operation | executeBusinessAction | The operation you  need to execute a businessAction|
|sessionName | {{sessionName}} | The value of a hashing value that you need to connect to coreBOS.|
|businessactionid | E.g 43063 | The id of the businessAction that you want to execute|
|context | {"ID":"module_rest_idx74"} | The id of the module and the record id that you want to execute the businessAction.|


!! Only block detail view widgets supported
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
    "result": "<input type=\"hidden\" id=\"comments_parentId\" value=\"74\" /> <table class=\"small\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\"> <tr class=\"detailview_block_header comments_block_header\"> <td colspan=\"4\" class=\"dvInnerHeader\"> <div style=\"float: left; font-weight: bold;\"> <div style=\"float: left;\"> <a href=\"javascript:showHideStatus('tblModCommentsDetailViewBlockCommentWidget','aidModCommentsDetailViewBlockCommentWidget','$IMAGE_PATH');\"> <span class=\"exp_coll_block inactivate\"><img id=\"aidModCommentsDetailViewBlockCommentWidget\" src=\"themes//images/activate.gif\" style=\"border: 0px solid rgb(0, 0, 0);\" alt=\"Hide\" title=\"Hide\"></span></a> </span></a> </div><b>&nbsp;Comments Information</b></div> <span style=\"float: right;\"> <img src=\"themes//images/vtbusy.gif\" border=0 id=\"indicatorModCommentsDetailViewBlockCommentWidget\" style=\"display:none;\">\n\t\t\tShow : <select class=\"small\" onchange=\"ModCommentsCommon.reloadContentWithFiltering('DetailViewBlockCommentWidget', '74', this.value, 'tblModCommentsDetailViewBlockCommentWidget', 'indicatorModCommentsDetailViewBlockCommentWidget');\"> <option value=\"All\" selected>All</option> <option value=\"Last5\" >Last 5</option> <option value=\"Mine\" >Mine</option> </select> </span> </td> </tr> </table> <div id=\"tblModCommentsDetailViewBlockCommentWidget\" style=\"display: block;\"> <table class=\"small\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\"> <tr style=\"height: 25px;\"> <td colspan=\"4\" align=\"left\" class=\"dvtCellInfo commentCell\"> <div id=\"contentwrap_ModCommentsDetailViewBlockCommentWidget\" style=\"overflow: auto; margin-bottom: 20px; width: 100%; word-break: break-all;\"> <div id=\"comment_id_113830\"> <div id=\"mouseArea_113830\" onmouseover=\"hndMouseOver(19,'113830');\" onmouseout=\"fnhide('crmspanid');\" > <div id=\"dtlview_113830\"> <div class=\"dataField\" id=\"comment_content_113830\" style=\"width: 99%; padding-top: 10px;\">\n\t\t\tçmmnote\n\t\t</div> <div class=\"dataLabel\" style=\"border-bottom: 1px dotted rgb(204, 204, 204); width: 99%; padding-bottom: 5px;color:darkred;\">\n\t\t\tAuthor: Joe Bordes on 2022-02-16 16:47:50\n\t\t</div> </div> <div id=\"editarea_113830\" style=\"display:none\"> <textarea id=\"txtbox_113830\" class=\"detailedViewTextBox\" onFocus=\"this.className='detailedViewTextBoxOn'\" onBlur=\"this.className='detailedViewTextBox'\" cols=\"90\" rows=\"8\">çmmnote</textarea> <br><a href=\"javascript:;\" class=\"detailview_ajaxbutton ajax_save_detailview\" onclick=\"ModCommentsCommon.editComment('113830');\">Save</a> </div> </div> </div> </div> </td> </tr> <tr style=\"height: 25px;\" class='noprint'> <td class=\"dvtCellLabel\" align=\"right\">\n\t\t\tAdd Comment\n\t\t</td> <td width=\"100%\" colspan=\"3\" class=\"dvtCellInfo\" align=\"left\"> <div id=\"editarea_ModCommentsDetailViewBlockCommentWidget\"> <textarea id=\"txtbox_ModCommentsDetailViewBlockCommentWidget\" class=\"detailedViewTextBox\" onFocus=\"this.className='detailedViewTextBoxOn'\" onBlur=\"this.className='detailedViewTextBox'\" cols=\"90\" rows=\"8\"></textarea> <br> <button class=\"slds-button slds-button_success\" title=\"Save\" onclick=\"ModCommentsCommon.addComment('ModCommentsDetailViewBlockCommentWidget', '74');\" style=\"color:#ffffff;\" > <svg class=\"slds-button__icon slds-button__icon_left\" aria-hidden=\"true\"> <use xlink:href=\"include/LD/assets/icons/utility-sprite/svg/symbols.svg#save\"></use> </svg>\n\t\t\t\t\t\tSave\n\t\t\t\t</button> <button class=\"slds-button slds-button_neutral\" title=\"Clear\" onclick=\"document.getElementById('txtbox_ModCommentsDetailViewBlockCommentWidget').value='';\" style=\"margin-left: 0;\" > <svg class=\"slds-button__icon slds-button__icon_left\" aria-hidden=\"true\"> <use xlink:href=\"include/LD/assets/icons/utility-sprite/svg/symbols.svg#redo\"></use> </svg>\n\t\t\t\t\t\tClear\n\t\t\t\t</button> </div> </td> </tr> </table> </div>"
}
```

 


#### executeBusinessAction - coreBOS Webservice Development 

**The operation:**
```json
<?php

//parameters
$params = "sessionName=$cbSessionID";
$params.= "&operation=executeBusinessAction";
$params.= "&businessactionid=43063";
$params.= '&context={"ID":"module_rest_idx74"}';

//Retrieve must be GET Request.
$response = $httpc->fetch_url("$cbURL?$params");
$dmsg.= debugmsg("Raw response (json)", $response);

//decode the json encode response from the server.
$jsonResponse = json_decode($response, true);
$dmsg.= debugmsg("Webservice response", $jsonResponse);

//operation was successful get the token from the response.
if ($jsonResponse['success']==false) {
	$dmsg.= debugmsg('failed:'.$jsonResponse['error']['message']);
	echo 'rule failed!';
} else {
	echo $jsonResponse['result'];
}
?>
```


**Output:**

![output](output.PNG?classes=max)



<head>
  <style type="text/css">
    div.alpha + table  { width: 600px; border: 1px solid black }
    div.alpha + table td { border: 1px solid black;border-bottom: 1px solid black; }
    div.alpha + table th { border: 1px solid black;border-bottom: 1px solid black;background-color:#f2f2f2 }
     div.alpha + table tr:nth-child(even) {background: #f2f2f2}

  .max {
  width: 600px ;
 }