---
title: 'GenDoc::Examples'
metadata:
    description: 'TNon Supported Elements'
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
        - gendoc

---

# Table with Header and Rows

[Table with Header and Rows](tablacabecerafilas)

## Iteration

### Add number of elements

```
{foreach Fichero}
{iteration} {Fichero.filename}
{/foreach}
```

### Block on first iteration

```
{foreach Fichero.nivel=ALTO}
{ifexists iteration=1}
The next list of files have HIGH level:
{/ifexists}
{Fichero.filename}
{/foreach}
```

### Negative Conditions

If we want to obtain the records that do not meet a condition, we will use:

```
{foreach <MODULE>.<FIELD> != <VALUE>}
```

That will get all records with the field "Destruction Method" NOT empty.

### Nested foreach

You can put foreach tags of related entities up to any level, this means that from an Account, you can reach one or several contacts, and from there reach their potentials and from there, loop over the related quotes.

[Next](../03.gendoctips)| Chapter 5: GenDoc::Tips and Tricks

------------------------------------------------------------------------