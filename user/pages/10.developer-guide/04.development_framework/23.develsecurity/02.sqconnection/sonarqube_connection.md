---
title: 'Sonarqube Connection'
metadata:
    description: 'Learn how to configure and connect Sonarqube to control your Evolutivo.FW code base.'
    author: 'Joe Bordes'
content:
    items:
        - '@self.children'
    order:
        by: date
        dir: desc
taxonomy:
    category:
        - development
        - application
        - security
    tag:
        - howto
---

Learn how to configure and connect Sonarqube to control your Evolutivo.FW code base.

===

Evolutivo takes its coding responsibilities very seriously. We study, review, and apply general best practices in all our work, but having the tranquility of knowing that we are backed by a tool like [Sonarqube](https://www.sonarsource.com/products/sonarqube/) is so reassuring 😊

We use it as we code to keep issues at bay but also dedicate time to reviewing the recommendations and refactoring our code accordingly. This is not a trivial task, mainly because the refactor must be backed by unit tests, but it is essential to the continued success of the platform.

Read on to learn how to configure your editor environment to work with evolutivo.fw or connect to your project.

## Install Sonarqube server

We use the open-source version of Sonarqube and install it using the docker compose files. This is extremely easy. You just have to be careful to configure the persistent volumes correctly and make backups. I share here the configuration we use.

```yaml
```

The Postgresql database and the configuration files are backed up regularly within our company backup policies. Mostly using rsnapshot.

## Configuring a project


## Executing analysis

- download and install the command line analysis tool
- create a configuration file for your project
- launch analysis


## Configuring your IDE

I use Visual Studio code, so I am going to explain here only how to connect this IDE, others should be just as easy.

- install the Sonarqube extension
- get a token from Sonarqube for your project
- connect the project clone to the server

## Start enjoying the power of guidance

example of throw exception

## Review results and start fixing

## Connecting to Sonarqube web and guidance

 
