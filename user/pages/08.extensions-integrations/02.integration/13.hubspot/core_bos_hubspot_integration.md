---
title: 'coreBOS-Hubspot Integration'
metadata:
    description: 'Hubspot is CRM-like online service to manage your leads and inbound marketing.'
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
        - hubspot
---

The CoreBOS HubSpot integration is a feature that allows seamless connectivity and data synchronization between the coreBOS CRM platform and HubSpot, a popular marketing automation and sales software. This integration enables businesses to streamline their marketing, sales, and customer relationship management efforts by synchronizing data and automating various processes.

===

With the CoreBOS HubSpot integration, users can:

1. Sync Contacts and Leads: The integration enables bidirectional synchronization of contact and lead information between CoreBOS and HubSpot. This ensures that customer data remains consistent and up to date in both systems.

2. Automate Lead Generation: HubSpot's powerful lead generation tools can be utilized within CoreBOS, allowing businesses to capture leads directly from their website forms or landing pages. These leads are then automatically synced into CoreBOS for further nurturing and sales follow-up.

3. Track Marketing Activities: CoreBOS integration with HubSpot enables tracking of marketing activities, such as email campaigns, website visits, and social media interactions. This data can be used to gain insights into customer behavior and tailor marketing strategies accordingly.

4. Automate Workflows and Lead Nurturing: The integration allows for the automation of workflows and lead nurturing processes. Actions triggered in CoreBOS, such as lead status changes or specific events, can initiate automated workflows in HubSpot. This ensures timely and personalized communication with leads throughout the sales cycle.

5. Reporting and Analytics: CoreBOS can leverage HubSpot's reporting and analytics capabilities to measure the effectiveness of marketing campaigns, track lead conversions, and assess overall sales performance. This data-driven approach helps businesses make informed decisions and optimize their marketing and sales strategies.

In summary, the CoreBOS HubSpot integration facilitates seamless data synchronization and automation between the CoreBOS CRM platform and HubSpot, empowering businesses with enhanced marketing, sales, and customer relationship management capabilities.

## Functionality

The functionality implemented with this integration is to keep totally in sync any marked records from the modules:

- Accounts
- Contacts
- Leads
- Potentials

In order to do this there are basically two actions:

1. Send CreateUpdateDelete (CUD) actions to hubspot
2. Get CUD actions from hubspot

The integration will detect CUD actions in the CRM and send them to Hubspot immediately (or almost).

As per Hubspot recommendations we must poll their system every 5-6 minutes in search of modifications. They do not have a generic way of getting informed of changes that happen in their system and even in the poll we get all records changed in the last 30 days. So, changes in Hubspot will take a little longer to detect, around 5 minutes or so.

To get this synchronization working we need a forever running script (daemon) setup in linux. We have chosen the open source project PHPDaemon to implement this process. PHPDaemon will fork tasks to take care of the polling and the syncing.

The idea of the script is that it reads from coreBOS Message Queue system every five seconds (configurable by a global variable). When we detect a CUD action in coreBOS we put a message on the queue for the Hubspot integration. Every five seconds the queue is checked and if a message is pending it is processed as an individual task.

There should always be a message on the queue to wake up the polling process. When time comes to deliver the message the polling process will be launched, any changes will be updated and a new message will be put on the queue for the next wake up.

So, in order for this to work you need to have the daemon running. That is done from inside the top of the coreBOS install with the command:

`include/cbmqtm/run.php -d`

You can run this command without the -d in order to get it on screen. Ctrl-C will kill the daemon as well as a `kill -9 pid`. The pid is saved in the include/cbmqtm directory as a blocking mechanism.

To access the Hubspot information we need to establish some values. First you will need a developers account. I created one here:

http://developers.hubspot.com/docs/overview

And then registered that user with a normal user account

Then I had to `Create App` and create an API key for this App. I called it coreBOS, but you can call it whatever you want. This is what my setup looks like:

![hubspot app configuration](hubspotappconfig.png?width=96%)

I suppose you will have to follow the inverse path. Access as your current user and create a developer account for that so you can associate your current information with the App and API key. Obviously you can create your own developer account for testing.

With this information you must navigate to:

`http://your_server/your_corebos/index.php?action=integration&module=Utilities&_op=getconfighubspot`

Which should show you a screen like this:

![corebos hubspot configuration](coreboshubspotconfig.png?width=96%)

On this page you can setup your API key and set the poll frequency. Note that Hubspot has usage limits so be careful. As you can see I have it set to 60 minutes polling for testing, they recommend a minimum of 5 minutes. I have a default value of 6 minutes.

When we read a deal from Hubspot, it is related to both a Contact and an Account. In coreBOS it can only be related to one of them so the last option on this page is asking with which you prefer.

Next we must setup the field mappings for each module and direction of the sync.

We have 4 modules supported and we can get information in both directions for each so we need 8 mappings:

- Contacts2HubSpot
- Accounts2HubSpot
- Leads2HubSpot
- Potentials2HubSpot
- HubSpot2Contacts
- HubSpot2Accounts
- HubSpot2Leads
- HubSpot2Potentials

This is what my test mappings looks like:

![corebos hubspot maps](coreboshubspotmaps.png?width=96%)

### Contacts2HubSpot

```xml
<map>
  <originmodule>
    <originname>Contacts</originname>
  </originmodule>
  <targetmodule>
    <targetname>HubSpot</targetname>
  </targetmodule>
  <fields>
    <field>
      <fieldname>firstname</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>firstname</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>lastname</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>lastname</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>email</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>email</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>phone</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>phone</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
  </fields>
</map>
```

### Accounts2HubSpot

```xml
<map>
  <originmodule>
    <originname>Accounts</originname>
  </originmodule>
  <targetmodule>
    <targetname>HubSpot</targetname>
  </targetmodule>
  <fields>
    <field>
      <fieldname>name</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>accountname</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>description</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>email1</OrgfieldName>
        </Orgfield>
        <Orgfield>
          <OrgfieldName>phone</OrgfieldName>
        </Orgfield>
        <delimiter> - </delimiter>
      </Orgfields>
    </field>
    <field>
      <fieldname>phone</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>phone</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
  </fields>
</map>
```

### HubSpot2Potentials

```xml
<map>
  <originmodule>
    <originname>HubSpot</originname>
  </originmodule>
  <targetmodule>
    <targetname>Potentials</targetname>
  </targetmodule>
  <fields>
    <field>
      <fieldname>potentialname</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>dealname</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>sales_stage</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>dealstage</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>amount</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>amount</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>closingdate</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>closedate</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
  </fields>
</map>
```

### HubSpot2Contacts

```xml
<map>
  <originmodule>
    <originname>HubSpot</originname>
  </originmodule>
  <targetmodule>
    <targetname>Contacts</targetname>
  </targetmodule>
  <fields>
    <field>
      <fieldname>firstname</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>firstname</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>lastname</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>lastname</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>email</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>email</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>phone</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>phone</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>assistantphone</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>testprop</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
  </fields>
</map>
```

### HubSpot2Accounts

```xml
<map>
  <originmodule>
    <originname>HubSpot</originname>
  </originmodule>
  <targetmodule>
    <targetname>Accounts</targetname>
  </targetmodule>
  <fields>
    <field>
      <fieldname>accountname</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>name</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>description</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>description</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>phone</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>phone</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>employees</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>acctestprop</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
  </fields>
</map>
```

The activation process will create a new block on each module with a set of fields to both manage the integration and give information to the users. This is what my Contacts HubSpot looks like:

![control fields](controlfields.png?width=96%)

As you can see there are 7 new fields:

- HubSpot ID, this is the internal ID on HubSpot and is used for syncing purposes. It is readonly
- HubSpot Record, this is a URL to take you directly to this record on HubSpot
- Last Sync is the last time this record was changed
- Sync with Hubspot: this field is REALLY important. If this field is not checked the records will NOT be synced with HubSpot. You can set default values for it as well as mass edit as needed. Note that I had it happen to me to see that a record I was creating was not being sent to HubSpot and it was because I forgot to check this field when creating.
- Create in HubSpot indicates if the record was created in HubSpot
- Deleted in HubSpot indicates that we have received a Delete event from HubSpot. We do not delete the record in the CRM, just mark this field as true and set the date on the next field
- Date the record was deleted in HubSpot

That should be all you need to start testing.

## Comments

- The message queue is in the database table: cb_messagequeue
- Some error messages are logged in the message queue, specifically when we cannot create or update a record coming from HubSpot. These message are currently not being purged nor processed.
- The table cb_mqsubscriptions holds processes listening on the queue, you should have three entries here, one for create and update, one for delete and one for polling.
- Deletes in the CRM ARE sent to HubSpot
- HubSpot settings information are saved in the table: cb_settings  We now have a generic key-value store in coreBOS accessible via the coreBOS_Settings class. You can save any values here. We created this in order to have a place to save information without having to create a lot of small tables
- In one of the tests I did the daemon died with an “Out of Memory” error. I suppose it is related to the users or the fork/task. We will have to keep an eye on this as PHP is really not suited for this type of process. Theoretically we could use a Celery based task manager and RabbitMQ (among others) to manage the queue. Our collaborators at AT Consulting are currently doing this. There are also some PHP alternatives so we will get to this as needed. 
- Since we have total control over the polling frequency via the message queue we could create some escalation or advanced logic like not polling during the weekends or increment the frequency during some hours of the day….
- The message queue and task manager were on our roadmap. It is a generic solution that can be used for many cases. You can use that freely for your own developments, so ask as you need.
- The same applies to the coreBOS Settings key-value store.
