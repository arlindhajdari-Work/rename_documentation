---
title: 'How to open a capture popup with a preselected set of records.'
metadata:
    description: 'How to open a capture popup with a preselected set of records'
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
        - popup
    tag:
        - howto
        - capture
---

When the user clicks on the select icon of a capture field (uitype 10) a popup screen appears with the list of records of the module being selected. In certain situations, it is necessary to pre-filter the results for the user

===

In fact, the application already does this in various parts, for example when selecting a contact after having selected an account on an invoice. Only the list of contacts related to the account will appear.

### Open Popup Hook Method

This tutorial will teach you how to implement such a feature for your uitype10/capture fields.

What we need to do to get this working is to inform the popup code to launch a search on the set of records to return. This functionality already exists in the popup code, so we don't need to add any code there, we *just* have to pass in the right parameters to let the popup code know that it has to set up a conditional query instead of a full query.

The three parameters the popup code expects to see in order to setup a conditional query are:

- **query** =true
- **search** =true
- **searchtype** =\[BasicSearch|advance\]

if **searchtype=BasicSearch** then we have to send in these additional variables:

- **search\_field** = name of field to search on, for example accountname
- **search\_text** = text to look for always as a non-sensitive "contains"

if **searchtype=advance** then we have to send in this additional variable:

- **advft\_criteria** =\[{json object that defines conditions}\] array of json objects which represent the conditions
- **advft\_criteria\_groups** =\[null,{"groupcondition":""}\] array or logical unions between the different groups. If you only have one group this variable is not needed.

where the json object has this format:

```json
{
    "groupid":"number that identifies the group of conditions",
    "columnname":"coreBOS advanced column identifier"
    "comparator":"comparison operator"
    "value":"text to look"
    "columncondition":"and|or" (logical operator to join with the next condition)
}
```

the coreBOS advanced column identifier has this format:

**table\_name:field\_name:column\_name:label:data\_type**

for example

vtiger\_account:accountname:accountname:Accounts\_Account\_Name:V

the comparison operator can be

- e: igual | equal | "="
- n: distinto | not equal | "&lt;&gt;"
- s: empieza con | begins with | "LIKE" ("$value%")
- ew: termina con | ends with | "LIKE" ("%$value")
- c: contiene | like | "LIKE" ("%$value%")
- k: no contiene | not like | "NOT LIKE" ("%$value")
- l: menor que | less than | "&lt;"
- b: menor que | less than | "&lt;"
- g: mayor que | greater than | "&gt;"
- a: mayor que | greater than | "&gt;"
- m: menor o igual | less or equal | "&lt;="
- h: mayor o igual | greater or equal | "&gt;="

<div class="notices blue">
Note that this JSON object is much more complex than is shown here supporting not only various fields but also different groupings of conditions. If you need a complex condition I would recommend creating a filter with the condition. On the filter, there is a nice editor that will permit you to add the fields, conditions, and different groupings. Then simply capture the save event to see how coreBOS creates the JSON object and use that. </div>

Now that we know what we have to do, [let's see some examples](../../../03.architecture-concepts/76.popup_open_hook).

### Native relmod_id Method

Before we had the search and open popup hook the application used a "parameter" based search method which is still in place (we just love backward compatibility). This system expects a pair of REQUEST variables to be passed in and will filter the results based on those using a specific query.

The supported set of modules is hardcoded and limited but in the end, the Popup code calls the generic getQueryByModuleField method where you can adapt your query based on the two variables for your modules also.

The two variables are

- **relmod_id** is the record id we must restrict the records to
- **parent_module** is the module of the relmod_id record

So you could open a popup passing in these variables and then detect them in your getQueryByModuleField method to adapt the popup query accordingly.

<div class="notices blue"> vtlib_open_popup_window permits you to attach more parameters to the open window URL by adding them in the last ID parameter. You can see an example of all of this being used <a href="https://github.com/tsolucio/corebos/commit/967d27401be62cf7892436fe1a4ca7a84b35884a"> <strong>in this commit</strong></a>.
</div>
