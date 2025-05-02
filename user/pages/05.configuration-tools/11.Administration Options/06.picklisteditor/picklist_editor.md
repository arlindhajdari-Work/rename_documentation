---
title: 'Picklist Editor'
metadata:
    description: 'Customize the picklist values in different modules.'
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
        - adminmanual
    tag:
        - picklist
        - picklisteditor
---

As the name itself says, picklist is a dropdown field with a list of options available, within which, only one option can be selected. For instance, *Lead status* in the *Leads* module.

**Picklist Editor** can be used to customize the picklist values in different modules. Select a role before performing global actions such as add, edit and, delete; as the picklist values vary across roles.

## Get started
Click on Settings *Icon > CRM Settings → Picklist Editor* (This can be found under studio block)

![](locatepicklisteditor.png?width=70%)

To customize a picklist, select the module that it is in from *Select Module* dropdown (ex: Leads); consequently, Select picklist dropdown displays the corresponding picklist fields (I*ndustry, Lead Source, Lead Status, Rating, Salutation*) available for that module. This dropdown can be used to select the picklist field for performing global actions.

![](globaloperationspicklist.png?width=70%)

## Add new Picklist values
-   Click on the Add Item button next to the Select picklist dropdown.
-   This will bring up a popup with the existing picklist values displayed on the left-hand side.
-   You can add new values in the textarea on top-right and assign role(s) on right hand lower side of the popup accordingly.
-   Click *Save* to update your changes.

<div class="notices blue">
Note: You can add multiple values and assign multiple roles at the same time
</div>

For instance, add 'newValue' to *Lead source* field in Leads module
![](picklisteditoradd.png?width=70%)

<div class="notices blue">
Note: If you don't select any role for the new picklist values, they will be present in the picklist values but not displayed for any role (other than admin).
</div>

## Edit picklist values
-   Click on the Rename Item button next to the Select picklist dropdown.
-   This will bring up a popup with the existing picklist values in select box.
    -  select a picklist value you intend to edit.
    -  you can edit the picklist value in the textbox below the existing picklist values.
-   Once you are done with the changes, click on the Apply button to save your changes to the picklist.

![](picklistadd.png?width=70%)

<div class="notices blue">
Note: It cannot be replaced with an empty value
</div>

## Delete existing picklist values
This operation can be performed to delete the picklist value(s) of any module permanently.

-   Click on the Delete Item button next to the *Select picklist* dropdown.
-   This will bring up a popup with existing picklist values.
-   Select the value(s) you intend to delete, choose a value from *Replace* with dropdown and click on *Delete* button.

For example, delete picklist values (Partner,Public Relations,Direct Mail,other) and replace with 'Other'.

![](picklistdelete.png?width=50%)

Deleted picklist values will be replaced with another value. The information stored in deleted values will be moved to newly defined value.

<div class="notices blue">
Note: You should have at least one value in any picklist.
</div>

## Create a custom picklist field
You can create new custom picklist fields using the layout editor.

-   Go to Settings → Module Manager
-   Click on module settings icon, highlighted below, at extreme right of each module.

![](contactssettings.png?width=80%)

-   Click on Layout Editor
-   Click on add custom field icon, highlighted below.

![](createcontactfield.png?width=80%)


-   Select field type as *Pick List* on left hand side, provide a picklist name in *Label* on top-right, and provide values in *Pick list Values *textarea on righthand lower side of the popup.

![](newpicklist.png?width=70%)

## Re-arrange Picklist Values
You can re-arrange the existing picklist values for each role.

-   Choose the desired module from the Select Module dropdown.; e.g. Leads.
-   Select the role to which the changes should be reflected from Picklist Available in Leads For field.
-   Click on the Assign button; Consequently, a popup will be displayed where you can add or hide picklist values by moving them around.
-   Re-arrange the picklist values by clicking on the arrows provided on the right side of the popup.

![](re-arrangepicklistvalues.png?width=70%)

To transfer the changes to other roles, click on the link Add to Other Roles, Select the desired role(s) and click the Save button to update changes.

## Role based Picklist Values

The values available in a picklist for any given user are defined by that user's role AND those values available for users under this user's role in the hierarchy. Since a user is able to see and edit all information available to those roles below his, it is normal that this user will automatically see all the values available to the users in sub-roles.

So, if you need to make a value not available for a user, remember to eliminate that value from all of that user's sub-roles.

This restriction affects ONLY the possibility for these users to assign that value to newly created records and records that currently do not have that value. In other words, if a user does not have access to a value X in a picklist, they will not be able to set that value to a new record nor a record that has some other value, but if the record currently has value X assigned they will be able to leave it with that value.

All users will always see the values assigned to a record, even if they do not have permission to use that value as a valid assignment.

In other words:

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Create</strong></td>
<td>Users only see values they have permission to access.</td>
</tr>
<tr>
<td><strong>Retrieve Picklist</strong></td>
<td>Users see value assigned in the record, even if they don't have access to the value.</td>
</tr>
<tr>
<td><strong>Retrieve</strong></td>
<td>Retrieving infromation works as explained above for List View, Detail View and Reports. Exporting is special and will always give you the real value saved in the field.</td>
</tr>
<tr>
<td><strong>Update Picklist</strong></td>
<td>Users see value assigned in the record, even if they don't have access to the value.</td>
</tr>
<tr>
<td><strong>Update Multi-Picklist</strong></td>
<td>Users only see values they have permission to access. Any other values assigned will be perserved.</td>
</tr>
</tbody>
</table>

<br>
## Video Tutorial

[plugin:youtube](https://youtu.be/p3VXYMP-wjY)
