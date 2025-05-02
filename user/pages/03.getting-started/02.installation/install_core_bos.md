---
title: 'Install coreBOS'
metadata:
    description: 'How to install coreBOS'
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
        - installation
    tag:
        - install
        - getting-started
---

## Requirements

- Apache 2.x or above.
- MySQL 8.x
- PHP from 7.4.x to 8.1. PHP 8.1 is recommended.

<span></span>

 !!! This is a typical **WAMP/LAMP stack**. All linux distributions have this natively so we recommend you install the packages from your distribution (make sure you have the right versions). On windows download the XAMPP stack from apache friends. You can see the [list of application versions here](http://code.stephenmorley.org/articles/xampp-version-history-apache-mysql-php).

### MYSQL Requirements

Please make sure to review MySQL configuration (my.cnf or server start parameters)

<table class="table table-striped">
<tbody>
<tr>
<td>ENGINE=InnoDB</td>
<td>Should be available. (Turn off --skip-innodb)</td>
</tr>
<tr>
<td>ANSI Mode</td>
<td>Should be disabled</td>
</tr>
</tbody>
</table>

### PHP Extensions

Following extensions should be enabled for your PHP setup

<table class="table table-striped">
<tbody>
<tr>
<td>GD</td>
<td>Mandatory</td>
<td>Charts and graphs generation are dependent on this library.</td>
</tr>
<tr>
<td>IMAP</td>
<td>Mandatory</td>
<td>Webmails Module is dependent on this library.</td>
</tr>
<tr>
<td>Zlib</td>
<td>Mandatory</td>
<td>Used for backups and module packaging among others</td>
</tr>
<tr>
<td>DOM (php-xml)</td>
<td>Mandatory</td>
<td>For coreBOS Updater and GenDoc (at least)</td>
</tr>
<tr>
<td>OpenSSL</td>
<td>Optional</td>
<td>Imap with OpenSSL should be enabled in case Mail server needs to be connected via SSL</td>
</tr>
<tr>
<td>Curl</td>
<td>Optional</td>
<td>This one is optional but really important for any external communications, like SMS, Google Sync or RSS</td>
</tr>
<tr>
<td>MBString</td>
<td>Mandatory</td>
<td>Used everywhere now that we support PHP 8</td>
</tr>
</tbody>
</table>

### PHP Configuration

Make sure to verify if your PHP configuration meets the recommended values.

<table class="table table-striped">
<thead>
<tr class="header">
<th>Variable</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>allow_call_time_pass_reference</td>
<td>on</td>
</tr>
<tr>
<td>error_reporting</td>
<td>E_ERROR</td>
</tr>
<tr>
<td>safe_mode</td>
<td>off</td>
</tr>
<tr>
<td>display_errors</td>
<td>on</td>
</tr>
<tr>
<td>file_uploads</td>
<td>on</td>
</tr>
<tr>
<td>max_execution_time</td>
<td>600</td>
</tr>
<tr>
<td>max_input_vars</td>
<td>6000</td>
</tr>
<tr>
<td>post_max_size</td>
<td>36M</td>
</tr>
<tr>
<td>memory_limit</td>
<td>1024M</td>
</tr>
<tr>
<td>log_errors</td>
<td>off</td>
</tr>
<tr>
<td>output_buffering</td>
<td>on</td>
</tr>
<tr>
<td>register_globals</td>
<td>off</td>
</tr>
<tr>
<td>request_order</td>
<td>GP</td>
</tr>
</tbody>
</table>

 ! The maximum size of file uploads is defined by the PHP **upload_max_filesize** directive. Remember to set this variable to accommodate the file size you need to upload. coreBOS has a Global Variable that can limit the upload BELOW this directive, never above, PHP defines the maximum limit.
 ! 
 ! I normally set this variable to 32Mb

 ! If you have the PHP Suhosin extension installed, this extension adds restrictions to make PHP more secure, but some of these restrictions break coreBOS.
 ! 
 ! To solve this problem you must change two variables in the suhosin config file: (normally: /etc/php5/conf/suhosin.ini)
 ! 
 ! - suhosin.post.max_vars = 8000
 ! - suhosin.request.max_vars = 8000
 ! 
 ! After this, you must restart your apache server.

 !! For security reasons, it is **VERY** important that you set the value of **request_order** to **GP**.
 !! 
 !! coreBOS barely uses cookies and it does not look for them in the $\_REQUEST superglobal.
 !! 
 !! Most modern Linux servers already set this value to GP by default so you are probably already covered but check just in case.
 !! 
 !! You can [read a little more about this here](https://www.owasp.org/index.php/PHP_Security_Cheat_Sheet#Use_of_.24_REQUEST).

### File Permissions

Provide read-write access to the following files and folder (recursively):

 ! Read and Write permissions should be enabled for user/group who owns webserver process (like www-data or httpd or apache).

- config.inc.php
- install.php
- cache
- storage/
- install/
- user_privileges/
- Smarty/cache/
- Smarty/templates_c/
- modules/
- cron/modules/
- backup/
- Smarty/templates/modules/
- test/
- logs/

**Please make sure you meet all these requirements**

## Install

- Download the source code from GitHub
- copy the code into a folder accessible from your web server install
- type in the URL of the folder into your browser
- you should get the **Configuration Wizard** welcome page

![](corebosinstall01.png?width=100%)

- click on the Install button and accept the license
- Review all the pre-installation checks. You should be able to proceed with some PHP recommendations in red, but ONLY those, any other red check MUST be fixed before proceeding.
- Fill in all the information required and continue
  - you will need a MySQL user with access to a database that may exist or not, if it doesn't exist you will also need a MySQL user with enough permission to create a database
 ! If the database exists it **MUST** be empty, the install procedure DOES NOT migrate, there is a migration procedure available if necessary.

- you can choose the password for the only user that will be created.

![](corebosinstall02.png?width=100%)

- now wait for all the installation work to be done
- if all goes well you should receive a verification page welcoming you to the application
- press the **Finish** button to reach the login page
- **execute the database changes**, this is done using the **[coreBOS Updater](../../10.developer-guide/04.development_framework/11.develtutorials/08.corebosupdater)**, which is a module that will take care of managing all the updates from now on. It will read the set of changes that need to be done and will permit you to apply them and undo some of them.
  - login to the application as the admin user and go to the "**coreBOS Updater**" module.
  - click on the **Get Updates** button
  - go back to the list view and click on the **Apply All** button

For additional security it is recommended that you take three more steps:

1. Configure a [Basic Authentication](https://wiki.apache.org/httpd/PasswordBasicAuth) password protection on the application
2. Delete all unused files. You can launch the **bettersafe.sh** script and also remember to eliminate the install and migration scripts and directory which have been renamed during the install process
3. the **bettersafe.sh** will also **set the config.inc.php file to read-only** which is a very good idea even if you don't want to  execute bettersafe

**Now comes all the fun**

- Configure the application
- Import your data
- Create users

### FAQ

> I installed in windows but the Popup screen is empty.

XAMMP configures your PHP to load files only from a couple of directories. By default, it does not look for files in the current directory which is something that coreBOS depends upon. You must edit your php.ini file, look for the include_path directive and add the current directory. Something like this;

`include_path = ".;C:\php\pear;C:\wamp\www"`

What I usually do when I have to install on Windows is edit config.inc.php and add this line towards the end:

`echo get_include_path();`

then I edit the php.ini directive putting the same value and adding the current directory (.)

> I have problems installing/recovering the database

apply this change in my.cnf `max_allowed_packet = 16M` <https://discussions.corebos.org/showthread.php?tid=1550>

> Checkout this cool oneline install process from one of our users!

[plugin:youtube](https://youtu.be/_c-8Dgxan5Q)

