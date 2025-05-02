---
title: Asterisk
metadata:
    description: 'Asterisk'
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
        - integration
    tag:
        - asterisk
---

## Design

![](corebosasterisk.svg)

===

### How to simulate a call

Activate PBX for the user you want to test with. In this example I set extension 14 for admin user (userid=1):

```sql
UPDATE `vtiger_asteriskextensions` SET `asterisk_extension`='14', `use_asterisk` = '1'
  WHERE `vtiger_asteriskextensions`.`userid` = 1;
```

Since we are making the change directly in the database, the user file is not updated, so go to the users' preferences and click on the "Recalculate" action.

Once you do that, reload the coreBOS page and open the inspector network tab. You will see that asterisk.js has been loaded and that the polling has started.

Now we insert a call directly in the DB:

```sql
INSERT INTO `vtiger_asteriskincomingcalls`
  (`from_number`, `from_name`, `to_number`, `callertype`, `flag`, `timer`, `refuid`)
  VALUES
  ('03-3608-5660', 'joeb', '14', 'SIP', '0', UNIX_TIMESTAMP(), 'any_unique_id');
```

the important number here is the "14" which must match the extension we set in the update above.

Now you should see the asterisk popup notification in the application.

### Other Things

[Vtiger + popup + llamada entrante + cola](../02.llamadaentrantecola)

### FAQ

<div class="notices blue"><h2>Since the extension is polling, is there a way to reduce the number of events detected?</h2></div>

Configure your asterisk server with the next settings to filter events by putting them in manager.conf (in freepbx it would be manager\_custom.conf) (asterisk &gt;= 1.8):

```
    read = all
    write = all
    writetimeout = 2000
    eventfilter=!Event: DMTF
    eventfilter=!Event: RTCPSent
    eventfilter=!Event: RTCPReceived
    eventfilter=!Event: VarSet
    eventfilter=!Event: Cdr
    eventfilter=!Event: ExtensionStatus
    eventfilter=!Event: ChannelUpdate
    eventfilter=!Event: PeerStatus
    eventfilter=!Event: Registry
```

Since we applied this change the asteriskclient is much more stable.
