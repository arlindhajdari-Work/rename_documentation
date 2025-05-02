---
title: 'Mautic and coreBOS'
metadata:
    description: 'bidirectional synchronization of contacts and companies.'
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
        - marketing
    tag:
        - mautic
---

The current state of the integration with Mautic is a bidirectional synchronization of contacts and companies.

All the work happens on the coreBOS side. Two workflows are in charge of sending the modifications to Mautic via its API and two notification webhooks are responsible for receiving information from Mautic and updating records inside coreBOS.

===

To get the synchronization working we must configure both applications.

## Configure Mautic

First, we must activate the API so coreBOS can send the information to Mautic.

![Mautic API Enable](mauticapienable.png?width=100%)

Then we configure two webhooks to send the Account/Company and Contact information from Mautic to coreBOS

![Mautic Contact webhook](mauticcontactwebhook.png?width=100%)

![Mautic Account webhook](mauticaccountwebhook.png?width=100%)

 !!! To get all that working in Mautic you must clear the cache. To the extreme where I had to go directly to the var/cache directory and delete all the files there.

Finally, we must create two custom fields on the Contacts and Company modules to hold the coreBOS CRMID.

- **company_corebos_id** in Companies
- **corebos_id** in Contacts

![Mautic Contact Custom Field](mauticcontactcustomfield.png?width=100%)

## Configure coreBOS

In coreBOS we go to the Utilities page and click on Mautic card. Activate the integration and fill in the URL of your Mautic install and the credentials of the user to use to synchronize the information.

![coreBOS Mautic Activation](corebosmauticactivation.png?width=100%)

Next, we must create three workflows for each module. One to control the creation, the other for the update, and the last one for the delete operation. A total of six workflows that look like this:

![coreBOS Contacts workflows](coreboscontactsworkflows.png?width=100%)

![coreBOS Contacts workflow create](coreboscontactsworkflowcreate.png?width=100%)

![coreBOS Contacts workflow update](coreboscontactsworkflowupdate.png?width=100%)

![coreBOS Contacts workflow delete](coreboscontactsworkflowdelete.png?width=100%)

 !!! It is very important to set the conditions of the workflows correctly or you will easily fall into an infinite loop where coreBOS sends information to Mautic and Mautic sends back the change.

Finally, we have to create some Field Mapping Business maps to define which fields we want to synchronize in both directions.

**MauticToContacts, MauticToAccounts, ContactsToMautic, AccountsToMautic**

This is what the Contacts maps looked like in my tests.

**MauticToContacts**

```xml
<map>
    <originmodule>
        <originname>MauticContact</originname>
    </originmodule>
    <targetmodule>
        <targetname>CoreBOS</targetname>
    </targetmodule>
    <fields>
        <field>
            <fieldname>mautic_id</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>id</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>firstname</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>firstname</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>lastname</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>lastname</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>email</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>email</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>mailingstreet</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>address1</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>mailingcity</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>city</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>mailingstate</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>state</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>mailingzip</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>zip</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>mailingcountry</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>country</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>mobile</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>mobile</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>homephone</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>phone</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>fax</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>fax</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>website</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>website</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>facebook</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>facebook</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>foursquare</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>foursquare</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>instagram</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>instagram</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>linkedin</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>linkedin</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>skype</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>skype</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>twitter</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>twitter</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>points</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>points</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>attribution</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>attribution</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>date_attribution</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>attribution_date</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>last_active</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>last_active</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
                <field>
            <fieldname>pref_locale</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>preferred_locale</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>pref_tz</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>timezone</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>leadsource</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>Promoter</OrgfieldName>
                    <OrgfieldID>CONST</OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>title</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>title</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>newsletter</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>newsletter</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
    </fields>
</map>
```

**ContactsToMautic**

```xml
<map>
    <originmodule>
        <originname>coreBOS</originname>
    </originmodule>
    <targetmodule>
        <targetname>MauticContact</targetname>
    </targetmodule>
    <fields>
        <field>
            <fieldname>corebos_id</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>id</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>firstname</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>firstname</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>lastname</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>lastname</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>email</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>email</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>address1</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>mailingstreet</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>city</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>mailingcity</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>state</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>mailingstate</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>zip</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>mailingzip</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>country</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>mailingcountry</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>mobile</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>mobile</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>phone</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>homephone</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>fax</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>fax</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>website</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>website</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>facebook</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>facebook</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>foursquare</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>foursquare</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>instagram</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>instagram</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>linkedin</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>linkedin</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>skype</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>skype</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>twitter</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>twitter</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>points</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>points</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>attribution</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>attribution</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>attribution_date</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>date_attribution</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>last_active</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>last_active</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
                <field>
            <fieldname>preferred_locale</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>pref_locale</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>timezone</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>pref_tz</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>title</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>title</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>newsletter</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>newsletter</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
    </fields>
</map>
```

**MauticToAccounts**

```xml
<map>
    <originmodule>
        <originname>MauticAccounts</originname>
    </originmodule>
    <targetmodule>
        <targetname>CoreBOS</targetname>
    </targetmodule>
    <fields>
       <field>
            <fieldname>accountname</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>companyname</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field> 
            <fieldname>email1</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>companyemail</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
         <field>
            <fieldname>website</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>companywebsite</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
    </fields>
</map>
```

**AccountsToMautic**

```xml
<map>
    <originmodule>
        <originname>coreBOS</originname>
    </originmodule>
    <targetmodule>
        <targetname>MauticAccount</targetname>
    </targetmodule>
    <fields>
        <field>
            <fieldname>corebos_id</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>account_no</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>companyname</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>accountname</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
       <field>
            <fieldname>companyemail</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>email1</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
     <field>
            <fieldname>mobile</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>mobile</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
        <field>
            <fieldname>companyphone</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>phone</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
       <field>
            <fieldname>companywebsite</fieldname>
            <Orgfields>
                <Orgfield>
                    <OrgfieldName>website</OrgfieldName>
                    <OrgfieldID></OrgfieldID>
                </Orgfield>
            </Orgfields>
        </field>
     </fields>
</map>
```

## Notes

* Since the actions are separate, you can configure individual actions, like only creating or editing and not deleting.
* you have full control of the fields that are synced through the maps
* records are not really deleted: in coreBOS they will be marked as deleted setting a check box field in the record and in Mautic the corebos_id and company_corebos_id fields will be set to blank to stop the synchronization between the two applications for this record.

## Mautic Form Integration

Besides the bidirectional Contact/Account integration we also support forms. This part of the integration permits Evolutivo to receive the fields of a form created in Mautic and create a Contact and, optionally, a Potential directly in Evolutivo. This is exactly what the [web forms](https://blog.evolutivo.it/blog/mail2entity) and [web service webforms](https://corebos.com/docs_grav/extensions-integrations/coreboswswebform) extension do but, using Mautic you get the extra benefit of all the automation magic Mautic brings to the table.

To get this working, in Mautic we must configure another webhook to send the form data to Evolutivo:

![mautic form webhook](mauticformwebhook.png?width=100%)

Remember to add ALL the mandatory fields in the Contact module to the forms you create in Mautic.

![mautic form fields](mauticformfields.png?width=100%)

On the Evolutivo side, you need to configure two things. One is to fill in the webhook secret in the Mautic integration configuration field and the other is to set the global variable `Mautic_CreatePotential_OnFormSubmission` to 1 if you want to have the form create also a potential record for you.

Note that if the contact filling the form already has a record in Mautic/Evolutivo, the record will be updated and a new potential record will be added.

## Going Forward

Some of the future goals are:

* Delegate mass emails from coreBOS to Mautic
* Send workflow emails using Mautic templates
* Send coreBOS events to Mautic. For example, when an invoice is paid send the event to Mautic so it can trigger campaigns and other actions.
* Enhance Mautic to make decisions using coreBOS information. For example, answering questions like, "Does this contact have unpaid invoices?"
* Enhance Mautic to launch coreBOS workflows
* Mass capture of events from everywhere
