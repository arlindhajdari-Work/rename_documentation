---
title: 'Information Map Business Mapping'
metadata:
    description: 'Information Map Business Mapping'
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
        - businessmappings
    tag:
        - informap
---

The coreBOS Information Map is a mechanism that allows the implementor to define a set of information that can be easily changed without creating a new module. It is particularly useful when the information set is small and consists of small pieces of data.

===

The XML map follows this specific format:

```xml
<map>
  <information>
    <infotype>put here some distinctive category of your information</infotype>
    <value>any information</value>
    <value>you need</value>
    <value>to use in your code</value>
    <value>...</value>
  </information>
</map>
```

The `<infotype>` element is used to provide a distinctive category or name for the information being defined. It helps in identifying and referencing the specific set of data.

The `<value>` elements represent the individual pieces of information within the set. Multiple `<value>` elements can be included, each containing a different piece of data.

The coreBOS Information Map serves as a parameter for various functionalities within the application. For example, it can be used as a parameter for workflow expression methods that calculate business dates. Instead of repeating a list of dates in each workflow where these functions are used, the map can be referenced by providing its crmid/name. This makes it easier to maintain the list of dates as it can be updated in one place (the map) rather than modifying multiple workflows.

In the next provided example, the map defines a list of holidays for multiple years. By using the `<infotype>` as "Holidays" and including `<value>` elements for each holiday date, the map can be referenced and used in workflows to calculate business dates, taking into account the defined holidays.

coreBOS uses this type of map as a parameter to the workflow expression methods that calculate business dates. The **next\_date** and **holidaydifference** accept a comma separated list of dates to define which dates are holidays. Instead of having to repeat that list in every workflow where you need to use these functions and then have to edit them once a year, we can pass in as a parameter the crmid/name of an information business map with the dates, something like this:

```xml
<map>
  <information>
    <infotype>Holidays</infotype>
    <value>2017-01-01</value>
    <value>2017-01-06</value>
    <value>2017-04-17</value>
    <value>2017-04-25</value>
    <value>2017-05-01</value>
    <value>2017-06-02</value>
    <value>2017-08-15</value>
    <value>2017-11-01</value>
    <value>2017-12-08</value>
    <value>2017-12-25</value>
    <value>2017-12-26</value>
    <value>2018-01-01</value>
    <value>2018-01-06</value>
    <value>2018-04-01</value>
    <value>2018-04-02</value>
    <value>2018-04-25</value>
    <value>2018-05-01</value>
    <value>2018-06-02</value>
    <value>2018-08-15</value>
    <value>2018-11-01</value>
    <value>2018-12-08</value>
    <value>2018-12-25</value>
    <value>2018-12-26</value>
    <value>2019-01-01</value>
    <value>2019-01-06</value>
    <value>2019-04-21</value>
    <value>2019-04-22</value>
    <value>2019-04-25</value>
    <value>2019-05-01</value>
    <value>2019-06-02</value>
    <value>2019-08-15</value>
    <value>2019-11-01</value>
    <value>2019-12-08</value>
    <value>2019-12-25</value>
    <value>2019-12-26</value>
    <value>2020-01-01</value>
    <value>2020-01-06</value>
    <value>2020-04-12</value>
    <value>2020-04-13</value>
    <value>2020-04-25</value>
    <value>2020-05-01</value>
    <value>2020-06-02</value>
    <value>2020-08-15</value>
    <value>2020-11-01</value>
    <value>2020-12-08</value>
    <value>2020-12-25</value>
    <value>2020-12-26</value>
  </information>
</map>
```

Making it much easier to maintain.

Overall, the CoreBOS Information Map provides a convenient way to manage and update small sets of information that are utilized in different parts of the application. It helps streamline maintenance efforts by centralizing the data and allowing easy modification when needed.

<br>
------------------------------------------------------------------------

[Next](../09.field_dependency) | Chapter 13: Field Dependency.

------------------------------------------------------------------------