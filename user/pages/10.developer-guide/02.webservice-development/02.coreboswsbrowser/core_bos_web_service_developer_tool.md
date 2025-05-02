---
title: 'coreBOS Web Service Developer Tool'
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

### Announcement video

[plugin:youtube](https://www.youtube.com/watch?v=PWY9tRcES9o)

Installation
------------

[Code on GitHub](https://github.com/tsolucio/coreBOSwsBrowser)  
Installation is very easy, basically extract the code from
[GitHub](https://github.com/tsolucio/coreBOSwsBrowser) and copy it into
a directory accessible from the web, point your browser to the directory
and you should be ready to go.

Usage
-----

The different parts of the application are:

### Query Launcher

Simply type your query into the text box and click on the execute
button.

### Type List

This is an information page, so simply accessing is enough to get all
available information.

### Test Code for PHP and Javascript

Write your code into the code editor or load a pre-existing script and
edit it. You can click on execute as many times as you need to see the
internals of the executions.

In order to simplify the scripts, there are a set of variables and
functions you have access to in your scripts:

-   URL of the site we logged in with: **$cbURL**
-   Username we logged in with: **$cbUserName**
-   UserID we logged in with: **$cbUserID**
-   Accesskey we logged in with: **$cbAccessKey**
-   SessionID we logged in with: **$cbSessionID**
-   cbwsLibrary connection to coreBOS: **$cbconn**, this is a
    coreboswslibrary object
-   http\_curl connection to coreBOS: **$httpc**, this is a cURL wrapper
-   Obviously any PHP code is valid and supported
-   Finally there is a high level debug function called **debugmsg()**
    which accepts two parameters, a header string which will be printed
    in bold and a variable of any time which will be dumped using the
    PHP print\_r function

#### Adding test code

Just copy the script into the **testcode** directory and it will be
detected automatically.


<br>
------------------------------------------------------------------------

[Next](../../02.webservice-development/14.coreboswswebform )| Chapter 16: coreBOS Webservice Webform.


------------------------------------------------------------------------