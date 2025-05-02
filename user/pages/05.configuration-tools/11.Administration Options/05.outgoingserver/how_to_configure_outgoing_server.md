---
title: 'How to Configure Outgoing Server'
metadata:
    description: 'Configuration of Outgoing Server.'
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
        - email
        - outgoing
        - outgoingserver
---

coreBOS needs an email account to send out administrative emails regarding the operation of the application. Using this email account the program will send warning emails from workflows, notification of calendar events and end of import information (for example).

Since the application requires this email account we decided to also use it to send normal work email messages from the users. For this to work and appear that each user sends emails from his own email we use a feature implemented into the mailing protocol (SMTP) called RELAY. Using this technique, the program connects to the server with the account that is configured and tells it that it will be sending an mail on behalf of another email account.

This characteristic of the SMTP system has gone through a phase of bad press because of its abuse by spammers and viruses that exploit it to send unauthorized messages on behalf of other users. That is why some servers, with stricter security measures, do not support this feature and will **NOT** work with coreBOS or only allow sending emails as one single user, the one configured in the outgoing server settings.

The outgoing server settings can be set in the Settings section of the application and in there, in the Outgoing Server section.

```
Settings > Outgoing Server
```

![](outgoingserver.png?width=100%)

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Outgoing Server	</strong></td>
<td>this is the server to which we must connect to send emails. This field supports a special extended syntax with which we can specify the protocol and port to use like this:<br>

<div class="notices blue">
tls://smtp.gmail.com:587

or

ssl://msexchange:587 </div></td>
</tr>
<tr>
<td><strong>User Name and Password</strong></td>
<td>the user name and passwords that will give us access to the server</td>
</tr>
<tr>
<td><strong>handler_method</strong></td>
<td>The exact name of the function that will be called. In the script indicated in the previous column, we can have as much code as we need to, with many functions and full access to all of the coreBOS infrastructure, but only ONE function will be called for each service. This column indicates which one</td>
</tr>
<tr>
<td><strong>Email From</strong></td>
<td>This field will force all emails leaving the system to seem to come from this email. Although the email will be sent from this account, the "Reply to" field will be the email of the user sending the email. Thus if the recipient clicks on respond the response will be sent to the user. I suppose this has some spam/company image justification</td>
</tr>
<tr>
<td><strong>Requires Authentication?</strong></td>
<td>permits us to define the protocol to use for the connection</td>
</tr>
</tbody>
</table>

When you save the connection data, coreBOS will launch a test to connect and send an email. If the email is not successfully sent **NO** data will be saved. We will be returned to the configuration page with a message saying that the email could not be sent. At this point, there is a connection, authentication or lack of RELAY support error and you must go to the [debugging techniques](../../../10.developer-guide/04.development_framework/04.debuging/item.md#email).

<div class="notices red">
When we are returned to the settings page, the previous values are present. We cannot see the password field but is it most probably INCORRECT, the value you introduced is NOT filled in again. Please introduce the password on ALL tests that you launch.
</div>

<div class="notices red">
coreBOS prior to March 2015 did not support sending emails with an empty body. The error message returned was very misleading indicating that there was a problem with the email configuration. <strong>DO NOT test</strong> emails with empty bodies. As of March 2015 emails with no body are supported.
</div>

If we reach this message while debugging:

```
SMTP -> FROM SERVER:550 5.7.1 Client does not have permissions to send as this sender
SMTP -> ERROR: DATA END command failed: 550 5.7.1 Client does not have permissions to send as this sender
SMTP Error: data not accepted.
```

The mail server is saying that we do NOT have permission to send. It basically says that the error is because the account that is connected must be the same as the sender, the server does not support RELAY.

If you reach this point, I recommend you register for an account at [sendgrid](https://sendgrid.com/), it really works great and gives you much more information than you have now. They have free accounts with a limit of 400 emails a day and for a small amount of money, you can do even more. We use it regularly to mass mailings from coreBOSCRM and to control administrative email deliveries. It is worth more than it costs.

## Some pages related to problems configuring outgoing server

- [http://community.office365.com/es-es/f/203/t/199699.aspx](http://community.office365.com/es-es/f/203/t/199699.aspx)
- [https://discussions.vtiger.com/index.php?p=/discussion/55230/smtp-mail-settings-for-office-365-exchange/p1](https://discussions.vtiger.com/index.php?p=/discussion/55230/smtp-mail-settings-for-office-365-exchange/p1)
- [http://technet.microsoft.com/en-us/library/dn554323.aspx](http://technet.microsoft.com/en-us/library/dn554323.aspx)

## FAQ

<div class="notices blue">
<h2>Method for installing coreBOS on a 1and1 Linux Shared Hosting Package</h2> </div>

[This very old PDF file](vtigercrm_1and1_installation.pdf) shared on the forum explains some issues. The important part is this one:
Open the file vtigercrm/modules/Emails/class.phpmailer.php in your favorite text editor.
Find the following lines:

```
function IsSMTP() {
$this->Mailer = "smtp";
```

Change "smtp" to "sendmail"

---

<div class="notices blue">
<h2>How do I configure a gmail account?</h2>
</div>

This forum thread says that you have to use **smtp.gmail.com** and select **TLS** as the authentication method. Also leave the "Email from" field empty as (I think) gmail does not support that feature.

Also [this page explains activating the service on Google side](../05.outgoingservergmail).

---

<div class="notices blue">
<h2>How can I check my spam score?</h2>
</div>

Send an email from the application to the email address indicated at [Mail Tester](https://www.mail-tester.com/) and after a few seconds click on the "Check Score" button. Review the recommendations and repeat.

---

## Debugging errors

Activate the debug log at level **FATAL** and set the **Debug_Email_Sending** global variable to 1. This will send the whole conversation between coreBOS and the email server to the log file so you can diagnose the problem.

<div class="notices blue">
In previous versions, we used to need the changes below which I leave here as a reference only. The global variable method is better.
</div>

To debug the outgoing email server the best is to activate PHPMailer debugging with the changes below and look in the debug log file (logs/vtigercrm.log)

```diff
diff --git a/modules/Emails/class.phpmailer.php b/modules/Emails/class.phpmailer.php
index 8427255..61bd55c 100644
--- a/modules/Emails/class.phpmailer.php
+++ b/modules/Emails/class.phpmailer.php
@@ -326,7 +326,7 @@ class PHPMailer
      * @var integer
      * @see SMTP::$do_debug
      */
-    public $SMTPDebug = 0;
+    public $SMTPDebug = 4;
 
     /**
      * How to handle debug output.
diff --git a/modules/Emails/mail.php b/modules/Emails/mail.php
index a8cac72..7674172 100755
--- a/modules/Emails/mail.php
+++ b/modules/Emails/mail.php
@@ -328,7 +328,14 @@ function setMailServerProperties($mail)
        $mail->Host = $server;          // specify main and backup server
        $mail->Username = $username ;   // SMTP username
        $mail->Password = $password ;   // SMTP password
-
+global $log;$log->fatal(array(
+       'SMTPOptions' => $mail->SMTPOptions,
+       'SMTPSecure' => $mail->SMTPSecure,
+       'Host' => $mail->Host = $server,
+       'Username' => $mail->Username = $username,
+       'Password' => $mail->Password = $password,
+));
+$mail->Debugoutput = function($str, $level) { global $log;$log->fatal($str);};
        return;
}
```