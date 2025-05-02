---
title: Autocomplete
metadata:
    description: 'Autocomplete functionality'
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
        - autocomplete
---

Autocomplete functionality is so typical for a backend that coreBOS had to have this functionality natively. We have two methods that permit us to easily implement this functionality.

===

### Methods

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getFieldAutocomplete</th>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Executes a search in the list of fields of a module for the given term with the selected operator.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>getFieldAutocomplete(term:string, filter:string, searchinmodule:string, fields:string, returnfields:string, limit:number):Map</td>
</tr>
<tr>
<td>Send as:</td>
<td>GET</td>
</tr>
<tr>
<td>Parameters:</td>
<td>=&gt; term: search term<br />
=&gt; filter: operator to use: eq, neq, startswith, endswith, contains<br />
=&gt; searchinmodule: valid module to search in<br />
=&gt; fields: comma-separated list of fields to search in<br />
=&gt; returnfields: comma-separated list of fields to return as result, if empty fields will be returned<br />
=&gt; limit: maximum number of values to return</td>
</tr>
<tr>
<td>Response:</td>
<td>Map of records found, indexed by their CRMID with the value of a Map of the returnfields fields</td>
</tr>
<tr>
<td>Example:</td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/334_getFieldAutocomplete.php">Developer Tool</a></td>
</tr>
</tbody>
</table>

<br>
<br>


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>getReferenceAutocomplete</th>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>Executes a search in the entity fields of the given modules for the given term with the selected operator.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>getReferenceAutocomplete(term:string, filter:string, searchinmodules:string, limit:number):Map</td>
</tr>
<tr>
<td>Send as:</td>
<td>GET</td>
</tr>
<tr>
<td>Parameters:</td>
<td>=&gt; term: search term<br />
=&gt; filter: operator to use: eq, neq, startswith, endswith, contains<br />
=&gt; searchinmodules: comma-separated list of modules to search in<br />
=&gt; limit: maximum number of values to return</td>
</tr>
<tr>
<td>Response:</td>
<td>Array of records found with three values for each one:<br />
=&gt; crmid: ID of the record<br />
=&gt; crmname: entity name of the module followed by the module name<br />
=&gt; crmmodule: module the record belongs to</td>
</tr>
<tr>
<td>Example:</td>
<td><a href="https://github.com/tsolucio/coreBOSwsDevelopment/blob/master/testcode/334_getReferenceAutocomplete.php">Developer Tool</a></td>
</tr>
</tbody>
</table>

<br>

### Autocomplete Example

This section explains how to implement an autocomplete dropdown and
selection UI using the coreBOS web service API.

Let’s go over the important points of the next code which implements the
autocomplete
```php
    <html>
    <head>
        <script src="include/Webservices/WSClientp.js"></script>
        <script>
            var uname = 'admin';
            var akey = 'cdYTBpiMR9RfGgO';
            var cburl = 'http://localhost/coreBOSTest';
            var cbconn = new cbWSClient(cburl);
            var charCount = 0;
        </script>
        <link rel="stylesheet" href="include/LD/assets/styles/salesforce-lightning-design-system.css" type="text/css" />
    </head>
    <body>
    <div class="slds-form-element">
        <label class="slds-form-element__label" for="combobox-id-1">Relate to</label>
        <div class="slds-form-element__control">
        <div class="slds-combobox_container">
        <div class="slds-combobox slds-dropdown-trigger slds-dropdown-trigger_click" aria-expanded="false" aria-haspopup="listbox" role="combobox">
        <div class="slds-combobox__form-element slds-input-has-icon slds-input-has-icon_right" role="none">
        <input type="text" class="slds-input slds-combobox__input" id="combobox-id-1" aria-autocomplete="list" aria-controls="listbox-id-1" autoComplete="off" role="textbox" placeholder="Search..." onkeyup="charCount = this.value.length;if (charCount>3) { doSearch(this.value); }" />
        <span class="slds-icon_container slds-icon-utility-search slds-input__icon slds-input__icon_right">
        <svg class="slds-icon slds-icon slds-icon_x-small slds-icon-text-default" aria-hidden="true">
        <use xlink:href="include/LD/assets/icons/utility-sprite/svg/symbols.svg#search"></use>
        </svg>
        </span>
        </div>
        <div id="listbox-id" class="slds-dropdown slds-dropdown_length-with-icon-7 slds-dropdown_fluid" role="listbox" style="display:block;">
            <ul class="slds-listbox slds-listbox_vertical" role="presentation" id="ulfillin"></ul>
        </div>
        </div>
        </div>
        </div>
    </div>
    <script>
    cbconn.doLogin(uname, akey, false).then((info) => {
        console.log(info);
    });

    function recordTemplate(record) {
        var image = 'account';
        if (record.crmmodule=='Contacts') {
            image = 'contact';
        }
        return `
        <li id="${record.crmid}" role="presentation" class="slds-listbox__item">
            <div class="slds-media slds-listbox__option slds-listbox__option_entity slds-listbox__option_has-meta" role="option">
            <span class="slds-media__figure slds-listbox__option-icon">
            <span class="slds-icon_container slds-icon-standard-account">
            <svg class="slds-icon slds-icon_small" aria-hidden="true">
            <use xlink:href="include/LD/assets/icons/standard-sprite/svg/symbols.svg#${image}"></use>
            </svg>
            </span>
            </span>
            <span class="slds-media__body">
            <span class="slds-listbox__option-text slds-listbox__option-text_entity">${record.crmname}</span>
            </span>
            </div>
        </li>`;
    }

    function getRecords(term) {
        //////////////
        let params = {
            'term': term,
            'filter': 'contains',  // 'eq', 'neq', 'startswith', 'endswith', 'contains'
            'searchinmodules': 'Accounts,Contacts',
            'limit': '10'
        };
        return cbconn.doInvoke('getReferenceAutocomplete', params, 'GET') 
    }

    function doSearch(term) {
        getRecords(term).then(res => {
            console.log(res);
            var elements = '';
            res.forEach(info => elements += recordTemplate(info));
            document.getElementById('ulfillin').innerHTML = elements;
        });
    }
    </script>
    </body>
    </html>
```
1. We load the javascript promise based library, create the necessary HTML and connect to our coreBOS from line 1 to line 37.
2. recordTemplate is just to fill in the drop-down with the values returned from the call
3. getRecords is the operative function that sends the search term to coreBOS method **getReferenceAutocomplete** with the correct parameters to search in the Accounts and Contacts module.
4. doSearch triggers when the user types in the characters, makes the call and loads the results

<br>
------------------------------------------------------------------------

[Next](../../06.getrelatedcontrols)| Chapter 11: get Related Records method.

------------------------------------------------------------------------