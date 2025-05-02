---
title: 'Use of OpenOffice with Data inside the Application'
metadata:
    description: 'This is the OpenOffice, LibreOffice + Rich Text Format merge feature for coreBOS'
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
        - gendoc
        - integration
    tag:
        - openoffice
        - libreoffice
---

This is the OpenOffice, LibreOffice + Rich Text Format merge feature for coreBOS

Usage:
------

Create a template file using OpenOffice or LibreOffice. As placeholders for the fields in coreBOS use the name of the entity followed by the name of the field without any spaces and in capital letters, for example: ACCOUNT\_ACCOUNTNAME will be replaced with the real account name being merged.

These templates can only have **one record per template**. We have an advanced merge extension which has this capability and much more.

Multi-line address (or descriptions or any field) are not supported by the merge extension due to the way it manipulates the internal structure of the document. To overcome this limitation we have introduced a small workaround whereas we will replace the newline characters for two exclamations (!!), then in the merged document you will have to convert these two symbols back to newlines. To help with this task we <a href="https://discussions.corebos.org/documentation/lib/exe/fetch.php?media=es:user:libreofficemacros.macro"> include two macros that do the work for you</a> You will have to add the OpenOffice BASIC macros included in the project to your word processor.

<div class="notices blue">
You can also get the file from the build/oo-merge directory </div>

[An example template(.odt)](oo_test_template.odt) is included and can also be found in the build/oo-merge directory. The template uses some labels as an example.

Login with a user with administrative rights.

Go to Settings-&gt;Mail Merge and load an OpenOffice or LibreOffice (.odt) or Rich Text Format (.rtf) template for a specific module.

The supported modules are Leads, HelpDesk, Accounts, Contacts.

Go to a specific module, select one or more items (e.g. one or more Contacts), choose the correct template in the 'Select template to Mail Merge:' combobox and click the 'Merge' button.

Label Printing
--------------

### Uso de OpenOffice con Datos de la Aplicación: Impresión de Etiquetas

[Creating Mail Merge Documents From Text/CSV or Spreadsheets](https://openoffice.blogs.com/openoffice/2007/01/mail_merge_in_o.html)

Son cuatro pasos:

1. Obtener los datos en formato CSV u Hoja de Cálculo
2. Convertir los datos en una base de datos de OpenOffice
3. Crear un documento de etiquetas, carta o sobre y rellenarla con los campos que queremos
4. Imprimir, posiblemente seleccionando los registros que queremos incluir

[plugin:youtube](https://youtu.be/mM5dsPDt6ig)

Esta plantilla se compartió en el grupo de LinkedIn hace tiempo y es un ejemplo real de uso para impresión de sobres:

[Plantilla de impresión directa de sobres C4.](c4envelope-template.odt)

Translation
-----------

In file: modules/Settings/language/xx\_yy.lang.php, cange line
```

    'LBL_DOC_MSWORD'=>'File has to be a Document of type doc/msword',
```
to
```
    'LBL_DOC_MSWORD'=>'File has to be a Document of type doc/msword, or OpenOffice/odt or Rich Text Format/rtf',
```
In file: include/language/xx\_yy.lang.php, add line:
```
    'DownloadMergeFile'=>'Download merged document'
```
<div class="notices red"> <strong>THIS IS IMPORTANT</strong> if you
don't add the translation string to your language file you will not be
able to download the file.</div>

History
-------
**[Joe] Installed by default in coreBOS <br>**
**[Joe] Version 5.4.0 Updated for compatibility with vtiger 5.4.0<br>**
**[Joe] Version 5.3.0 Updated for compatibility with vtiger 5.3.0<br>**
**The multiline address field support has been added by Peter A. Gebhardt (casati)<br>**
**Version 5.2.1 Updated for compatibility with vtiger 5.2.1<br>**
**The fix for the html special chars has been provided by xweber on the vtiger forums.<br>**
**The code for the utf8 escape sequences in rtf files has been taken from <br>**
**[https://sourceforge.net/projects/phprtf/](https://sourceforge.net/projects/phprtf/)<br>**
**Version 5.1.0 Fixes problems with html special chars &,<,>,... for OpenOffice documents and supports utf8 chars in rtf documents.<br>**
**This extension was born from a forum thread which had code for 4.2, JPL TSolucio, S.L. (Joe Bordes) ported it and maintains it with the <br>Help of StudioSynthesis and other community members. Special mention to Peter A. Gebhardt (casati) who helped in the upgrade to 5.3.0**