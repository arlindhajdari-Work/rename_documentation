---
title: 'BPM Example'
metadata:
    description: 'Menu Editor'
    author: 'Eleni Kullira'
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
        - adminmanual
    tag:
        - howto
        - BPM
---

## BPM Example DOCUMENTATION

Business process management (**BPM**) is a disciplined approach to identify, design, execute, measure, monitor, and control both automated and non-automated business processes to achieve consistent, targeted results aligned with an organization’s strategic goals. BPM involves the deliberate, collaborative and increasingly technology-aided definition, improvement, innovation, and management of end-to-end business processes that drive business results, create value, and enable an organization to meet its business objectives with more agility. BPM enables an enterprise to align its business processes to its business strategy, leading to effective overall company performance through improvements of specific work activities either within a specific department, across the enterprise, or between organizations.

**A BPM Example:**

Task name :** Approval process**

Task Description:

!!! Clients ask for a way to block the modification of prices and discounts in quotes. Additionally, some quotes will have an approval mechanism for discounts.

The client has this hierarchy:

```
CEO
  | Finance
  | Sales Director
  | Assistant
  | Area Manager
```

Example use case: Area Manager creates a quotes which has a certain marginality. If the marginanlity is greater than 20 % the quote's automatically approved. If it's between 15 and 20% then the Sales Director needs to approve it. If it's lower than 15 than Sales Director, Finance and CEO have to approve it. Assistant can create a quote for Area Manager but than he needs to approve it.

To solve this task  we’ve created extra status (quote stage) (Approved, Awaiting Approval, Refused, Approved by Finance,Approved by CEO etc),a Workflow Task, a [Mermaid Business Question](../../../06.analytics/01.business-questions/item.md#mermaid-graphs) and a [Process Flow](https://blog.corebos.org/blog/bpmprocessflow2) with some Process Steps.

### The Mermaid Business Question:

![Mermaid](mermaid.PNG?classes=maxsize)

<br>

![SQL](SQL.PNG?classes=maxsize)

<br>

```
A[Created] --> B[Refuse]
    A --> C[Approved]   
    I --> D
    A --> D[Approved by CEO]
    A --> E[Refused by CEO]
    B --> F[Accepted by Finance]
    B --> G[Refused by Finance]
    C --> F
    C --> G
    F --> I[Awaiting Approval]
    G --> I
    I --> E
```

### The Process Flow

![SQL](processflow.PNG?classes=maxsize)

Taking the task step by step:

#### 1-If the marginanlity is greater than 20 % the quote's automatically approved-

For this step it’s not necessary to make a process step we need a simple **update field** workflow as in the example below:

![SQL](wf.PNG?classes=maxsize)

#### 2-If it's between 15 and 20% only then the Sales Director needs to approve it.-

In this case the Quote need to be approved only from the Sales Director so the quote stage goes from Created directly to Approved by CEO or Refused by CEO

To do this we need to create:

#### 2.1  2 steps in the Process Steps module

The first **Created** → Approved by CEO

![Process_steps](ps1.PNG?classes=maxsize)

The second **Created** → Refused by CEO

![Process_step](ps2.PNG?classes=maxsize)

#### 2.2 A Condition Expression Map

The condition expresion map holds the logic of the implementation.

![Map](map1.PNG?classes=maxsize)

```
<map><expression>
<![CDATA[if AND(marginality>'14',marginality<'21',
getCurrentUserField('roleid') == 'H4') then 1 else 0 end]]>
</expression></map>
```

**H4 → the role id of Sales Director**

#### 2.3 A Validation Map 

The validation is an intermediary map created in order to validate the condition expresion map which holds the logic of the implementation.

```
<map>
  <originmodule>
    <originname>Quotes</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>marginality</fieldname>
         <validations>
        <validation>
          <rule>expression</rule>
          <restrictions>
          <restriction>sales_director_role</restriction>
          </restrictions>
        </validation>
      </validations>
    </field>
  </fields>
</map>
```

#### 3-If it's lower than 15 than Sales Director, Finance and CEO have to approve it.-

In this case the Quote need to be approved firstly by the Sales Director, secondly by Finance and finally from CEO. This part of the tasks have to go step by step, so if the Sales Director have not denied or approved the quote no one else have the permission to do it. The map goes :
**Created → Approved/Refuse → Approved by Finance/Refuse by Finance → Approved by CEO/Refuse by CEO**

#### 3.1 Sales direktor 

##### 3.1.1  2 steps in the Process Steps module

The first **Created** → Approved

![Process_step](ps3.PNG?classes=maxsize)

The second **Created** → Refused

![Process_step](ps4.PNG?classes=maxsize)

##### 3.1.2 A Condition Expression Map

The condition expresion map holds the logic of the implementation.


![Map](map2.PNG?classes=maxsize)

```
<map><expression><![CDATA[if AND(marginality<'15',getCurrentUserField('roleid') == 'H4') then 1 else 0 end]]></expression></map>
```

**H4 → the role id of Sales Director**

##### 3.1.3 A Validation Map

The validation is an intermediary map created in order to validate the condition expresion map which holds the logic of the implementation.

```
<map>
  <originmodule>
    <originname>Quotes</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>marginality</fieldname>
         <validations>
        <validation>
          <rule>expression</rule>
          <restrictions>
          <restriction>second_user_role</restriction>
          </restrictions>
        </validation>
      </validations>
    </field>
  </fields>
</map>
```

#### 3.2 Finance 

##### 3.2.1  2 steps in the Process Steps module

The first **Approved** → Approved by Finance / Refused by Finance

![Process_step](ps5.PNG?classes=maxsize)

![Process_step](ps6.PNG?classes=maxsize)

The second **Refused** → Approved by Finance / Refused by Finance

![Process_step](ps7.PNG?classes=maxsize)

![Process_step](ps8.PNG?classes=maxsize)

#### 3.2.2 A Condition Expression Map

The condition expresion map holds the logic of the implementation.

![Map](map3.PNG?classes=maxsize)

```
<map><expression>if getCurrentUserField('roleid') == 'H3' then 1 else 0 end></expression></map>
```

**H3 → the role id of Finance**

##### 3.2.3 A A Validation Map  

The validation is an intermediary map created in order to validate the condition expresion map which holds the logic of the implementation.

```
<map>
  <originmodule>
    <originname>Quotes</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>marginality</fieldname>
         <validations>
        <validation>
          <rule>expression</rule>
          <restrictions>
          <restriction>third_role</restriction>
          </restrictions>
        </validation>
      </validations>
    </field>
  </fields>
</map>
```

### 3.3  CEO 

#### 3.3.1  2 steps in the Process Steps module

The first Approved by Finance / Refused by Finance → **Awaiting Approval**

![Process_step](ps9.PNG?classes=maxsize)

![Process_step](ps10.PNG?classes=maxsize)

The second **Awaiting Approval→Approved by CEO / Refused  by CEO**

![Process_step](ps11.PNG?classes=maxsize)

![Process_step](ps12.PNG?classes=maxsize)

##### 3.3.2 A Condition Expression Map

The condition expresion map holds the logic of the implementation.
 
![Map](map4.PNG?classes=maxsize)

```
<map><expression>if getCurrentUserField('roleid') == 'H2' then 1 else 0 end></expression></map>
```

**H2 → the role id of CEO**

##### 3.3.3 A Validation Map

The validation is an intermediary map created in order to validate the condition expresion map which holds the logic of the implementation.

```
<map>
  <originmodule>
    <originname>Quotes</originname>
  </originmodule>
  <fields>
    <field>
      <fieldname>marginality</fieldname>
         <validations>
        <validation>
          <rule>expression</rule>
          <restrictions>
          <restriction>ceo_role</restriction>
          </restrictions>
        </validation>
      </validations>
    </field>
  </fields>
</map>
```

<head>
<style type="text/css">
.maxsize {
  width: 600px ;
}
</style>
</head>
