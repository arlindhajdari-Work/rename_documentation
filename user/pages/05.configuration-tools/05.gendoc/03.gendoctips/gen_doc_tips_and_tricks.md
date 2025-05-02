---
title: 'GenDoc::Tips and Tricks'
metadata:
    description: 'Tips and Tricks'
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
        - integration
    tag:
        - gendoc

---

### Related Records

[can't get to the related record tree](https://discussions.corebos.org/showthread.php?tid=1615)

### Uso de OpenOffice con Datos de la Aplicación: Impresión de Etiquetas

[Creating Mail Merge Documents From Text/CSV or Spreadsheets](http://openoffice.blogs.com/openoffice/2007/01/mail_merge_in_o.html)

Son cuatro pasos:

- Obtener los datos en formato CSV u Hoja de Cálculo
- Convertir los datos en una base de datos de OpenOffice
- Crear un documento de etiquetas, carta o sobre y rellenarla con los campos que queremos
- Imprimir, posiblemente seleccionando los registros que queremos incluir

[plugin:youtube](https://youtu.be/mM5dsPDt6ig)

Puedes encontrar una plantilla para sobres que se compartió en el grupo de LinkedIn hace tiempo y es un ejemplo real de uso para impresión de sobres (Plantilla de impresión directa de sobres C4).

### Taxes

The product and service lines information of an inventory module is saved in the [Inventory Details](https://blog.corebos.org/blog/inventorydetails) module. So when we want to print one of these modules we will create a `foreach` loop on the related inventory details records.

When the tax grouping is set to `Individual` mode we will have all the tax details for each product/service line in the corresponding inventory detail record, so we will have to print the values from there as we do with the other fields (quantity, for example).

When the tax grouping is set to `Group`, all the individual lines will have the same tax amount and it will also be saved in the financial information block of the master record. So we can either get the value from any line or from the master record itself.

I can imagine that it will be easier to create two separate templates to print individual and grouped tax modes but it may be possible to create just one using the `conditional` directive.

### Tax Percent for Group

When we choose group taxing mode, most of the information we need for the output is set in the financial information block. One of the values that is missing is the **tax percentage**. This information can be calculated in a custom field and then output but it is already present in each of the inventory detail records so we could also get it from three using a construct like this:

```
{foreach InventoryDetails.sequence_no=1}
{InventoryDetails.id_tax1_perc}
{InventoryDetails.id_tax2_perc}
{InventoryDetails.id_tax3_perc}
{InventoryDetails.id_tax4_perc}
{/foreach}
```

This will retrieve only the first inventory line and output the values. Note that all inventory detail lines have the same value because we are in tax grouping mode, not individual.

**See also `Rounding values` below**

### Rounding values

This trick can be applied to any numeric field but it is common when showing tax, discounts and inventory line information:

`{expressionround((sum_taxtotal/pl_net_total)*100, 2)}`

and shows another way of calculating (dynamically) the **tax percentage**.

### Converting Numbers to Text

A typical request is to convert a number into a text string explanation of the number. In other words, convert `123.3` into `One Hundred and Twenty three dot three`. We have a workflow that does this. Actually, we have a translation service in the application that gives various functions among which is this one. So, this brings us two ways of doing this:

1.- Create a custom field and update it using the workflow expression `num2str(amount, 'en')`
2.- Directly use the expression in the template `{expressionnum2str(amount, 'en')}`

The supported translations can be seen in the `cbtranslation/number2string.php` script around line 184.

