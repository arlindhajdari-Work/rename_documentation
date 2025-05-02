---
title: 'Javascript Debugging'
metadata:
    description: 'Javascript Debugging'
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
    tag:
        - debug.log
---

Due to the popularity of javascript and it's importance inside web applications (coreBOS), as of June 2018 coreBOS has added functionality to be able to log messages that happen in your javascript code to the backend logging system.

===

to get this to work we must:

- load the coreBOS webservice library in order to make web services calls
- load the logging javascript library. This can be done by adding this code to your project:

<!-- -->

    <script type="text/javascript" src="include/Webservices/WSClientp.js"></script>
    <script>
    var cbws=new cbWSClient('http://localhost/coreBOSwork');
    cbws.extendSession();
    </script>
    <script type="module" src="include/js/loadjslog.js"></script>

Once that code has been included we will have a logging object at our
service that is called **jslog** and has this interface:

### jslog(connection, level, message)

    jslog(cbws, 'fatal', 'message to log');

-   **level** can be: fatal, trace, error, warn, debug, info
-   **message** can be any string, if that string is convertable to a
    JSON object it will be converted before logging

### Helper methods

-   jslog.fatal(connection, message)
-   jslog.trace(connection, message)
-   jslog.error(connection, message)
-   jslog.warn(connection, message)
-   jslog.debug(connection, message)
-   jslog.info(connection, message)

### Browser console

Additionally you can configure jslog to send the same message it is
sending to the backend also to the browser console by setting the
jslog2console variable like this:

    jslog.jslog2console = true;

### Deactivate logging

In certain situations it could be useful to keep the logging messages
around while we are tacking down some hard to find bug but we want to
deactivate them temporarily. **jslog** has a settings option for this
called **active**

    jslog.active = false;

### Examples

    jslog.fatal(cbws, JSON.stringify({'var1':'kdkdkd','var2':'llll'}));
    jslog.debug(cbws, "{'var1':'kdkdkd','var2llll'}");
    jslog.jslog2console=true;
    jslog(cbws, 'info', "this message will appear in the console also!");

### Destination log file

The messages sent to the backend will appear in the file
**logs/javascript.log** and you must have the [log4php.properties settings file configured correctly](../04.debuging) as well as
the $LOG4PHP\_DEBUG = true; variable.
