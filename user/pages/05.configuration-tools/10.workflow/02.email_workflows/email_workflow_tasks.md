---
title: 'Email Workflow Tasks'
metadata:
    description: 'Send Emails.'
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
        - adminmanual
        - workflows
    tag:
        - workflow
        - emails
---

## Meta Variables

### Comments


This metavariable was created to support the help desk process and permits you to add and format a list of the comments on the ticket to your email.

It also supports the FAQ module and all the other modules that have comments. So, although unlikely, you could send all the comments on an opportunity to the related account or contact, or, more interesting, send them to the user in charge of the opportunity when one is added.

===

<div class="notices blue">
Note that the generic ModComments module is supported separately in the workflow settings, so you can send emails with the comments from there directly and probably have more conditions.
</div>

The syntax of this meta variable is:

```xml
$(general : (__VtigerMeta__) [dateformat_]comments[_num[sort][_format[_field]]])
```
where:

<table class="table table-striped">
<tbody>
<tr>
<td><strong>dateformat</strong></td>
<td>Optional PHP standard date formatting syntax that will be applied to all dates. If not given the date format of the user executing the command will be used</td>
</tr>
<tr>
<td><strong>num</strong></td>
<td>Indicates the number of comments you want, 0 will retrieve all comments</td>
</tr>
<tr>
<td><strong>sort</strong></td>
<td>Indicates the number of comments you want, 0 will retrieve all comments</td>
</tr>
<tr>
<td><strong>format</strong></td>
<td>text, HTML or table</td>
</tr>
<tr>
<td><strong>field</strong></td>
<td>creator, comment, date, all: indicates the field to retrieve</td>
</tr>
</tbody>
</table>

### Examples

<table class="table table-striped">
<tbody>
<tr>
<td><strong>comments</strong></td>
<td>returns all comments sorted ascending in HTML format, see below for exact format</td>
</tr>
<tr>
<td><strong>comments_1d_text_comment</strong></td>
<td>return in text format the last comment added</td>
</tr>
<tr>
<td><strong>comments_1d_text</strong></td>
<td>return all three fields (creator, date and comment) in text format of the last comment added. Each field will be ended with a new line character</td>
</tr>
<tr>
<td><strong>comments_4d</strong></td>
<td>returns last 4 comments in HTML format</td>
</tr>
<tr>
<td><strong>comments_4a</strong></td>
<td>returns first 4 comments in HTML format</td>
</tr>
<tr>
<td><strong>comments_4</strong></td>
<td>returns first 4 comments in HTML format</td>
</tr>
<tr>
<td><strong>comments_0d</strong></td>
<td>returns all comments sorted descending in HTML format</td>
</tr>
<tr>
<td><strong>comments_0d_text</strong></td>
<td>returns all comments sorted descending in text format</td>
</tr>
<tr>
<td><strong>d.M.Y - H:i_comments</strong></td>
<td>returns all comments sorted ascending in HTML format, with specific date format</td>
</tr>
</tbody>
</table>

### Styles and Formats

In **text format mode** the value of the field will be returned with no additional characters unless you asked for all the fields, in that case, each field will be ended with a new line character.

The **creator field** will be returned as the first and last name of the user or contact.

The **date field** will be formatted to the settings of the user assigned to the ticket launching the workflow.

<div class="notices blue">
If you want to completely set the date format you can use the standard PHP date formatting right after the date field. This only works when retrieving the date field individually:
$(general : (__VtigerMeta__) comments_1d_text_dated.m.Y - H:i)
</div>

The **comment field** will be stripped of any inline style or scripts to avoid potential hacks or compromises of clients' computers.

In **HTML format mode** all fields will be returned in an unordered list element (UL). Each comment will be in its own DIV which will contain the unordered list and contain each field being returned in its own list item (LI).

The whole set of comments will be enclosed in a DIV element.

So the structure looks like this:

```html
<div class="comments">
  <div class="commentdetails">
    <ul class="commentfields">
      <li class="commentcreator">...</li>
      <li class="commentdate">...</li>
      <li class="commentcomment">...</li>
    </ul>
  </div>
  ...
</div>
```

Since each element has its own class you can add inline CSS to your email and format the comments as you like.

As an example, this CSS:

```css
<style type="text/css">
.comments {
  margin: 10px
}
 
.commentfields {
  color: brown;
  list-style-type: none;
}
 
.commentfields:hover {
  background-color: #F5FFCC;
}
 
.commentcreator {
  position: absolute;
  font: bold italic 16px/1.5 Helvetica, Verdana, sans-serif;
  word-wrap: normal;
  width: 160px;
}
 
.commentdate {
  font: bold italic 16px/1.5 Helvetica, Verdana, sans-serif;
  padding-left: 170px;
}
 
.commentcomment {
  font: 14px/1.5 Helvetica, sans-serif;
  padding-left: 170px;
  color: #555;
}
</style>
```

will produce the output you can see in the next image which is from my email reader (thunderbird) with the hover effect captured:

![](workflowemailcommentmetavariablehtmlformatexample.png?width=100%)


### Inventory Details

Very similar to the Comments we can do the same with the product lines in the inventory modules.

The syntax of this meta variable is:

```php
$(general : (__VtigerMeta__) inventorydetails[_format[_field]]])
```

where:


<table class="table table-striped">
<tbody>
<tr>
<td><strong>format</strong></td>
<td>text, HTML or table</td>
</tr>
<tr>
<td><strong>field</strong></td>
<td>quantity, listprice, extgross, linetotal, or * for all fields. pdoname is always present as the name of the product or           service</td>
</tr>
</tbody>
</table>

### Related Lists

Very similar to the Comments we can do the same with the related lists of the main module of the email.

The syntax of this meta variable is:

```php
$(general : (__VtigerMeta__) relatedlist_relatedmodulename[_format[_field]]])
```

where:

<table class="table table-striped">
<tbody>
<tr>
<td><strong>relatedmodulename</strong></td>
<td>related module name. if the given module is not related the list will be empty</td>
</tr>
<tr>
<td><strong>format</strong></td>
<td>text, HTML or table</td>
</tr>
<tr>
<td><strong>field</strong></td>
<td>list of fields to show
</td>
</tr>
</tbody>
</table>


<br>
------------------------------------------------------------------------

[Next](../../../07.knowledge-base/10.configuration-store/businessmap/contacts2accounts/id:37247bed69140cef25a6eeb241753653/store:configuration) | Chapter 2: Contacts2Accounts.

------------------------------------------------------------------------