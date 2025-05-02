---
title: 'Documentation Guide'
metadata:
    description: 'Documentation woes.'
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
        - documentation
        - contribute
    tag:
        - howto
---

## How to Contribute to the coreBOS Documentation

This documentation site is open source. It is developed using [GRAV CMS](https://getgrav.org/) and can be found at this repository:

`https://github.com/coreBOS/coreBOSDocumentation.git`

To set up a writing environment, clone that repositoy into a directory accessible by your local webserver:

```shell
cd /var/www/html
git clone https://github.com/coreBOS/coreBOSDocumentation.git corebosdocs
```

then you have to download the theme. Move into the user/themes/ directory, delete the quark directory, clone the theme online and recover the files you deleted:

```shell
cd corebosdocs/user/themes
rm -rf quark
git clone https://github.com/coreBOS/coreBOSDocumentationTheme.git quark
git checkout quark/templates/flex/
```

Next we install grav dependencies and give access to the files to the web server user:

```shell
cd corebosdocs
bin/grav install
sudo chgrp -R www-data .
```

now you can access the URL (http://localhost/corebosdocs), create the admin user and start writing.

You can learn all about grav cms markdown at their site and then follow the typical git pull request workflow to share your work with the world.

### Contributing to the stores

This site use Flex objects to create **stores** for some special sections. These are currently

* GenDoc Templates
* Business Maps
* Extensions and Modules

To contribute to these you have to add the new entry in the admin section. Look at the fields of the existing records to get an idea of the information you have to add. In the case of configuration settings and modules you also have to add some documentation. This is done by creating a subdirectory inside:

* `user/pages/07.knowledge-base/10.configuration-store/businessaction/` for business actions
* `user/pages/07.knowledge-base/10.configuration-store/businessmap/` for business maps
* `user/pages/07.knowledge-base/10.configuration-store/changeset/` for changesets
* `user/pages/07.knowledge-base/10.configuration-store/menu/` for menus
* `user/pages/07.knowledge-base/10.configuration-store/workflow/` for workflows
* `user/pages/08.extensions-integrations/01.corebosmodules/` for extensions and modules

with a page named `corebosstore.md`. This page can follow the same markdown rules as any other page and should contain, at a minimum the configuration option or fields of the module. A brief explanation of what it is for and what you can expect to get from it is recommended.

![coreBOS Module Store](corebosmodulestore.png?width=100%)

![coreBOS Module in Store](corebosmoduleinstore.png?width=100%)

## coreBOS Documentation

![work in progress](workinprogress.png?resize=150&classes=float-right)

Documentation is a continuous and ever going, ungrateful task that
**needs to be done**. No matter how much time and care you put into it,
it is rarely used and even when it is, it is hard to understand because
who wrote it knew to much of what he was explaining :-).

As brilliantly put by [Karl Fogelin](http://www.red-bean.com/kfogel) in his book
[Producing Open Source Software](http://producingoss.com/en/getting-started.html\#documentation):

 !!! Documentation is essential. There needs to be something for people to read, even if it's rudimentary and incomplete. This falls squarely into the "drudgery" category referred to earlier, and is often the first area where a new open source project falls down. Coming up with a mission statement and feature list, choosing a license, summarizing development status---these are all relatively small tasks, which can be definitively completed and usually need not be revisited once done.

Documentation, on the other hand, is never really finished, which may be
one reason people sometimes delay starting it at all.The most insidious
thing is that documentation's utility to those writing it is the reverse
of its utility to those who will read it. The most important
documentation for initial users is the basics: how to quickly set up the
software, an overview of how it works, perhaps some guides to doing
common tasks. Yet these are exactly the things the writers of the
documentation know all too well---so well that it can be difficult for
them to see things from the reader's point of view, and to laboriously
spell out the steps that (to the writers) seem so obvious as to be
unworthy of mention.

But that isn't enough for us, so we have created this open source
documentation project called coreBOSDocs, where we will be writing
articles about the application, uploading videos and tutorials for all
those issues and hurdles you may run into.

We invite you to participate and help us create a great documentation
site for **coreBOS**, any help is welcome, from creating tickets of issues you
would like us to talk or write about, to writing those articles yourself.

So, step right in and help out with the **_coreBOS Documentation Site_**

## Writing It All Down

One of our many inspirations is the pragmatic and useful book [Producing Open Source Software](http://producingoss.com) by [Karl Fogel](http://www.red-bean.com/kfogel).

In the part of the book where he touches on documenting developer best
practices he, once again, perfectly nails the situation, so I am
basically just going to copy one paragraph I think is specially
important and redirect you there: [Writing It All Down](http://producingoss.com/en/written-rules.html)

 !!! Don't try to be comprehensive. No document can capture everything people need to know about participating in a project. Many of the conventions a project evolves remain forever unspoken, never mentioned explicitly, yet adhered to by all. Other things are simply too obvious to be mentioned, and would only distract from important but non-obvious material. For example, there's no point writing guidelines like "Be polite and respectful to others on the mailing lists, and don't start flame wars," or "Write clean, readable bug-free code." Of course these things are desirable, but since there's no conceivable universe in which they might not be desirable, they are not worth mentioning. If people are being rude on the mailing list, or writing buggy code, they're not going to stop just because the project guidelines said to. Such situations need to be dealt with as they arise, not by blanket admonitions to be good. On the other hand, if the project has specific guidelines about how to write good code, such as rules about documenting every API in a certain format, then those guidelines should be written down as completely as possible.

## Article about the importance of Documentation

[Motivating Developers to Care About Documentation](https://getdx.com/best-practices/documentation-culture-engineering)

I felt very inspired by the article above and decided to share it here. I will paste here some of the concepts I took away as important.

### What is documentation?

* documentation is bureaucracy
* documentation is a nice-to-have
* documentation takes too much time

All of these are **myths**. Documentation, done well, helps the team move faster with less rework. If you want to scale, you need documentation, it’s **not a nice-to-have**. And if it takes too much time it’s because the process isn’t set up right.

### Why do we need documentation in the first place?

1. making better decisions across the organization,
2. helping people get the right information when they need it,
3. making our onboarding process more self-service (my opinion is that onboarding should be 80% self-serve)
 !!! ask yourself if writing the documentation will help us with one of those objectives

### Tips for helping teams maintain the practice

* Make documentation easy.
* Treat documentation like a discipline.
* Reinforce the behavior.





