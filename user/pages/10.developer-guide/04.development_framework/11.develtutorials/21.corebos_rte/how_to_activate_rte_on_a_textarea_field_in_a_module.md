---
title: 'How to activate RTE on a textarea field in a module'
metadata:
    description: 'How to activate RTE on a textarea field in a module'
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
        - rte
---

- set the Global Variable **Application\_Use\_RTE** to 1 for the  module, which is it's default value
- create an [Extended Field Information Mapping](../../../../05.configuration-tools/02.business-maps/28.extendedfieldinfo) declaring the fields you want to have RTE activated
- enjoy!

------------------------------------------------------------------------

------------------------------------------------------------------------

<div class="notices red">THE PATCH BELOW IS NOT NECESSARY ANYMORE!</div>

It has been made obsolete by the [Extended Field Information Mapping](../../../../05.configuration-tools/02.business-maps/28.extendedfieldinfo) where you can establish which textarea fields in which modules you want to edit with RTE.

We leave the patch here as a historical reference.

------------------------------------------------------------------------

------------------------------------------------------------------------

How to activate RTE on a module
===============================

-   Activate RTE feature in Config Editor
-   modify template to add support for the module you want. If the
    module has more than one field with this feature you have to also
    add a block of code to launch CKEditor on the field
-   modify the EditView.php script of the module by passing the USE\_RTE
    variable
-   modify the detail view of the fields to process and show HTML
    symbols

This next patch does this for HelpDesk (Trouble Tickets)

```php
    diff --git a/Smarty/templates/salesEditView.tpl b/Smarty/templates/salesEditView.tpl
    index 96ce7b2..febb003 100755
    --- a/Smarty/templates/salesEditView.tpl
    +++ b/Smarty/templates/salesEditView.tpl
    @@ -251,7 +251,7 @@ function AddressSync(Addform,id)
     <input name='search_url' id="search_url" type='hidden' value='{$SEARCH}'>
     </form>
     
    -{if ($MODULE eq 'Emails' || $MODULE eq 'Documents' || $MODULE eq 'Timecontrol') and ($USE_RTE eq 'true')}
    +{if ($MODULE eq 'Emails' || $MODULE eq 'Documents' || $MODULE eq 'Timecontrol' || $MODULE eq 'HelpDesk') and ($USE_RTE eq 'true')}
        <script type="text/javascript" src="include/ckeditor/ckeditor.js"></script>
     <script type="text/javascript" defer="1">
        var textAreaName = null;
    @@ -279,6 +279,26 @@ function AddressSync(Addform,id)
            {rdelim}
        {rdelim});
        var oCKeditor = CKEDITOR.instances[textAreaName];
    +   {if $MODULE eq 'HelpDesk'}
    +       textAreaNameSolution = "solution";
    +       CKEDITOR.replace( textAreaNameSolution,
    +       {ldelim}
    +           extraPlugins : 'uicolor',
    +           uiColor: '#dfdff1',
    +               on : {ldelim}
    +                   instanceReady : function( ev ) {ldelim}
    +                        this.dataProcessor.writer.setRules( 'p',  {ldelim}
    +                           indent : false,
    +                           breakBeforeOpen : false,
    +                           breakAfterOpen : false,
    +                           breakBeforeClose : false,
    +                           breakAfterClose : false
    +                   {rdelim});
    +               {rdelim}
    +           {rdelim}
    +       {rdelim});
    +       var oCKeditorsolution = CKEDITOR.instances[textAreaNameSolution];
    +   {/if}
     </script>
     {/if}
     
    diff --git a/include/utils/DetailViewUtils.php b/include/utils/DetailViewUtils.php
    index 73c555e..b9f5515 100755
    --- a/include/utils/DetailViewUtils.php
    +++ b/include/utils/DetailViewUtils.php
    @@ -237,7 +237,7 @@ function getDetailViewOutputHtml($uitype, $fieldname, $fieldlabel, $col_fields,
                     $label_fld[] = '';
             }
        } elseif ($uitype == 19) {
    -       if ($fieldname == 'notecontent' or $module=='Timecontrol')
    +       if ($fieldname == 'notecontent' or $module=='Timecontrol' or $module=='HelpDesk')
                $col_fields[$fieldname] = decode_html($col_fields[$fieldname]);
            else
                $col_fields[$fieldname] = str_replace("&lt;br /&gt;", "<br>", $col_fields[$fieldname]);
    diff --git a/modules/HelpDesk/EditView.php b/modules/HelpDesk/EditView.php
    index a042b55..3331f20 100755
    --- a/modules/HelpDesk/EditView.php
    +++ b/modules/HelpDesk/EditView.php
    @@ -22,7 +22,7 @@ if($_REQUEST['record'] != '') {
        //Added to display the ticket comments information
        $smarty->assign("COMMENT_BLOCK",$focus->getCommentInformation($_REQUEST['record']));
     }
    -
    +$smarty->assign("USE_RTE", vt_hasRTE());
        $smarty->display("salesEditView.tpl");
     
     ?>
    \ No newline at end of file
```