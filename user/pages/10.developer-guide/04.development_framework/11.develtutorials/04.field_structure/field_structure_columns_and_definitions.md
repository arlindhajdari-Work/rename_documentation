---
title: 'Field Structure: Columns and definitions'
metadata:
    description: 'Each field has to be displayed in two different ways for the Detail view and Edit view.'
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
        - field
    tag:
        - structure
---

### Display Types for Fields in Modules

Each field has to be displayed in two different ways for the Detail view and Edit view. Display type column defines a field to be displayed either in Edit view or the Detail view or both.

===

The following are some of the display types that are used:

- **1** - Displayed both in Detail view and Edit view
- **2** - Displayed only in the Detail view (Ex. Created time, Modified time) Read-only field. The application will never update this type of field, the only way to set a value is using direct SQL (save\_module or custom handler, for example)
- **3** - It is not displayed either in DetailView nor EditView, but can be shown in ListView. For example Total, subtotal in Invoice Module. These Fields are not tied to any block.
- **4** - a Read-Only field that can be modified with workflows. **NOTE** if you want to save a displaytype 4 field from inside your custom code using the normal "save" method, you **MUST** trick that save to think it is being called from the workflow system by setting the $from\_wf global variable to true before the save (and back to false after)
- **5** - Only in create mode. Cannot be used in workflows

### typeofdata for Fields in Modules

<table class="table table-striped">
<td>typeofdata</td>
<td>data type</td>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C</td>
<td>Checkbox/Boolean</td>
</tr>
<tr class="even">
<td>D</td>
<td>Date</td>
</tr>
<tr class="odd">
<td>DT</td>
<td>DateTime</td>
</tr>
<tr class="even">
<td>E</td>
<td>EMail</td>
</tr>
<tr class="odd">
<td>I</td>
<td>Integer</td>
</tr>
<tr class="even">
<td>N</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>NN</td>
<td>Negative Number</td>
</tr>
<tr class="even">
<td>O</td>
<td>RecurringType/Duration_minutes</td>
</tr>
<tr class="odd">
<td>P</td>
<td>Password</td>
</tr>
<tr class="even">
<td>T</td>
<td>Time</td>
</tr>
<tr class="odd">
<td>V</td>
<td>Varchar</td>
</tr>
</tbody>
</table>

### Examples: extracted directly from the database

<table class="table table-striped">
<td>typeofdata</td>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C~O</td>
</tr>
<tr class="even">
<td>DT~M~time_start</td>
</tr>
<tr class="odd">
<td>DT~M~time_start~Time Start</td>
</tr>
<tr class="even">
<td>D~M</td>
</tr>
<tr class="odd">
<td>D~M~OTH~GE~date_start~Start Date &amp; Time</td>
</tr>
<tr class="even">
<td>D~O</td>
</tr>
<tr class="odd">
<td>D~O~OTH~GE~sales_start_date~Sales Start Date</td>
</tr>
<tr class="even">
<td>D~O~OTH~GE~start_date~Start Date</td>
</tr>
<tr class="odd">
<td>D~O~OTH~GE~support_start_date~Support Start Date</td>
</tr>
<tr class="even">
<td>D~O~OTH~G~start_period~Start Period</td>
</tr>
<tr class="odd">
<td>E~M</td>
</tr>
<tr class="even">
<td>E~O</td>
</tr>
<tr class="odd">
<td>I~M</td>
</tr>
<tr class="even">
<td>I~O</td>
</tr>
<tr class="odd">
<td>NN~O</td>
</tr>
<tr class="even">
<td>N~M</td>
</tr>
<tr class="odd">
<td>N~O</td>
</tr>
<tr class="even">
<td>N~O~10,2</td>
</tr>
<tr class="odd">
<td>N~O~2,2</td>
</tr>
<tr class="even">
<td>N~O~2~2</td>
</tr>
<tr class="odd">
<td>O~O</td>
</tr>
<tr class="even">
<td>P~M</td>
</tr>
<tr class="odd">
<td>T~M</td>
</tr>
<tr class="even">
<td>T~O</td>
</tr>
<tr class="odd">
<td>V~M</td>
</tr>
<tr class="even">
<td>V~O</td>
</tr>
<tr class="odd">
<td>V~O~LE~150</td>
</tr>
<tr class="even">
<td>V~O~LE~16</td>
</tr>
<tr class="odd">
<td>V~O~LE~25</td>
</tr>
<tr class="even">
<td>V~O~LE~4</td>
</tr>
<tr class="odd">
<td>V~O~LE~9</td>
</tr>
</tbody>
</table>

In the above examples:

    *M; Indicates Mandatory field 
    *O; Indicates Optional field

### Basic Validations on Numbers and Dates

On numeric and date fields you can add some more information on the typeofdata column in order to perform some basic validations when editing.

Numeric fields accept a comparison operator followed by a number to use in the comparison.

    N~O~LE~22

will assure that the number in this field is smaller or equal to 22

Date fields accept the same comparison operator followed by the field name of another date field being edited in the browser and will make sure that the relation indicated by the operator is true.

    D~O~OTH~GE~dateinservice~Date in Service

the date in this field will be equal to or bigger than the value in dateinservice field

Accepted comparators are: L,LE,E,NE,G,GE

### Mass Edit

-  0 is blocked non editable, it cannot be activated in layout editor
-  1 is mass editable
-  2 is disabled mass editable but can be enabled in layout editor

### Quick Create

-  0 is always shown and cannot be deactivated in the layout editor
-  1 is not shown but can be set in the layout editor
-  2 is shown but can be unset in the layout editor
-  3 is never shown and cannot be activated in the layout editor

### Presence

-   0 always active, cannot be modified in layout editor
-   1 inactive
-   2 active and editable
