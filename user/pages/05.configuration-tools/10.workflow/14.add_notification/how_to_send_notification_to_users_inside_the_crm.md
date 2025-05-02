---
title: 'How to send notification to users inside the CRM'
metadata:
    description: 'How to use Add notification Workflow task to send notifications about specific tasks to different users inside the CRM.'
    author: 'Enea Dudija'
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
        - workflow
    tag:
        - howto
---

The **add notification** Workflow task helps us build an automation that notifies the user inside the CRM through a popup window for specific eminders and pending tasks according to the conditions we set. These notifications will appear in the **notification panel and Pending Action widget**.

===

To implement this feature we need to have in mind the following rules: 

    The workflow should be created in the module that we want to see the notification for.


### The body of the workflow task:

**Module**: We specify the module for the Notification window. By default will be the module triggering the workflow.

**Record**: Record related to the notification. Information from the record will be used to show the event. Leave it empty in order to take the record triggering the workflow.

**Action Date**: Date of the notification in ISO format. By default will be the date time of the workflow trigger.

**Time**: Time of the notification. By default will be the date time of the workflow trigger.

**Notify Owner**: User owner of the notification. By default will be the current user when the workflow triggers.


You can specify one or more action buttons in the Action section.


**One action case:**

 ```json
{"label":"Process It","link":"javascript:getProcessInfo('','DetailView','Save','','9221|BusinessProcess|$RECORD$')"}
```

**More actions case:**

```json
["hideDefaultButtons",{"label":"Process It","link":"javascript:getProcessInfo('','DetailView','Save','','9221|BusinessProcess|$RECORD$')"},{"label":"wow","link":"javascript:getProcessInfo('','DetailView','Save','','9221|BusinessProcess|$RECORD$')"}]
```

  Basically it is a JSON structure. So we split the button sections by comma, and each button should be inside the curly brackets {}. The hole thing should be inside the square brackets [].  

In the **“link”** parameter we can specify any javascript function that Evolutivo supports.


  There are two default buttons that appear to the notification popup. We can hide them by specifying a **"hideDefaultButtons"** string at the first element: 


```json
["hideDefaultButtons",{"label":"Process It","link":"javascript:getProcessInfo('','DetailView','Save','','9221|BusinessProcess|$RECORD$')"},{"label":"wow","link":"javascript:getProcessInfo('','DetailView','Save','','9221|BusinessProcess|$RECORD$')"}]
```


  You can make the action button go to a specific url:
  
   ```json
{"label":"test","link":"javascript:gotourl('https://google.com')"}
```
