---
title: 'Popup capture hooks'
metadata:
    description: 'The action of this hook happens when you select a record in a popup capture screen related with a uitype 10 field.'
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
        - event
    tag:
        - hooks
        - popup
---

## Popup capture hooks

The action of this hook happens when you select a record in a popup capture screen related with a uitype 10 field.

Since there are two modules participating in this event there are two ways of seeing and intercepting the event. One from the point of view of the module that is being selected and that is sending the selected field into the underlying module. This is the module that appears in the popup screen and that the user clicks on to select a record. The other point of view is that of the module receiving the selected record, the module that has the uitype 10 field and has it filled in when the user selects a record.

It would be something like these two conversations:

- Sending Module: <p style="color:red;"> I'm in a popup screen and the user just selected one of my records. Do you want to take over and fill in the field or do you want me to do it? </p>
- Receiving Module:<p style="color:red;"> Hey! One of my uitype 10 fields just got filled in. Do you want me to do some additional actions?</p>>

### Popup capture hook. Capture or Sending Module

This hook happens in the GUI on the browser in javascript when the user selects a record inside the popup screen. It launches your javascript code INSTEAD of the default javascript code to fill in the field. That means that you have to do ALL the work. Normally you will call the default function and then do some additional magic that you may require before closing the window.

The typical use case is to fill in some additional fields besides the ones that the default behavior does.

To hook into this functionality you must create a function in your module's javascript file. This function will receive three parameters:

<table class="table table-striped">
<tbody>
<tr>
<td><strong>recordid</strong></td>
<td>the crmid of the record that has been selected in the popup</th>
</tr>
<tr>
<td><strong>value</strong></td>
<td>the text representation of the record that has been selected in the popup</td>
</tr>
<tr>
<td><strong>target_fieldname</strong></td>
<td>the destination field name in the form in the browser</td>
</tr>
<tr>
<td><strong>formname</strong></td>
<td>the form that the destination field is in</td>
</tr>
</tbody>
</table>


Then you must add a property to your module: <strong> popup_function </strong> with the name of your function. That is all that is needed.

To test this functionality you can try this: add this function to Accounts.js

```php
function myspecialcapture(recordid,value,target_fieldname,formname) {
  // first we launch the default functionality
  vtlib_setvalue_from_popup(recordid,value,target_fieldname,formname);
  alert('This is our special intercepted capture function');
  window.close();
}
```
Now add this property to Accounts.php:

```php 
var popup_function = 'myspecialcapture';
```
and go to Potentials and try to capture an Account.

### Popup capture hook. Receiving Module

This hook happens in the GUI on the browser in javascript when the user selects a record inside the popup screen. It launches your javascript code AFTER having done the work of selecting the record and will permit you to add some additional functionality to the selection process.

The typical use case is to fill in some additional fields besides the ones that the default behavior does. Since the popup screen is closed and we will usually fill in the additional fields via an AJAX call, the function is executed in the browser window, not the popup screen.

To hook into this functionality you must create a function in the receiving module's javascript file with the name:

```php 
{ModuleName}setValueFromCapture
```
this function will receive the parameters:

<table class="table table-striped">
<tbody>
<tr>
<td><strong>recordid</strong></td>
<td>the crmid of the record that has been selected in the popup</th>
</tr>
<tr>
<td><strong>value</strong></td>
<td>the text representation of the record that has been selected in the popup</td>
</tr>
<tr>
<td><strong>target_fieldname</strong></td>
<td>the destination field name in the form in the browser</td>
</tr>
</tbody>
</table>

To test the functionality I created this function in Potentials.js

```php 
function PotentialssetValueFromCapture(recordid,value,target_fieldname) {
	console.log(recordid,value,target_fieldname);
	var url = "module=Accounts&action=AccountsAjax&file=Save&accountname=vtiger&dup_check=true&record=3";
	new Ajax.Request(
		'index.php',
		{
			queue: {
				position: 'end',
				scope: 'command'
			},
			method: 'post',
			postBody:url,
			onComplete: function(response) {
				var str = response.responseText;
				document.EditView.description.value = str;
			}
		}
		);

}
```
If you add this code and then go to select an account/contact you will see that the Description field will get filled in with the message. The ajax call launched the duplicate account functionality, so depending on your install it will be an OK or a NOK message. The important thing is to see the example, I could have filled in any field with any information.

