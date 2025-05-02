---
title: 'Related Panes Mapping'
metadata:
    description: 'This map defines additional panes or tabs on a modules detail view.'
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
        - adminmanuals
        - businessmappings
    tag:
        - relatedpanes
---

The coreBOS Related Panes Business Mapping serves the purpose of defining additional panes or tabs within a module's detail view. These extra panes function similarly to the "More Information" pane and include a dropdown menu with different blocks contained within the pane.

===

<div class="notices yellow">
Note that when a Related Pane mapping is defined for a module, the default "More Information" tab will NOT be added. If you want it, you have to add it into your mapping using the `defaultMoreInformation` directive.
</div>

A pane can consist of any combination of four types of blocks:

- **RelatedList**: a related list of records with actions, this is the current content of the default "More Information" tab
- **Widget**: this is a block that must be constructed following the [DetailViewWidget specification](../../../10.developer-guide/04.development_framework/11.develtutorials/16.add_special_block). You have full control of the space designate to this block
- **CodeWithoutHeader**: this will open a "div" and directly include your code inside
- **CodeWithHeader**: this will add a header following the look and feel of the default related list blocks and the open a "div" and directly include your code inside

The accepted format is:

```xml
<map>
  <originmodule>
    <originname>ModuleName</originname>
  </originmodule>
  <panes>
    <pane>
      <label></label>
      <sequence></sequence>
      <defaultMoreInformation></defaultMoreInformation> special marker to get default application more information, if present the blocks sections is ignored
      <blocks>
        <block>
        <label></label>
        <sequence></sequence>
        <type></type> RelatedList | Widget | CodeWithHeader | CodeWithoutHeader
        <loadfrom></loadfrom> related list label or id | file to load | widget reference
        <loadphp></loadphp>
        <handler_path></handler_path>
        <handler_class></handler_class>
        <handler></handler>
        </block>
      </blocks>
    </pane>
    .....
  </panes>
</map>
```

As with other business mappings the name of the record is what triggers the functionality. In this case the name must be **{Module}RelatedPanes**, for example, **AccountsRelatedPanes**

If *loadfrom* is **Widget** then the directives *handler\_path*, *handler\_class* and *handler*, if given, will be used to construct the Detail View Widget reference object.

If *loadphp* is given the file indicated as the value will be executed inside the context of the pane being loaded. This is where you will create additional Smarty variables and context for your code.

Examples
--------

```xml
    <map>
      <originmodule>
        <originname>Accounts</originname>
      </originmodule>
      <panes>
        <pane>
          <label>Comercial</label>
          <sequence>2</sequence>
          <blocks>
           <block>
            <label></label>
            <sequence>0</sequence>
            <type>RelatedList</type>
            <loadfrom>Invoice</loadfrom>
           </block>
           <block>
            <label></label>
            <sequence>1</sequence>
            <type>RelatedList</type>
            <loadfrom>Contacts</loadfrom>
           </block>
          </blocks>
        </pane>
        <pane>
          <label>Marketing</label>
          <sequence>1</sequence>
          <blocks>
           <block>
            <label></label>
            <sequence>2</sequence>
            <type>RelatedList</type>
            <loadfrom>Campaigns</loadfrom>
           </block>
           <block>
            <label></label>
            <sequence>1</sequence>
            <type>RelatedList</type>
            <loadfrom>Potentials</loadfrom>
           </block>
          </blocks>
        </pane>
        <pane>
          <label>More Information</label>
          <sequence>3</sequence>
          <defaultMoreInformation>1</defaultMoreInformation>
        </pane>
      </panes>
     </map>
```

This mapping will add two tabs and the default "More Information" tab. In the first tab you will find the Campaigns and Potentials related lists. In the second tab you will find the Contacts and Invoice related lists.

```xml
    <map>
      <originmodule>
        <originname>Accounts</originname>
      </originmodule>
      <panes>
        <pane>
          <label>pane1</label>
          <sequence>2</sequence>
          <blocks>
           <block>
            <label>blk0</label>
            <sequence>0</sequence>
            <type>RelatedList</type>
            <loadfrom>Invoice</loadfrom>
           </block>
           <block>
            <label>DetailViewBlockCommentWidget</label>
            <sequence>2</sequence>
            <type>Widget</type>
            <loadfrom>block://ModComments:modules/ModComments/ModComments.php</loadfrom>
           </block>
           <block>
            <label>blk1</label>
            <sequence>1</sequence>
            <type>RelatedList</type>
            <loadfrom>Contacts</loadfrom>
           </block>
          </blocks>
        </pane>
        <pane>
          <label>pane2</label>
          <sequence>1</sequence>
          <blocks>
           <block>
            <label>blk4</label>
            <sequence>2</sequence>
            <type>CodeWithoutHeader</type>
            <loadfrom>Smarty/templates/modules/Potentials/ProcessWorkflow_edit.tpl</loadfrom>
           </block>
           <block>
            <label>blk3</label>
            <sequence>1</sequence>
            <type>CodeWithHeader</type>
            <loadfrom>Smarty/templates/modules/Potentials/ProcessWorkflow_detail.tpl</loadfrom>
           </block>
          </blocks>
        </pane>
      </panes>
     </map>
```

This business map adds two tabs. The first one contains two special code blocks which you can see in [this documentation page](../../../10.developer-guide/04.development_framework/11.develtutorials/17.add_editdetail_block). The second tab contains two related lists and the typical Comments block.

Note that there is no "More Information" tab in this example.

<br>
------------------------------------------------------------------------

[Next](../13.import) | Chapter 16: Import.

------------------------------------------------------------------------