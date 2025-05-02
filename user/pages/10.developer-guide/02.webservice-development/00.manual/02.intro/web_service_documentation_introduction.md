---
title: 'Web service documentation: Introduction'
metadata:
    description: 'Introduction of Web service documentation'
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
        - intro
---

The web service interface in coreBOS is a simple, powerful, and secure **operation oriented** application programming interface (API) to work with entities stored in the application which tries to provide an easier way to integrate with other software systems.

===

To understand this documentation, you should have a basic familiarity with software development, Web services, and the coreBOS application.

In other words, the application has an HTTP based, operational REST protocol (<http://en.wikipedia.org/wiki/Representational_State_Transfer>) API. This software architecture defines a consistent and secure way to access the majority of the information contained in our coreBOS.

**Consistent**, because with a small set of commands we can access all the entities in the system, not only the base modules but also any new modules created following the vtlib rules.

**Secure**, not only because it has implicit user validation, but also because all the web service functions will apply the role and privileges system defined in the application to the information returned by this interface.

The REST protocol is a web-based protocol similar to SOAP but with a more standard and limited set of commands to work with. It defines a small set of commands with which we are supposed to be able to implement all the necessary actions that could be done. In this way, it is much easier to learn than SOAP, which requires different commands for all the operations and easier to maintain the new code on both sides of the communication. Although we diverge from a pure REST interface this idea of web service implementation has extended the official REST definition and added some features that are part of the coreBOS way of working and also given us an easy way to extend it even more if needed.

The REST interface gives us almost direct database access to the information contained in our coreBOS without going through the user interface, making integration with other applications much easier to implement and upgrade as new versions are released. All the REST operations actions are applied immediately, so changes are visible as they occur.

### Generic Information

All the communication in REST is done through the HTTP protocol. Each REST command must be sent using GET or POST. This is NOT interchangeable, so it is important to know how to call each service. Obviously, we will need to have support for a way to execute HTTP calls from our software application to be able to use the web service interface.

To access the web service, all calls are made through http to the script **webservice.php** like this:

```php
    http://your_server/your_corebos/webservice.php?operation=[operation]&sessionName=[sessionname]&[operation parameters]
```

and all responses will be returned through this protocol in the form of **JSON encoded objects**.

The implementation of the REST protocol uses the JSON format to represent the structures of data being interchanged between your external application and coreBOS. This means that we have to encode in JSON format all information sent to the web service and decode all information received.

The response we usually be a JSON object with two fields

- **success**: boolean which indicates if the call was correct or not
- **result**: if success is true this field contains the answer to the call
- **error**: if success is false this field will contain an error response which contains two fields
  - code: a one-word code identifying the error
  - message: a textual description of the error

Some calls, very few, will also return a third field on success, named **moreinfo** which usually contains some piggyback "nice to have" information related to the response but that can be ignored if not needed.

So all responses will fit into one of these response objects:

**Correct call**

```php
    Response {
      success:Boolean=true
      result:Object // whatever information the call must return
    }
```
**Correct call with more information field**

```php
    Response {
      success:Boolean=true
      result:Object // whatever information the call must return
      moreinfo:Object // whatever information additional information the call must return
    }
```
**Incorrect/Error call**

```php
    Response {
      success:Boolean=false
      error:ErrorObject
    }
```

where ErrorObject is

```php
    ErrorObject {
      code:String // error type ID
      message:String // textual description of error
    }
```

The last bit of useful information is that in this implementation, object identifiers for each record in the system are structured as a number, followed by an 'x', followed by another number:

```php
    objectTypeId 'x' objectId   for example 3x22
```

The first number, objectTypeId, uniquely defines the module we are working with. For those of us who know coreBOS internals, this is NOT the module's tabid. You would think that would have been the correct number to use, but for some reason, web service generates an independent unique identifier for each module, and that is the number that must be used here. You can get this number from the [Describe REST service](../../08.methodreference).

The second number is the exact record identifier. This number identifies uniquely the record we want to access, for example, this number distinguishes two different Accounts, or any record in the system from any other. Internally this is the crmid of the record (vtiger\_crmentity.crmid).

<br>
------------------------------------------------------------------------

[Next](../08.ops) | Chapter 2: Operations.

------------------------------------------------------------------------