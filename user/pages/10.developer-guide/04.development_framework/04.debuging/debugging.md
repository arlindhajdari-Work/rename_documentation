---
title: Debugging
metadata:
    description: 'Debugging'
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
        
    tag:
        - debug.log
---

PHP
---

-   Turn on logging library usage, in file config.inc.php
    ````
    $LOG4PHP_DEBUG = true;
    ```
-   Activate the type of logging and log level, in the file
    include/logging/config.php
    -   for example, for the main application log file set 
    ```
        'APPLICATION' =>; [
          'Enabled' => true,
          'Level' => 'DEBUG',
          'MaxBackup' => 10,
          'File' => 'corebosapp',
       ],
    ```

-   The log files will be written in the **logs** directory. For the
    rootLogger it will be logs/corebosapp-{date}.log

<div class="notices red">
Make sure logs/ folder has write
access to apache server process owner. </div>

<div class="notices blue">
When you activate the DEBUG level a
lot of information gets written into the log file, among this data is
the regular Activity Reminder call which is rather bothersome. You can
deactivate that call using the <strong>Debug_ActivityReminder_Deactivated</strong>
global variable </div>

<div class="notices blue">
In coreBOS installs prior to March 2021, you have to set the debug level in the file log4php.properties
</div>

Database
--------

-   Turn on debuging for ADODB instanced in
    include/database/PearDatabase.php (at end of file)
     ```
     if(empty($adb)) {
     $adb = new PearDatabase();
     $adb->connect();
     // ADD THIS LINE
     $adb->setDebug(true);
    }
    ```

Smarty
------

-   In file, Smarty\_setup.php add the following to class constructor
    ```
    function `function vtigerCRM_Smarty() {
     $this->Smarty();
     $this->template_dir = 'Smarty/templates';
     // ...
     // ADD THIS LINE
     $this->debugging = true;
    }
    ```
AJAX and Javascript
-------------------

-   Chrome and Firefox have webdevelopers tools and firebug.
-   [Interesting explanation on how to see javascript errors](http://codex.wordpress.org/Using_Your_Browser_to_Diagnose_JavaScript_Errors#Step_3:_Diagnosis)
-   [Javascript Debugging](../07.jsdebuging)

Global Variables
----------------

There are various debug global variables that can help you diagnose
problems with your coreBOS installation.

Webservice
----------

-   What I usually do is edit the curl call and dump the raw result
    coming from coreBOS. Obviously the log4php system is also very
    useful in this case.
-   The exact code change is one of these two depending on POST or GET
    calls:

```

    diff --git a/vtwsclib/Net/curl_http_client.php b/vtwsclib/Net/curl_http_client.php
    index c52dd76..a42eb3c 100644
    --- a/vtwsclib/Net/curl_http_client.php
    +++ b/vtwsclib/Net/curl_http_client.php
    @@ -183,7 +183,7 @@ class Curl_HTTP_Client
     
            //and finally send curl request
            $result = curl_exec($this->ch);
    -
    +var_dump($result); // GET
            if($this->has_error())
            {
                return false;
    @@ -243,7 +243,7 @@ class Curl_HTTP_Client
     
            //and finally send curl request
            $result = curl_exec($this->ch);
    -
    +var_dump($result);  // POST
            if($this->has_error())
            {
                return false;
```
Also, the ajax call in the browser can be seen and is very useful also
to see the raw result (Firebug is your friend)

Additionally, one of our former team members [used this patch](https://discussions.corebos.org/documentation/lib/exe/fetch.php?media=devel:patches:debug_webservices.diff), which produces the error on screen or in the AJAX response.

Email
-----

[Have a read here about how coreBOS outgoing email server works and how to configure it](../../../05.configuration-tools/11.Administration%20Options/05.outgoingserver).

Activate the debug log at level **FATAL** and set the
**Debug\_Email\_Sending** global variable to 1. This will send the whole
conversation between coreBOS and the email server to the log file so you
can diagnose the problem.

<div class="notices blue"> In previous versions, we used to need
the changes below which I leave here as a reference only. The global
variable method is better. </div>

To debug the outgoing email server the best is to activate PHPMailer
debugging with the changes below and look in the debug log file
(logs/vtigercrm.log)
```
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

Frequent problems
-----------------

<div class="notices blue">
<h2>Sorry! Attempt to access restricted file</h2>
<p>Make sure the webserver user has write permission in the <i>user_privileges</i> directory and that the new user's permission file is correct (it will be user_privileges_##.php and sharing_privileges_##.php). <br> <br>

If that is correct (most probably will be or you wouldn't get to this error) you will have to add some debug message to see exactly what file the application is looking for and can't find. That will be something like this: <br> <br>

<a href="https://github.com/tsolucio/corebos/commit/26cf68eb89b888aa71d99f3d0e1e5d48b6cf7081"><strong>https://github.com/tsolucio/corebos/commit/26cf68eb89b888aa71d99f3d0e1e5d48b6cf7081</strong></a>
 </p>
</div>