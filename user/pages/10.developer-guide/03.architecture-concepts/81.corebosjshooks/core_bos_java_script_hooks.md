---
title: 'coreBOS JavaScript Hooks'
metadata:
    description: 'You can override any javascript function with the corebosjshook class.'
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
        - hooks,
        - javascript
---

You can override any javascript function with the **corebosjshook** class.

This class is an instantiation of the [meld class from cujoJS](https://github.com/cujojs/meld) and you can use any of the many options this library has to insert your functionality where you need to.

===

I would recommend reading the [meld reference guide,](https://github.com/cujojs/meld/blob/master/docs/reference.md) the [meld API](https://github.com/cujojs/meld/blob/master/docs/api.md) and have a look at the different examples they have in [their Bundled Aspects](https://github.com/cujojs/meld/blob/master/docs/aspects.md) to get an idea of what can be done. 

Let's see an example of how to use this class in coreBOS.

I am going to pick the **massDelete** JavaScript function which is executed when you click on the "Delete" button on any list view and add a simple "Hello world" message.

![](massdelete.png?width=100%)

First we need a place where we can load our own JavaScript code, this is done using the coreBOS PHP action links as explained in the [How to add action links to a module](../../04.development_framework/11.develtutorials/18.add_actions) development tutorial and looks like this:

```php 
include_once('vtlib/Vtiger/Module.php');
$module = Vtiger_Module::getInstance('Accounts');
$module->addLink('FOOTERSCRIPT', 'corebosjshookexample', 'corebosjshookexample.js', '', 1, null, TRUE);
```

<div class="notices blue">
We put the code in the footer to make sure it loads after all the other functions we need to plug into.
</div>

After executing that code any JavaScript we put inside the file *corebosjshookexample.js* will be loaded and executed in the browser, so our first version will simply output the message always so we make sure it is loaded correctly.

```php
alert('Hello world');
```

Our next version will add the message before the mass delete function:

```php 
function massdeleteBeforeHelloWorld(module) {  // use the same signature as the function we override
  alert('BEFORE: Hello world from ' + module);
}
var beforemassdelete = corebosjshook.before('massDelete',massdeleteBeforeHelloWorld);
```
Now after

```php
function massdeleteBeforeHelloWorld(module) {  // use the same signature as the function we override
  alert('BEFORE: Hello world from ' + module);
}
function massdeleteAfterHelloWorld(result) {  // receives result of the massdelete function
  alert('AFTER: Hello world from AFTER massDelete');
}
var beforemassdelete = corebosjshook.before(window,'massDelete',massdeleteBeforeHelloWorld);
var aftermassdelete = corebosjshook.after(window,'massDelete',massdeleteAfterHelloWorld);
```
Finally, we completely override the whole function and call it from our own function

```php 
function massdeleteBeforeHelloWorld(module) {  // use the same signature as the function we override
  alert('BEFORE: Hello world from ' + module);
}
function massdeleteAfterHelloWorld(result) {  // receives result of the massdelete function
  alert('AFTER: Hello world from AFTER massDelete');
}
function massdeleteAroundHelloWorld(jpoint) {
  console.log(jpoint);
  alert('AROUND: Hello world');
  jpoint.proceed(jpoint.args[0]);
}
var beforemassdelete = corebosjshook.before(window,'massDelete',massdeleteBeforeHelloWorld);
var aftermassdelete = corebosjshook.after(window,'massDelete',massdeleteAfterHelloWorld);
var onmassdelete = corebosjshook.around(window,'massDelete',massdeleteAroundHelloWorld);
```
![](massdeletebefore.png?width=100%)

As you can see it is very simple to plug in functionality into any existing function or class method and we barely skimmed the possibilities in this article.

You can [find the code on this gist.](https://gist.github.com/joebordes/bb2e74f5dcedfa247451e378730438bc) 












