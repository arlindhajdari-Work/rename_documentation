---
title: 'Web Service Query Language'
metadata:
    description: 'Basic Query Language'
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
        - query
---

Query
-----

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Retrieve a set of records with an SQL like language that understands the entities in the system and their relations</td>
</tr>
<tr>
<td><strong>Profile:</td>
<td>query(<a href="query:String">query:String</a>):Object</td>
</tr>
<tr>
<td><strong>Send Type:</td>
<td>GET</td>
</tr>
<tr>
<td><strong>Parameters:</td>
<td>query: query language command terminated in semicolon</td>
</tr>
<tr>
<td><strong>Returns:</td>
<td>array of rows with the results found. each row will contain the same amount of columns corresponding to the query command executed</td>
</tr>
<tr>
<td><strong>URL Format:</td>
<td><code>http://corebos_url/webservice.php?operation=query&amp;query=[query command]</code></td>
</tr>
</tbody>
</table>

Basic Query Language
--------------------

Since coreBOS is a complete business application it needed a more powerful service to retrieve information than the standard REST protocol could offer, something closer to a GraphQL interface (we didn't have GraphQL back then). To cover this need, a hybrid SQL language was created VQL (Vtigercrm Query Language). This language is a reduced subset of the standard SQL language with extensions to "understand" the business entities contained in each coreBOS. The limitations are:
- subqueries are not supported
- no mathematical aggregation functions are supported except count(\*)
- we can only execute queries against entities, not direct database tables and once we consult an entity we have access to all its fields no matter how many tables it is separated into in the database application. There are some special entities due to their non-standard internal structure:
  - **Currency**: we can execute queries against defined currencies in the application
  - **Groups**: we can get a list of defined groups
  - **DocumentFolders**: we can get a list of document folders created
  - **LoginHistory**: historic access data
  - **AuditTrail**: operational data for all users
  - **Workflow**: list the workflows in the application
  - **ModTracker**: field-level changes on records
- the result set is restricted to 100 records by default. You can overcome this limit by specifically setting a limit clause and by paging the result set (recommended).

Even with these limitations, it is an incredible and powerful language.

The accepted format definition is:

```sql
select [distinct] * | <column_list> | <count(*)>
from <object>
[where <conditionals>] 
[order by <column_list>] [limit [<m>, ]<n>];
```

- column\_list: comma-separated list of field names
- object: module name
- conditionals: condition operations, in clauses, or like clauses separated by 'and' or 'or' operands these are processed from left to right
  - conditional operators: &lt;, &gt;, &lt;=, &gt;=, =, !=
  - in clauses: &lt;column name&gt; in (&lt;value list&gt;)
    - value list: a comma-separated list of values
  - like clauses: &lt;column name&gt; like '&lt;value pattern&gt;'
- the column list in the order by clause can have at most two column names.
- m, n: integer values to specify the offset and limit respectively. If only one value is given it is applied as limit

![](coreboswebservicequery.png?width=100%)

Try these VQL commands.

```SQL
select * from contacts
select firstname,contact_no,phone from contacts
select firstname,contact_no,phone from contacts order by firstname
select count(*) from contacts
/* Only four records starting from the first */
select firstname,contact_no,phone from contacts order by firstname limit 4
/* Only four records starting from the third */
select firstname,contact_no,phone from contacts order by firstname limit 3, 4
select * from groups
select * from workflow
select * from invoice where hdnGrandTotal > 5000
select * from invoice where hdnGrandTotal > 5000 and invoicestatus = 'Created'
select * from invoice where hdnGrandTotal > 5000 and invoicestatus like '%Created%'
```

There are **four different syntaxes** supported.

One is **the original query language** inherited from vtiger CRM. This is rather limited as it doesn't support related entities nor parenthesis in the conditions.

So we made a first enhancement based on **the [getRelatedRecords](../06.getrelatedcontrols) work**. This second syntax was created before we started the coreBOS project and was added as a base feature when it was born. You can read about this second syntax below and see it in use in our [Customer Portal Extension]( /en/extensions/coreboscp).

Finally, we enhanced the syntax a third time based on the work done in **the QueryGenerator class** which gives us a rich and flexible syntax with support for related modules and advanced conditions.

The problem is that in order to maintain backward compatibility we have kept all the syntaxes together and detect dynamically which one to use for each query. This is a bit misleading sometimes.

When a query is sent to the webservice query API it looks for the string "related.", if this string is found we apply the [Related Entity Query Syntax](../09.querylanguage/item.md#related-entity-query-syntax), if the string is not found we look for "not in", "not null", "." or "(". None of these strings are supported by the query syntax inherited from vtiger CRM so we apply the Extended QueryGenerator syntax. Finally, we apply the original VQL syntax.

<div class="notices red">
So, be careful when sending a query as it can easily be sent to the syntax parser you don't expect.
</div>

Let's go over that again.

- All queries use the list type module name in the FROM and WHERE sections
- [Related Entity Query Syntax](../09.querylanguage/item.md#related-entity-query-syntax) is based on the getRelatedRecords web service endpoint, so anything you can do with the query language can be done with this endpoint. The reverse is not true as the getRelatedRecords method has some functionality that cannot be accessed through the query language. This query language functionality is deprecated and not recommended, it works, and will continue to do so, but the QueryGenerator syntax is more powerful and the recommended way to get information from the query language.
- Given a web service query, the detection of what parser to use follows these steps:

#### 1.- Related modules

When a query is sent to the web service query API it looks for the string "related."

If this string is found we apply the Related Entity Query Syntax.

```sql
select * from projecttask where related.project=30x144
select * from projecttask where related.project=30x144 and projecttaskname='dsf'
select * from documents where related.accounts=3x12
select * from documents where filelocationtype='E' and related.contacts=4x22
select * from Documents where (related.Contacts='4x22') AND (filelocationtype LIKE '%I%') LIMIT 5;
select * from modcomments where related.helpdesk=9x114
select * from modcomments where related.helpdesk=9x114 and commentcontent like 'hdcc%'
select * from products where related.products=6x58 // only product children are accessible with this syntax
select * from products where related.contacts=4x22 // only directly related products
select * from products where related.contacts=4x22 and productcategory='Software' // only directly related products
select * from Products where related.Contacts='4x22' LIMIT 5;
select * from Products where related.Contacts='4x22' order by productname LIMIT 5;
```

#### 2.- Extended syntax - not related

If the string 'related' is not found we look for "not in", "not null", "." or "(".

None of these strings are supported by the query syntax inherited from vtiger CRM so we apply the Extended QueryGenerator syntax.

```sql
SELECT projectname,modifiedtime
FROM project
where projectname like '%cap%' and (modifiedtime>'2016-06-30 19:11:59' or modifiedtime<'2016-07-30 19:11:59')

SELECT *
FROM project
where projectname like '%cap%' and (modifiedtime>'2016-06-30 19:11:59' or modifiedtime<'2016-07-30 19:11:59')
```

#### 3.- Use legacy VQL

**Query to more than one module (joins)**

There are no "joins" in WebService Query Language, but coreBOS will do them for you. Remember that coreBOS WebService Query Language talks about entities, not tables.

We do *select...from accounts* not *select...from vtiger\_accounts*

In this same line, you have to specify fields prefixed by their module name and WSQL will do whatever it has to do to get the field from the directly related module. For example

`select firstname, Accounts.accountname from Contacts;`

Note, that fields on the module **DO NOT** have a prefix. The result of this query is VERY different:

`select Contacts.firstname, Accounts.accountname from Contacts;`

In this second query, we are accessing the first name of the Contact RELATED to the contacts. The Contact module has a related field to itself (Reports To), the column in the query above is retrieving the name from the RELATED contact through the Reports To field, not the name on the contact record itself.

So, if you want fields from a related module, just ask for them

#### Examples

```sql
SELECT * FROM Products where productname='sample' LIMIT 10;

select projectname,modifiedtime
from project
where projectname like '%o%' and modifiedtime>'2016-06-30 19:11:59'
```

which will be sent to the original query parser, but we can also send it like this

```sql
select projectname,modifiedtime
from project
where (projectname like '%o%' and modifiedtime>'2016-06-30 19:11:59')
```

which would be parsed by the QueryGenerator class. In this example, both should return the same set of values, but in this example, things are very different:

```sql
select projectname,modifiedtime
from project
where projectname like '%cap%' and modifiedtime>'2016-06-30 19:11:59' or modifiedtime<'2016-07-30 19:11:59'

select projectname,modifiedtime
from project
where projectname like '%cap%' and (modifiedtime>'2016-06-30 19:11:59' or modifiedtime<'2016-07-30 19:11:59')
```

returning a completely different set as the original query parser evaluates the conditions in order of appearance with no parenthesis.

Besides the enhanced syntax, there are **two very important things to note** about this dynamic switch.

**One** is that the original query parser and QueryGenerator parser use different ways of identifying a related record. The original parser uses the web service ID while the QueryGenerator uses the record's entity field name. In other words, when adding conditions on related fields (uitype10), the original parser expects the CRMID of the related record while the QueryGenerator parser expects the value of the entity link field.

For example, this query:

```sql
select projecttaskname,projectid,modifiedtime
from ProjectTask
where projectid='33x6772' and  modifiedtime>'2015-08-12 10:10:48' and modifiedtime<'2015-09-12 10:10:48'
```

looks like this:

![](wsvqlrelfieldreference01.png?width=100%)

but if we add parenthesis and launch the query we get no results returned.


```sql
select projecttaskname,projectid,modifiedtime
from ProjectTask
where (projectid='33x6772' and  modifiedtime>'2015-08-12 10:10:48' and modifiedtime<'2015-09-12 10:10:48')
```

with the parenthesis, we are using the QueryGenerator parser and must set the projectid field to the entity link field which is project name. The correct query looks like this:

```sql
select projecttaskname,projectid,modifiedtime
from ProjectTask
where (projectid='Owen' and  modifiedtime>'2015-08-12 10:10:48' and modifiedtime<'2015-09-12 10:10:48')
```

![](wsvqlrelfieldreference02.png?width=100%)

Optionally, we can search directly on the project ID with the extended QueryGenerator syntax:

```sql
select projecttaskname,projectid,modifiedtime
from ProjectTask
where (Project.id='33x6772' and  modifiedtime>'2015-08-12 10:10:48' and modifiedtime<'2015-09-12 10:10:48')
```

The **second** is that the original query parser will automatically add the "limit 100" to the query while the QueryGenerator will not do this.

You can find a whole set of examples in the [coreBOS Web Service Developer Tool](../02.coreboswsbrowser) and the
[webservice query unit tests suite](https://github.com/tsolucio/coreBOSTests/blob/master/include/Webservices/VtigerModuleOperation_QueryTest.php).

Query return limit
------------------

The select statement only returns 100 records. This is due to timeout and resource restrictions. If you want to obtain more records you must use the *limit* modifier. Any select statement with a limit modifier will try to return all the records indicated in the limit. So, if we have a contacts table with 150 records, this query:

`select * from contacts;`

will return 100 records, while this query:

`select * from contacts limit 200;`

will return the 150 records.

`select firstname,contact_no,phone from contacts order by firstname limit 4;`

Only four records starting from the first

`select firstname,contact_no,phone from contacts order by firstname limit 3, 4`

Only four records starting from the third

<div class="notices blue">If you are receiving timeouts you can increment the default timeout by modifying the code:<br>
<a href="https://github.com/tsolucio/coreBOSwsLibrary/blob/master/php/Net/HTTP_Client.php#L29">1-PHP</a> <br>
<a href="https://github.com/tsolucio/coreBOSwsLibrary/blob/master/php/Net/curl_http_client.php#L162">2-cURL</a> <br>
<a href="https://github.com/tsolucio/coreBOSwsLibrary/blob/master/php/Net/curl_http_client.php#L206">3-cURL</a> <br>
</div>

Related Entity Query Syntax
---------------------------

[plugin:youtube](https://www.youtube.com/watch?v=5B0A6IPMnJM)

Constructing on top of the [getRelatedRecords](../06.getrelatedcontrols) function we have extended the REST query syntax to benefit from that functionality, making it easy to query related entities and filter them also.

The new syntax enhances the *where* conditional statement to support module names preceded with the "*related*" string and followed by the id of the entity:

`where related.modulename=id`

Examples:

```sql
select * from projecttask where related.project=30x144
select * from projecttask where related.project=30x144 and projecttaskname='dsf'
select * from documents where related.accounts=3x12
select * from documents where filelocationtype='E' and related.contacts=4x22
Select * from Documents where (related.Contacts='4x22') AND (filelocationtype LIKE '%I%') LIMIT 5;
select * from modcomments where related.helpdesk=9x114
select * from modcomments where related.helpdesk=9x114 and commentcontent like 'hdcc%'
select * from products where related.products=6x58 // only product children are accessible with this syntax
select * from products where related.contacts=4x22  // only directly related products
select * from products where related.contacts=4x22 and productcategory='Software'  // only directly related products
Select * from Products where related.Contacts='4x22' LIMIT 5;
Select * from Products where related.Contacts='4x22' order by productname LIMIT 5;
```

- queryparameters support *limit* and *offset* for those sets of related records where the total count is very high or simply high enough to want to be able to page through.
- queryparameters support column definitions, reducing the size of information being returned
- **multiple entities, IDs or related modules** are **NOT** supported with this API. We have created the extended query language functionality, based on Query Generator for this.

There are a few restrictions we couldn't overcome:

- only one related entity may be used, as the getRelatedRecords function works with only one entity ID, we inherit this restriction. If more than one is put in the query, only the first is used and the rest are ignored and eliminated.
- the product relation is limited to directly related records, which means that on a contact we will only have access to the ones on his +info tab, or for a product we can only see it's bundle child products.
- advanced filtering (limited by current query syntax)

<div class="notices blue">
The Webservice extended query language functionality, based on Query GeneratorQuery overcomes some of these limitations.
</div>

Searching for empty relations
-----------------------------

When you have a web service query, and you want to select records from a module where a certain related (UI10) field is empty use:

`select * from PurchaseOrder where po_related_soid = 15x0`

Where 15 is the web service ID for the module of the UI10 field (in this case SalesOrder). Then use the 'x', and add a 0.

'po\_related\_soid' is a placeholder for the fieldname you want to check on, replace that with your own. Of course, also replace the module name with your own.

[Thanks Luke!](https://discussions.corebos.org/showthread.php?tid=912)

Errors that can be returned
---------------------------

Besides errors that may be returned by the underlying code this function uses, it can return directly these errors:

- **INVALID\_MODULE**: Given module (module) cannot be found, which one will be specified in the message.
- **ACCESSDENIED**: Permission to perform the operation on module (module) is denied. The current user cannot work with one of the modules
- **INVALIDID**: Id specified is incorrect. The given ID does not correspond to an entity in the application.
- **ACCESSDENIED**: Permission to read given object is denied. The current user does not have read access to the records.
- **RECORDNOTFOUND**: The record you are trying to access is not found. The given ID is pointing to a deleted record or is incorrect.

Connecting to the web service API with Postman
----------------------------------------------

Using [Postman](https://www.postman.com/) to access the coreBOS Web service API is rather easy. The main trick to keep in mind is that GET requests parameters go in the PARAMS tab and POST requests parameters go in the BODY tab.

The [Login is a two-step process](../07.login) so we have to create two requests and manually calculate the access token MD5.

Here you can see the Challenge setup:

![](postmanchallenge.png?width=100%)

Here you can see the Challenge setup:

![](postmanlogin.png?width=100%)

Here you can see the Challenge setup:

![](postmanquery.png?width=100%)

And here you can see a quick demo of how to do it:

[plugin:youtube](https://www.youtube.com/watch?v=z4UZw0eQ7Kw)

<br>
------------------------------------------------------------------------

[Next](../08.methodreference)| Chapter 5:Method Reference.

------------------------------------------------------------------------