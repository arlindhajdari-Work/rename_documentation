---
title: 'Elastic Search/Kibana Integration'
metadata:
    description: 'Elastic Search/Kibana Integration'
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
        - elasticsearch 
---

coreBOS External Integration
------------

The **coreBOS-ElasticSearch** integration works on the idea that ES
(Elastic Search) is more than capable of handling ALL the information we
have in our CRM, so we directly send it all over for you to analyze.

The integration will continuously send to Elastic:

-   Full CRM records for all modules installed
-   All individual changes made to any field on any module
-   All audit information it can pick up: for example, logins and each
    action executed by each user

So, once setup, you will be able to plugin Kibana to your ES server and
start analyzing and visualizing all your information.

<div class="notices blue">

Note that the initial setup will give
you a lot of information, almost everything [see below the pending list of things to do](../02.elasticsearchexternal/item.md#things-we-still-need-to-do)  
that is happening in your CRM will be available to you, but there may
still be room for improvement. We can create specialized indexes in
order to facilitate the study of certain groups of actions by
denormalizing tables for you, we can add information and events that you
may be interested in, or we can simply help you analyze the enormous
amount of information we just put at your finger tips, so <strong> don't
hesitate to contact us for help </strong> </div>


The information will be saved in **three indexes**:

### companydata index

This index contains one type per each module in the CRM and inside all
the records of that module in their current state in the CRM. Even the
deleted ones, which will be marked with their "deleted" field set to 1.

As with the special "deleted" field, each record also contains a few
other common fields:

- **deleted**: 0 if the records is available in the CRM and 1 if not
- **record\_id**: the internal crmid of the record
- **record\_module**: the internal english name of the module: Potentials, HelpDesk, ...|
- **creatorid**: internal USERID of the user who created the record
- **apptags**: list of tags associated to the record

### companydatachange index

This index contains a list of each individual change occurred on any record in the crm. The structure is like this:

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Field</strong></td>
<td><strong>Type</strong></td>
<td><strong>Contains</strong></td>
</tr>

<tr>
<td>record_module</td>
<td>string</td>
<td>Name of the module affected by the change
</td>
</tr>

<tr>
<td>record_id</td>
<td>long</td>
<td>Internal CRMID of the record affected</td>
</tr>

<tr>
<td>userid</td>
<td>long</td>
<td>Internal USERID of the user who made the change</td>
</tr>

<tr>
<td>changedon</td>
<td>date</td>
<td>Date of the change</td>
</tr>

<tr>
<td>operation</td>
<td>string</td>
<td>Action executed: CREATED or UPDATED</td>
</tr>

<tr>
<td>field</td>
<td>string</td>
<td>Name of the field affected by the change
</td>
</tr>

<tr>
<td>prevalue</td>
<td>string</td>
<td>Value prior to the change</td>
</tr>

<tr>
<td>postvalue</td>
<td>string</td>
<td>Value after the change</td>
</tr>
</tbody>
</table>


### companydataaudit index

This index contains a list of each individual action occurred in the
application by the users in their daily use. The structure is like this:

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Field</strong></td>
<td><strong>Type</strong></td>
<td><strong>Contains</strong></td>
</tr>
<tr>
<td>operation</td>
<td>string</td>
<td>Action executed: login, login portal, logout, detailview, webservice, …</td>
</tr>
<tr>
<td>record_module</td>
<td>string</td>
<td>Name of the module affected by the action
</td>
</tr>
<tr>
<td>record_id</td>
<td>long</td>
<td>Internal CRMID of the record affected
</td>
</tr>
<tr>
<td>userid</td>
<td>long</td>
<td>Internal USERID of the user who made the change</td>
</tr>
<tr>
<td>doneon</td>
<td>date</td>
<td>Date of the action</td>
</tr>
<tr>
<td>donefrom</td>
<td>ip</td>
<td>IP from which the action was requested</td>
</tr>
<tr>
<td>moreinfo</td>
<td>string</td>
<td>A bucket of variable information related to the action</td>
</tr>
</tbody>
</table>


![](cbelasticsearch.png?width=90%)


Setup coreBOS
-------------

1.  Make sure you have an up to date coreBOS that supports all the
    events this extension looks for
2.  Go to Module Manager and install the extension
3.  Go to Settings for the extension and fill in the IP and access
    information for you ES server
4.  Verify that the cron for Elastic is present and **DEactivated**. We
    will activate it once we have imported all our current information
5.  Deactivate Audit History and Mod Tracker, simply to reduce overhead
    doing the same thing twice

<div class="notices blue">
In general the heavy weight process is
the audit trail, ModTracker is calculated for all records on all saves
whether you decide to save the information or not so if your users are
used to having it on screen and find it useful you can leave it. In my
opinion, ES gives you a much more powerful interface to analyze this
information, but you may not want to give access to the full change log
to everybody.</div> 

Setup Elastic Search
--------------------

This is, by far, the most important part of the setup. For Elastic to
properly index our information it is fundamental that we give it a
*mapping* of the information we have. We must define the type and the
way we want each of our fields to be analyzed and indexed in order to be
able to get the best out of our data.

We have a process that will generate a default mapping based on the
different types of fields supported by coreBOS. With this and the
fantastic job Elastic does by default, we are in a pretty good situation
to answer the questions we have about our business but there is still
royom for improvement. Data analysis is a complex subject and really
depends on the questions you need to answer and the things you want to
study so the default mapping generated may need some special tuning for
your exact data. Don't hesitate to contact us for help.

1.  You will need an Elastic Search server installed
2.  Go to the command line of your install and execute:
    ```php 
    php modules/cbElasticSearch/generateESMap.php {version}> cbesmap.json
    ```
    where {version} is a string that will be used to create the aliases
    for the indexes

3.  Open cbesmap.json in an editor. You will see the complete set of
    commands you need to send to your elastic server to get all the
    indexes defined. You can fine tune as necessary and the copy and
    paste those commands into your ES server.

<div class="notices blue">
if the data generated is to big to
paste in directly, you can send it in via POST on the command line with
curl, something like this: 
<div class="notices black">
curl -XPOST 'http://localhost:9200/cdatav001' -d @cbes1.json
</div>
 </div> 


<div class="notices red">
TODO: Add this to Settings: a
button to generate the mapping and send it directly to ES
 </div> 

Elastic is now ready to receive your information

Import Current Data into Elastic
--------------------------------

As soon as you installed the coreBOS-ES integration extension it started
picking up information about everything that is happening, but it won't
be able to send it all until ES has the current state of our data. For
this to happen we have to execute the import process which will pickup
all the information in our CRM and send it to ES.

The information sent is:

-   The current set of fields for all records in all modules. Even the
    deleted ones
-   It will look in the audit trail table and send all that information
    over
-   It will look in the login history information and send all that
    information
-   It will look in ModTracker for individual field changes and will
    send those over

<div class="notices red">
If you have your own change log
module/extension this is the time to create a process to send that information over too
 </div> 

Due to the amount of information that can be sent I would recommend
doing this from the command line to avoid unnecessary timeouts. In any
case the import process is prepared to stop and continue where it left
off so you can just continue to execute it until you have all your
information there.

```php 
php modules/cbElasticSearch/cbesimport.php
```

Getting Information from Elastic into the CRM
---------------------------------------------

Among other things that can be done I paste here ideas generated by team
at in Albania.

### Ajax JSON type related list

One way is to represent the changes of the normal index as lines of a
related list inside the record that we want to explore.

Evolutivo created a json "de-compiler" of another project called angular
block inside the application itself. It produces a representation inside
the detail view of the record. The Ajax technology used is an Angular.js
grid.

The best thing related to this approach of showing data, is the
possibility to add actions related to that specific log, for example it
would be possible to revert to a previous state.

![](esrelatedlist.png?width=90%)



### Elasticsearch extension in coreBOS

Another approach would be creating a search client directly as an
extension in the application. There can also be found some ready to
install clients using opensource software in order to embed them in the
application, without having to re-create the whole thing from scratch.

![](esembededsearch.png?width=90%)

One intelligent approach would be also store the URL of the entity in
the ES Document in order to directly access from the search

### Kibana integration

Another approach is the possibility to create an extension inside
coreBOS and then show in that the search done by some super-user in the
Kibana Application.

This would help in order to improve some restrictions on security.

Things we still need to do
--------------------------

-   Add in Settings: a button to generate the mapping and send it
    directly to ES
-   Import full documents into ES for full document searches
-   Control many to many relations. The current integration does not
    index this information. I need more experience and to see how the
    current relations are handled by real users asking questions
-   User events. Since Users is a special module most events on users
    module aren't registered. We need to change that and index those
    events like any other module.
-   Tags: add/delete events
-   Inventory modules: denormalize? is InventoryModules enough?
    NestedObjects?

------------------------------------------------------------------------

[Next](../../02.maps) | Chapter 2: coreBOSCRM GeoLocalization Map extension

------------------------------------------------------------------------