---
title: 'Payment gateway'
metadata:
    description: 'The Payment module of coreBOS includes a payment gateway that we can configure to use any of the online payment services supported.'
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
        - paymentgateway
---

The Payment module of coreBOS includes a payment gateway that we can configure to use any of the online payment services supported. Once configured, we just have to include the necessary HTML code to send the user to the gateway and the rest of the process is automatic.

## Configuration

Before being able to use it, it is necessary to configure the payment gateway. Access the integrations page:

index.php?action=index&module=Utilities

The configuration contains a block with the key **corebos** to configure the access to coreBOS and a key **omnipay** to configure access to the gateway by Omnipay. The following is an example to use Redsys, other gateways will use different parameters.

## Usage
The cases of contemplated use are the following:

1. **Pending Payment** The client is required to pay an outstanding debt.
2. **Order registration + Payment** We register an order from the customer and then we ask for payment.
In both of these cases, the payment is made in a web browser.

## Pending Payment
The client has already registered a debt in the Payment module of coreBOS, we may have done it manually or by other means such as workflows or web services. As the client does not have access to coreBOS we can send him an email detailing the pending payment and access to the gateway to make this payment or if we have a web for clients (customer portal), we can do it there on their pending payments page.

![](paymentgatewayexist.png?width=100%)

## Implementation

We will include the following form in the mail or web page that should redirect to our gateway.

```php
<form action="https://url/notificationdriver.php?type=Pay" method="POST">
  <input type="hidden" name="cpid" value="...">
  <input type="submit" value="Pay">
</form>
```
Optionally we can include these variables in the form to have greater control of the transaction:

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Return Pages</strong></td>
<td><strong></strong></td>
</tr>
<tr>
<td><strong>notify_url</strong></td>
<td>URL to notify about the payment result</td>
</tr>
<tr>
<td><strong>return_url	</strong></td>
<td>URL of the page to which the user will return if the payment is correct</td>
</tr>
<tr>
<td><strong>cancel_url</strong></td>
<td>URL of the page to which the user will return if the payment is incorrect</td>
</tr>
</tbody>
</table>
<br>
The notification is sent as a POST request to the URL that we indicate in notify_url.

## Order registration + Payment

If the customer registers his own purchase, for example in an online store, we can register the purchase data from there in coreBOS at the same time it is confirmed and then direct the customer to the payment gateway.

![](paymentgatewaycart.png?width=100%)

The data that this operation needs is:

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Client Data</strong></td>
<td><strong></strong></td>
</tr>
<tr>
<td><strong>nif</strong></td>
<td>NIF</td>
</tr>
<tr>
<td><strong>firstname</strong></td>
<td>first name</td>
</tr>
<tr>
<td><strong>lastname</strong></td>
<td>last name</td>
</tr>
<tr>
<td><strong>mobile</strong></td>
<td>cell phone</td>
</tr>
<tr>
<td><strong>email</strong></td>
<td>email</td>
</tr>
</tbody>
</table>
<table class="table table-striped">
<tbody>
<tr>
<td><strong>Sales Data</strong></td>
<td><strong></strong></td>
</tr>
<tr>
<td><strong>subject</strong></td>
<td>Reference</td>
</tr>
<tr>
<td><strong>firstname</strong></td>
<td>first name</td>
</tr>
<tr>
<td><strong>moreinfo</strong></td>
<td>Description</td>
</tr>
<tr>
<td><strong>fecha</strong></td>
<td>Date</td>
</tr>
<tr>
<td><strong>pdoid</strong></td>
<td>Product ID</td>
</tr>
</tbody>
</table>
<table class="table table-striped">
<tbody>
<tr>
<td><strong>Return Pages</strong></td>
<td><strong></strong></td>
</tr>
<tr>
<td><strong>notifyUrl</strong></td>
<td>URL to notify about the payment result</td>
</tr>
<tr>
<td><strong>returnUrl</strong></td>
<td>URL of the page to which the user will return if the payment is correct</td>
</tr>
<tr>
<td><strong>cancelUrl</strong></td>
<td>URL of the page to which the user will return if the payment is incorrect</td>
</tr>
</tbody>
</table>
<br>

We will include this information in a form like this:

```php
<form action="https://url/notificationdriver.php?type=Pay" method="POST">
  <input type="hidden" name="..." value="...">
  ...
  <input type="submit" value="Pay">
</form>
```
When you send the form, the Payment will be created and the payment process will start in the configured gateway.

## Payment gateway in the Client Portal coreBOSCP

The payment gateway of coreBOS is directly integrated into the customer portal. The payment records associated with each contact can be seen in the portal and appear with some buttons to make the payment as you can see in the following two images:

![](pasarelacypenportallv.png?width=100%)
![](pasarelacypenportaldv.png?width=100%)

When clicking on the icon, we will access directly to the defined payment gateway and upon completion of the payment, we will return to the client's portal, either to the page *index.php#site/ThankYouForPayment* if the payment has been made correctly or to *index.php#site/ErrorInPayment* if there have been any error.

<div class="notices blue">

The correct and erroneous payment pages in the portal can be easily customized by editing the files:<br><br>

- protected/views/site/ThankYouForPayment.php<br>
- protected/views/site/ErrorInPayment.php
</div>