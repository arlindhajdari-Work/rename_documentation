---
title: 'Design your login page'
metadata:
    description: 'Design your login page'
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
        - aplication
    tag:
        - login
---

The login page is one the most modified parts of the application code, producing conflicts when we want to modify it, so we decided to implement a way for each implementor/developer to define their own page layout and switch easily from one to another. As of January 2018, you can now setup your own Login page without having to modify the coreBOS base code.

A login page must have a few minimum requirements

- it must have a **unique name template** saved in a directory of the same name inside **Smarty/templates/Login**, for example Smarty/templates/Login/yourpage.tpl
- it must contain a form with its' action set to **index.php**
- the form must have these hidden fields

```html
<input type="hidden" name="module" value="Users" />
<input type="hidden" name="action" value="Authenticate" />
<input type="hidden" name="return_module" value="Users" />
<input type="hidden" name="return_action" value="Login" />
```

- the form must have an input field for the user name called **user\_name**
- the form must have an input field or the user password called **user\_password**

The layout gives you control inside the head section of the HTML page. The application will output the initial HTML page directives, the default charset, the favicon, and the title and then give you control. So you can load your stylesheets, scripts or whatever you need. Then continue with the body where you can use smarty template syntax to access some application variables and set out any layout you wish.

Finally, the application will close the HTML body and page for you.

Optionally, you may use some javascript code to set focus on the login fields and detect if CapsLock is active which is also loaded by the initial header code.

It is recommended that you put the next piece of code where you would like to show login errors to the user and set the styling you want to the errorMessage class:

```xml
{if $LOGIN_ERROR neq ''}
<div class="errorMessage">{$LOGIN_ERROR}</div>
{/if}
```

By convention, the resources used by your page should be saved inside the themes/login/yourpage directory but since you have full control of what you load you can actually access whatever you need.

Additionally, you must implement a two-factor authentication login page for those users who have this feature activated. This is basically the same page you have already created with some additional changes:

- another hidden input field like this:

```html
<input type="hidden" name="twofauserauth" value="{$authuserid}" />
```

- you must fill in the **user\_name** field with the Smarty variable **$uname**. I usually make this field read-only
- the password field is not required
- a field to capture the authentication code called **user\_2facode** which is where the user must introduce the code they have received
- you should also add a link to get a new code unless you are using the Google Code Generation application:

```html
<a href="javascript:sendnew2facode({$authuserid});">{'LBL_2FAGETCODE'|getTranslatedString:'Users'}
```

The two factor authentication page must also live inside the Smarty/templates/Login/ directory and have the same name as your login page ended in **2fa**, that would be **yourpage2fa** in the example we are using here.

The last step is to set the new login page as the one to use. Currently this is done setting the **$cbodLoginPage** variable in **modules/Settings/configod.php** file.

The best way to understand all the above is studying the existing login layouts and discussing your doubts with us in the forum or gitter live chat.

## Login Page Customisation

Starting from 11th December 2023 we added a feature to choose the login template using the "Login Template" picklist / dropdown found in the cbCompany module. By choosing the template from that field the login page will change accordingly.

After you create your new login template you will need to add its name to the "Login Template" picklist using the changeset.

The changeset can be in this format;

```php
class addMyCustomLoginTemplate extends cbupdaterWorker {

	public function applyChange() {
		if ($this->hasError()) {
			$this->sendError();
		}
		if ($this->isApplied()) {
			$this->sendMsg('Changeset ' . get_class($this) . ' already applied!');
		} else {
			$module = Vtiger_Module::getInstance('cbCompany');
			$field = Vtiger_Field::getInstance('login_template', $module);
			if ($field) {
                // $template_name - should hold the value of your new login template,
                // incase you created: MyCustomLogin.tpl and MyCustomLogin2fa.tpl
                // then the template_name should be 'MyCustomLogin'
                // i.e. only the actual template will be used and not the one with 2fa
                // and the name should be without .tpl
                $template_name = 'MyCustomLogin';
				$field->setPicklistValues(array($template_name));
			}
			$this->sendMsg('Changeset ' . get_class($this) . ' applied!');
			$this->markApplied(false);
		}
		$this->finishExecution();
	}
}
```

Don't hesitate to share your designs with the community!!

Here you have some ideas in case you need inspiration:

- [50 Free HTML5 And CSS3 Login Forms](https://colorlib.com/wp/html5-and-css3-login-forms/)
- [20 Beautiful Login Page/Form Designs](https://cssauthor.com/20-beautiful-login-pageform-designs-inspiration/)
- [10 Awesome Login Screen Ideas](https://www.rolustech.com/blog/sugarcrm-login-screen-customization-10-awesome-login-screen-ideas/)
