---
title: 'Document Management View'
metadata:
    description: 'Dedicated Document Management view that can be used to access documents in various parts of the application.'
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
        - dms
        - document
---

The Document Management System view, or **DMS view** for short, is an extension that permits us to work with the documents saved in the application from different points of view.

===

We will be presented with a tree view based on the folders created in the application where we will be able to navigate through the folders and work with the documents contained in each folder. We will be able to search, view, create, delete, and even edit/update the documents if they are in a format supported for that ([OnlyOffice editor must be configured](https://blog.evolutivo.it/blog/onlyofficeedit)). Additionally, we will be able to copy the document and a link to it. There are even some special options for emails where you can convert the `.eml` file into a real email record and import the attachments contained inside the email.

There are various ways to access the DMS view. The first is to just change the action in URL of any module.

https://your_server/your_corebos/index.php?action=DMS&module=Documents

This access shows us all the folders and documents available in the application.

Another way is to create a list view button on any module like this:

- Type: LISTVIEWBASIC
- URL: `DMSModal()`

![List View DMS action](ListViewDMSAction.png?width=100%)

This will load the same view with an automatic filter on the documents related to the records in the select filter.

Finally, we can also add the DMS view as a widget, either inline in the detail view or in a related pane.

- Type: DETAILVIEWWIDGET
- URL: `block://DMSWidget:modules/Utilities/DMSWidget.php`

![DMS Widget action](DMSWidgetAction.png?width=100%)

![Accounts DMS Widget](AccountsDMSWidget.png?width=100%)

## Customization options

### Global Variables

- **Application_DMS_OrderByFolders**: Sort folders in DMS based on some given fields e.g. foldername. In this case the folders are ordered in alphabetical order. Default sort for folders is "sequence".
- **Application_DMS_RemoveEntityColumn**: This variable is used to remove the "Entity" column in DMS. This column shows other records the document is related with.
- **Application_DMS_ShowAllAction**: Show or not the "Show All" action in DMS. The default value is to show this option.

### Business Maps Columns

We can define the columns we want to show in the DMS view by using a `MassUpsertGrid` map. We also can indicate the document and document folder columns we want the search functionality to work with defining the columns between `search` tags.

- Default business map name: `DMS_Columns`
- Type: `MassUpsertGridView`
- Content:

```xml
<map>
<originmodule>
  <originname>Documents</originname>
</originmodule>
  <search>(Here we define the filter feature in the DMS)
    <group>(Here we define in base of what we are filtering: Documents,DocumentFolders)
      <name>Documents</name>
      <fields>(here we define the Document fields to filter on)
        <field>
          <name>notes_title</name>
          <label>Title</label>
        </field>
        <field>
          <name>assigned_user_id</name>
          <label>Assigned To</label>
        </field>
        <field>
          <name>note_no</name>
          <label>Document No</label>
        </field>
        <field>
          <name>filename</name>
          <label>File Name</label>
        </field>
      </fields>
    </group>
    <group>
      <name>DocumentFolders</name>
      <fields>(here we define the DocumentFolders fields to filter on)
        <field>
          <name>foldername</name>
          <label>Folder Name</label>
        </field>
      </fields>
    </group>
  </search>
  <columns>(Here we define the DMS columns to show in DMS view)
    <field>
      <name>smownerid</name>
    </field>
    <field>
      <name>note_no</name>
    </field>
    <field>
      <name>title</name>
    </field>
    <field>
      <name>notecontent</name>
    </field>
  </columns>
</map>
```

Another example, changing only the columns.

```xml
<map>
  <originmodule>
    <originname>Documents</originname>
  </originmodule>
  <columns>
    <field>
      <name>smownerid</name>
    </field>
    <field>
      <name>note_no</name>
    </field>
    <field>
      <name>title</name>
    </field>
  </columns>
</map>
```

We can also override the default business map by passing in the name of the map we want to use in the `bmapname` request parameter in the URL `bmapname=testmap`

### Business Maps Filtering

DMS also supports file type filtering, enabling users to display specific file types within their DMS widget. The implementation of this functionality is based on another business map as follows:

- Map Name: Mandatory (No specific rules)
- Map Type: Condition Query
- Target Module: Documents
- Content

```xml
<map>
  <module>Documents</module>
  <fields>filetype</fields>
  <conditions>[{"fieldname":"filetype","operation":"contains","value":"png/pdf...","valuetype":"rawtext","joincondition":"","groupid":"0"}]</conditions>
  <return>query</return>
</map>
```

For example, to do this in a List View, create a Business Action with the following details:

- Link Type: LISTVIEWBASIC
- Link URL: DMSModal(0, 'mapname');
- Link Label: DMS
- Module List: Module where DMS will be displayed
- Active: TRUE

To support this filter in a widget, as a Related List within the related pane map for the module, insert the following block:

```xml
<block>
  <label>Documenti</label>
  <sequence>0</sequence>
  <type>Widget</type>
  <loadfrom><![CDATA[block://DMSWidget:modules/Utilities/DMSWidget.php?ConditionQuery=mapname]]></loadfrom>
</block>
```

By following these steps, users can effectively filter and display specific file types in both ListView and RelatedLists views within the DMS widget, enhancing document management capabilities.

## More Information

[plugin:youtube](https://youtu.be/eoy7DpLWgOs)
