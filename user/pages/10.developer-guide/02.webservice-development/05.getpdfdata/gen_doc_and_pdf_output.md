---
title: 'GenDoc and PDF output'
metadata:
    description: 'GenDoc and PDF output'
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
        - add
---

## *GenDoc Template Merge*

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Get the binary representation of a template with records from a GenDoc supported module.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>getmergedtemplate(template, crmids, output_format)</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>GET</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>template – document web service ID that contains the template to merge<br />
crmids – comma-separated list of records to merge with the template<br />
output_format – pdf, odt, onepdf, oneodt</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>array –<br />
<strong>message</strong>: yes/no result,<br />
<strong>file</strong>: file name to a zip archive that contains the merged document(s)</td>
</tr>
</tbody>
</table>

## *GenDoc Document Conversion*
--------------------------

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Allows a web service client to send an OpenOffice/LibreOffice document for it to be converted into any format supported by unoconv and retrieve the resulting file</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>gendoc_convert(file: encoded, convert_format: string)</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td><strong>file</strong> – file structure<br />
- name: filename<br />
- size: size<br />
- type: type of the document<br />
- content: base 64 encoded content of the file<br />
<strong>convert_format</strong>: string, format to convert input file</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td><strong>result</strong>: result of operation (success|error)<br />
<strong>file</strong>: file: resulting file structure (same as input parameter)</td>
</tr>
<tr>
<td><strong>Comments:</strong></td>
<td>one of the unoconv alternatives must be installed and functional in the coreBOS install</td>
</tr>
</tbody>
</table>

## *Inventory modules*
-----------------

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Get the PDF representation of an inventory or supported module record.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>getpdfdata(id)</td>
</tr>
<tr>
<td><strong>Send as:</strong></td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>id – quote, salesorder, invoice, purchaseorder or custom module web service ID.<br />
CustomerPortal_PDF_Modules – global variable defines more modules supported by this endpoint.<br />
CustomerPortal_PDF – global variable defines how to get the PDF: PDFMaker, GenDoc, or Native<br />
CustomerPortal_PDFTemplate_{module} – defines the templateID to use for GenDoc and PDFMaker</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>array –<br />
<strong>recordid</strong>: ID passed as parameter,<br />
<strong>modulename</strong>: name of the module of the ID,<br />
<strong>pdf_data</strong>: base64 encoded string representing the PDF</td>
</tr>
<tr>
<td><strong>Comments:</strong></td>
<td>The user must have read access to the ID and the ID must belong to a supported module.<br />
There are 4 Global Variables that permit defining what method and template to use for the output.</td>
</tr>
<tr>
<td><strong>Example:</strong></td>
<td>see <strong>400_getpdf.php</strong> and <strong>400_getpdfdirect.php</strong> in <a href="http://github.com/tsolucio/coreboswsbrowser">coreBOSwsBrowser</a></td>
</tr>
</tbody>
</table>

<br>
------------------------------------------------------------------------

[Next](../00.manual/05.wfrlqsat)| Chapter 8: Workflows, Rules, Questions and Actions.

------------------------------------------------------------------------
