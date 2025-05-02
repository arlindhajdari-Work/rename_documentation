---
title: 'Help Desk:: Trouble Tickets'
metadata:
    description: 'Trouble Tickets'
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
        - module
    tag:
        -help desk
---

- [Is it possible to make coreBOS work using "block hours" or "term contracts"?](../../04.user-manual/helpdesk#is-it-possible-to-make-corebos-work-using-block-hours-or-term-contracts)

- [Is there a way that the block hours accepts decimal e.g like 1.7hours?](../../04.user-manual/helpdesk#is-there-a-way-that-the-block-hours-accepts-decimal-e-g-like-1-7hours)

<div class="notices blue">
<h2>Is it possible to make coreBOS work using "block hours" or "term contracts"?</h2>
<hr>
A <strong> block hours contract</strong> is if they were to purchase 10 hours of work up front. For every hour (e.g. hour of work on a trouble ticket) it would take off the appropriate number of hours of the block hours that were purchased.<br><br>

To accomplish this the recommended approach is to create a <strong> Service Contract </strong> with <strong>Tracking Units</strong> of type hours and with <strong>Total Units </strong> set to 10 hours. Then each time a new trouble ticket is created it must be related to the Service Contract (create through service contract related list). When you close the ticket, indicate the total number of hours used (or accumulate them with the Time Control module). The field <strong> Used Units </strong> will automatically get filled in when you close the ticket and that will update the rest of the fields on the service contract like: progress, Actual Duration (in Days), end date and even the status will be changed to closed. The only missing piece is to launch an event that you could capture in workflows to send an email or take some action (we are working on that), so you currently have to manually filter the contracts to see which ones have expired.<br><br>

<hr>

A <strong> term contract </strong> would be if the customer were on a 365 day contract and it would automatically deduct a day off of the contract until the 365 days had been completed.<br><br>

This is a flat rate contract and can easily be accomplished with recurring sales orders. You create a sales order when the client contracts your service, you establish a recurring period depending on the duration of the contract, when the time is up a new invoice will be created, which is all you need to control.<br><br>

You can see below an example setup for a <strong> one year contract billed monthly:</strong>
</div>


![](oneyearcontractbilledmonthly.jpg?width=100%)

<div class="notices blue">
<h2>Is there a way that the block hours accepts decimal e.g like 1.7hours?</h2>
<hr>
I just did a test and all I had to do to get it working with decimals was change the typeofdata of the ticket field. It is set to integer so it won't accept decimal values.<br><br>

This is the query I used:
<div class="notices blue">
UPDATE `vtiger_field`<br>
 SET `uitype` = '7',`typeofdata` = 'N~O'<br>
 WHERE `vtiger_field`.`fieldname` = 'hours' AND tabid=13;<br>
</div>
It would be better to change the type of the hours field in tickets from varchar to decimal but it works the same.

<div class="notices blue">
This has been incorporated as default behavior in coreBOS </div></div>

