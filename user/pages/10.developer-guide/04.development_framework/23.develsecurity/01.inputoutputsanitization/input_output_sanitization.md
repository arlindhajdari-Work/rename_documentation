---
title: 'Input/Output Sanitization'
metadata:
    description: 'Learn the tools you need to sanitize data coming in and going out of Evolutivo.FW.'
    author: 'Joe Bordes'
content:
    items:
        - '@self.children'
    order:
        by: date
        dir: desc
taxonomy:
    category:
        - development
        - application
        - security
    tag:
        - howto
---

Learn the tools you need to sanitize data coming in and going out of Evolutivo.FW

===

Repeating here the importance of sanitizing the data received from our users and sent back to them is not necessary, articles about that are easily found all over the internet. so, in this article, I will concentrate on the tools and mechanisms **evolutivo.FW** gives us to sanitize our data.

## Input Data

To sanitize the information we get from our users we use the ubiquitous [HTML Purifier library](http://htmlpurifier.org/). We have two wrappers around that library.

`vtlib_purifier` function. This function takes a string and cleans it for us returning an HTML string with no javascript and many other dangerous HTML structures eliminated. This is the most common way we have to sanitize data in **evolutivo.FW** and it can be found in almost all scripts contained in the application.

A quick example looks like this

```php
echo vtlib_purify('hello <script>alert("there")</script>!!');
```

results in sending the string `hello !!` to the browser. You can find [more examples](https://code.spike.studio/EvolutivoCode/EvolutivoFWTests/src/branch/master/include/utils/VtlibUtilsTest.php#L28) to understand better the functionality in our unit tests.


The other wrapper is the [`request` class](https://code.spike.studio/EvolutivoCode/EvolutivoFW/src/branch/master/include/utils/Request.php). This class uses the `vtlib_purify` function to automatically clean all the variables sent to the class, so we can access them directly without having to apply the function, but it also helps with the usage of these values by giving a few helper methods. Let's see how that works.

```php
// instantiate the class
$req = new Vtiger_Request();
// send variables we want santized
$req->set('return_module', $_REQUEST['return_module']);
// set variable we want santized and set it also in the global context
$req->setGlobal('return_module', $some_variable);
// set a default value for the key
$req->setDefault('return_module', 'Accounts');
// read a variable using internal default value
$var = $req->get('return_module');
// read a variable setting local default value
$var = $req->get('return_module', 'Contacts');
// the get method sanitizes and also decodes JSON strings
// check if variable exists
if ($req->has('return_module')) {
    echo "return_module is saved";
}
// check if it the variable is empty
if ($req->isEmpty('return_module')) {
    echo "return_module is empty";
}
// delete a variable
$var = $req->delete('return_module');
// set an array of values
// the first array will be sanitized, the second will stay as given
$req = new Vtiger_Request($_REQUEST, $_REQUEST);
// we can read the RAW values with
$var = $req->getRaw('return_module');
// we can use `getAll` to get the complete array
$var = $req->getAll();
$var = $req->getAllRaw();
```

You can understand that it gives a higher-level wrapper than the simple `vtlib_purify` function with some extra checks, but it isn't bringing any additional security to the table. Probably not even saving code nor making it easier to maintain, which is why we don't use it much. That said, you will find scripts based on this class and it may be useful for you at some point, so it is important to know we have it and what it does.

There is another method in this class that is useful: `getReturnURL`. This method will return a URL string of all the variables that have the prefix `return`. This makes it easy to quickly construct a URL to be sent to the browser.

```PHP
$req = new Vtiger_Request();
$req->set('return_module', $_REQUEST['return_module']);
$req->setDefault('return_action', 'DetailView');
$req->set('return_action', $_REQUEST['return_action']);
$req->set('return_record', $return_id);
header('Location: index.php?' . $req->getReturnURL());
// equivalent to
header('Location: index.php?module='
    .vtlib_purify($_REQUEST['return_module']).'&action='
    .(empty($_REQUEST['return_action']) ? 'DetailView' : vtlib_purify($_REQUEST['return_action']))
    .'&record='.vtlib_purify($return_id)
);
```

The `getReturnURL` method saves us a lot of code but, sadly **it is the incorrect approach**. HTML Purifier is **not the correct solution for URL encoding** nor is the `http-build-query` PHP function this method works with. The correct solution is explained in the next section.

## Output Data

When sending data to the browser we must be careful, not only to send secure and relevant information but also to make sure we construct valid HTML and javascript.

To accomplish this, we use the [laminas escaper library](https://github.com/laminas/laminas-escaper). The [documentation for this library can be found here](https://docs.laminas.dev/laminas-escaper/intro/) and is very straightforward. Identical to our wrapper around HTML Purifier we also have a wrapper around laminas escaper: `vtlib_escape`

This function expects a string that we want to send to the browser and the destination of that string which can be:

- **html**: directly fed into the browser page
- **attr**: destined to be an attribute or property of an HTML element
- **js**: destined to be embedded as part of javascript code, usually strings
- **css**: destined to be embedded as inline CSS
- **url**: part or whole URL, the value of the href property of an HTML link element for example

This looks like this:

```php
echo '<a href="'.vtlib_escape($folder['repurl'], 'url').'" '
 .'onClick=\'MoveReport("'.vtlib_escape($folder['fname'], 'js').'");\'>'
 .vtlib_escape($folder['name'], 'html').'</a>';
```

## General Theory

In the backend, the general idea is that we will use `vtlib_purify` on any value we receive from the browser before using it or saving it, and then we will use `vtlib_escape` on the output we send to the browser, encoding it depending on its destination.

## Frontend world

In the frontend, we also have some things to consider. We sometimes have a problem with using the encoded values sent by evolutivo.FW. We can receive the values either in UTF8 or HTML encoded. We are slowly moving to UTF8 everywhere and this is becoming less and less important, but there are still some places where we may receive information in HTML. The general rule when we encounter this situation is to change the backend to send the information in UTF8, but if that cannot be done, for whatever reason, we can decode the string before using it with the `vtlib_unescape` javascript function. Note that we have no problem working with UTF8, you do not need to use the `vtlib_unescape` function with UTF8 encoded strings. There is an example of how this works below.

```php
<html>
<head>
  <script src="include/js/vtlib.js"></script>
</head>
<body>
<?php
include 'vtlib/Vtiger/Module.php';
$varutf8 = "hello <script>alert('you are hacked!')</script> there 'áçèñtös\".";
$varhtml = "hello &lt;script&gt;alert(&#39;you are hacked!&#39;)&lt;/script&gt; there &#39;áçèñtös&quot;.";
?>
<input type="checkbox" id="usehtml" checked> HTML&nbsp;&nbsp;
<button type="button" onclick="setvaluedirect()">Direct Value Set</button>
<button type="button" onclick="setvalueunescape()">Unescape Value Set</button>
<br>
<form>
  <input id="field1" style="width:600px;"><br>
  <textarea id="field2" style="width:600px;"></textarea><br>
  <div id="field3" style="width:600px;border:1px;border-style:dashed;height:20px;"></div><br>
  UTF8 Value from backend <b>hacked</b>: <?php echo $varutf8; ?><br>
  UTF8 Value from backend sanitized: <?php echo vtlib_escape($varutf8, 'html'); ?><br>
  HTML Value from backend: <?php echo $varhtml; ?><br>
  HTML Value from backend sanitized: <?php echo vtlib_escape($varhtml, 'html'); ?><br>
  Right click and select the "view page source" option to see the difference
</form>
<script>
var htmlvalue = "<?php echo vtlib_escape($varhtml, 'js'); ?>";
var utf8value = "<?php echo vtlib_escape($varutf8, 'js'); ?>";
function emptyFields() {
  document.getElementById('field1').value = '';
  document.getElementById('field2').value = '';
  document.getElementById('field3').innerHTML = '';
}
function setvaluedirect() {
  emptyFields();
  let v = utf8value;
  if (document.getElementById('usehtml').checked) {
    v = htmlvalue;
  }
  document.getElementById('field1').value = v;
  document.getElementById('field2').value = v;
  document.getElementById('field3').innerHTML = v;
}
function setvalueunescape() {
  emptyFields();
  let v = utf8value;
  if (document.getElementById('usehtml').checked) {
    v = htmlvalue;
  }
  document.getElementById('field1').value = vtlib_unescape(v);
  document.getElementById('field2').value = vtlib_unescape(v);
  document.getElementById('field3').innerHTML = vtlib_unescape(v);
}
</script>
</body>
</html>
```

![Escape Example code](escapescript.png?width=100%)

Additionally, and, in fact, every day more as we move our functionality to the browser, it is possible that we need to manipulate HTML (and javascript?) in the browser directly. To accomplish this task, we have included the [DOMPurify javascript library](https://github.com/cure53/DOMPurify). The usage is rather restricted because we normally will get the information in the browser already sanitized from the backend, but we may want to sanitize text being written by the user (an email template, for example), or received from a web service call either from the backend or another external service. We have a global `DOMPurify` object available in the browser for these tasks.

```js
$('#cbmodule').append(
  `<option value="${DOMPurify.sanitize(notify_module)}">${DOMPurify.sanitize(mod_information[notify_module].label)}</option>`
);
```

## Path Ahead

As an application that has been around a long time, we have some legacy code here and there 😉. As we revisit the code, and when time permits, we slowly are transforming all that legacy code to align with the security guidelines explained above. This is, like many other tasks an ungrateful one, another one of those tasks that, if done correctly, have no visual impact on the user experience and cater to the needs of a small group of people (those trying to hack the application instead of using it).

We have most, if not all the inputs, under control, the outputs require more work, especially the integration with the browser parts, so there is work to be done, although a real security evaluation needs to be conducted to understand the extent of the pending work.

