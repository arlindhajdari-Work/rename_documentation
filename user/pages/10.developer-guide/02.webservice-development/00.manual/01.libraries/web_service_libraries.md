---
title: 'Web service libraries'
metadata:
    description: 'Abstraction library that hides the details of connection and low-level conversation going on and permits us to create applications faster.'
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
        - webservice
    tag:
        - library
---

In order to make programming with the web service API easier, we have created an abstraction library that hides the details of connection and low-level conversation going on and permits us to create applications faster.

===

For example, instead of going through the two-step login process, we can use the library and simply call **doLogin**, that method will execute the tow-step process and return the result.

In a similar manner, we can execute **doUpdate** and not have to worry if it is a GET or a POST nor if we have to add the session id to the call.

We have libraries for many languages and they all follow a similar structure which is the method prefixed with "do":

- doLogin
- doListTypes
- doDescribe
- doCreate
- doRetrieve
- doQuery
- doInvoke

There are many of these functions and depending on the maintenance team of each library there will be more or less.

One very important function is **doInvoke** which permits us to execute any web service method.

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>doInvoke</th>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Execute any web service method.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>doInvoke(method:string, parameters:array, type:string):array</td>
</tr>
<tr>
<td><strong>Send Type:</strong></td>
<td>GET</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>=&gt; method: name of the method to execute<br />
=&gt; parameters: array with the parameter needed by the method<br />
=&gt; type: GET or POST</td>
</tr>
<tr>
<td>Response:</td>
<td>the response of the method called</td>
</tr>
</tbody>
</table>

[You can find the libraries here.](https://github.com/tsolucio/coreBOSwsLibrary)


