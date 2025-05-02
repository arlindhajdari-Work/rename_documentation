---
title: 'How to Anonymize your database: masquerade'
metadata:
    description: 'How to Anonymize your database: masquerade'
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
        - anonymization
        - integration
    tag:
        - masquerade
        - anonymize
---

1.- Clone the base project

    git clone https://github.com/coreBOS/masqueradeAnonymizer.git

2.- Install masquerade

    curl -L -o masquerade.phar https://github.com/elgentos/masquerade/releases/latest/download/masquerade.phar
    chmod +x masquerade.phar

3.- Edit config.yaml file and set access to the database you want to
anonymize. **REMEMBER**: make a backup! **DO NOT** work directly on the
production database (just in case it wasn't obvious).

4.- Adapt the existing anonymization files. For each module file in the
config directory, you will have to add an anonymization step for the
custom fields you have created. You can apply a specific transformation
to each one and you can read the ones we have created for examples, also
[read below for some guidelines](item.md#anonymization-rules)

5.- Create new anonymization files for each custom module you may have
created for your coreBOS install. [Read below for some guidelines](item.md#anonymization-rules)

6.- Run

    ./masquerade.phar run

7.- Debug and repeat until finished

8.- After finishing the anonymization, we recommend you put all the
files in the build directory of coreBOS, something like:
`build/anonymize` and version them inside the project.

Anonymization Rules
-------------------

- Use Faker methods [listed here](https://github.com/fzaninotto/Faker#formatters)
- Use

```shell
php build/HelperScripts/listmodules.php 1
```

  to get a list of all your custom modules and extensions
- Use

```shell
php build/HelperScripts/listfields.php modulename
```

  to get the list of fields of your modules
- Do not anonymize uitype 4 (auto-increment fields)
- Do not anonymize picklist fields. These do not contain sensitive information and they will break the coreBOS application if the value contained in the field is not registered as an authorized picklist value
- I would recommend not modifying DateTime fields either but you can if you need to
- Do not anonymize foreign keys (uitype 10 fields) so the references stay in place and you don't break related lists
- All users are anonymized except the admin user, so you can login with this user. If you need to keep some other users unmodified [add them to the "skip-list"](https://github.com/coreBOS/masqueradeAnonymizer/blob/main/config/corebos/vtiger_users.yaml#L4)
- if you need audit trail or login history [edit the cleanup.yaml script](https://github.com/coreBOS/masqueradeAnonymizer/blob/main/config/corebos/cleanup.yaml)

References
----------

- [Masquerade](https://github.com/elgentos/masquerade)
- [Anonymizing databases - introducing Masquerade](https://elgentos.nl/blog/anonymizing-databases-introducing-masquerade/)
- [Project Repository](https://github.com/coreBOS/masqueradeAnonymizer.git)
