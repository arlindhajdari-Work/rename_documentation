---
title: 'How to Configure Outgoing Server for GMail'
metadata:
    description: 'Configuration of Outgoing Server for GMail.'
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
        - adminmanual
    tag:
        - email
        - outgoing
        - outgoingserver
        - gmail
        - google
---

## Envio de correos desde coreBOS utilizando una cuenta de Gmail

Para poder utilizar una cuenta de correo de GMail como servidor de correo saliente en coreBOS hay que realizar unas configuraciones en google.

Existen dos posibilidades.

Si tienes activado la autentificación a dos niveles en tu cuenta, tienes que crear una clave de aplicación igual que has hecho para los otros programas como Thunderbird u Outlook.

Si no tienes activado esa opción de seguridad, tienes que activar la opción de acceso de aplicaciones menos seguras como se describe a continuación.

Entra en tu cuenta de Gmail:

![](app_seguras_00.jpg?width=100%)

En la pantalla a la que accedes, has de ir a la opción "Inicio de sesión en Google"

![](app_seguras_01.jpg?width=100%)

En la siguiente pantalla, debes buscar, hacia el final de la página, la opción "Permitir el acceso de aplicaciones menos seguras"

![](app_seguras_02.jpg?width=100%)


Y establecer el valor a **SI**.

![](app_seguras_03.jpg?width=100%)

Con esto ya debería dejar enviar correo desde dentro de tu coreBOS.

### La configuración en coreBOS ha de ser:

- Servidor: smtp.gmail.com
- Usuario: el usuario que uses en gmail, o sea la cuenta de correo
- Contraseña: la contraseña para acceder al correo
- Email de: no es necesario ya que gmail no soporta esta característica
- ¿Requiere autentificación?: Establecerla en TLS

![](app_seguras_04.jpg?width=100%)
