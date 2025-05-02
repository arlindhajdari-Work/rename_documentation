---
title: 'coreBOS Service Worker'
metadata:
    description: 'coreBOS Service Worker'
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
        - serviceworker
    tag:
        - cache
        - worker
---

As of the moment of the creation of this page, we are using version 5.0.0 of Google's Service Worker Workbox functionality in order to permanently cache all the files we can on the client's computer. It is not a full-blown offline service worker as coreBOS depends too much on the backend to work offline. We use it to cache all the elements that we know will not change so that they can be read directly from the user's computer. In this way, we reduce the load on the server and make the application a little faster.

You can get more information on how we implemented this in these links:

- [https://developer.chrome.com/docs/workbox/reference/workbox-build/](https://developer.chrome.com/docs/workbox/reference/workbox-build/)
- [https://developer.chrome.com/docs/workbox/modules/workbox-cli/](https://developer.chrome.com/docs/workbox/modules/workbox-cli/)

## Things you need to know

- for the service worker to update all the files in cache (after an update of your code) you **MUST close all tabs and then reload the page** you are on
- if just one file in the set of cached files cannot be loaded the whole cache is invalidated. This can happen, for example, if you have some AD-Blocking software, so it is recommended that you **put your coreBOS install URL in the whitelist** of that software
- to regenerate the service worker you must install workbox in your server and execute `include/sw-precache/regen_swprecache`
- if you are developing some new features that have to go in javascript files you cannot modify any of the files in the service worker list as your changes will not be picked up by the browser: use hooks. **Do not update the service worker in your project** as it will give you a lot of conflicts (we update it a lot).
- the list of cached files can be found in the service-worker.js file and in the sw-precache-config.js configuration file
- if you really need to make a change in one of those files, talk to us, we will negotiate a way to make that happen
