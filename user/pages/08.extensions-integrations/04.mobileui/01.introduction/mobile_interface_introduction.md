---
title: 'Mobile Interface Introduction'
metadata:
    description: 'Mobile Interface Introduction'
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
        - mobile
    tag:
        - mobile
---

## 1.- What is CoreBOS Mobile?

It is a **module** created by [CRM-NOW](https://www.crm-now.de/), which has been integrated into coreBOS by default, to support it and add new functionalities.

This module allows us to have a mobile interface to access a large part of the coreBOS data.

===

## 2.- What is it for?

Podremos consultar de forma rápida nuestra agenda, crear eventos, consultar y crear clientes, contactos, oportunidades.

También es una buena herramienta para los técnicos, ya que pueden consultar las incidencias abiertas, añadir el tiempo y material que le dedican a esta, si tienen el módulo de **Control Tiempo Material activo**, y poder cerrar la incidencia con la firma del cliente sobre esta.

We can quickly consult our agenda, create events, consult and create clients, contacts, opportunities.

It is also a good tool for technicians since they can consult the open support requests, add the time and material that they dedicate to it, if they have the module of **Time/Material Control** active, and be able to close the incident, even with the signature of the client.

## 4.- Who can use it?
Any user of coreBOS who needs to consult or manage their agenda, consult customer data, contacts or opportunities.

An ideal profile could be the technical and commercial ones that have to make visits to clients.

## 5.- Since when is it available?
The first version that we integrated from CRM-NOW was on May 10, 2016.

## 6.- A little bit of history
This module already existed before the version of CRM-NOW, the one that came from vtigerCRM was used, but it was not practical to use.

That's why when we learned that **Frank Piepiorra**, from CRM-NOW, had a new version of this module shared with the community and saw that it had a much more pleasant and practical aspect, we decided to integrate it.

We spent some time on this first version to make it work correctly on coreBOS, plus some fixes and small features that we added, but after a few months they released another version, which is the one we started from, that looked better, not only the exterior, but the interior was better structured to be able to maintain it and improve it little by little.

This second version was incorporated on December 2, 2016, with our changes already included and since then we have not stopped supporting it and adding new things, as our clients have been testing it and requesting fixes and functionalities.

## 7.- How can coreBOS Mobile be used?
Very easy. If the URL of our coreBOS is: [http://mi.coreboscrm.com](http://mi.coreboscrm.com/) we should add to the end /Mobile.php so it would look like this: [http://mi.coreboscrm.com/Mobile.php](http://mi.coreboscrm.com/Mobile.php)

We will see a login screen where we can enter our username and password of coreBOS and get to work!

## 8.- How is it configured?
In order to use coreBOS Mobile, you do not need to do anything, but you can configure certain parts.

## Global Variables
We have in the Global Variables module, two variables for the coreBOS Mobile interface.

-   **Mobile_Module_by_default**: Set the default module to show when entering the Mobile module.
-   **Mobile_Related_Modules**: Activate the modules that we want to have related lists. The name of each module must be indicated separated by commas. The default value that exists is: **Contacts, Potentials, HelpDesk, Documents, Timecontrol**. So it is recommended to keep these values ​​and add the new modules you want after these. **For example**: Contacts, Potentials, HelpDesk, Documents, Timecontrol, **Assets**

## Mobile Profile

Another thing we can do from coreBOS is to create a specific profile for when you enter coreBOS Mobile.

The user of coreBOS belongs to a particular role and this role has a profile. If you do not have any Mobile profile, the user will see the same modules and fields in both coreBOS and coreBOS Mobile, but if we want to differentiate this we must add a profile to this role as follows.

We create a profile as always, but the name MUST start with **Mobile** :: in front and then the rest of the profile name, the system already knows that this profile is only used when entering coreBOS Mobile.

![](mui_profile.png?width=100%)

## 8.- How is it used?
## User and password

As in the application, we must authenticate with our username and password.

![](mui_login.png?width=50%)

## Home Page

By default, it shows us the calendar and the events we have for today if there are any.

![](mui_calendar.png?width=50%)

## List View

If we do not want to see the calendar, but show the list of all the events and use the filters as in any module, we just have to move the widget from the top right to **Off**

![](mui_calendarlist.png?width=50%)

## Create New Record
To create a new record, we must press the cross, which we will always see in the list view.

![](mui_logincreate.png?width=10%)

## Detail View

In the detail view we have 3 icons that serve for the following:

![](mui_detailview.png?width=50%)

## Edit View

In the edit view, we enter the data we need and to save we must press the following icon.

![](mui_editview.png?width=50%)

## Search Related Records

A difference we have with coreBOS is in the fields of type relationship, instead of opening a new window, we have the functionality of autocomplete. As we write, we will suggest options to select.

![](mui_search.png?width=50%)

## Menu
If we open the menu we can navigate through the different modules, quick create, global search, and log out.

![](mui_menu.png?width=50%)

[plugin:youtube](https://youtu.be/ArXcdomoJ10)