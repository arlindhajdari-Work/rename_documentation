---
title: 'Webservice: Working with Documents and Images'
metadata:
    description: 'Installation and usage'
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
        - tool
---

## Create, Update and Retrieve Documents

The purpose of these enhancements are to permit uploading files when we create/update documents through the web service interface. This extension also adds functionality that permits establishing relationships with other entities to the document we are creating.

Calls to REST methods of Create, Retrieve and Update maintain their profile and keep working as before. This extension adds to these calls a set of special fields that will be acknowledged by the enhancements.

The special fields are:

<table class="table table-striped">
<tbody>
<tr>
<td><strong>relations</strong></td>
<td>a comma separated list of webservice identifiers.</td>
</tr>
<tr>
<td><strong>filename</strong></td>
<td>array with these fields:<br>
  name: string, name of the file to upload,<br>
  size: file size<br>
  type: file type<br>
  content: base64_encode(file)</td>
</tr>
</tbody>
</table>

With the virtual field **relations** we can establish relationships
between the document and any other record. For example, we can upload a
document and automatically relate it with a trouble ticket (HelpDesk).

Since a document can be related to many other records, the **relations**
parameter is a comma-separated list of entities. The document being
created will be related to all of them.

This new **relations** field will also be returned when executing a
Retrieve. The format will be a comma-separated list of related entities.

To permit uploading documents we have added another virtual field called
**filename**. It is an array with the four values we need to upload an
attachment:

- name: name of the attachment in the application
- size: size of the file being sent
- type: type of the file being sent
- content: base64 encoded string with the full contents of the file

As of **coreBOS 5.6** you will also receive another virtual field when
retrieving a document record. This field is called **\_downloadurl** and
represents the absolute path of the file attachment in the application.
This will permit easy linking from external applications and websites.
This functionality is especially useful for e-commerce sites.

This virtual field is also added to the query language when it is
possible.

<div class="notices blue">
the <strong>_downloadurl</strong> virtual field will only be present in documents with a file location type of Internal
</div>

Next, you can find some examples.

### Create
```php
    <?php
    include_once('cbwsclib/WSClient.php');
    require_once 'debugoutput.php';

    $url = 'http://localhost/corebos/webservice.php';
    $wsClient = new WSClient($url);
    // Login
    if (!$wsClient->doLogin('admin', 'pon la que corresponda')) {
      die('Login error.');
    }
     
    //name of the module for which the entry has to be created.
    $moduleName = 'Documents';

    // get file to upload
    $finfo = finfo_open(FILEINFO_MIME); // return mime type ala mimetype extension
    //$filename = 'createdoc.php';
    $filename = 'image001.png';
    $mtype = finfo_file($finfo, $filename);  // posiblemente haya que instalar librerias PECL adicionales a PHP
    $model_filename=array(
        'name'=>$filename,
        'size'=>filesize($filename),
        'type'=>$mtype,
        'content'=>base64_encode(file_get_contents($filename))
    );

    //fill in the details of the contacts.userId is obtained from loginResult.
    $contactData  = array(
        //'assigned_user_id'=>$userId,
        'notes_title' => 'REST Test createdoc',
        'filename'=>$model_filename,
        'filetype'=>$model_filename['type'],
        'filesize'=>$model_filename['size'],
        'filelocationtype'=>'I',
        'filedownloadcount'=> 0,
        'filestatus'=>1,
        'folderid' => '22x1',
        'relations' => '9x66873',  // besides creating the document it will relate it to this record
    );

    //encode the object in JSON format to communicate with the server.
    $objectJson = Zend_JSON::encode($contactData);
    if ($dcall==1) printvar("Create, sending in",$objectJson);

    $response = $wsClient->doCreate($moduleName, $contactData);
    if ($dcall==1) printvar("Raw response (json) Create",$response);

    $id = $response['id'];
    var_dump($response);
    ?>
```
### *RESULT OF THE CALL 

There is no visual difference from a normal call, the difference is in
the input parameters to the call and the changes that occur in the
application.

### Update
```php
    <?php
    include_once('cbwsclib/WSClient.php');
    require_once 'debugoutput.php';

    $url = 'http://localhost/corebos/webservice.php';
    $wsClient = new WSClient($url);
    // Login
    if (!$wsClient->doLogin('admin', 'pon la que corresponda')) {
      die('Login error.');
    }

    //name of the module for which the entry has to be created.
    $moduleName = 'Documents';

    // get file to upload
    $finfo = finfo_open(FILEINFO_MIME); // return mime type ala mimetype extension
    $filename = 'updatedoc.php';
    $mtype = finfo_file($finfo, $filename);  // posiblemente haya que instalar librerias PECL adicionales a PHP
    $model_filename=array(
        "name"=>$filename,
        "size"=>filesize($filename),
        "type"=>$mtype,
        'content'=>base64_encode(file_get_contents($filename))
    );
    //fill in the details of the contacts.userId is obtained from loginResult.
    $contactData  = array(
        'notes_title' => 'REST Test updatedoc',
        'filename'=>$model_filename,
        'filetype'=>$model_filename['type'],
        'filesize'=>$model_filename['size'],
        'filelocationtype'=>'I',
        'filedownloadcount'=> 0,
        'filestatus'=>1,
        'folderid' => '22x1',
        'id' => '7x134089',
        // 'relations' NOT SUPPORTED ON UPDATE: use set_relations webservice call
    );

    //encode the object in JSON format to communicate with the server.
    $objectJson = Zend_JSON::encode($contactData);
    if ($dcall==1) printvar("Update, sending in",$objectJson);

    $response = $wsClient->doUpdate($moduleName, $contactData);
    if ($dcall==1) printvar("Raw response (json) Update",$response);

    $id = $response['id'];
    var_dump($response);
    ?>
```
### *RESULT OF THE CALL 

There is no visual difference from a normal update call, the difference
is in the input parameters to the call and the changes that occur in the
application.

### Retrieve
```php
    <?php
    require 'dologin.php';

    // To obtain the identifier of the document you can use the Query operation
    $accountId = '7x134063';

    //sessionId is obtained from loginResult.
    $params = "sessionName=$sessionId&operation=retrieve&id=$accountId";
    //Retrieve must be GET Request.
    $httpc->get("$endpointUrl?$params");
    $response = $httpc->currentResponse();
    if ($dcall==1) printvar("Raw response (json) Retrieve",$response);

    //decode the json encode response from the server.
    $jsonResponse = Zend_JSON::decode($response['body']);
    if ($dcall==1) printvar("Webservice response Retrieve",$jsonResponse);

    //operation was successful get the token from the response.
    if($jsonResponse['success']==false)
        //handle the failure case.
        die('retrieve failed:'.$jsonResponse['error']['message']);

    $retrievedObject = $jsonResponse['result'];
    var_dump($retrievedObject);
    ?>
```
### *RESULT OF THE CALL 
```php
    Webservice response Retrieve

    array
      'success' => boolean true
      'result' => 
        array
          'notes_title' => string 'testd1' (length=6)
          'createdtime' => string '2013-10-15 12:08:06' (length=19)
          'modifiedtime' => string '2013-10-15 12:08:06' (length=19)
          'assigned_user_id' => string '19x1' (length=4)
          'notecontent' => string '<p>fdfgdfgdsflm</p><p>fg</p><p>lfmg</p><p>alfkmg</p>' (length=52)
          'filetype' => string 'text/x-sql' (length=10)
          'filesize' => string '922' (length=3)
          'filelocationtype' => string 'I' (length=1)
          'fileversion' => string '' (length=0)
          'filestatus' => string '1' (length=1)
          'filedownloadcount' => string '3' (length=1)
          'folderid' => string '22x1' (length=4)
          'note_no' => string 'DOC5379' (length=7)
          'id' => string '7x134063' (length=8)
          'relations' => !!! THIS IS NEW !!!
            array
              0 => string '9x66873' (length=7)   !!! related to record 66873 of the entity 9 !!!
          '_downloadurl' => string 'http://localhost/coreBOSwork/storage/2014/August/week2/134063_1.jpg' (length=64)
```
### Retrieve Attachment

This new REST method returns the base64 encoded file attached to the
given document. This call is added with two goals in mind, to obtain
information of the attachment of a document without downloading the
whole file which would slow many operations, and to no have to add yet
another virtual field to the native Retrieve operation to indicate if we
want to receive the whole file or not.

The **profile** of the method is

    retrievedocattachment(id:Id,returnfile:boolean):Map


<table class="table table-striped">
<tbody>
<tr>
<td><strong>id</strong></td>
<td>a comma separated list of webservice identifiers.</td>
</tr>
<tr>
<td><strong>returnfile</strong></td>
<td>1 if we want the whole file, 0 if we just want the attachment information</td>
</tr>
</tbody>
</table>

The **response** is an object with the fields of the attachment. For
each given identifier we will get an array with this structure:

<table class="table table-striped">
<tbody>
<tr>
<td><strong>filename</strong></td>
<td>is an array with the fields:<br>
  name: string, name of the file to upload,<br>
  size: file size<br>
  type: file type<br>
  content: base64_encode(file)</td>
</tr>
</tbody>
</table>


If the parameter **returnfile** is 0, the field **content** will be empty (no file sent, reducing bandwidth usage and time)

Find next an example code of a call to this method followed by the resulting output.

### *Example Code of Call
```php
    <?php
    require 'dologin.php';

    //fill in the details of the document id. Can be obtained using vtwsbrowser
    // select id from documents
    $docId='7x134063';
    //sessionId is obtained from loginResult.
    $params = array("sessionName"=>$sessionId, "operation"=>'retrievedocattachment', "id"=>$docId,'returnfile'=>'1');
    // must be POST Request.
    $httpc->post("$endpointUrl", $params, true);
    $response = $httpc->currentResponse();
    if ($dcall==1) printvar("Raw response (json) RetrieveDocAttachment",$response);

    //decode the json encode response from the server.
    $jsonResponse = Zend_JSON::decode($response['body']);
    if ($dcall==1) printvar("Webservice response RetrieveDocAttachment",$jsonResponse);

    //operation was successful get the token from the reponse.
    if($jsonResponse['success']==false)
        //handle the failure case.
        die('RetrieveDocAttachment failed: '.$jsonResponse['error']['message']);

    // fix for IE catching or PHP bug issue
    header("Pragma: public");
    header("Expires: 0"); // set expiration time
    header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
    // browser must download file from server instead of cache

    // force download dialog
    header("Content-Type: application/force-download");
    //header('Content-Type: application/pdf');   FIXME
    header("Content-Type: application/download");

    // use the Content-Disposition header to supply a recommended filename and
    // force the browser to display the save dialog.
    header('Content-Disposition: attachment; filename="'.$jsonResponse['result']['0']['filename'].'"');

    /*
    The Content-transfer-encoding header should be binary, since the file will be read
    directly from the disk and the raw bytes passed to the downloading computer.
    The Content-length header is useful to set for downloads. The browser will be able to
    show a progress meter as a file downloads. The content-lenght can be determined by
    filesize function returns the size of a file.
    */
    header("Content-Transfer-Encoding: binary");

    echo base64_decode($jsonResponse['result']['0']['attachment']);
    exit;
    ?>
```

### *RESULT OF THE CALL 

```php
    Raw response (json) RetrieveDocAttachment

    array
      'url' => string 'http://localhost/corebos/webservice.php' (length=39)
      'code' => int 200
      'headers' => 
        array
          'date' => string 'Fri, 18 Oct 2013 08:41:30 GMT' (length=29)
          'server' => string 'Apache/2.2.22 (Ubuntu)' (length=22)
          'x-powered-by' => string 'PHP/5.3.10-1ubuntu3.8' (length=21)
          'expires' => string 'Thu, 19 Nov 1981 08:52:00 GMT' (length=29)
          'cache-control' => string 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0' (length=62)
          'pragma' => string 'no-cache' (length=8)
          'content-length' => string '1376' (length=4)
          'connection' => string 'close' (length=5)
          'content-type' => string 'application/json' (length=16)
      'body' => string '{"success":true,"result":{"7x134063":{"recordid":"134063","filetype":"text\/x-sql","filename":"restconfig.sql","filesize":922,"attachment":"LS0KLS0gUmV0cmVpdmUgRG9jdW1lbnQgYW5kIENoYW5nZSBEb2N1bWVudCBjbGFzcwotLQp1cGRhdGUgdnRpZ2VyX3dzX29wZXJhdGlvbl9zZXEgc2V0IGlkPWlkKzE7CklOU0VSVCBJTlRPIGB2dGlnZXJfd3Nfb3BlcmF0aW9uYCAoCmBvcGVyYXRpb25pZGAsCmBuYW1lYCAsCmBoYW5kbGVyX3BhdGhgICwKYGhhbmRsZXJfbWV0aG9kYCAsCmB0eXBlYCAsCmBwcmVsb2dpbmAKKQpWQUxVRVMgKAooc2VsZWN0IG1heChpZCkgZnJvbSB2dGlnZXJfd3Nfb3BlcmF0aW9uX3NlcSksJ3JldHJpZXZl'... (length=1376)

    Webservice response RetrieveDocAttachment

    array
      'success' => boolean true
      'result' => 
        array
          '7x134063' => 
            array
              'recordid' => string '134063' (length=6)
              'filetype' => string 'text/x-sql' (length=10)
              'filename' => string 'restconfig.sql' (length=14)
              'filesize' => int 922
              'attachment' => string 'LS0KLS0gUmV0cmVpdmUgRG9jdW1lbnQgYW5kIENoYW5nZSBEb2N1bWVudCBjbGFzcwotLQp1cGRhdGUgdnRpZ2VyX3dzX29wZXJhdGlvbl9zZXEgc2V0IGlkPWlkKzE7CklOU0VSVCBJTlRPIGB2dGlnZXJfd3Nfb3BlcmF0aW9uYCAoCmBvcGVyYXRpb25pZGAsCmBuYW1lYCAsCmBoYW5kbGVyX3BhdGhgICwKYGhhbmRsZXJfbWV0aG9kYCAsCmB0eXBlYCAsCmBwcmVsb2dpbmAKKQpWQUxVRVMgKAooc2VsZWN0IG1heChpZCkgZnJvbSB2dGlnZXJfd3Nfb3BlcmF0aW9uX3NlcSksJ3JldHJpZXZlZG9jYXR0YWNobWVudCcsICdpbmNsdWRlL1dlYnNlcnZpY2VzL1JldHJpZXZlRG9jQXR0YWNobWVudC5waHAnLCAndnR3c19yZXRyaWV2ZWRvY2F0dGFjaG1lbnQnLCAnUE9TVCcsICcw'... (length=1232)
```

### Create, Update and Retrieve Images

Following a similar approach as the **filename** virtual field added for
uploading document files, we have added also a generic virtual field to
all the other modules in the application named **attachments**.

**attachments** is an array of file information for each image field
contained in a module where you want to upload a file and can be used in
Create, Update and Revise operations.

Let's suppose that you have two image fields on a module named cf_998
and cf_999. You can upload files to these two fields with an array like
this:

```php
    $recordInfo = array(
        ...other fields in the record...
        'cf_998' => 'barcode',
        'cf_999' => 'somename',
        'attachments' => array(
            'cf_998' => array(
                'name'=>'barcode',  // no slash nor paths in the name
                'size'=>strlen($file_data),
                'type'=>'image/png',
                'content'=>base64_encode($file_data)
            ),
            'cf_999' => array(
                'name'=>'somename',  // no slash nor paths in the name
                'size'=>strlen($file2_data),
                'type'=>'application/pdf',
                'content'=>base64_encode($file2_data)
            ),
        ),
        ...other fields in the record...
    );
```
A normal Retrieve call on a record with images will return the
information of the file; the name, the location on disk (URL), and some
other metadata in a virtual field with the same name of the field
followed by "imageinfo", but we have also added a method in order to
retrieve file information of a record.

getRecordImages allows a web service client to retrieve the information
of the image attachments associated with a record, which can then be
used with the build/HelperScripts/getImageData.php script to obtain the
image data itself.

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getRecordImages</td>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Returns an array of file information for each image field of a module.</td>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>getRecordImages(id:string):Map</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>GET</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>=&gt;00id: web service id of the record with image fields we want to get.</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>an array with: name, path, URL, type, internal ID, for each file in the record</td>
</tr>
</tbody>
</table>

**Examples:**

- [Create with Image](https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/438_createWithImage.php)
- [Update with Image](https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/438_updateWithImage.php)
- [How to update an image field from code](../../../10.developer-guide/04.development_framework/11.develtutorials/31.updateimagefield/)

### Product Multi-Image field

The product module contains a special, non-standard image field which
may contain many images. coreBOS does not recommend the use of this
field. Individual images should be used instead.

When calling Retrieve on a product the first image found in the
multi-image field will be returned. It is NOT guaranteed to always get
the same image.

You can use the **addProductImages** method to insert images in this field.

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>addProductImages</td>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Inserts a set of images into the Product multi-image field</td>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>addProductImages(id:string, files:Map):Map</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td> =&gt; id: web service ID of the product record to upload the images to<br />
=&gt; files: an array of images to upload, each array entry must contain two fields: name and content (base64 encoded)</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>an array with information of the executed operations</td>
</tr>
</tbody>
</table>


<br>
------------------------------------------------------------------------

[Next](../../../05.configuration-tools/05.gendoc)| Chapter 7: GenDoc and PDF output.

------------------------------------------------------------------------