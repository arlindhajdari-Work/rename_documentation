---
title: 'Mail Converter'
metadata:
    description: 'This feature permits Configuring an IMAP mailbox to scan for messages and convert them to appropriate entities in the application.'
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
        - adminmanual
    tag:
        - logo
---

This feature permits Configuring an IMAP mailbox to scan for messages and convert them to appropriate entities in the application.

Mail Converter adds the capability to scan your mailbox and take actions on messages that matches the established criteria.

The main functionality it was created for is to manage the Help Desk workflow with the logic that can be seen in the next image:

![](mailscanner-create-update-ticket-flow_166.jpg?width=100%)

<div class="notices red">
The Regular expression to process tickets correctly is:
<div class="notices blue">
Re: TT[0-9]+ \[ Ticket Id : [0-9]+ \] (.+)
</div>

What we put in the last block of parenthesis is what the application uses to match the ticket, if it is a number it will look for the CRMID if not it will look for the subject of the ticket. 
</div>

## Configure Mailbox

You can access the Converter in **Settings → Mail Converter**

You need to provide the mailbox information on which the scan needs to be performed. By default the mailbox will be disabled as no information is available.

![](mailconverterconfigurations.png?width=80%)

<div class="notices blue">
Make sure that the status is <i>Enable</i> before saving the mailbox information. Scan will not be performed if the status is <i>Disable</i> </div>

Provide configuration details to establish connection with your mail server and click on the Save button; As a result, all the available folder names will be fetched. If the connection fails the information will not be saved.

## Select Folders
After mailbox setup you can select the folders which should be considered for scanning the mails. Click on the <i>Select Folders</i> button.

![](mailconverterselectfolder.png?width=80%)

You can exclude or include the folders by selecting/de-selecting the checkbox as shown here:

![](mailboxfolder.png?width=80%)

## Rules

You can setup one or multiple rules on a mailbox which permit you to perform actions on a mail based on the criteria.

![](setuprulebutton.png?width=80%)

Click on the *Add Rule* button and set up the actions that you would like to perform on a mail.

![](configurerule.png?width=80%)

## Rule criteria

Rule criteria are evaluated as follows:

<table class="table table-striped">
<tbody>
<tr>
<td><strong>From</strong></td>
<td>Check for the input occurrence in the FROM field of the email</th>
</tr>
<tr>
<td><strong>To</strong></td>
<td>Check for the input occurrence in the TO field of the email
</td>
</tr>
<tr>
<td><strong>Subject</strong></td>
<td>Compare the input with SUBJECT of email using one of the condition selected (Contains, Not Contains, Equals, Not Equals, Begins With, Not Begins With, Regex)</td>
</tr>
<tr>
<td><strong>Body</strong></td>
<td>Compare the input with BODY of email using one of the condition selected (Contains, Not Contains, Equals, Not Equals, Begins With, Not Begins With)</td>
</tr>
<tr>
<td><strong>Match</strong></td>
<td><strong>All Condition</strong> – All the input conditions should evaluate as true to take Action</td>
</tr>
<tr>
<td></td>
<td><strong>Any Condition</strong> – At least one condition should evaluate as true to take Action</td>
</tr>
</tbody>
</table>
<br>
Once a successful matching on an email occurs, the action will be applied on it as follows:
<br>
<table class="table table-striped">
<tbody>
<tr>
<td><strong>Create Ticket</strong></td>
<td>Creates a new trouble ticket record with the following:<br>
Title = SUBJECT of email<br>
Description = BODY of email<br>
Attachments of email will be linked to the trouble ticket record</th>
</tr>
<tr>
<td></td>
<td>Lookup is made for existing Contact/Account based on FROM field of email and ticket is associated to matching record (if found)
</td>
</tr>
<tr>
<td><strong>Update Ticket</strong></td>
<td>Updates existing trouble ticket record with the following:<br>
Comment = BODY of email</td>
</tr>
<tr>
<td></td>
<td>Lookup is made on existing trouble ticket based on FROM field of email and title or CRMID match. Preferable to select Regex as Subject and paste the following code in the text area
<div class="notices blue">
Ticket Id[^:]?: ([0-9]+) </div></td>
</tr>
<tr>
<td><strong>Add to Contact[FROM]</strong></td>
<td>Lookup is made for existing Contact based on FROM field of email. On success a new email record is created and is associated to matching record.</td>
</tr>
<tr>
<td><strong>Add to Contact[TO]</strong></td>
<td> Lookup is made for existing Contact based on TO field of email. On success a new email record is created and is associated to matching record.</td>
</tr>
<tr>
<td><strong>Add to Account[FROM]</strong></td>
<td>Lookup is made for existing Account based on FROM field of email. On success a new email record is created and is associated to matching record.</td>
</tr>
<tr>
<td><strong>Add to Account[TO]</strong></td>
<td>Lookup is made for existing Account based on TO field of email. On success a new email record is created and is associated to matching record.</td>
</tr>
</tbody>
</table>
<br>
**Example:** Rule to create trouble ticket from any email is shown below:
![](mailconverterconfiguredrule.png?width=80%)

## Rule Priority
One or more rules for the mailbox which are applied in sequence while Scanning. You can change the order (Priority) by clicking the arrow marks.

<div class="notices blue">
If the email matches the conditions defined for a given rule, the remaining rules are not applied.
</div>

## Manual Scanning
Click the *Back* button after setting rule or rules.

After setting up at least one rule you can scan the mailbox.

![](mailconverterbackbutton.png?width=80%)

Now click on the *Scan Now* button. It might take long time based on the amount of emails that will be present in the mailbox (configured folders)

![](scannowbutton.png?width=80%)

As soon as scanning is finished you will get changes according to the rules you have set for creating and updating Trouble Ticket or adding an e-mail to Organizations or Contacts.

!!! **Note:** When using WorkFlows, the module `MailConverter` uses is actually `Messages`, not `E-Mails`.
