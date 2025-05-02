---
title: 'Invoke Custom Functions Workflow Tasks'
metadata:
    description: 'Implement many different actions'
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
        - customfunction
       
---

This type of workflows is like an open set of functionality that can implement many different actions. In reality it is a simple and defined way of enhancing the workflow system without going through the trouble of adding a new screen (not that that is very complicated but this is easier).

So with custom functions we can find a lot of different options and operations to activate on our records.

The steps are:

-   create a new workflow and select the main module
-   give it a name and set the conditions
-   create a new task and select the "Invoke Custom Function" task
-   On the configuration screen we will find a drop down select box with the available functions for that module
-   Simply select the function and save

that is it, there is nothing to configure as these are atomic action functions, everything they need to know is given to them by the save context.

===
## Available Custom Functions

### ***UpdateInventory***


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Modules</strong></td>
<td>Invoice, SalesOrder</td>
</tr>
<tr>
<td><strong>Functionality</strong></td>
<td>when creating will subtract all stock from the products associated to the record\ when editing will restore all the stock of the previous record and subtract all the stock of the new record</td>
</tr>
</tbody>
</table>

===


### ***NotifyOwnerOnTicketChange***


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Modules</strong></td>
<td>HelpDesk</td>
</tr>
<tr>
<td><strong>Functionality</strong></td>
<td>Sends email to the user assigned to the ticket when the ticket changes</td>
</tr>
</tbody>
</table>


===


### ***NotifyParentOnTicketChange***


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Modules</strong></td>
<td>HelpDesk</td>
</tr>
<tr>
<td><strong>Functionality</strong></td>
<td>Sends email to the account/contact assigned to the ticket when the ticket changes</td>
</tr>
</tbody>
</table>


===


### ***NotifyOnPortalTicketCreation and NotifyOnPortalTicketComment***


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Modules</strong></td>
<td>HelpDesk</td>
</tr>
<tr>
<td><strong>Functionality</strong></td>
<td>Sends email when ticket is created pr commented on in portal</td>
</tr>
</tbody>
</table>


===


### ***Update Contact Assigned To***


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Modules</strong></td>
<td>Accounts and Contacts</td>
</tr>
<tr>
<td><strong>Functionality</strong></td>
<td>hanges the user assigned to all contacts associated to an account when the account is saved OR changes the user assigned to the Contact being saved when it is related to an Account</td>
</tr>
</tbody>
</table>

<br>
------------------------------------------------------------------------

[Next](../02.email_workflows) | Chapter 9: Email Workflow Tasks.

------------------------------------------------------------------------