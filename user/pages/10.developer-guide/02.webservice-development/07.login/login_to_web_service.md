---
title: 'Login to Web Service'
metadata:
    description: 'Login process to Web Service'
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

## Access to the System

You need a valid coreBOS user to access the webservice. All the operations you can do through the REST interface will be limited by the coreBOS permission system of the connected user.

The REST API does not use the users password to connect. Instead it needs the user's access key which is a unique identifier created for each user that can be found in the user's preferences page.

![](accesskey.png?width=100%)

The login operation establishes a session between the REST client and the coreBOS application, validates the user and returns a session identifier which must be used in all subsequent calls to coreBOS.

This login process is done in two steps, first we ask coreBOS for a challenge sequence and then we use the returned string to encode our access key for the final validation.

## Get Challenge

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>get a challenge string to encode the password for login</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>getchallenge(username:String):GetChallengeResult</td>
</tr>
<tr>
<td><strong>Send Type:</strong></td>
<td>GET</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>username: name of an active and valid user in coreBOS</td>
</tr>
<tr>
<td><strong>Returns:</strong></td>
<td>A GetChallengeResult object with the challenge token and it's time to live<br>
<code>GetChallengeResult{
token:String //challenge string
serverTime:TimeStamp //time on server
expireTime:TimeStamp //expire time of token
}</code></td>
</tr>
<tr>
<td><strong>URL Format:</strong></td>
<td><code>http://corebos_url/webservice.php?operation=getchallenge&amp;username=[username]</code></td>
</tr>
</tbody>
</table>

<br>

## Login

Now that we have the challenge token we can proceed with the login step.
For this we have to send the user name and a verification string. This
verification string can be constructed in two ways:

      *as an md5 encrypted string of the challenge token plus the user's access key
      *as a concatenation of the token string plus the user's password this is insecure and NOT recommended

This operation is executed as POST


<table class="table table-striped">
<tbody>
<tr>
<td><strong>Purpose:</strong></td>
<td>Validate the user's access in the web service interface. The use of the getchallenge token is required</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>login(username:String, accessKey:String):LoginResult</td>
</tr>
<tr>
<td><strong>Send Type:</strong></td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>username: name of the active coreBOS user that needs access<br />
accessKey: [token+password|md5(token+accesskey)]</td>
</tr>
<tr>
<td><strong>Returns:</strong></td>
<td>A LoginResult object with the session identifier and some additional information<code>LoginResult{
sessionId:String //unique session identifier
userId:String //application user webserivce ID
version:String //Webservice interface version
vtigerVersion:String //coreBOS version
}</code></td>
</tr>
<tr>
<td><strong>URL Format:</strong></td>
<td><code>http://corebos_url/webservice.php?operation=login&amp;username=[username]&amp;accessKey=[accessKey]</code></td>
</tr>
<tr>
<td><strong>Comments:</strong></td>
<td>The accessKey parameter is written with a capital 'K'<br />
The user's access key can be found on the user's profile screen inside the application</td>
</tr>
</tbody>
</table>

<br>


## Logout

<table class="table table-striped">
<tbody>
<tr>
<td><strong>Method:</strong></td>
<td>logout</th>
</tr>
<tr>
<td><strong>Purpose:</strong></td>
<td>The logout service eliminates the session information, invalidating any further operations with that session ID. For security reasons this method should be called when the user of the external application finishes his tasks. He should have an option to close the application.</th>
</tr>
<tr>
<td><strong>Profile:</strong></td>
<td>logout(sessionId:string):Map</td>
</tr>
<tr>
<td><strong>Send Type:</strong></td>
<td>POST</td>
</tr>
<tr>
<td><strong>Parameters:</strong></td>
<td>username: name of the active coreBOS user that needs access<br />
accessKey: [token+password|md5(token+accesskey)]</td>
</tr>
<tr>
<td><strong>Returns:</strong></td>
<td>=&gt; sessionId: session ID to invalidate.</td>
</tr>
<tr>
<td><strong>Response:</strong></td>
<td>map with one entry: successfull</td>
</tr>
</tbody>
</table>

<br>

## More Information

-   This method of authentication is called Challenge-Handshake
    Authentication Protocol and it is more secure than a
    username/password authentication. [Read here for more
    information](https://tools.ietf.org/html/rfc1994)
-   [Read here for methods on how to change the user password and/or access key](../08.methodreference)


<br>
------------------------------------------------------------------------

[Next](../09.querylanguage)| Chapter 4:Query language.

------------------------------------------------------------------------