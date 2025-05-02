---
title: 'How to add a special block to a module'
metadata:
    description: 'How we could add a new block in the detail view of a module where we could add some special functionality that we may need'
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
        - module
        - block
---

The goal of this tutorial is to show how we could add a new block in the
detail view of a module where we could add some special functionality
that we may need.

This is basically a two-step process; first, we have to add the
information into the database so the application knows that it has to
load a new block and what code it has to launch to fill it in, then we
have to implement that class to generate the output.

For this tutorial, I am simply going to sum the number of Purchase
Orders related to a contact and show that in a block on the contacts
detail view.

To change the database we use vtlib and add a DetailViewWidget Link
using vtlib:

```php
$module->addLink(
  'DETAILVIEWWIDGET',
  'DetailViewPOINFOBlockWidget',
  "block://ContactPOInfoWidget:modules/Contacts/ContactPOInfoWidget.php"
);
```

As can be seen, we are adding a DETAILVIEWWIDGET with the label
DetailViewPOINFOBlockWidget and with the link

```php
block://ContactPOInfoWidget:modules/Contacts/ContactPOInfoWidget.php
```

this last part is the really important one. It is saying that to
generate the widget, the application must load a class named
*ContactPOInfoWidget* which can be found in the file
*modules/Contacts/ContactPOInfoWidget.php*. Obviously, we can call the
class as we like (as long as it doesn't conflict with existing classes)
and put the file wherever we want (as long as it is accessible inside
coreBOS).

This class must implement only one method: *getWidget()* which will
return the name of another class which will implement our functionality.

<div class="notices blue"> The full script can be accessed in
the download link at the end. </div>

Now we have to implement the logic. This happens in a class that we must
create and that can do anything we need it to. The class runs inside
coreBOS so it has access to all the functionality of the application and
we can use Smarty to generate output.

This class must implement one method called *process()* which will be
called to generate the output on the screen.

In the case of this tutorial, that method executes a query against the
database to obtain the purchase order information and then loads a
Smarty template to generate a similar output to the existing blocks.

Have a look at the code which can be downloaded below and here is a
screenshot of how it looks on screen:

![](contactpostatswidget.png?width=100%)

<div class="notices blue">We could also add an additional
HeaderScript link to load some external javascript library we may need
to implement our functionality or load the information we need via
ajax/javascript which is how ModComments works. You can see an example
by studying that code.</div>

### [Contact Purchase Order Statistics Widget](adddvw.zip)

## Developer Blocks


From the example above you see that it is rather complex to add a new
block with some custom code inside. So we have extended the
possibilities in two ways. [One is using templates](../17.add_editdetail_block) and the other is using what
we call developer blocks.

Developer blocks construct upon the idea above but make it easier to
create the content giving us more boilerplate code done for us.

The initial idea is the same as above, you need a class that you
reference in the DETAILVIEWWIDGET, this class returns another class that
must implement a *process()* method. What we do is that this second
class extends the [class DeveloperBlock](https://github.com/tsolucio/corebos/blob/master/modules/Vtiger/DeveloperWidget.php#L17)
which gives you a set of predefined functions to help you concentrate
only on the actual logic of your requirement.

Additionally, we have modified the DEAILVIEWWIDGET code to permit you to
send more parameters into your class which is done using the URL
parameter syntax.

<div class="notices blue">
<a href="http://blog.corebos.org/blog/developerblock">You can find a blog
post</a> with a step by step
example and <a href ="asktoproceeddevblock.zip" attributes-list download > download the related code clicking here. </a> </div>

The coreBOS Question analytical module has [an example of the usage of the Developer Block](https://github.com/tsolucio/corebos/blob/master/modules/cbQuestion/cbQuestionWidget.php)
which makes it easy to get the execution of the question into a block.
Try these steps to see the result:

### Create a Business Question

Like this:

![](bquestion01.png?width=100%)

<table class="table table-striped">
<td>Columns:</td>
<td><code>[{"fieldname":"countres","operation":"is","value":"count(ticket_title)","valuetype":"expression","joincondition":"and","groupid":"0"},{"fieldname":"ticketstatus","operation":"is","value":"ticketstatus","valuetype":"fieldname","joincondition":"and","groupid":"0"}]</code></td>
</tr>
<tr class="even">
<td>Condition:</td>
<td><code>[{"fieldname":"$(parent_id : (Accounts) account_no) ","operation":"is","value":"$account_no$","valuetype":"raw","joincondition":"and","groupid":"0"}]</code></td>
</tr>
<tr class="odd">
<td>Type properties:</td>
<td><code>{"key_label":"ticketstatus","key_value":"countres"}</code></td>
</tr>
</tbody>
</table>
<br>

### Create a Business Action

**This one will appear in the body of the detail view.**

<table class="table table-striped">
<td>Type:</td>
<td>DETAILVIEWWIDGET</td>
</tr>
<tr class="even">
<td>Action:</td>
<td><code>block://bqanswer:modules/cbQuestion/cbQuestionWidget.php:QID=43177&amp;RECORDID=$RECORD$</code></td>
</tr>
<tr class="odd">
<td>Module:</td>
<td>Accounts</td>
</tr>
</tbody>
</table>
<br>

### Create another Business Action

**This one will appear in the right panel.**

<table class="table table-striped">
<td>Type:</td>
<td>DETAILVIEWWIDGET</td>
</tr>
<tr class="even">
<td>Action:</td>
<td>module=cbQuestion&amp;action=cbQuestionAjax&amp;file=cbQuestionWidget&amp;QID=43177&amp;RECORDID=$RECORD$</td>
</tr>
<tr class="odd">
<td>Module:</td>
<td>Accounts</td>
</tr>
</tbody>
</table>

<div class="notices red">
NOTE that the QID value is
actually the CRMID of the Business Question you created in the first
step, so you MUST change the <strong>43177</strong> above to the one assigned to your record </div>

### Appearence

Now go to any account with tickets and you should see something like
this:

![](bquestion02.png?width=100%)

### Another example: Show Message

The application has another native developer block that permits you to
show a message. Watch the next video to see how that works and learn a
little more about how this development resource works.

[plugin:youtube](https://youtu.be/aAs2FVJ0veE)

### Another example: Mass Upload Documents

The application has another native developer block that permits you to
mass upload documents. Watch the next video to see how that works and
[look at the commit to see the code](https://github.com/tsolucio/corebos/commit/889884362b82ff24a8c1b5499f22e7705e55d519).

[plugin:youtube](https://youtu.be/lW3RrQQQb-4)

### Show IFRAME

You can show an IFRAME in a block with the **showHTMLBlock**, something
like this:

    block://showHTMLBlock:modules/Utilities/showHTMLBlock.php:op=iframe&height=400px&ex=http%3A%2F%2Fcorebos.org%3Fifcrmid%3D%24RECORD%24%26ifmodule%3D%24MODULE%24

where you are passing to the Develop Block these parameters:

-   **op** =iframe (there are curently no other options)
-   **height** string of iframe height, optional
-   **ex** URL Encoded string with the URL to load in iframe. you can
    use the meta variables
    -   $RECORD$ which will be changed to CRMID of the current record if
        it exists
    -   $MODULE$ which will be changed to the MODULE NAME

### Developer Block Template

This is the starting point of any developer block (the boilerplate).
```php
<?php
/*************************************************************************************************
** PUT YOUR LICENSE HERE **
 *************************************************************************************************/
require_once 'modules/Vtiger/DeveloperWidget.php';
global $currentModule;
 
class YOURWIDGETNAMEHERE {
	// Get class name of the object that will implement the widget functionality
	public static function getWidget($name) {
		return (new YOURWIDGETNAMEHERE_DetailViewBlock());
	}
}
 
class YOURWIDGETNAMEHERE_DetailViewBlock extends DeveloperBlock {
	// Implement widget functionality
	private $widgetName = 'YOURWIDGETNAMEHERE';
 
	// This one is called to get the contents to show on screen
	public function process($context = false) {
		global $adb;
		$this->context = $context;
		$smarty = $this->getViewer();
		*************
		ALL YOU LOGIC GOES HERE
		*************
		return THE_HTML_YOU_WANT_TO_SHOW_INSIDE_THE_BLOCK;
	}
}
 
if (isset($_REQUEST['action']) && $_REQUEST['action']==$currentModule.'Ajax') {
	$smq = new YOURWIDGETNAMEHERE_DetailViewBlock();
	echo $smq->process($_REQUEST);
}
```

## How to add a special block to a module using templates

You can find a much easier way to add this type of block which also supports Edit View in [this tutorial](../17.add_editdetail_block).
