---
title: 'How to add custom validations to your module'
metadata:
    description: 'How to add custom validations to your module'
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
        - businessmappings
    tag:
        - validations
---

<div class="notices red">This method has been superseded by the Validations BussinessMap</div>

[Validations Bussiness Map](../../../../05.configuration-tools/02.business-maps/26.validations). Although the system described here is still valid and working (for backward compatibility), it is recommended to use the more flexible and powerful validation business mapping. <strong>Implemented as of 2017-05-30.</strong>

Each field in a module has two native types of validation:

- data type validation: when you define a field on a module you indicate the type that it is; integer, string, currency, date, ...  So when you are editing a record with that field on screen coreBOS will automatically ensure that the value introduced is of the correct type.
- mandatory validation: you can indicate which fields must contain a value, in other words, they cannot be left empty

Besides these two types which are supported by all fields, and some
additional undocumented tricks that can be done using an extended syntax
in the typeofdata field, there are only a handful of hardcoded
validations in the system:

- no accountname duplicates
- mandatory email on contact if portal user checked
- contact birthday
- sales order recurring settings
- start and end dates on calendar

If you want to add your own validations, for the moment you will have to
add some code.

Each module supports special validations that can be done in a PHP file
called:

    {ModuleName}Validation.php

which **must** live inside the module's directory.

So, for example, you [can see in the
application](https://github.com/tsolucio/corebos/blob/master/modules/Accounts/AccountsValidation.php)
the file

    modules/Accounts/AccountsValidation.php

which contains the validation of "no duplicate accountname".

All these validation files support the same syntax; they will receive an
array of all the values that are currently in the user's browser in the
$\_REQUEST variable called *structure* and they must return one of three
outputs:

1.  %%%OK%%% to indicate that all validations have passed correctly
2.  %%%CONFIRM%%% followed by any message to produce a screen that will
    ask for confirmation using the text following the CONFIRM label
3.  Any other output/message which will be interpreted as an error
    message that will be shown to user

Examples
--------

**No duplicate Leads based on email and phone**

    global $log,$currentModule,$adb;

    $screen_values = json_decode($_REQUEST['structure'],true);

    $query = 'SELECT count(*) as cnt
        FROM vtiger_leaddetails
        INNER JOIN vtiger_crmentity on vtiger_leaddetails.leadid = vtiger_crmentity.crmid
        INNER JOIN vtiger_leadscf on vtiger_leaddetails.leadid = vtiger_leadscf.leadid
        INNER JOIN vtiger_leadaddress on vtiger_leaddetails.leadid = vtiger_leadaddress.leadaddressid
        WHERE vtiger_crmentity.deleted = 0 and vtiger_leaddetails.converted=0 ';

    $email = vtlib_purify($screen_values['email']);
    $phone = vtlib_purify($screen_values['phone']);
    if (!empty($email) and !empty($phone)) {
        $query.='and (email = ? or phone = ?) ';
        $params = array($email,$phone);
    } elseif (!empty($email)) {
        $query.='and email = ? ';
        $params = array($email);
    } elseif (!empty($phone)) {
        $query.='and phone = ? ';
        $params = array($phone);
    } else {
        echo '%%%OK%%%';
        die();
    }

    $id = vtlib_purify($screen_values['record']);
    if(!empty($id)) {
        $query .= 'and vtiger_leaddetails.leadid != ?';
        array_push($params, $id);
    }

    $result = $adb->pquery($query, $params);
    if($adb->query_result($result,0,'cnt') > 0) {
        echo getTranslatedString('LBL_LEAD_EXISTS','Leads');
        die;
    }

    echo '%%%OK%%%';

**No duplicate Contacts based on email**

    global $log,$currentModule,$adb;

    $screen_values = json_decode($_REQUEST['structure'],true);

    $query = 'SELECT count(*) as cnt
        FROM vtiger_contactdetails
        INNER JOIN vtiger_crmentity on vtiger_contactdetails.contactid = vtiger_crmentity.crmid
        INNER JOIN vtiger_contactaddress on vtiger_contactaddress.contactaddressid=vtiger_contactdetails.contactid
        INNER JOIN vtiger_contactsubdetails on vtiger_contactsubdetails.contactsubscriptionid=vtiger_contactdetails.contactid
        INNER JOIN vtiger_contactscf on vtiger_contactscf.contactid=vtiger_contactdetails.contactid
        WHERE vtiger_crmentity.deleted = 0 ';

    $email = vtlib_purify($screen_values['email']);
    if (!empty($email)) {
        $query.='and (email = ? or secondaryemail = ?) ';
        $params = array($email,$email);
    } else {
        echo '%%%OK%%%';
        die();
    }

    $id = vtlib_purify($screen_values['record']);
    if(!empty($id)) {
        $query .= 'and vtiger_contactdetails.contactid != ?';
        array_push($params, $id);
    }

    $result = $adb->pquery($query, $params);
    if($adb->query_result($result,0,'cnt') > 0) {
        echo getTranslatedString('LBL_CONTACT_EXISTS','Contacts');
        die;
    }

    echo '%%%OK%%%';

**Blocked Quotes depending on Quote Stage**

<div class="notices blue"> This isn't really validation but you
can do it this way also.</div>

    global $log,$currentModule,$adb;

    $screen_values = json_decode($_REQUEST['structure'],true);

    $record = vtlib_purify($screen_values['record']);
    $closedstages = array('Approved','Cancel','Paid','Delivered');
    if (!empty($record)) { // editando
        $qrs = $adb->pquery('SELECT quotestage FROM vtiger_quotes WHERE quoteid=?',array($record));
        if ($qrs and $adb->num_rows($qrs)>0) {
            $dbqstage = $adb->query_result($qrs, 0, 0);
            //$frqstage = vtlib_purify($_REQUEST['quotestage']);
            if (in_array($dbqstage, $closedstages)) {
                echo 'This quote is closed. Please duplicate it to edit and change.';
                die();
            }
        }
    }

    echo '%%%OK%%%';
