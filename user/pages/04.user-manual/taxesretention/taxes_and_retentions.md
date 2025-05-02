---
title: 'Taxes and Retentions'
metadata:
    description: 'Configuración Impuestos y Retenciones'
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
        - taxes
        - retentions
        - recargo
        - equivalencia
        - impuestos
---

## Taxes and Retentions

### Taxes

El **recargo de equivalencia** es un impuesto adicional que se puede configurar como cualquier otro impuesto.

Para facilitar la asignación automática de impuestos según productos y/o cuentas hemos creado la extensión de Control avanzado de impuestos: [Advanced Tax Control System](https://blog.corebos.org/blog/advancedtax)

[plugin:youtube](https://youtu.be/nKT8p9Af-Zc)

### Retentions

Las retenciones se tratan como impuestos negativos. Dado que esto ya está soportado por la aplicación no es necesario hacer mucho, solo ir a la sección de impuestos en la configuración y crear el impuesto negativo.

![Impuesto Negativo](impuestoretencion01.png?width=100%)

Después de eso hay que revisar los valores de impuestos en cada factura para asegurarse que se está aplicando los valores correctos.

Dado que el objetivo final de la gestión de impuestos y retenciones es poder obtener las cantidades trimestrales para facilitar nuestras obligaciones fiscales, la aplicación desglosa todos los impuestos aplicados en cada factura en campos individuales en el propio registro, esto permite realizar informes sobre estos campos. Además en la sección de configuración de impuestos se permite distinguir los impuestos propios de las retenciones con la finalidad de totalizar de manera separada cada tipo de impuesto. Estos totales se pueden ver en cada factura, en la sección de "Información Financiera" y podremos realizar informes y/o exportar la información a hojas de cálculo para su presentación a nuestro asesor.

![Impuesto Negativo Factura](impuestoretencion02.png?width=100%)

Con los campos autocalculados que desglosan cada impuesto y los totales debería ser sencillo formatear la salida PDF de cada módulo.