---
title: 'Administration FAQ'
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
        - adminmanual
    tag:
        - faq
---

- ["report to" field in user profile have some influence in hierarchy and permission?](../13.FAQ/item.md#report-to-field-in-user-profile-have-some-influence-in-hierarchy-and-permission)
- [How to increment maximum file upload. File upload field with message 'Maximum upload size is MB'](../13.FAQ/item.md#how-to-increment-maximum-file-upload-file-upload-field-with-message-maximum-upload-size-is-mb)
- [Hi, I'm looking at including the Project ID in a email sent from a workflow on project creation (to make a URL link in the email)](../13.FAQ/item.md#hi-i-m-looking-at-including-the-project-id-in-a-email-sent-from-a-workflow-on-project-creation-to-ma)
- [My vtigercron.php script isn't working because I don't have PHP CLI installed. How can I fix that?](../13.FAQ/item.md#my-vtigercron-php-script-isn-t-working-because-i-don-t-have-php-cli-installed-how-can-i-fix-that)
- [My vtigercron.php script isn't working because I don't have PHP CLI installed. I changed the CLI to apache2handler following the previous question. Can that produce any problems?](../13.FAQ/item.md#my-vtigercron-php-script-isn-t-working-because-i-don-t-have-php-cli-installed-i-changed-the-cli-to-a)
- [I know as a security feature vtiger CRM/coreBOS will auto log out a user after a certain time. Is there a way to adjust how long the system waits before auto logging out a user?](../13.FAQ/item.md#i-know-as-a-security-feature-vtiger%20CRM-and-corebos-will-auto-log-out-a-user-after-a-certain-time-is-)
- [How to extend the session. I keep getting logged out of the program](../13.FAQ/item.md#how-to-extend-the-session-i-keep-getting-logged-out-of-the-program)
- [From Portal column doesn't display the correct value. It seems that even though my customers create tickets from the Customer Portal, the column From Portal is NO for all the tickets. How does this work? Should it not be YES for the tickets created from Customer Portal?](../13.FAQ/item.md#from-portal-column-doesn-t-display-the-correct-value-it-seems-that-even-though-my-customers-create-t)
- [Automatic number fields are not sorting correctly. For example, I get TT1, TT11, TT12, TT2,... instead of TT1, TT2, TT3, ..., TT11, TT12](../13.FAQ/item.md#automatic-number-fields-are-not-sorting-correctly-for-example-i-get-tt1-tt11-tt12-tt2-instead-of-tt1)
- [How can I reset the admin user password?](../13.FAQ/item.md#how-can-i-reset-the-admin-user-password)
- [How can I deactivate the "Don't show this dialog" or "evitar que este pagina cree dialogo" checkbox on alert messages?](../13.FAQ/item.md#how-can-i-deactivate-the-don-t-show-this-dialog-or-evitar-que-este-pagina-cree-dialogo-checkbox-on-a)
- [How can I hide the Tag Cloud for all users?](../13.FAQ/item.md#how-can-i-hide-the-tag-cloud-for-all-users)
- [Is there a way to make a shortcut (web based) that takes a user directly to a trouble ticket that is associated with a specific asset? In other words, simply clicking on a link it would add a new trouble ticket to the asset.](../13.FAQ/item.md#is-there-a-way-to-make-a-shortcut-web-based-that-takes-a-user-directly-to-a-trouble-ticket-that-is-a)
- [My user has blocked access to his account due to too many login attempts. How can I reset his access?](../13.FAQ/item.md#my-user-has-blocked-access-to-his-account-due-to-too-many-login-attempts-how-can-i-reset-his-access)
- [How can we rollback a mass edit?](../13.FAQ/item.md#how-can-we-rollback-a-mass-edit)
- [Inventory module Purchase Order does not permit inline edit when total and subtotal are negative](../13.FAQ/item.md#inventory-module-purchase-order-does-not-permit-inline-edit-when-total-and-subtotal-are-negative)

<br>
<div class="notices blue">
<h2>"report to" field in user profile have some influence in hierarchy and permission?</h2>
</div>

<h3>No - it helps in identifying the owner. Sharing access (record level) permission is based on Roles instead.</h3>

--- 
<br>
<div class="notices blue">
<h2>How to increment maximum file upload. File upload field with message 'Maximum upload size is MB'</h2>
</div>

<h3>Forums and Google say to edit the php.ini file, increasing both upload_max_filesize and also post_max_size. I set them both to 25M & restarted server, but still no joy.

So then changed config.inc.php for the upload_maxsize to 25000000 and it worked. NOTE: The configuration editor will show a value of 25, (to the right of "(Max 5MB)" but I tested it and it DOES work. Interestingly, it also shows the proper 25M value when the user uploads a file/document.
<br>
<br>
<strong>reilogix</strong>
 <a href="https://discussions.vtiger.com//discussion/166163/file-upload-field-with-message-039maximum-upload-size-is-mb039#Item_3">Forum Thread</a></h3>
---
<br>
<div class="notices blue">
<h2>Hi, I'm looking at including the Project ID in a email sent from a workflow on project creation (to make a URL link in the email)</h2>
</div>

<h3>Use the Detail View URL link meta variable.</h3> 
![](detailviewurl.png?width=100%)

<div class="notices blue">
Versions of coreBOS after February 2015 have a new meta-variable called RecordId which you can use also.
</div>
--- 

<br>
<div class="notices blue">
<h2>My vtigercron.php script isn't working because I don't have PHP CLI installed. How can I fix that?</h2>
</div>

<h3>I found this solution via google, so I guess more people have had problems. I changed line 19 of vtigercron.php into:</h3>

```php
if (PHP_SAPI === "apache2handler" || (isset($_SESSION["auth...
```
<h3>Originally the ‘apache2handler’ is set to ‘cgi’ if I remember correctly. I remember having to add a temporary line to the vtigercron.php file to check what my setting needed to be, so this could be used as a selector. <br><br>

I found this <a href="https://discussions.vtiger.com//discussion/53017/vtiger-5-4-0-cron-jobs/p1">forum post in which this was mentioned that helped me</a>.<br>
This was the solution I used from that forum post:<br><br>

<strong>FIX POSTED</strong> for vtiger 5.4.0 cron error: <strong> "Access Denied" </strong> when file permissions set correctly <br> <br>

After some debugging, I found that the error occurring in [vtiger ]/vtigercron.php occurs in the first line of code after the includes:
<br> <br>
ERROR LOCATION <br>
</h3>

```php
if (PHP_SAPI === "cli" || (isset($_SESSION["authenticated_user_id"]) && isset($_SESSION["app_unique_key"]) && $_SESSION["app_unique_key"] == $application_unique_key)) {
```
<h3>This statement fails because PHP_SAPI <> "cli", furthermore session variables $_SESSION["app_unique_key"] and $_SESSION["authenticated_user_id"] are blank.<br><br>
FIX INSTRUCTIONS <br><br>
</h3>

1.  To fix, add the following line above that statement to find out what value PHP_SAPI is for YOUR server.
```php
echo(PHP_SAPI);
```
1.  Check your adminstrative email for the cron job or check the log. You will notice that the value of PHP_SAPI is not "cli" but rather something like "cgi-fcgi" (or fast cgi).
2.  In the statement above , if(PHP_SAPI === "cli" …. , replace "cli" with "cgi-fcgi" or whatever your value of PHP_SAPI is. And of course, you can now delete the echo statement.

---
<br>
<div class="notices blue">
<h2>My vtigercron.php script isn't working because I don't have PHP CLI installed. I changed the CLI to apache2handler following the previous question. Can that produce any problems?</h2>
</div>

<h3>The answer is that we don't know. The list of possible values and environments within which coreBOS cron can run are very big, the minor implications of each one and how they can affect the crons are nearly impossible to test. What we HAVE tested is PHP CLI and that will work.<br><br>

For example, simple crons like SendReminder which simply launches an SQL command and sends an email should have no problem in any environment, but workflows, scheduled reports or importing could have a different set of issues depending on the environment. Exactly apache2handler means you are running in a shared environment and under normal user restrictions, that could produce permission issues with the scheduled reports file attachments, in which case the email could not pick up the generated file, but that really depends on the configuration of the operating system….<br><br>

In short, you most probably won't have any problems with the change, but it is difficult for us to state that categorically.</h3>

---

<br>
<div class="notices blue">
<h2>I know as a security feature vtiger CRM and coreBOS will auto log out a user after a certain time. Is there a way to adjust how long the system waits before auto logging out a user?</h2>
</div>

<h3>Neither vtiger CRM nor coreBOS have any timeout logout security measures. This is managed by PHP. What vtiger CRM and coreBOS do is save authentication information in the PHP session. If this session is deleted then your browser cannot login and will ask you for credentials again. For security reasons, PHP deletes the session information every now and then, and you get kicked out of coreBOS. So to change this behavior you have to configure your PHP, not coreBOS. <a href="https://it.lmgtfy.app/?q=php+garbage+collection+gc_probability">Look for gc_probability, gc_maxlifetime and the other garbage collector (gc_) variables.</a></h3>

---

<br>
<div class="notices blue">
<h2>How to extend the session. I keep getting logged out of the program</h2>
</div>

<h3>This issue is not directly related to the application itself. The problem is that sensitive information like the password is saved in the PHP session variables. While that session is alive, the application can pick up the values and authenticate. PHP has a process that eliminates the session variables on a variable time span. When PHP clears the variables, the application cannot authenticate and asks again for the information.<br><br>

The PHP variables that control this are the <strong>Garbage Collector</strong> variables. In php.ini is <strong>gc_probability</strong> default set to 0, because Ubuntu use its cron job for cleaning php session files (<a href="https://www.appnovation.com/blog/session-garbage-collection-php">more info</a>).<br><br>

You can also increase <strong>session.gc_maxlifetime</strong> in php.ini.</h3>

---
<br>
<div class="notices blue">
<h2>From Portal column doesn't display the correct value. It seems that even though my customers create tickets from the Customer Portal, the column From Portal is NO for all the tickets. How does this work? Should it not be YES for the tickets created from Customer Portal?</h2>
</div>

<h3>The From Portal field is really an internal field for ticket notification management. So its value is forced so that the workflow notifications work correctly. The value of this internal field is changed so that the notifications go out when they should.</h3>

If you need a way to determine if a given ticket came from the portal or not I would recommend you do this:<br>

- create yourself a custom field checkbox called "Created by portal" (or something like that)
- modify the "Workflow for Ticket Created from Portal" workflow by adding an "Update Field" task and set your custom field to true
- use your custom field for filtering and reports
- forget that the from_portal field exists :-)

In any case if you do want to go down the path of changing the way that field works and adapting the workflows accordingly it all happens in the file: modules/HelpDesk/HelpDeskHandler.php

---
<br>
<div class="notices blue">
<h2>Automatic number fields are not sorting correctly. For example, I get TT1, TT11, TT12, TT2,... instead of TT1, TT2, TT3, ..., TT11, TT12</h2>
</div>

<h3>This is because it is not a numeric field but a text field due to the initial text prefix, the whole field is text, and text sorts differently than numbers. In fact, if you do an alphabetic or dictionary sort you will see that the order is correct.<br><br>

To fix this, the solution is to add as many zeros 0 as you think you will have numbers. For example, in the above cases we could define the numeric part with a length of 3, so it would end up like this: TT001, TT002, TT003, …, TT011, TT012. Which will sort correctly for the first 1000 autonumeric field values.<br><br>

Since you most probably have an incorrect setup you can play around with this query, you will need to run multiple queries based on the Ticket number length. It will add 0's to the number. Thanks VTE</h3>

```sql
### SELECT - Testing
SELECT 
  ticketid,
  ticket_no,
  LEFT(ticket_no, 2) AS TT,
  RIGHT(ticket_no, 3) AS num,
  CONCAT(LEFT(ticket_no, 2), '0', RIGHT(ticket_no, 3)) 
FROM
  `vtiger_troubletickets` 
WHERE LENGTH(ticket_no) < 6  AND LENGTH(ticket_no) >= 5
```

```sql
### Update
UPDATE
  `vtiger_troubletickets` 
  SET ticket_no=CONCAT(LEFT(ticket_no, 2), '0', RIGHT(ticket_no, 3)) 
WHERE LENGTH(ticket_no) < 6  AND LENGTH(ticket_no) >= 5

```

<div class="notices yellow">
If you are rolling your own code you can also get the right order with this trick:<br><br>
<div class="notices blue">
SELECT * FROM vtiger_accounts ORDER BY LENGTH(account_no), account_no;</div>
Got from <a href="http://discussions.corebos.org/thread-217.html">our forum</a> and <a href="https://stackoverflow.com/questions/153633/natural-sort-in-mysql/12257917#12257917">from here</a>.
<br><br>

thanks Peter! </div>

---
<br>
<div class="notices blue">
<h2>How can I reset the admin user password?</h2>
</div>

<h3>Execute this SQL in your database:</h3>

```sql
UPDATE vtiger_users SET user_password='$1$ad$hsl2KFybNRnbXBa.b.WWv.',
  crypt_type='MD5', failed_login_attempts=0 WHERE id=1;
```
---
<br>
<div class="notices blue">
<h2>How can I deactivate the "Don't show this dialog" or "evitar que este pagina cree dialogo" checkbox on alert messages?</h2>
</div>

<h3>AFAIK you can't, this is a security measure imposed by the browser and there is nothing you can do about it. The only solution is to simply ignore it and continue on with your work.

In case you have already checked it, Log out of the application, close the browser, open it again and access the application normally. The setting only lasts for the session, so alerts will be re-enabled once the new session begins in the new tab.</h3>

---
<br>
<div class="notices blue">
<h2>How can I hide the Tag Cloud for all users?</h2>
</div>

<h3>Directly in the database:</h3>

```sql
UPDATE `vtiger_homestuff` SET `visible`=1 WHERE `stufftype`='Tag Cloud'
```
---
<br>
<div class="notices blue">
<h2>Is there a way to make a shortcut (web based) that takes a user directly to a trouble ticket that is associated with a specific asset? In other words, simply clicking on a link it would add a new trouble ticket to the asset.</h2>
</div>

<h3>Yes. The trick here is to emulate the action of clicking on the "Add Ticket" button on the Tickets related list in Assets. This would look like this:</h3>

```
https://your_server/your_corebos/index.php?module=HelpDesk&return_module=Assets&return_action=CallRelatedList&return_id=YOUR_ASSET_CRMID&cbfromid=YOUR_ASSET_CRMID&action=EditView&createmode=link
```
<h3>Obviously the dynamic part of the URL is the asset CRMID you want to relate the ticket with, YOUR_ASSET_CRMID, in the example. Using the coreBOS Tests example data, there is an asset with CRMID 4062, so I constructed this URL:</h3>

```
http://localhost/coreBOSwork/index.php?module=HelpDesk&return_module=Assets&return_action=CallRelatedList&return_id=4062&cbfromid=4062&action=EditView&createmode=link
```
<h3>and it worked as expected.</h3>
---

<br>
<div class="notices blue">
<h2>My user has blocked access to his account due to too many login attempts. How can I reset his access?</h2>
</div>

<h3>If you have access as an admin user, you can go to Settings > Users and edit the profile of the user who has blocked access. Search for the "Login Attempts" field and set it to 0. <br><br>

If you have blocked all the admin users you will have to go directly to the database, find the admin users' row in the vtiger_users table and set the "loginattempts" column to 0</h3>

---
<br>
<div class="notices blue">
<h2>How can we roll back a mass edit?</h2>
</div>

<h3>Some ideas come to mind, all rather "techy":</h3>

- Recover from a backup of the database. This is the easiest option with the only downside of losing information/work since the last backup, but you are doing frequent backups anyway, right? :-)
- If the amount of work done doesn't permit you to recover from the database then you can recover the backup database into a copy, extract the table with the lost data, and copy it into the production database. Now create an update SQL command to update the incorrectly updated fields from the backup table. This option is a surgical backup recovery only of the fields you have updated instead of a full backup recovery. [You can read the exact steps here.](../04.tutorials/01.recovermasseditchange)
- Another similar alternative to the last step is using the coreBOS history tracker. If you have ModTracker activated on the module you have mass edited, then you have a register of the old and new values in the ModTracker database tables. So you can manually handcraft update SQL commands to recover the original values. This is like recovering from the backup table but harder and you must have ModTracker active before doing the mass edit.
- If you have Record Versioning active on the module with the mass edit error then it is REALLY simple, you just set the previous version as the active record. I don't remember if that can be done as a mass action but since all the other solutions require going to the database, you can go there also to make the previous version active if it can't be done through the UI.

---
<br>
<div class="notices blue">
<h2>Inventory module Purchase Order does not permit inline edit when total and subtotal are negative</h2>
</div>

This is due to the validation of typeofdata field that the application does. The typeofdata column for those two fields is set to `N~O`, a non negative number. We have to set it to a Negative Number (`NN`) with this SQL

```sql
UPDATE `vtiger_field` SET `typeofdata` = 'NN~O'
WHERE `vtiger_field`.`fieldname` in ("hdnGrandTotal","hdnSubTotal")
  AND tablename = "vtiger_purchaseorder"
```
