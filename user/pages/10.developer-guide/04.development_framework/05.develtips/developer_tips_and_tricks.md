---
title: 'Developer Tips and Tricks'
metadata:
    description: 'Developer Tips and Tricks. Questions and answers'
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
        - contribute
    tag:
        - guidelines
---

Find here a set of questions and answers about developing and fine tuning the application from within

===

- [How can I activate Single Pane for only one (my) module, independent of the system settings?](../develtips#how-can-i-activate-single-pane-for-only-one-my-module-independent-of-the-system-settings)
- [Custom date fields load by default "today". We need a custom date field to be empty by default, how can we accomplish this.](../develtips#custom-date-fields-load-by-default-today-we-need-a-custom-date-field-to-be-empty-by-default-how-can-)
- [How to create custom formula function for field expressions in workflows](../develtips#how-to-create-custom-formula-function-for-field-expressions-in-workflows)
- [How can I get the Edit button to open in a new window](../develtips#how-can-i-get-the-edit-button-to-open-in-a-new-window)
- [PDF Formatting](../develtips#pdf-formatting)
- [How to eliminate currency sign in report exports](../develtips#how-to-eliminate-currency-sign-in-report-exports)
- [Modify record default view order](../develtips#modify-record-default-view-order)
- [How can I deactivate the delete button on my custom fields in layout editor](../develtips#how-can-i-deactivate-the-delete-button-on-my-custom-fields-in-layout-editor)
- [How to recalculate privileges and regenerate user_privilege files from the command line.](../develtips#how-to-recalculate-privileges-and-regenerate-user-privilege-files-from-the-command-line)
- [When we go to create a quote, we choose the opportunity to relate, with a popup window to select among the created opportunities. Is there any way to **ONLY** see the open opportunities, so that by default all closed opportunities do not appear. (Cuando vamos a hacer un presupuesto como saben escogemos la oportunidad a relacionar, donde aparece una ventana para elegir la oportunidad creada. Hay alguna manera en que NO aparezca la oportunidad que se haya cerrado o clasificado en (Cerrado Ganado) ya que como saben, siguen apareciendo todas las oportunidades que tenga el vendedor).](../develtips#when-we-go-to-create-a-quote-we-choose-the-opportunity-to-relate-with-a-popup-window-to-select-among)
- [How can I get a blank currency field instead of 0?](../develtips#how-can-i-get-a-blank-currency-field-instead-of-0)
- [How can I add a module to an existing uitype10 field? or, How can I relate a module with another module that already has a uitype 10 field for relations?](../develtips#how-can-i-add-a-module-to-an-existing-uitype10-field-or-how-can-i-relate-a-module-with-another-modul)
- [How can I change the order of modules that appear in the picklist of a multi-module capture field. For example, the "Related To" field on the calendar.](../develtips#how-can-i-change-the-order-of-modules-that-appear-in-the-picklist-of-a-multi-module-capture-field-fo)
- [How can I get the SQL constructed for a Report?](../develtips#how-can-i-get-the-sql-constructed-for-a-report)
- [How can I get the SQL constructed for a List View?](../develtips#how-can-i-get-the-sql-constructed-for-a-list-view)
- [API control to turn-off Eventing triggers could be helpful when doing bulk operations like import/export.](../develtips#api-control-to-turn-off-eventing-triggers-could-be-helpful-when-doing-bulk-operations-like-import-ex)
- [How can I activate workflows when importing records?](../develtips#how-can-i-activate-workflows-when-importing-records)
- [How can I save() a record in a custom workflow function without launching the workflows and events again?](../develtips#how-can-i-save-a-record-in-a-custom-workflow-function-without-launching-the-workflows-and-events-aga)
- [A question regarding the functions to add in common utils, for example google drive file saving. For that I need to create a function in utils files and need to use those either in save.php file or in custom workflow functions. Is it a good idea?](../develtips#a-question-regarding-the-functions-to-add-in-common-utils-for-example-google-drive-file-saving-for-t)
- [I get an SQL error when launching the FAQ custom field support changeset. What can I do to fix it?](../develtips#i-get-an-sql-error-when-launching-the-faq-custom-field-support-changeset-what-can-i-do-to-fix-it)
- [Race condition in webservice 2-steps login process](../develtips#race-condition-in-webservice-2-steps-login-process)
- [Suppress header and footers in module action calls](../develtips#suppress-header-and-footers-in-module-action-calls)
- [I would like to be able to return to the newly created entity after creation, instead of returning to the previous one. For instance, when an invoice is created from an account, I would like to return to the newly created invoice instead of the account.](../develtips#i-would-like-to-be-able-to-return-to-the-newly-created-entity-after-creation-instead-of-returning-to)
- [Suppose I want to create a bunch of new modules with a set of data fields, but each module will also need some specific fields unique to it. I can think of two ways of doing this:](../develtips#suppose-i-want-to-create-a-bunch-of-new-modules-with-a-set-of-data-fields-but-each-module-will-also-)
- [How would I be able to mass print a set of invoices or sales orders?](../develtips#how-would-i-be-able-to-mass-print-a-set-of-invoices-or-sales-orders)
- [Mail Manager attachment relations. Update createdtime](../develtips#mail-manager-attachment-relations-update-createdtime)


<div class="notices blue">
<h2>How can I activate Single Pane for only one (my) module, independent of the system settings?</h2> </div>

You have to force the state in DetailView and CallRelatedList [Single Pane forced on module patch](https://discussions.corebos.org/documentation/lib/exe/fetch.php?media=devel:patches:singlepaneforcedonmodule.diff)

<div class="notices red">
This is obsolete, you do this now with global variables.</div>

```
--- a/CallRelatedList.php
+++ b/CallRelatedList.php
@@ -16,7 +16,7 @@
 $action = vtlib_purify($_REQUEST['action']);
 $record = vtlib_purify($_REQUEST['record']);
 $isduplicate = vtlib_purify($_REQUEST['isDuplicate']);
-
+$singlepane_view = 'true';
 if($singlepane_view == 'true' && $action == 'CallRelatedList') {
 	header("Location:index.php?action=DetailView&module=$currentModule&record=$record&parenttab=$category");
 } else {
--- a/DetailView.php
+++ b/DetailView.php
@@ -71,6 +71,7 @@
 }
 
 $smarty->assign('IS_REL_LIST', isPresentRelatedLists($currentModule));
+$singlepane_view = 'true';
 $smarty->assign('SinglePane_View', $singlepane_view);
 
 if($singlepane_view == 'true') {
```
---
<br>

<div class="notices blue">
<h2>Custom date fields load by default "today". We need a custom date field to be empty by default, how can we accomplish this.</h2> </div>

Look for this field meta data in the database table vtiger_field and change the value of the column generatedtype to 2.

---
<br>

<div class="notices blue">
<h2>How to create custom formula function for field expressions in workflows</h2> </div>

[https://discussions.vtiger.com/index.php?p=/discussion/168584/created-custom-formula-function-for-field-expressions-sub-string](https://discussions.vtiger.com/index.php?p=/discussion/168584/created-custom-formula-function-for-field-expressions-sub-string)

<div class="notices red">
This is obsolete, you do this inserting information in the database and creating the function in a separate file. Ask on gitter.
</div>

with global variables.

The next code adds a substring function and should suffice to show how to add more funtions. Please share if you create any.

```
Index: modules/com_vtiger_workflow/expression_engine/VTExpressionsManager.inc
===================================================================
--- modules/com_vtiger_workflow/expression_engine/VTExpressionsManager.inc	(revisión: 938)
+++ modules/com_vtiger_workflow/expression_engine/VTExpressionsManager.inc	(revisión: 939)
@@ -41,7 +41,7 @@
 	function expressionFunctions() {
 		return array('concat' => 'concat(a,b)', 'time_diffdays' => 'time_diffdays(a,b)', 'time_diff' => 'time_diff(a,b)',
 			'add_days' => 'add_days(datefield, noofdays)', 'sub_days' => 'sub_days(datefield, noofdays)',
-			'get_date' => "get_date('today')");
+			'get_date' => "get_date('today')", 'substring' => "substring(stringfield,start,end)");
 	}
 }
 
Index: modules/com_vtiger_workflow/expression_engine/VTExpressionEvaluater.inc
===================================================================
--- modules/com_vtiger_workflow/expression_engine/VTExpressionEvaluater.inc	(revisión: 938)
+++ modules/com_vtiger_workflow/expression_engine/VTExpressionEvaluater.inc	(revisión: 939)
@@ -144,6 +144,15 @@
 	}
 }
 
+function __vt_substring($arr) {
+	if (count($arr)<2 or count($arr)>3) return $arr[0];
+	if (count($arr)==2) {
+		return substr($arr[0],$arr[1]);
+	} else {
+		return substr($arr[0],$arr[1],$arr[2]);
+	}
+}
+
 /** END * */
 class VTFieldExpressionEvaluater{
 	function __construct($expr){
@@ -165,7 +174,8 @@
  	            'time_diffdays' => '__vt_time_diffdays',
 				'add_days' => '__vt_add_days',
 				'sub_days' => '__vt_sub_days',
-				'get_date' => '__vt_get_date'
+				'get_date' => '__vt_get_date',
+				'substring' => '__vt_substring'
 		);
 
 		$this->operations = array_merge($this->functions, $this->operators);
```

[plugin:youtube](https://youtu.be/k4RgrfxY880)

---
<br>

<div class="notices blue">
<h2>How can I get the Edit button to open in a new window</h2>
</div>

You have to apply this next code change.
```
diff --git a/include/js/general.js b/include/js/general.js
index d79cc33..c5eae5d 100755
--- a/include/js/general.js
+++ b/include/js/general.js
@@ -4066,6 +4066,7 @@ function submitFormForActionWithConfirmation(formName, action, confirmationMsg)
 function submitFormForAction(formName, action) {
 	var form = document.forms[formName];
 	if (!form) return false;
+	form.target="_blank";
 	form.action.value = action;
 	form.submit();
 	return true;
```
<div class="notices red">
Note that you may have to make a similar change in some other parts of the code, I <strong>ONLY</strong> did a quick test to answer the forum question. </div>
---
<br>

<div class="notices blue">
<h2>PDF Formatting</h2> </div>

See this page for tips on playing with PDF output: [PDF Formatting](../08.pdfformating)

---
<br>

<div class="notices blue">
<h2>How to eliminate currency sign in report exports</h2> </div>

This patch accomplishes this functionality. You don't have to collect the currency symbol, just save the value and format like with the php function "number_format" to get the value with the correct decimals.
```
Index: modules/Reports/ReportUtils.php
===================================================================
--- modules/Reports/ReportUtils.php     (revisión: 5892)
+++ modules/Reports/ReportUtils.php     (revisión: 5964)
@@ -75,11 +75,10 @@
                        $cur_sym_rate = getCurrencySymbolandCRate($currency_id);
                        if($value!='') {
                                $formattedCurrencyValue = CurrencyField::convertToUserFormat($currency_value, null, true);
-                               $fieldvalue = CurrencyField::appendCurrencySymbol($formattedCurrencyValue, $cur_sym_rate['symbol']);
+                               $fieldvalue = number_format($formattedCurrencyValue,2,'.','');
                        }
                } else {
-                       $currencyField = new CurrencyField($value);
-                       $fieldvalue = $currencyField->getDisplayValue();
+                       $fieldvalue = number_format($value,2,'.','');
                }

        } elseif ($dbField->name == "PurchaseOrder_Currency" || $dbField->name == "SalesOrder_Currency"
```
---
<br>
<div class="notices blue">
<h2>Modify record default view order</h2> </div>

Each module has defined it's default column for sorting. This must be changed in the code in the module's main script. For example, for Accounts we can find:

```php
//Added these variables which are used as default order by and sortorder in ListView
  var $default_order_by = 'accountname';
  var $default_sort_order = 'ASC';
```
where we can change the variable $default_order_by to any valid column of the account
<div class="notices red">
For this to work we must set the variable 'LISTVIEW_DEFAULT_SORTING' to true in the file config.performance.php </div>

---
<br>
<div class="notices blue">
<h2>How can I deactivate the delete button on my custom fields in layout editor</h2> </div>
Go to the database and change the value of vtiger_field.presence to

- 0: always active, cannot be modified in layout editor
- 1: inactive
- 2: active and editable

---
<br>
<div class="notices blue">
<h2>How to recalculate privileges and regenerate user_privilege files from the command line.</h2> </div>

This is a very useful trick when we lose the user_privileges directory or the admin user files and can't login.

```php
cd <application root directory>
php -r "require_once 'include/utils/UserInfoUtil.php'; RecalculateSharingRules();"
```
---
<br>
<div class="notices blue">
<h2>When we go to create a quote, we choose the opportunity to relate, with a popup window to select among the created opportunities. Is there any way to **ONLY** see the open opportunities, so that by default all closed opportunities do not appear. (Cuando vamos a hacer un presupuesto como saben escogemos la oportunidad a relacionar, donde aparece una ventana para elegir la oportunidad creada. Hay alguna manera en que NO aparezca la oportunidad que se haya cerrado o clasificado en (Cerrado Ganado) ya que como saben, siguen apareciendo todas las oportunidades que tenga el vendedor).</h2> </div>

This should work although I have my doubts about this functionality because I understand that you may want to associate the closed won opportunity to the quote. NOTE that the patch affects Quotes and SalesOrders.

```
diff --git a/Popup.php b/Popup.php
index 16e7048..c6faf32 100644
--- a/Popup.php
+++ b/Popup.php
@@ -237,6 +237,9 @@ else
 		$url_string .='&recordid='.vtlib_purify($_REQUEST['recordid']);
         	$where_relquery = getRelCheckquery($currentModule,$_REQUEST['return_module'],$_REQUEST['recordid']);
 	}
+	if ($currentModule=='Potentials' and (isset($_REQUEST['restrictclosed']) and $_REQUEST['restrictclosed']=='1')) {
+		$where_relquery = " and sales_stage not like 'Closed%' ";
+	}
 	if(isset($_REQUEST['relmod_id']) || isset($_REQUEST['fromPotential']))
 	{
 		if($_REQUEST['relmod_id'] !='')
diff --git a/include/js/general.js b/include/js/general.js
index d0feb0a..72db333 100755
--- a/include/js/general.js
+++ b/include/js/general.js
@@ -2379,9 +2379,9 @@ function selectPotential()
 		parent_module = 'Contacts';
 	}
 	if(record_id != '')
-		window.open("index.php?module=Potentials&action=Popup&html=Popup_picker&popuptype=specific_potential_account_address&form=EditView&relmod_id="+record_id+"&parent_module="+parent_module,"test","width=640,height=602,resizable=0,scrollbars=0");
+		window.open("index.php?module=Potentials&action=Popup&html=Popup_picker&popuptype=specific_potential_account_address&form=EditView&restrictclosed=1&relmod_id="+record_id+"&parent_module="+parent_module,"test","width=640,height=602,resizable=0,scrollbars=0");
 	else
-		window.open("index.php?module=Potentials&action=Popup&html=Popup_picker&popuptype=specific_potential_account_address&form=EditView","test","width=640,height=602,resizable=0,scrollbars=0");
+		window.open("index.php?module=Potentials&action=Popup&html=Popup_picker&popuptype=specific_potential_account_address&form=EditView&restrictclosed=1","test","width=640,height=602,resizable=0,scrollbars=0");
 }
 //to select Quote Popup
 function selectQuote()
```
---
<br>
<div class="notices blue">
<h2>How can I get a blank currency field instead of 0?</h2> </div>

More or less like this:

[blankinsteadofzero.diff](https://discussions.corebos.org/documentation/lib/exe/fetch.php?media=devel:blankinsteadofzero.diff)

---
<br>
<div class="notices blue">
<h2>How can I add a module to an existing uitype10 field? or, How can I relate a module with another module that already has a uitype 10 field for relations?</h2> </div>

This is very easy with vtlib. Simply get an instance of the field you want to modify and use the setRelatedModules() method. Have a look at the code below:
```php
<?php
// Turn on debugging level
$Vtiger_Utils_Log = true;
 
include_once('vtlib/Vtiger/Module.php');
 
$modname = 'Potentials';
$module = Vtiger_Module::getInstance($modname);
 
if($module) {
	$field = Vtiger_Field::getInstance('related_to',$module);
	$field->setRelatedModules(Array('Invoice'));
 
	echo "<br><b>Modified Field on $modname module.</b><br>";
 
} else {
	echo "<b>Failed to find $modname module.</b><br>";
}
 
?>
```
---
<br>
<div class="notices blue">
<h2>How can I change the order of modules that appear in the picklist of a multi-module capture field. For example, the "Related To" field on the calendar.</h2> </div>

You have to do this from database.

- First you have to know the fieldname, in this case it is "rel_id"
- Go to vtiger_field table and search this field to get the fieldid, for example: 1994
- After that you have to got to vtiger_fieldmodulerel, search this fieldid and you will see something like the next image, where you have to change the sequence to order the values:
![](sortmodulemultimodulecapture.png?width=100%)

---
<br>
<div class="notices blue">
<h2>How can I get the SQL constructed for a Report?</h2> </div>

Use the Debug_Report_Query Global variable

---
<br>
<div class="notices blue">
<h2>How can I get the SQL constructed for a List View?</h2> </div>

Use the Debug_ListView_Query Global variable

---
<br>
<div class="notices blue">
<h2>API control to turn-off Eventing triggers could be helpful when doing bulk operations like import/export.</h2> </div>

For bulk operation script setting $VTIGER_BULK_SAVE_MODE to true - turns off the Evening API.

---
<br>
<div class="notices blue">
<h2>How can I activate workflows when importing records?</h2> </div>

The import module set variable $VTIGER_BULK_SAVE_MODE = true , to not load the events to execute workflows. When you need to execute workflows when import records, you can apply the next patch. This patch force the validation to isBulkSaveMode, with this the workflows always will be load in any part of code.

After your importation, remember to undo the patch.

```
diff --git a/data/CRMEntity.php b/data/CRMEntity.php
index 30b7c2e..c737722 100755
--- a/data/CRMEntity.php
+++ b/data/CRMEntity.php
@@ -48,6 +48,7 @@ class CRMEntity {
         * to improve performance.
         */
        static function isBulkSaveMode() {
+               return false;
                global $VTIGER_BULK_SAVE_MODE;
                if (isset($VTIGER_BULK_SAVE_MODE) && $VTIGER_BULK_SAVE_MODE) {
                        return true;
```
---
<br>
<div class="notices blue">
<h2>How can I save() a record in a custom workflow function without launching the workflows and events again?</h2> </div>

Instead of calling save(), use saveentity(), that will not trigger the workflows again. 

<div class="notices blue">  
The answer to this is not only for workflow custom functions but in general whenever we need to save a record without launching workflow or events. </div>  

---
<br>
<div class="notices blue">
<h2>A question regarding the functions to add in common utils, for example google drive file saving. For that I need to create a function in utils files and need to use those either in save.php file or in custom workflow functions. Is it a good idea?</h2> </div>

I would suggest that you add your function and libraries in the event/custom code that you create. For example, suppose that you need to include some google drive library and some new functions to the save event of a document. You decide to add a vtiger.aftersave event. In the file where your new functionality resides you will add the library include at the beginning and your functions inside the new class so you don't need to modify the common utils base code. Something like this:

```php
<?php
require_once('google drive library');
 
class YourCustomEventHandlerClass extends VTEventHandler {
 
    function YourNewFunction() {
     ...
    }
 
    function handleEvent($eventName, $entityData) {
      global $log, $adb;
      ...
      $this->YourNewFunction();
      ...
    }
}
?>
```
---
<br>
<div class="notices blue">
<h2>I get an SQL error when launching the FAQ custom field support changeset. What can I do to fix it?</h2> </div>

It seems that your database can't setup the foreign key constraint for some reason. The correct path would be to review your data and make sure it is correct. In other words, the SQL must work, if it doesn't there is some inconsistency in your FAQ table. As an extreme case you can eliminate the constraint, the program will work the same and you will have custom field support on the FAQ module, simply the information in those custom fields will not be deleted when you eliminate a FAQ. Here is the change:

```
diff --git a/build/changeSets/cffaq.php b/build/changeSets/cffaq.php
index 3a10292..cf4896a 100644
--- a/build/changeSets/cffaq.php
+++ b/build/changeSets/cffaq.php
@@ -23,8 +23,7 @@ class cffaq extends cbupdaterWorker {
                } else {
                        $this->ExecuteQuery("CREATE TABLE IF NOT EXISTS vtiger_faqcf (
                                                faqid int(19),
-                                               PRIMARY KEY (faqid),
-                                               CONSTRAINT fk_1_vtiger_faqcf FOREIGN KEY (faqid) REFERENCES vtiger_faq(id) ON DELETE CASCADE
+                                               PRIMARY KEY (faqid)
                                                ) ENGINE=InnoDB DEFAULT CHARSET=utf8", array());
                        $this->sendMsg('Changeset '.get_class($this).' applied!');
                        $this->markApplied();
```

---
<br>
<div class="notices blue">
<h2>Race condition in webservice 2-steps login process</h2> </div>

I encountered a race condition using the 2-steps login process provided by vtiger's webservices. Say that you have a multi-process / multi-threaded application using vtiger's webservices. Each thread/process has to call getchallenge+login before proceeding in doing what they have to do (that's what doLogin() in vtwsclib does).

The problem lies in the getchallenge phase. include/Webservices/AuthToken.php does

```
delete from vtiger_ws_userauthtoken where userid=?

```
for the current user. This instruction can be executed in between the 2 getchallenge+login steps of another webservice thread/process, therefore destroying its chance of doing a correct login.

Maybe the solution would be for the getchallenge step to detect if there is already an existing (not expired) outstanding getchallenge request for the current user and return that.

[trac #6500](http://trac.vtiger.com/cgi-bin/trac.cgi/ticket/6500)
```php
Index: trunk/include/Webservices/AuthToken.php
===================================================================
--- trunk/include/Webservices/AuthToken.php	(revision 7)
+++ trunk/include/Webservices/AuthToken.php	(working copy)
@@ -19,6 +19,14 @@
 		$servertime = time();
 		$expireTime = time()+(60*5);
 
+		$sql = "select userid,token,expiretime, count(*) as count from vtiger_ws_userauthtoken group by userid=?";
+		$res = $adb->pquery($sql,array($userid,$servertime));
+		$result = $adb->fetchByAssoc($res);
+		if ($result['count']>=1) {
+			return array("token"=>$result["token"],"serverTime"=>$servertime,"expireTime"=>$result["expiretime"]);
+		}
+		
+
 		$sql = "delete from vtiger_ws_userauthtoken where userid=?";
 		$adb->pquery($sql,array($userid));
```

---
<br>
<div class="notices blue">
<h2>Suppress header and footers in module action calls</h2> </div>

The following URL format will suppress the header and footer information.
```
index.php?module=MyModule&action=MyModuleAjax&file=MyAction&ajax=true&...
```

---
<br>
<div class="notices blue">
<h2>I would like to be able to return to the newly created entity after creation, instead of returning to the previous one. For instance, when an invoice is created from an account, I would like to return to the newly created invoice instead of the account.</h2> </div>

Add this code to Save.php of the Invoice
```php
$source_id = $_REQUEST['return_id'];
unset($_REQUEST['return_id']);
$source_module = $_REQUEST['return_module'];
$_REQUEST['return_module'] = 'Invoice';
$_REQUEST['return_action'] = 'DetailView';
```
so it ends up looking like this:
```php
<?php
$source_id = $_REQUEST['return_id'];
unset($_REQUEST['return_id']);
$source_module = $_REQUEST['return_module'];
$_REQUEST['return_module'] = 'Invoice';
$_REQUEST['return_action'] = 'DetailView';
require_once('modules/Vtiger/Save.php');
?>
```

***Thanks Luke :-)***

---
<br>
<div class="notices blue">
<h2>Suppose I want to create a bunch of new modules with a set of data fields, but each module will also need some specific fields unique to it. I can think of two ways of doing this:</h2><br> Use different base tables for each module's specific data and have a common related table to store the common data.
Use a common base table and have different related tables for the specifics.</div>

As long as the field is mapped with target-table or column through meta-data and follows the Entity module convention system would continue to work.

Shared table poses a challenge when different module records enable edits of fields.

It would also come in the way of performance (specifically query cache invalidation).

If modules are from different publishers then sharing table is not a good idea, as the control or convention can be too tedious to maintain/manage.

---
<br>
<div class="notices blue">
<h2>How would I be able to mass print a set of invoices or sales orders?</h2></div>

Go to the Business Actions module and add a LISTVIEWBASIC button with this action:
```
massPrint(gVTModule)
```
---
<br>

<div class="notices blue">
<h2>Mail Manager attachment relations. Update createdtime</h2> </div>

**PLEASE be careful with the update SQL commands. Test them thoroughly**

```SQL
SELECT FROM_UNIXTIME(`lastsavedtime`),`lastsavedtime`, createdtime, modifiedtime
FROM `vtiger_mailmanager_mailattachments`
inner join vtiger_crmentity on crmid = attachid;
```

```SQL
UPDATE vtiger_crmentity
INNER JOIN `vtiger_mailmanager_mailattachments` ON crmid = attachid
SET createdtime = FROM_UNIXTIME(`lastsavedtime`), modifiedtime = FROM_UNIXTIME(`lastsavedtime`)
WHERE some condition
```

```SQL
SELECT *
FROM `vtiger_mailmanager_mailattachments`
inner join vtiger_crmentity on muid=crmid
```

```SQL
UPDATE vtiger_crmentity as matt
INNER JOIN vtiger_mailmanager_mailattachments ON matt.crmid = vtiger_mailmanager_mailattachments.attachid
INNER JOIN vtiger_crmentity as mail ON mail.crmid = vtiger_mailmanager_mailattachments.muid
SET matt.createdtime = mail.createdtime, matt.modifiedtime = mail.modifiedtime
WHERE some condition
```

```SQL
SELECT FROM_UNIXTIME(vtiger_mailmanager_mailrecord.lastsavedtime) AS unixLastSaved, vtiger_mailmanager_mailrecord.lastsavedtime, vtiger_mailmanager_mailrecord.muid, createdtime, modifiedtime, attachid, crmid
FROM vtiger_mailmanager_mailattachments
inner join vtiger_mailmanager_mailrecord on vtiger_mailmanager_mailattachments.muid = vtiger_mailmanager_mailrecord.muid
inner join vtiger_crmentity on crmid=attachid;
```

---
<br>
