---
title: 'SMS Notifier'
metadata:
    description: 'By using *SMS Notifier* extension you can communicate with your clients faster by sending personalized SMS Messages to customers.'
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
        - sms
---

By using *SMS Notifier* extension you can communicate with your clients faster by sending personalized SMS Messages to customers. Consequently, you can increase your sales and strengthen the relationship with your customers.

===

SMS Server Configuration
------------------------

To send SMS you need an SMS service provider details; This can be filled
by administrator from Settings page:

    *Go to Settings Icon > Module Manager. This can be found under Studio block.
    *Click on Settings Icon next to SMS notifier.
    *Click on the link **Server Configuration**

You can configure SMS Server information by clicking on **Server Configuration**.

![](smsserverconfiguration.png?width=70%)

Click on the *Add New* button and provide SMS provider information.

![](addnewaccount.png?width=50%)

<div class="notices blue">
The login details will be provided by
your SMS provider. You will have to register and buy login credentials
from them.</div>

Working
-------

### Sending Bulk SMS

To send SMS in bulk, go to the list view of Leads, Contacts, or
Organizations, Select the desired number of records and click on the
*Send SMS* button.

![](sendsms.png?width=70%)

When you click the button it will show all the phone fields available
for that module. You can select the field to which you want to send the
SMS and click on the *Select* button.

![](selectphonefield.png?width=50%)

### Compose SMS

This will now open a compose window block to type in your message. Click
on the *Send* button to send the message.

![](composesms.png?width=70%)

### SMS Log Details

Once an SMS is sent, the entry will be saved as a record in the *SMS
Notifier* module. The detail view contains the message body and status
of the message. The *Assigned To* field is the user who has sent the
SMS.

![](detailviewsms.png?width=70%)

### SMS Status

The status of the message can be **Delivered**, **Processing** or
**Failed**. The status information can be seen, indicated with colors,
in the detail view of the SMS record.

![](smsstatus.png?width=100%)

More Information
----------------

When an SMS is sent to a record(s) of any module (like Organizations,
Contacts or Leads), the history of messages sent will be listed in the
*More Information* tab of the particular record.

By default, a copy of the SMS will be sent to the user sending the SMS
if that user has his mobile phone configured in his preferences. If you
want to deactivate that functionality you can use the global variable
**SMSNotifier\_SendCopyToUser** setting it to 0

SMS Task with Work flow
-----------------------

Create a Work Flow and save it with the desired conditions. Click on the
*New Task* button and select SMS Task to automate the process of sending
SMS.

![](workflowsmstask.png?width=70%)

![](smsstaskworkflow.png?width=70%)

### Create SMS Task

Provide a label to the task and set the Status of the workflow. From the
Recipients field, select the number of users to whom the message should
be sent. While composing the message, Select the field values from the
dropdown to fill the values in the text area below.

![](workflowmessage.png?width=70%)

Test Provider
-------------

There is one special provider named Test Functionality that will
activate the service and log the calls made to the SMS gateway in the
log file. This is very useful for debugging and validating the
functionality of the service.

Writing Custom Providers
------------------------

If you have planning to use SMS service provider and don't find the
connector to it, you will need to write one.

SMSNotifier module defines ISMSProvider

```php
modules/SMSNotifier/ext/ISMSProvider.php
``` 
interface which should be
implemented by your custom provider.

A template sample provide is available at:
```php
modules/SMSNotifier/ext/providers/MyProvider.php.sample
```

Also look at ClickATell and other provider implementations:
```php
modules/SMSNotifier/ext/providers/ClickATell.php
```

### Currently supported Providers

-   [ClickATell](https://www.clickatell.com/), both HTTP and REST API
-   [TeleFacil](https://www.telefacil.com/wiki/index.php/Integraci%C3%B3n_con_Mensajer%C3%ADa_SMS_(SMSNotifier))
    (DuocomSMS)
-   [Skebby](http://www.skebby.com)
-   [SMS Factor](https://www.smsfactor.com)
-   [SMS Hosting](https://www.smshosting.it/en)
-   [SMS Masivos](http://www.smasivos.com)
