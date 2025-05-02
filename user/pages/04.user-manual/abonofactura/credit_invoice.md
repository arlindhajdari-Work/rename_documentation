---
title: 'Credit Invoice'
metadata:
    description: 'How to make a credit Invoice'
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
        - inventory
    tag:
        - invocie
        - abono
        - credit
---

## Abono Factura

- Añadir un producto ficticio denominado "Abono factura" con precio 0
- Acceder a la factura que hay que abonar
- Pulsar el botón de Duplicar
- Añadir a la referencia " - Abono"
- Cambiar el estado a "Abonada"
- Al pie de la factura seleccionar Ajuste y establecer a "Deducir" con el valor total del abono

![Deducción](clip221.png)

- Editar la primera linea de producto:
  - Seleccionar el producto "Abono factura"
  - Cantidad 1
  - Precio 0
- Eliminar todas las demás líneas

![Lineas](clip225.png?width=100%)

- Guardar e imprimir

Alternativamente, en coreBOS, podemos poner unidades y precios en negativo, así que en vez de eliminar todas las líneas y añadir una deducción, también se puede poner todas las unidades en negativo consiguiendo lo mismo.
