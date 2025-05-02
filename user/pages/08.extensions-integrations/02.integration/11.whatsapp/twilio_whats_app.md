---
title: 'Twilio WhatsApp'
metadata:
    description: 'The Twilio API for WhatsApp is the quickest way to add two-way messaging on WhatsApp into your web application'
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
        - integration
    tag:
        - WhatsApp
---

Twilio has created an API to integrate applications with WhatsApp. So you can send WhatsApp messages for marketing campaigns (for example) through another application. We have integrated this into coreBOS.

===

It works both ways. First, you send the WhatsApp message, then a Message record is created in the application and when the message is opened and read, Twilio sends a push notification marking the `Open` field in the Message record of coreBOS.

The first thing you should do is create a Twilio account. It is free at the beginning and you have a sandbox where you can test the integration before going live. Twilio will provide you with a number from which you can start testing the API. You have to register also some numbers you want to send the test message to.

![](screenshot_from_2019-02-18_10-41-35.png?width=100%)

Get the Sid, token and `from number` from Twilio

![](screenshot_from_2019-02-15_10-29-38.png?width=80%)

and put it in coreBOS in the Utilities extension *(index.php?module=Utilities&action=integration)*

![](screenshot_from_2019-02-15_12-20-19.png?width=80%)

We have created a Workflow Task type for WhatsApp messages. So we are going to create a new Workflow. For example, we want to send a message while saving a Contact that fulfills some conditions. We choose the phone fields of the module to which we are sending the message and we write the message body. We can also attach one or more files to the message. In this case, we are sending two or more messages. One with a message and another with attachments. You can send only attachments of a maximum size of 5MB. We are also creating multiple message records in coreBOS. One for the text message and another for the attachments.

![](screenshot_from_2019-02-15_15-59-08.png?width=80%)

![](screenshot_from_2019-02-18_15-04-25.png?width=80%)

After these steps, we can make a test and see the message arriving in WhatsApp and the records created in the CRM.

![](1550499687726.jpeg?width=40%)

![](screenshot_from_2019-02-18_15-08-38.png?width=100%)


On the other hand, to get the message status, we have to register a Callback URL in Twilio.

![](screenshot_from_2019-02-18_10-35-24.png?width=100%)


There is a file in coreBOS that gets the Twilio push notifications and updates the Open field in the Message with +1 each time a message is opened and read.

![](screenshot_from_2019-02-18_15-27-00.png?width=100%)

If we want to go live, we should upgrade the Twilio account, register one or more phone numbers as `from numbers`, and wait for Twilio to confirm them.

------------------------------------------------------------------------

[Next](../12.woocommerce) | Chapter 12: WordPress Woocommerce Integration

------------------------------------------------------------------------