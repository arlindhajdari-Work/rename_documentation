---
title: 'Aplication Information'
metadata:
    description: 'Aplication Information'
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
        - configuration
    tag:
        - howto
        - tutorial
---

- [Emails Sent by the application](01.emailssent)
- [Contacts](02.contacts)
- [Use of OpenOffice with Data inside the Application](03.openoffice_integrations)
- [Webservice Stress Tests](04.rest_stress_tests)