---
title: 'Replacing prototype/scriptaculous with jQuery in coreBOS'
metadata:
    description: 'Replacing prototype/scriptaculous with jQuery in coreBOS'
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
        - documentation
    tag:
        - upgrade
---

### [Reference: Migrating from PrototypeJS to jQuery](https://andykdocs.de/development/JavaScript/Migrating+from+PrototypeJS+to+jQuery/#3-Events)

===

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Event</strong></td>
<td><strong>Prototype</td>
<td><strong>jQuery</td>
<td><strong>Also recommended for coreBOS</td>
</tr>
<tr>
<td>Selecting DOM Elements</td>
<td>$('id')</td>
<td>jQuery("#id")</td>
<td>document.getElementById("id")</td>
</tr>
<tr>
<td></td>
<td>$$(selector)[x]</td>
<td>jQuery(selector).eq(x)</td>
<td></td>
</tr>
<tr>
<td>GET/SET content</td>
<td>$F('id')</td>
<td>jQuery("#id").val()</td>
<td></td>
</tr>
<tr>
<td></td>
<td>.innerHTML</td>
<td>.html()</td>
<td>document.getElementById(element).innerHTML</td>
</tr>
<tr>
<td></td>
<td>element.update('new content')</td>
<td>element.html('new content');
vtlib_executeJavascriptInElement(document.getElementById(element));</td>
<td>document.getElementById(element).innerHTML='new_content';
vtlib_executeJavascriptInElement(document.getElementById(element));</td>
</tr>
<tr>
<td></td>
<td>.value = x</td>
<td>.val(x)</td>
<td></td>
</tr>
<tr>
<td>Update style</td>
<td>.style.x = 'y'</td>
<td>.css({ x: 'y' })</td>
<td></td>
</tr>
<tr>
<td></td>
<td>.setStyle( style(s) )</td>
<td>.css( propertyName, value )</td>
<td></td>
</tr>
<tr>
<td></td>
<td>.hasClassName( className )</td>
<td>.hasClass( className )</td>
<td></td>
</tr>
<tr>
<td></td>
<td>.addClassName( className )</td>
<td>.addClass( className(s) )</td>
<td></td>
</tr>
<tr>
<td>Get/Set Attributes</td>
<td>.checked</td>
<td>.prop('checked')</td>
<td></td>
</tr>
<tr>
<td></td>
<td>disabled</td>
<td>.prop('disabled')</td>
<td></td>
</tr>
<tr>
<td></td>
<td>.some_attr</td>
<td>.attr('some_attr')</td>
<td></td>
</tr>
<tr>
<td></td>
<td>.getWidth()</td>
<td>.width()</td>
<td></td>
</tr>
<tr>
<td></td>
<td>.empty()</td>
<td>.is(':empty')</td>
<td></td>
</tr>
<tr>
<td>Effects</td>
<td>.fade({duration: x})</td>
<td>.fadeOut(x * 1000)</td>
<td></td>
</tr>
<tr>
<td></td>
<td>.appear({duration: x})</td>
<td>.appear({duration: x})</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Effect.Appear</td>
<td>.fadeOut(x * 1000)</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Effect.Appear</td>
<td>fadeIn()</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Effect.Fade</td>
<td>fadeOut()</td>
<td></td>
</tr>
<tr>
<td>Event Handlers</td>
<td>$(element_id).observe("click",
 function(event){ ... })</td>
<td>jQuery('#'+element_id).bind("click",
 function(jQueryEvent){ ... })</td>
<td></td>
</tr>
<tr>
<td></td>
<td>document.observe("dom:loaded",
 function() { ... });</td>
<td>$(document).ready()</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Event.observe(element, eventName, handler)</td>
<td>$('selector').bind(eventType, handler)</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Sortable.create("element" {
constraint:false,
tag:'div',
overlap:'Horizontal',
handle:'headerrow',
onUpdate:function(){
// do smth
}
})</td>
<td>jQuery("#element").sortabe({
constraint: false,
tag: 'div',
overlap: 'Horizontal',
handle: '.headerrow',
update: function () {
//do smth
}
})</td>
<td></td>
</tr>
<tr>
<td>AJAX</td>
<td>new Ajax.Request('index.php', {
queue : {position : 'end',
scope : 'command'},
method : 'post',
postBody : "urlstring",
onComplete : function(response) {
// do smth
}
});</td>
<td>jQuery.ajax({
method: 'POST',
url:'urlstring',
}).done(function (response) {
   //do smth
});</td>
<td></td>
</tr>

</tbody>
</table>

