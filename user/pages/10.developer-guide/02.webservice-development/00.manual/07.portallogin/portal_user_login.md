---
title: 'Portal user login'
metadata:
    description: 'Permitting our clients or employees to access information in the application and even manage certain parts of that information.'
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
        - login
---

A common use case for coreBOS is to permit our clients or employees to access information in the application and even manage certain parts of that information. This is what we call a **Customer Portal** application or, simply **external applications** because there are so many possible use cases.

The most typical scenario is for clients to be able to access some application where they can create issues (Support Tickets) about our service.

===

Other use cases are:

- client access to their invoices
- client can create purchases (although this is usually better through an e-commerce integration)
- employees can access their monthly salaries
- employees can access protocols and documentation
- employees can manage projects and project tasks
- employees can add time control records

the list of functionality goes on.

These are just some examples of external applications. In some cases, we can use ONE normal coreBOS user to access the information. The idea would be that we create a login page where we validate our client/employee using the **authenticateContact** endpoint, we access coreBOS using a normal user, then we restrict all the queries and operations based on the contact that has logged in.

The profile of the authenticateContact endpoint looks like this:

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Validate a contact in a coreBOS install</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>authenticateContact(email:String, password:String):LoginResult</td>
</tr>
<tr>
<td>Send Type:</td>
<td>POST</td>
</tr>
<tr>
<td>Parameters:</td>
<td>email: the registered email of an active contact in coreBOS<br />
password: internal password set when activating the contact for portal access</td>
</tr>
<tr>
<td>Returns:</td>
<td>LoginResult can be the contact web service ID if access is granted or false if not granted</td>
</tr>
<tr>
<td>URL Format:</td>
<td><code>http://corebos_url/webservice.php?operation=authenticateContact&amp;email=[email]&amp;password=[password]</code></td>
</tr>
<tr>
<td>Comments:</td>
<td style="color:red;"> This method is deprecated and should not be used anymore.</td>
</tr>
</tbody>
</table>



The problem with this approach is security.

Most importantly we are sending the password in clear, which shouldn't
be done, but we are also saving it in the backend in clear. This alone
is enough reason to stop using this approach.

Additionally, we are using a normal coreBOS user to access the
information. Even though we validate the contact independently of the
coreBOS user, we still have to login again with the coreBOS user,
normally hard-coding that users' access key in the code. Since we log in
with a coreBOS user, the permission system is in effect, but this user
has to have, at least, access to the information that ALL the contacts
need to access. For example, no matter what contact logs in, we are
using the same coreBOS user, that must have access to all the tickets in
the system. The external application code will filter the tickets based
on the logged in Contact, but the user has access to all the
information. If the contact using the application finds a way to execute
a query without restrictions they will be able to access the information
of other contacts.

This is a serious issue in the javascript world. A react or vuejs
application sends all the code to the browser where the contact will be
able to manipulate and override whatever they want.

This is where the **Portal User Login** comes to play. This
functionality implements a two step login process identical to the
normal coreBOS login process. We first make a call to
[getchallenge](../../07.login) with the contact
email, then we calculate a hash of the password with the token and send
that to finish the login.

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Validate a contact or employee access in the web service interface. The use of the getchallenge token is required</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>loginPortal(username:String, password:String, entity:String):LoginResult</td>
</tr>
<tr>
<td>Send Type:</td>
<td>GET</td>
</tr>
<tr>
<td>Parameters:</td>
<td>username: email of the active Contact or Employee that needs access<br/>
password: [selected_hash_method](token+password)<br/>
entity:Contacts or Employee</td>
</tr>
<tr>
<td>Returns:</td>
<td>A LoginResult object with the session identifier and some additional information<code>LoginResult{
sessionName:String //unique session identifier
user_name:String //coreBOS user webserivce ID related to this contact
contactid:String //contact/employee webservice ID
language:String //preferred language of the contact/employee
}</code></td>
</tr>
<tr>
<td>URL Format:</td>
<td><code>http://corebos_url/webservice.php?operation=loginPortal&amp;username=[username]&amp;password=[hashed password]&amp;entity=[entity type]</code></td>
</tr>
<tr>
<td>Comments:</td>
<td>The login information is all managed on the Customer Portal Information block in each contact/employee</td>
</tr>
</tbody>
</table>


This way we do not send the password around in plain text and the portal
application does not have a hard-coded coreBOS user and access key.
Besides that, each contact can have a different user assigned so we
could make modules private and assign the records to the users in
coreBOS to get some extent of security even if the portal application
user sends an unrestricted query (which, again, is extremely easy in
javascript). coreBOS comes to the rescue in this case also as we will
see below.

For the loginPortal endpoint to work we have to activate the
functionality in our coreBOS as, by default, it is not active. In the
coreBOS Updater you will find a blocked changeset named
**activatePortalFieldsContacts**, unblock and apply it. You should now
see this field block and detail view widget in the contacts records.

![](portalloginfields.png?width=100%)


As you can see we can define

-   if the contact has access or not
-   From-To dates the access is valid
-   the preferred language
-   the password hashing method
-   the coreBOS User that will be used when this contact logs in
-   additionally, using the detail view widget, we can:
    -   see if the contact has a password set or not
    -   set a password
    -   delete the password

This will permit us to manage the access as required

<div class="notices blue">
The same functionality will be
present in the Employees module if it is installed.</div>

One of the nice parts of this functionality is that we can associate
each Contact to one coreBOS user, this makes it easy to assign certain
administrative Contacts with a user that has more privileges. It also
permits us to have a lot fewer coreBOS users as most of the Contacts are
going to have the same permission and privilege settings.

But the real security benefit of the Portal Login is the native
information restrictions that will be imposed automatically.

The portal login returns a session name and a user. To all effects, it
will be as if the user selected in the contacts' record had logged in
and the permissions assigned to that user will take effect, but coreBOS
will mark the login as a special portal login, not just a normal user
login and it will apply restrictions on the information available.

For example, if a Contact is associated with UserX, who has access to
the tickets module and can see all the tickets of all contacts when the
external application logs in with the contact and launches a query to
retrieve a list of tickets:

    select * from HelpDesk;

coreBOS will know that this is a Portal Login and will add the condition
to filter on the tickets of the contact automatically

    select * from HelpDesk where parentid={Contact} or parentid={Contact.Account};

This will happen inside coreBOS, so we will be protected even in
javascript applications

Similar to the query example, restrictions will be imposed when doing
any other type of operation. For example, trying to Retrieve or Update a
record that the contact should not have access to, like trying to update
a Contact from another company, even though the coreBOS user associated
with the Contact may have permission to do so, the Contact doesn't so
the operation will be denied.

These Customer Portal Restrictions are a lifesaver.

TLDR;
-----

-   unblock and apply activatePortalFieldsContacts updater changeset
-   create a coreBOS user and define permissions to access from your
    external application
-   edit Contact you want to give access and set the Customer Portal
    fields
-   set the password for the contact using the detail view widget
-   use loginPortal endpoint to login using the Contacts' email and
    password you set
-   Customer Portal Restrictions will be imposed automatically so
    implement as you normally would


### sendRecoverPassword

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Send</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>sendRecoverPassword(username:String):Status</td>
</tr>
<tr>
<td>Send Type:</td>
<td>POST</td>
</tr>
<tr>
<td>Parameters:</td>
<td>email: the registered email of an active contact in coreBOS</td>
</tr>
<tr>
<td>Returns:</td>
<td>Status will be 0 if the email could be sent or non-zero if it couldn't be sent</td>
</tr>
<tr>
<td>URL Format:</td>
<td><code>http://corebos_url/webservice.php?operation=sendRecoverPassword&amp;username=[email]</code></td>
</tr>
<tr>
<td>Comments:</td>
<td style="color:red;"> This method is deprecated and should not be used anymore.</td>
</tr>
</tbody>
</table>
<br>

<div class="notices red">
We still do not have a valid substitute for this operation. We need to implement a "Recover Password" functionality.</div>

<br>
------------------------------------------------------------------------

[Next](../../00.manual/06.session)| Chapter 14: Extend Session and Logout.

------------------------------------------------------------------------

