---
title: 'Commit Guidelines we try to adhere to'
metadata:
    description: 'coreBOS Product/Price Enhancements'
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
        - contribute
    tag:
        - guidelines
        - format
---

[AngularJS Git Commit Message Conventions](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/mobilebasic?pli=1)

    <type>(<scope>) <subject>

another way of reading that is:

    what(where) how

in this second form, the *when* and *who* are controlled by git itself,
so sign your commits.

Some additional clarifications:

-   Any line of the commit message cannot be longer 100 characters! This
    allows the message to be easier to read on GitHub as well as in
    various git tools.
-   Allowed **&lt;type&gt;**
    -   **feat**: feature
    -   **adapt**: this is a feature, but it only affects a particular
        install, not the whole coreBOS project
    -   **fix**: bug fix
    -   **security**
    -   **i18n**: translation strings and enhancements
    -   **docs**: documentation
    -   **style**: formatting, missing semi colons, …
    -   **refactor**: code refactor
    -   **test**: when adding missing tests
    -   **chore**: maintenance tasks
-   Allowed **&lt;scope&gt;** could be anything specifying place of the
    commit change. For example a module name, webservice or functional
    feature
-   **&lt;subject&gt;** line contains succinct description of the
    change. Use imperative, present tense: "change" not "changed" nor
    "changes".
    -   If the commit fixes or is related to a ticket put the title or a
        summary of it, the actual ticket number is rather useless as
        time has taught me that ticket systems come and go while code
        and commit messages persist.
