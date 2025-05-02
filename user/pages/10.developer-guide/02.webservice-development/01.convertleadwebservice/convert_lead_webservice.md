---
title: 'Convert Lead Webservice'
metadata:
    description: 'Usage example of convert lead web service in order to convert an existing Leads into Accounts, Contacts & Opportunity using Webservice'
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
        - webservice
    tag:
        - lead
---

Usage example of convert lead web service in order to convert an existing Leads into Accounts, Contacts & Opportunity using Webservice.

===

Important points to note before using the following code:

- Check table vtiger_ws_entity to know the "id" (Webservice module ID) of the "Leads" module. Ensure that the Lead ID passed to vtws_convertleads function is in 'x' format.
- Following example uses standard vtwsclib library.
- Sample code:

```php
<?php
include_once('vtwsclib/Vtiger/WSClient.php');

function vtws_login(){
        $$url = 'http://en.vtiger.com/wip';
	$client = new Vtiger_WSClient($url);
	$login = $client->doLogin('admin', 'KpS9EjNz16JtPmoe');
        if(!$login) return 0;
        return $client;
}

function vtws_convertleads($recordid){
        $client = vtws_login();
        if ($client <> 0){
                $recordInfo = $client->doRetrieve($recordid);
                $wasError= $client->lastError();
                if($wasError) {
                        return $wasError['code'] . ':' . $wasError['message'];
                }
                if($recordInfo) {
                        $client1 = vtws_login();
                        $convert_lead_array = array();
                        $convert_lead_array['leadId'] = $recordInfo['id'];
                        $convert_lead_array['assignedTo'] = $recordInfo['assigned_user_id'];
                        $convert_lead_array['entities']['Accounts']['create']=true;
                        $convert_lead_array['entities']['Accounts']['name']='Accounts';
                        $convert_lead_array['entities']['Accounts']['accountname'] = $recordInfo['company'];
                        $convert_lead_array['entities']['Accounts']['industry']=$recordInfo['industry'];
                        $convert_lead_array['entities']['Potentials']['create']=true;
                        $convert_lead_array['entities']['Potentials']['name']='Potentials';
                        $convert_lead_array['entities']['Potentials']['potentialname']=$recordInfo['company'];
                        $convert_lead_array['entities']['Potentials']['closingdate']= date("Y-m-d", strtotime("+1 week Saturday"));
                        $convert_lead_array['entities']['Potentials']['sales_stage']= 'Prospecting';
                        $convert_lead_array['entities']['Potentials']['amount']= 0;
                        $convert_lead_array['entities']['Contacts']['create']=true;
                        $convert_lead_array['entities']['Contacts']['name']='Contacts';
                        $convert_lead_array['entities']['Contacts']['lastname']=$recordInfo['lastname'];
                        $convert_lead_array['entities']['Contacts']['firstname']=$recordInfo['firstname'];
                        $convert_lead_array['entities']['Contacts']['email']=$recordInfo['email'];
                        $convert_lead_json = json_encode($convert_lead_array);
                        $response = $client1->doInvoke('convertlead', array('element'=>$convert_lead_json));
                        $wasError = $client1->lastError();
                        if($wasError) {
                                return $wasError['code'] . ':' . $wasError['message'];
                        } else {
                                return 1;
                        }
                }
        }else{
                return 'Login failed';
        }
}

$d = '2x21022';
echo vtws_convertleads($d);

?>
```

<table>
<thead>
<table class="table table-striped">
<th>Purpose:</th>
<td>Permits the conversion of a lead into an account, contact and potential. This service is used by the application itself when converting leads.</td>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Profile:</strong></td>
<td>convertlead($entityvalues): Map</td>
</tr>
<tr class="even">
<td><strong>Send as:</strong></td>
<td>POST</td>
</tr>
<tr class="odd">
<td><strong>Parameters:</strong></td>
<td>&lt;code&gt; id: $entityvalues is an array. Consult the modules/Leads/LeadConvertToEntities.php to see an example.&lt;/code&gt;</td>
</tr>
<tr class="even">
<td><strong>Returns:</strong></td>
<td>Array with all the information of the new objects created</td>
</tr>
<tr class="odd">
<td><strong>URL Format:</strong></td>
<td><code>http://vtiger_url/webservice.php?operation=deleteUser&amp;sessionName=[session id]</code></td>
</tr>
</tbody>
</table>


<a href="https://discussions.vtiger.com//discussion/166499/usage-example-of-convert-lead-webservice">Thank you Ashutosh!</a></br>


<div class="notices blue">
You can also find an <a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/470_convertLead.php"><i>example in the coreBOS Webservice development</i></a> tool.
</div>

<div class="notices blue">
By setting $convert_lead_array['entities'][Contacts|Accounts|Potential]['create'] to false you can avoid creating a record in that module.
</div>

<div class="notices blue">
By default, a Lead is Converted into a Contact, but you can indicate the module you want to have the Lead values transferred to using the variable <strong>transferRelatedRecordsTo</strong>

 $convert_lead_array['entities']['transferRelatedRecordsTo'] = 'Accounts';

If you indicate that no Contact should be created the Lead values will be transferred to the Account.

If you indicate that neither a Contact nor an Account should be created the process will fail with a web service exception.
</div>

<div class="notices blue">
By default, the process will search for an existing Account with the same company name and relate the new records with this Account. This is done to avoid duplicates. You can override this behavior by assigning a value to the meta-variable <strong>forcecreate</strong> like this:

 $convert_lead_array['entities'][Accounts]['forcecreate'] = true;

Be careful as this will easily create duplicate account names and you won't be able to edit them unless you set the global variable <strong>Accounts_BlockDuplicateName</strong> to false.
</div>

<br>


[Next](../07.login) | Chapter 13: Portal user login.

