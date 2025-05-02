---
title: 'Workflows, Rules, Questions and Actions'
metadata:
    description: 'Workflows, Rules, Questions and Actions'
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
        - workflow
        - rule
        - question
        - action
---

### Workflows, Rules, Questions and Actions

#### ExecuteWorkflow-Operation 

Workflows are a very powerful part of the application. They permit us to automate our business logic to some extent making it possible to standardize process and have the application do some of the repetitive tasks our business requires. When you want to trigger a workflow, only from outside of the coreBOS,ie. from the portal or anywhere else and you don't have access to activate it from the corebos system, then it should be set to System Mass Actions.

**GET URL Format :**

```
http://144.91.100.102:8880/corebos/webservice.php?operation=ExecuteWorkflow&sessionName={{sessionName}}&workflow=46&entities=["module_rest_idx77"]
```

**Query parameters**

<div class="alpha right"></div>

|Key | Value | Description|
|--- | --- | ---|
|operation | ExecuteWorkflow | The operation you need to execute a workflow.|
|sessionName | {{sessionName}} | The value of a hashing value that you need to connect to coreBOS.|
|workflow | The workflow_id e.g. 46 | The workflow id that you want to trigger|
|entities | [module_id x record_id] e.g. [11x77] | The id of the module and the record that you want the workflow to be triggered|

**Response**
```json 
{
    "success": true,
    "result": true
}
```

If the response is “success:true” then the workflow has been triggered e.g if you trigger a update field workflow task the result will be :


The wf update field tasks :

![wf1](wf1.PNG?classes=max)

The account before the wf trigger:

![wf2](wf2.PNG?classes=max)

The account after the wf trigger:

![wf3](wf3.PNG?classes=max)


#### ExecuteWorkflowWithContext-Operation 

Basically you can execute a workflow from outside corebos using the ExecuteWorkflowWithContext operation, which allows you to include a new parameter named context. The value of the parameter context can be any set of workflow context variables that your workflow supports. So, if you are sending an email, it can be an id of a Message Template(MsgTemplate) record you need to send. What does that mean? Typically you will create a workflow with a Send Mail task, but you don't want to hardcode the mail template. You create the send mail task only to define the recepients, and cc of the mail, while the template is decided on the webservice request itself. Saying that, the send mail task will serve only as a placeholder for the real template defined in the ws request.
There is an extensive (and undocumented) list of context variables that permit tweaking the functionality of each workflow task.
The other parameters remain the same, you have to define the id of the workflow that you need to execute, the id of the record that you need that workflow to be executed towards, and as always the sessionName in order to authenticate.


**GET URL Format :**

```
http://144.91.100.102:8880/corebos/webservice.php?operation=ExecuteWorkflowWithContext&sessionName={{sessionName}}&workflow=43&entities=["module_rest_idx244623"]&context={"SendThisMsgTemplate":44127}
```

**Query parameters**
<div class="alpha right"></div>

|Key | Value | Description|
|--- | --- | ---|
|operation | ExecuteWorkflowWithContext | The operation you need to execute a workflow.|
|sessionName | {{sessionName}} | The value of a hashing value that you need to connect to coreBOS.|
|workflow | The workflow_id e.g. 43 | The workflow id that you want to trigger|
|entities | [module_id x record_id] e.g. ["module_rest_idx244623"] | The id of the module and the record that you want the workflow to be triggered|
|context | {"SendThisMsgTemplate":44127} | The context (message template) of the email that you want to send|

```json
Response 
{
    "success": true,
    "result": true
}
```

If the response is “success:true” then the workflow has been triggered e.g if you trigger a send mail workflow the result will be :


**The send mail tasks :**

![sendmail](sendmail1.PNG?classes=max)

**A message template that you want to send :**

![template](msgtemp.PNG?classes=max)

The email that has been sent have to be same with the context and no with th workflow send mail task:

![email](email.PNG?classes=max)



<head>
  <style type="text/css">
    div.alpha + table  { width: 600px; border: 1px solid black }
    div.alpha + table td { border: 1px solid black;border-bottom: 1px solid black; }
    div.alpha + table th { border: 1px solid black;border-bottom: 1px solid black;background-color:#f2f2f2 }
     div.alpha + table tr:nth-child(even) {background: #f2f2f2}

  .max {
  width: 600px ;
 }

[Next](../../13.globalsearch)| Chapter 9: Global Search.




------------------------------------------------------------------------