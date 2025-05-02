---
title: 'Workflow Tricks and Tips'
metadata:
    description: 'Workflow Tricks and Tips.'
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
        - workflow
    tag:
        - tricksandtips
---

Execute multiple commands in one expression
-------------------------------------------

One important limitation of the expression editor is that we can only execute one command at a time. We have introduced the Expression Evaluation task to overcome this limitation. That task permits us to save expression executions into variables that can be consumed by the next tasks in the workflow.

This next trick will permit you to execute more than one command in the same expression. It consists of abusing the if-then structure and use the condition evaluation to run the first command we need.

Let's suppose we have to write a link using the ID of a record. The workflow id field will return a web service ID but we need to separate the module id for the URL to work, from

***&lt;a href="index.php?module=cbReview&action=DetailView&record=33×99">***

to

***&lt;a href="index.php?module = bReview&action=DetailView&record=99"> ***

Three ideas come to mind:

**1.- Evaluate Expression**

Using the evaluate expression task we create an expression that uses explode to set the variables in the context, once the two separate values are in the context we can use them in the construction of the URL.

The expression in the execute expression task would be

    explode('x', id)

Supposing we save that into the context variable "wsid", then the expression for the update field would be

    concat('<a href="index.php?module=cbReview&action=DetailView&record=', getFromContext('wsid.1'), '">A review has been made.</a>')

**2.- Use string manipulation**

    concat('<a href="index.php?module=cbReview&action=DetailView&record=', substring(id, stringposition(id, 'x')+1), '">link</a>')

**3.- if-then trick**

    if setToContext('wsid', explode('x', id)) then concat('<a href="index.php?module=cbReview&action=DetailView&record=', getFromContext('wsid.1'), '">A review has been made.</a>') else '' end

Since we know that setToContext will return a truish value, we know that the command in the "then" part will always be executed and the "else" ignored and the setToContext has been executed so we can get the value we need from the context. Tricky but effective.

### getCRMIDFromWSID

The correct solution arrived in May 2021 by the hand of one of our new community members, [Miquel Perez](https://github.com/MiquelPerezGiner). He added a [new workflow expression function](https://github.com/tsolucio/corebos/commit/6f53bcf4e3850a9f20c027cc9fb432fc606ff129) that directly obtains the CRMID from the Web Service ID so the expression would end up looking like this:

    concat('<a href="index.php?module=cbReview&action=DetailView&record=', getCRMIDFromWSID(id), '">link</a>')

Thanks!