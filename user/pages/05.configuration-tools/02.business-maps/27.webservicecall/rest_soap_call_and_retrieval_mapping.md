---
title: 'REST/SOAP call and retrieval Mapping'
metadata:
    description: 'Learn how to call external applications using the workflow system to get or send information.'
    author: 'Joe Bordes'
content:
    items: '@self.children'
    limit: '5'
    order:
        by: date
        dir: desc
    pagination: '1'
    url_taxonomy_filters: '1'
taxonomy:
    category:
        - businessmappings
        - adminmanual
    tag:
        - webservicecall
---

This workflow task type, named "**Run Web Service**" can be used to launch a REST or SOAP call to another system and retrieve the results to be saved in fields of coreBOS or to be passed along the workflow set of tasks to be consumed in other workflow tasks by using the **getContext** function.

===

To use this task type we need a map of type **Webservice Mapping**. This map must be selected in the workflow task.

![](1.png?width=100%)

In the task, we can attach just one map which can be selected using the input field.

![](2.png?width=100%)
![](3.png?width=100%)

The "**Web Service Mapping**" defines the web service method parameters that will be launched and is divided into three sections:

- **wsconfig** where we define the necessary settings to make the call
- **fields** which define the parameters of the call and will permit us to capture values from the coreBOS application
- **Response**

### wsconfig

- &lt;wsurl&gt;Endpoint where we send the data&lt;/wsurl&gt;
- &lt;wshttpmethod&gt;GET, PUT, POST, DELETE&lt;/wshttpmethod&gt;
- &lt;methodname&gt;define the method that should be called&lt;/methodname&gt;
- wsuser and wspass in case the service uses these
- wsheader contain keyname and keyvalue pairs with information that must be sent in the header of the call
  - header keyvalue will be processed in search of the command **getContext(variable_name)** or **getSetting(variable_name)** (note that there are no quotes around the variable name). This expression will search for the variable_name in the workflow context or the coreBOS key-value store and use that instead of the hardcoded value which can be set here also.
- &lt;wstype&gt;REST or SOAP&lt;/wstype&gt;
- &lt;inputtype&gt;XML/URL/JSON/URLRESTFUL&lt;/inputtype&gt;
- &lt;outputtype&gt;JSON or XML&lt;/outputtype&gt;

Most of the directives are self-explanatory but there are a few that
need to be explained due to the process they have related.

The **INPUTTYPE** defines how we will send the parameters (fields) to
the end-point:

- XML and JSON will be set in the body of the call. The XML value will be URL-encoded
- URL will have the values added in the URL as GET parameters
- URLRESTFUL will search the wsurl directive for variables defined in the fields section preceded with a dollar sign. If they are present they will be substituted by the calculated value.

If the **OUTPUTTYPE** is JSON two additional tasks are performed:

- if the Response section has a "field" value for the response then we will save the value received from the call in the indicated field
- all the Response values received will be put into the workflow context. If no name is given in the Response section for the variable in the context the application will use the name of the variable returned preceded by the text **wsctx_**

### fields

- &lt;fields&gt;block that contains the input parameter fields&lt;/fields&gt;
- &lt;fieldname&gt;input parameter for REST/SOAP call&lt;/fieldname&gt;
- &lt;OrgfieldName&gt;fieldname in coreBOS where we get the input parameter value&lt;/OrgfieldName&gt;

this section is processed by the same engine that is used in the [Field Mapping Business Map](../18.mapping) so we can use all the options that we have there like Expressions and Rules

### Response

- &lt;Response&gt; block that contains the response fields coming from the call and where we have to save the values &lt;/Response&gt;
- &lt;fieldname&gt; the value we get back from web service call &lt;/fieldname&gt;
- &lt;destination&gt;&lt;field&gt; fieldname in coreBOS to update with the WS response &lt;/field&gt;&lt;/destination&gt; this directive is optional. If it is not given or is set to an empty value, the field will not be updated.
- &lt;destination&gt;&lt;context&gt; the name to use to set this value in the workflow context &lt;/context&gt;&lt;/destination&gt; if none is given we will use **wsctx_{fieldname}**

### Examples

#### An example of Map for SOAP Call:

```xml
<map>
    <originmodule>
    <originname>Accounts</originname>
    </originmodule>
     
    <wsconfig>
    <wsurl>http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl</wsurl>
    <wshttpmethod>POST</wshttpmethod>
    <methodname>checkVat</methodname>
    <wsresponsetime></wsresponsetime>
    <wsuser></wsuser>
    <wspass></wspass>
    <wsproxyhost></wsproxyhost>
    <wsproxyport></wsproxyport>
    <wsheader>
    <header> 
    <keyname>Content-type</keyname> 
    <keyvalue>application/json</keyvalue> 
    </header>
    </wsheader>
    <wstype>SOAP</wstype>
    <inputtype>JSON</inputtype>
    <outputtype>JSON</outputtype> 
    </wsconfig>
     
    <fields>
    <field>
    <fieldname>countryCode</fieldname>
    <Orgfields>
    <Orgfield>
    <OrgfieldName>bill_code</OrgfieldName>
    <OrgfieldID></OrgfieldID>
    </Orgfield>
    <delimiter></delimiter>
    </Orgfields>
    </field>
    <field>
    <fieldname>vatNumber</fieldname>
    <Orgfields>
    <Orgfield>
    <OrgfieldName>siccode</OrgfieldName>
    <OrgfieldID></OrgfieldID>
    </Orgfield>
    <delimiter></delimiter>
    </Orgfields>
    </field>
    </fields>
     
    <Response>
    <field>
    <fieldname>valid</fieldname>
    <destination>
    <field>tickersymbol</field>
    </destination>
    </field>
    <field>
    <fieldname>requestDate</fieldname>
    <destination>
    <field>ownership</field>
    </destination>
    </field>
    </Response>
</map>
```

#### An example of Map for REST Call:

```xml
<map>
    <originmodule>
    <originname>Accounts</originname>
    </originmodule>
     
    <wsconfig>
    <wsurl>http://localhost/facturascripts/api/3/divisas/$coddivisa</wsurl>
    <wshttpmethod>GET</wshttpmethod>
    <methodname>divisas</methodname>
    <wsresponsetime></wsresponsetime>
    <wsuser></wsuser>
    <wspass></wspass>
    <wsheader>
    <header> 
    <keyname>Content-type</keyname> 
    <keyvalue>application/json</keyvalue> 
    </header>
    <header> 
    <keyname>token</keyname> 
    <keyvalue>0WXmP4nVDIGNHKysuceA</keyvalue> 
    </header>
    </wsheader>
    <wstype>REST</wstype>
    <inputtype>URLRESTFUL</inputtype>
    <outputtype>JSON</outputtype> 
    </wsconfig>
     
    <fields>
    <field>
    <fieldname>coddivisa</fieldname>
    <Orgfields>
    <Orgfield>
    <OrgfieldName>tickersymbol</OrgfieldName>
    <OrgfieldID></OrgfieldID>
    </Orgfield>
    <delimiter></delimiter>
    </Orgfields>
    </field>
    </fields>
     
    <Response>
    <field>
    <fieldname>descripcion</fieldname>
    <destination>
    <field>ownership</field>
    </destination>
    </field>
    </Response>
</map>
```

Note how the $coddivisa variable in the URL `http://localhost/facturascripts/api/3/divisas/$coddivisa` will be substituted by the actual value that we have in coreBOS as defined in the fields section. In this case, the value of the tickersymbol field in the Account will be read and $coddivisa will be substituted with that value.

#### An example of two tasks passing context

This first map executes an authentication call and loads the authorization token into the workflow context and the second task uses that value to make an operation call.

```xml
<map>
    <originmodule>
    <originname>Accounts</originname>
    </originmodule>

    <wsconfig>
    <wsurl><![CDATA[http://localhost/corebostsolucio/webservice.php?operation=testcontext&id=2355]]></wsurl>
    <wshttpmethod>GET</wshttpmethod>
    <methodname>wslogin</methodname>
    <wsresponsetime></wsresponsetime>
    <wsuser></wsuser>
    <wspass></wspass>
    <wsheader>
    <header>
    <keyname>Content-type</keyname>
    <keyvalue>application/json</keyvalue>
    </header>
    <header>
    <keyname>Authorization</keyname>
    <keyvalue>9192929383834</keyvalue>
    </header>
    </wsheader>
    <wstype>REST</wstype>
    <inputtype>JSON</inputtype>
    <outputtype>JSON</outputtype>
    </wsconfig>

    <fields>
    </fields>

    <Response>
    <field>
    <fieldname>result</fieldname>
    <destination>
    <context>token</context>
    </destination>
    </field>
    </Response>
</map>
```

```xml
<map>
    <originmodule>
    <originname>Accounts</originname>
    </originmodule>

    <wsconfig>
    <wsurl>http://localhost/corebostsolucio/webservice.php?operation=testcontext2</wsurl>
    <wshttpmethod>POST</wshttpmethod>
    <methodname>wspost</methodname>
    <wsresponsetime></wsresponsetime>
    <wsuser></wsuser>
    <wspass></wspass>
    <wsheader>
    <header>
    <keyname>Content-type</keyname>
    <keyvalue>application/json</keyvalue>
    </header>
    <header>
    <keyname>Authorization</keyname>
    <keyvalue>getContext(token)</keyvalue>
    </header>
    </wsheader>
    <wstype>REST</wstype>
    <inputtype>JSON</inputtype>
    <outputtype>JSON</outputtype>
    </wsconfig>

    <fields>
    <field>
    <fieldname>token</fieldname>
    <Orgfields>
    <Orgfield>
    <OrgfieldName>accountname</OrgfieldName>
    <OrgfieldID></OrgfieldID>
    </Orgfield>
    <delimiter></delimiter>
    </Orgfields>
    </field>
    </fields>

    <Response>
    <field>
    <fieldname>description</fieldname>
    <destination>
    <field>accountname</field>
    </destination>
    </field>
    </Response>
</map>
```

### Utilizing getGlobalVariable, getContext, and getSetting
You have the flexibility to employ the functions `getGlobalVariable`, `getContext`, and `getSetting` within both the wsurl property and the headers of your application.

For instance, to incorporate a GlobalVariable, the following format can be used:
```xml
<wsurl>getGlobalVariable(HOST_GV_EXAMPLE)/corebostsolucio/webservice.php?operation=testcontext2</wsurl>
```

Similarly, for a getContext function, the syntax is as follows:
```xml
<wsurl>getContext(HOST_CONTEXT_EXAMPLE)/corebostsolucio/webservice.php?operation=testcontext2</wsurl>
```

To specify a getSetting function, you can use the following pattern:
```xml
<wsurl>getSetting(HOST_SETTING_EXAMPLE)/corebostsolucio/webservice.php?operation=testcontext2</wsurl>
```

### Related Articles

- [Run Web Service Workflow Task](https://blog.corebos.org/blog/runwswftask)
- [Run Web Service Workflow Task Change](https://blog.corebos.org/blog/runwswftaskchange)

<br>
------------------------------------------------------------------------

[Next](../02.application-menu ) | Chapter 22: Application Menu.

------------------------------------------------------------------------