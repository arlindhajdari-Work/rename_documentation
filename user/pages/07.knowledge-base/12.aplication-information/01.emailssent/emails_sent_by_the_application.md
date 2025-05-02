---
title: 'Emails Sent by the application'
metadata:
    description: 'Menu Editor'
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
        - notifications
    tag:
        - emails
---

### vtigercron: scheduler

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Send Reminder</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Send an email to remind of an upcoming activity. Send Reminder check box must be marked on the event.</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>Depends on workflow configuration</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Workflow: Send Reminder Template. You can adapt and adjust the template and tasks in the workflow, for example, sending different translated messages to the assigned user depending on his language settings.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>Depends on workflow configuration. By default to assigned and invited users. Not sent to contacts nor accounts.</td>
</tr>
<tr>
<td><strong>Note</strong></td>
<td>This workflow is a special system workflow that is launched independently from all the other workflows.</td>
</tr>
</tbody>
</table>
<br><br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Scheduled Report</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Generate a report and send it by email.</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>From Email field in Outgoing Server Configuration</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Hardcoded. Translatable.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>CRM Users selected when scheduling the report. Not sent to contacts nor accounts.</td>
</tr>
</tbody>
</table>
<br><br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Scheduled Report</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Send email informing on the result of a scheduled import.</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>From Email field in Outgoing Server Configuration</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Hardcoded. NOT Translatable.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>CRM User who launched the import. Not sent to contacts nor accounts.</td>
</tr>
</tbody>
</table>
<br><br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Workflow</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Send an email on account/contact creation when the Notify Owner field is true.</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>Depends on workflow configuration.</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Depends on workflow configuration.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>User assigned to the account/contact. Not sent to account nor contact.</td>
</tr>
</tbody>
</table>
<br><br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Workflow: Send Email to users on Potential creation</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Send an email on creation of opportunity.</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>Depends on workflow configuration.</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Template based in the workflow editor.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>User assigned to the opportunity</td>
</tr>
</tbody>
</table>
<br><br>


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Workflow: Send Email to user when Portal User is True</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Send an email on Portal User (contact) activation to the user assigned to the Contact, this is NOT the portal access details email.</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>Depends on workflow configuration</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Template based in the workflow editor.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>User assigned to the contact</td>
</tr>
</tbody>
</table>
<br><br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Workflow: Contact Creation or Modification</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Send email with <strong>Portal User (contact) access details</strong> to Contact.</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>email of the user activating the portal access</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Template from email templates.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>Contact being activated</td>
</tr>
</tbody>
</table>
<br><br>

--- 
<div class="notices blue">
See the specific HelpDesk email notification section
</div>
<br>
<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Workflow: Ticket Created from Portal</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Email confirmation of ticket creation from customer portal.</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>email of the contact creating ticket</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Hard coded. Translatable.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>Contact creating ticket and User assigned to the ticket</td>
</tr>
</tbody>
</table>
<br><br>


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Workflow: Ticket Updated from Portal</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Email confirmation of ticket comment/update from customer portal.</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>email of the contact creating ticket</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Hard coded. Translatable.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>User assigned to the ticket</td>
</tr>
</tbody>
</table>
<br><br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Workflow: Ticket Change, not from the Portal</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Email confirmation of ticket comment/update from vtiger CRM.</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>$HELPDESK_SUPPORT_EMAIL_ID</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Hard coded. Translatable.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>Contact related to the ticket and User assigned to the ticket</td>
</tr>
</tbody>
</table>
<br><br>


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Workflow: Events when Send Notification is True</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Send an email on creation of calendar event that has the "Send Notification" check box marked</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>Depends on workflow configuration</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Template based in the workflow editor.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>User assigned to the event</td>
</tr>
</tbody>
</table>
<br><br>


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Workflow: Calendar Todos when Send Notification is True</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Send an email on creation of calendar todos that has the "Send Notification" check box marked</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>Depends on workflow configuration</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Template based in the workflow editor.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>User assigned to the event</td>
</tr>
</tbody>
</table>
<br><br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Calendar Send Invitation</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Send email inviting other CRM users to an event.</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>Depends on workflow configuration</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Workflow</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>Users invited on event</td>
</tr>
</tbody>
</table>
<br><br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Test email to admin user on outgoing server configuration</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Send email confirming correct configuration of the outgoing server.</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>email of the admin user</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Hard coded.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>admin user</td>
</tr>
</tbody>
</table>
<br><br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Login details for user on creation</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Send email with login details of a user being created.</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>email of the admin user</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Hard coded. Translatable.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>new user being created</td>
</tr>
</tbody>
</table>
<br><br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>send_mail_for_password</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Send email with password to contact trying to recover Customer Portal lost password.</td>
</tr>
<tr>
<td><strong>From address</strong></td>
<td>email of the user assigned to the Contact</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>Hard coded. Translatable.</td>
</tr>
<tr>
<td><strong>Sent to</strong></td>
<td>Contact trying to recover his password</td>
</tr>
</tbody>
</table>
<br><br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Notify when a task is delayed beyond 24 hrs</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Notify task user that a task was due yesterday.</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>workflow</td>
</tr>
</tbody>
</table>
<br><br>

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Product Support Starting and Ending</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Notify product handler that support for a given product is starting or ending.</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>workflow</td>
</tr>
</tbody>
</table>
<br><br>


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Client End Support Notification 1 month</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Notify contact that their customer portal access is due to expire in a month.
</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>workflow</td>
</tr>
</tbody>
</table>
<br><br>


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Service</strong></td>
<td><strong>Client End Support Notification 1 week</strong></th>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Notify contact that their customer portal access is due to expire in a week.
</td>
</tr>
<tr>
<td><strong>Template</strong></td>
<td>workflow</td>
</tr>
</tbody>
</table>
<br><br>
