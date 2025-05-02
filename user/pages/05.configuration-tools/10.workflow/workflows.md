---
title: 'Workflows'
metadata:
    description: 'Types of Workflows'
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
        - adminmanuals
        - workflows
    tag:
        - workflows
        
---

Workflows are a very powerful part of the application. They permit us to automate our business logic to some extent making it possible to standardize processes and have the application do some of the repetitive tasks our business requires.

===

It is necessary to execute four steps to configure and setup a workflow:

- Select a module against which the workflow will be executed and give it a name
- Select when the workflow will be triggered
- Select any conditions that restrict for what records the workflow must take it's actions
- Define and configure the different tasks that the workflow will perform

In the next sections, you will be able to find more information on these steps.

- [Workflow launch conditions](10.workflow/10.workflow_launch_conditions)
- [Workflow step-by-step explanation](11.workflow_stepbystep)
- [Scheduled Time-based Workflows](05.scheduled_workflows)
- [Workflow conditions](08.workflow_conditions)

## Workflow Tasks

- [Update Workflow Tasks](06.update_workflows)
- [Upsert Workflow Task](07.upsert_workflows)
- [Add/Delete Tags Workflow Tasks](01.addeltag_workflows)
- [Related Product/Service Workflow Task](04.relateproductservice_workflows)
- [Invoke Custom Functions Workflow Tasks](03.invokecustomfunction_workflows)
- [SMS Workflow Tasks](../../04.user-manual/smsnotifier#sms-task-with-work-flow)

## Workflow Examples

- [Workflow Examples](09.workflow_examples)
- [How to send emails/SMS on specific weekdays](13.workflow_weekendwarning)
- [Workflow tricks and tips](12.workflow_tricksandtips)
