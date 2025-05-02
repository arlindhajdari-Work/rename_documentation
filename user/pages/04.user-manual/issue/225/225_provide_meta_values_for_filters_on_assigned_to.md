---
title: '225: Provide Meta Values for Filters on Assigned To'
metadata:
    description: '225: Provide Meta Values for Filters on Assigned To'
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
        - issue
---

## Detailed Explanation

### Meta variables for special fields

**Current User**

When searching on user fields like *Assigned To, Creator or Modified By* the system expects you to give the full user name to search on. In other words you have to use the first and last name of the user like this:

```
assigned_to = user.first_name + ' ' + user.last_name
```
A typical situation that arises often is the need to create a filter and show only the "current user"'s records. So you create a filter of activities to be done "today" and you don't want to have to create 50 "today" filters. one for each of your 50 users. Exactly the same way you don't have to create 365 filters for each day of the year for your "today" filter.

To accomplish this we can use a special meta-variable when defining our filters for the user fields. This field is called "**current_user**" as can be seen in the next image.

![](filter_current_user.png?width=100%)

### Blank Dates

You can search on blank dates using the dollar sign $

### Blank Fields

You can use the word null to search for empty values on related and text fields

![](blankrelationfieldonfilter.png?width=100%)