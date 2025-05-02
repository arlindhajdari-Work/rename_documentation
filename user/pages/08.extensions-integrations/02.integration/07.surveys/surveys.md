---
title: 'Surveys'
metadata:
    description: 'It is a research method used for collecting data from a predefined group of respondents to gain information and insights into various topics of interest.'
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
        - integration
    tag:
        - surveys
---

The survey integration system in **coreBOSCRM** is based on the idea of joining forces. We don't pretend to have a complete survey management system inside the application and compete with existing tools dedicated to this purpose, because we know we will never reach the level of quality and professionalism that companies which are fully dedicated to this can achieve. Our goal is to do what we do best: **manage your information**.

===

With this in mind, we have created four modules that permit us to control the set of surveys that we launch and the answers to these surveys that our clients fill in. So you will be able to match the answers with your clients, and even more importantly, you will be able to use all the process automation tools that you have in **coreBOSCRM** to react to these answers in near real-time making it easy to add a contact to a drip campaign or a segmentation list or even create calendar events depending on their answers.

There are four new modules which can be found in the "**Analysis**" menu:

![](cbcrm_survey_menu.png?width=100%)

On one hand, we have **surveys and questions**, which represent the exact survey and the questions that it contains. These modules simply contain a copy of the information created in the external survey program chosen. They do not create the survey in the external system, they simply record the fact that a survey was created and the questions it contained. The records in this module are auto-created when the first survey arrives.

On the other hand, we have the modules **survey done and answers**, these modules record the fact of a given client filling in and sending a survey and the exact answers he has given. The records in this module are auto-created as the surveys are submitted.

When the records are created all associated workflows are called so we can tie in with all the process automation tasks that the workflow system brings to the application.

Just to throw around some ideas, we could associate a workflow to the creation event of a survey done and send a "*thank you*" email to the client and at the same time put them into a segmentation list, we could monitor specific answers to some questions in order to put the client on some campaign or tag them with some label for future segmenting or send them a loyalty discount,... the possibilities and combinations are enormous.

Obviously, with all this information being injected directly into our production system simple things like creating a report to know how many people completed a given survey is a trivial task, directly supported by the application.

If you need more information, feel free to [ask us](https://corebos.org/contact).

### Survey Paths

As of summer 2024, we have added another module to the mix: Survey Paths. This module comes with a set of new fields also in other modules to make managing surveys a more powerful experience. We now have fields to register the person doing the interview, score the questions, give helpful indications and indicate the type of question for a better user experience, among others.

The survey path module serves the purpose of establishing a many-to-many relationship between surveys and questions. Up to now, we had a direct relation between surveys and questions. This obligated us to duplicate questions if we wanted to repeat them in other surveys. With survey path, we can select questions from a pool of questions and relate them to many surveys while still setting different sequences, points and adapting the question to fit better the survey. It also permits us to define which will be the next question in the case of a positive or negative response, so we can skip some questions in the flow if we need to.

### Supported Services

We currently support these survey services:

[Typeform](../09.typeform)

<div class="notices yellow">
We are open to other integrations, especially Google Forms and Survey Monkey and would be happy to help you get those into the list of supported services so don't hesitate to contact us if you need more.
</div>

------------------------------------------------------------------------

[Next](../08.tiddlywiki) | Chapter 8: Integration with TiddlyWiki

------------------------------------------------------------------------