---
title: 'Integration with Sabre/DAV WebDAV'
metadata:
    description: 'WebDAV stands for Web Distributed Authoring and Versioning, which is an extension to HTTP that lets clients edit remote content on the web.'
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
        - webdav 
---

<strong>[Wikipedia Definition](https://en.wikipedia.org/wiki/WebDAV) </strong>

<strong>[Blog Post Presentation](https://blog.corebos.org/blog/webdav) </strong>

### Configuration

- Activate Rewrite module in apache web server. Note, this integration does not work without Apache.
- Activate the service by setting the **WEBDAV\_Enabled** global variable to 1 for those users that you want to give access to.
- They will have to access the URL: <https://your_server/your_corebos/webdav>
- They will have to use their username and access key to be granted access
- Enjoy

### Mount Filesystem command

    sudo mount.davfs http://localhost/coreBOSTest/webdav webdav -o rw,uid=joe

------------------------------------------------------------------------

[Next](../11.whatsapp) | Chapter 11: Twilio WhatsApp

------------------------------------------------------------------------