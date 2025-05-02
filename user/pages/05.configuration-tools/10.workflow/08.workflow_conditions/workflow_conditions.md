---
title: 'Workflow Conditions'
metadata:
    description: 'Explain how the different conditions work'
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
        - workflow
        
    tag:
        - condition
        
---

*TBD FIXME: Explain how the different conditions work.*

Hidden and Hard to find Features
--------------------------------

### Comparing Last Modified By User and the current Assigned User

When defining the conditions we have access to all the fields of the
main module of the workflow and all its related entities on the
left-hand side of the condition, but on the right-hand side, we can only
access the fields directly related to the main module, not the fields of
the related entities.

In fact, the use cases for this type of conditions is very limited. In
all the years that we have been working with coreBOS this has rarely
come up and we usually solve it with some additional code for the
specific case.

Based on this question from a forum member:

<div class="notices blue">
<h3>We would like to set the "Workflow for Ticket Change, not from the
Portal" workflow to NOT send emails when the last modified user is the
same as the assigned to the user. If a person working on the ticket puts
some notes in there, we do not want an immediate email to themselves.
But, if someone else adds notes, we do want the assigned to the user to
get an email.</h3>

To solve this use case, which is common, we have enhanced coreBOS
(starting at <a href="https://github.com/tsolucio/corebos/commit/9a5307e1c28f87d42def73aaea606db9929349b6#diff-d41d8cd98f00b204e9800998ecf8427e" style="color:black;"><i>commit 9a5307</i></a> to support accessing the fields of the "assigned to" user of the main
module.

<div class="notices red">
It is ONLY for the fields of the
"assigned user" because those are already present when evaluating the
condition, no extra effort is needed except picking them
up.</div>

The syntax is a little different to make the code easier, maybe we will
enhance that someday to work as the left-hand side of the condition.
Currently, the syntax has to be:
<div class="notices blue">
 assigned_user_id : (Users) {field name} </div>

where {field name} has to be the internal field name of the user module.
For example to access the user name we would use <i>user_name</i> and to
access the first name we would use <i>first_name</i>.
<br>
<br>
Once applied the <a href="https://github.com/tsolucio/corebos/commit/9a5307e1c28f87d42def73aaea606db9929349b6#diff-d41d8cd98f00b204e9800998ecf8427e" style="color:black;"><i>code change detailed here</i></a>,
we can answer the question above as seen in the next image:
</div>
![](assignedtoworkflowconditions.png?width=100%)



### How to launch a workflow only when a record is related to an entity.

To accomplish this we simply need to do an **empty** or **not empty**
check on any non-empty field in the related module. So, for example, if
we need to launch a workflow on the Inventory Details module only when
the record is related to a Sales Order, then we will check the *Related
To* field of the Inventory Detail module for the *Subject* field on the
Sales Order. If the Inventory Details record is related to a Sales Order
then this field will have a value, if the record is related to some
other module, the SalesOrder field will be empty.


![](workflowcheckrelatedtoen.png?width=100%)