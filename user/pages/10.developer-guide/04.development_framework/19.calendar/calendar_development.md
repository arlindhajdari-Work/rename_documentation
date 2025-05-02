---
title: 'Calendar Development'
metadata:
    description: 'Calendar Development'
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
    tag:
        - calendar
---

## Integrate Custom Modules

For a custom module to be correctly supported in the Calendar module it must register itself by creating a few records in two tables.

===

### Module Fields Definitions

This table indicates the base start and end date fields and a comma separated list of fields to show in the popup summary box.

The table is *its4you\_calendar\_modulefields* and you can see an example looking at the code we use to fill in this table for the default modules (build/changeSets/ModulesOnCalendar.php).

### Module Status Definitions

This table indicates the search conditions to be used when filtering records on the calendar.

You can give search conditions for three status:

- **Planned**
- **Held**
- **Not Held**

The table is *its4you\_calendar\_modulestatus* and you can see an example looking at the code we use to fill in this table for the default modules (build/changeSets/ModulesOnCalendar.php).

### Timezone tests

In order to verify timezone on the calendar with DST changes I did this test. With the computer unconnected to the internet and set to mid-October, I create 18 calendar events, 6 for each of 3 users. The 6 events are 3 before DST change and 3 after the change. The 3 users are on UTC-3, UTC+1 (DST) and UTC. The database is set to UTC which is how it should be always.

This looks like this:

<table class="table table-striped">
<td></td>
<td>testtz-3</td>
<td>testtz</td>
<td>testymd</td>
</tr>
<tr class="even">
<td></td>
<td>UTC-3</td>
<td>UTC+1</td>
<td>UTC</td>
</tr>
<tr class="odd">
<td>15/10/17 10:00</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>15/10/17 23:30</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>16/10/17 00:30</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>04/11/17 10:00</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>04/11/17 23:30</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>05/11/17 00:30</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

I visually verify that all users see the events where they should appear. I enter as an admin user and see all events of all 3 users correctly situated by the timezone of the admin user.

Now I reboot the computer and set the date to the second of November in the BIOS.

I access coreBOS and visually verify that all users see the events where they should appear. I enter as an admin user and see all events of all 3 users correctly situated by the timezone of the admin user.

I create a Report on the events and verify that all three users see the events correctly and that the admin user also sees them all correctly.

I verify that the detail view is also correct.

I create an event with repeat over the DST weekend and verify that all events are created correctly.

I also verify that all the date information saved in the database is correct.
