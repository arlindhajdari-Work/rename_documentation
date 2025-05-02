---
title: 'Monitor the health of your coreBOS'
metadata:
    description: 'Monitor the health of your coreBOS.'
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
        - monitor
        - health
        - monitorstatus
---

If you would like to add your coreBOS install into your company's **IT Infrastructure Health Monitoring** system, the **ping** functionality is exactly what you are looking for.

This feature is expressly designed to be called from a tool like [Nagios](https://www.nagios.org/) or [Pandora](https://pandorafms.com/en/) and will execute a set of 10 tests against your coreBOS install. Actually 11 if you consider accessing the script itself as a test.

You must call the URL:

[http://your_server/your_corebos/ping.php](http://your_server/your_corebos/ping.php)

which must be accessible either using a user and password to overcome any apache authentication screen or by [explicitly excluding it](https://github.com/tsolucio/corebos/blob/master/htaccess.txt) from the authentication in the .htaccess file.

The script will return the string

```
OK: basic testing has passed
```
if all tests pass or one of the next error messages depending on the failure detected:

-   NOK: incorrect PHP version
-   NOK: no configuration file
-   NOK: no database configuration
-   NOK: no version file
-   NOK: no version configuration
-   NOK: missing program files: vtlib
-   NOK: version mismatch
-   NOK: could not access database
-   NOK: missing program file: users
-   NOK: missing admin user file