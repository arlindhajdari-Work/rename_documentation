---
title: 'Idempotent operations'
metadata:
    description: 'Steps and options for putting web service operations in the coreBOS queue for deferred execution'
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
        - webservice
        - queue
    tag:
        - add
---

As of July 2022, we have the possibilty to execute web service operations as idempotent operations.

The article [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) explains it perfectly. I had already thought of this solution before searching the internet for best practices to this problem. From that article, I would emphasize:

- our preferred approach is to incorporate a unique caller-provided client request identifier into our API contract. Requests from the same caller with the same client request identifier can be considered duplicate requests and can be dealt with accordingly.
- we can ignore
  - Semantic equivalence and support for default retry strategies
  - Late arriving requests and the life span of unique client request identifiers
- Responding when a customer changes request parameters on a subsequent call where the client request ID stays the same

## Supported Operations

The exact list of supported operations can be obtained by executing this SQL command in the database:

`SELECT name FROM vtiger_ws_operation where is_idempotency=1`

As of the moment of writing this article, they are:

- [create](../08.methodreference/item.md#create)
- [CreateWithValidation](../08.methodreference/item.md#validations-create-update-and-revise-with-validations)
- [update](../08.methodreference/item.md#update)
- [UpdateWithValidation](../08.methodreference/item.md#validations-create-update-and-revise-with-validations)
- [revise](../08.methodreference/item.md#revise)
- [ReviseWithValidation](../08.methodreference/item.md#validations-create-update-and-revise-with-validations)
- [upsert](../08.methodreference/item.md#upsert)
- [MassCreate](../08.methodreference/item.md#masscreate-massupsert)
- [MassUpdate](../08.methodreference/item.md#massupdate)
- [convertlead](../01.convertleadwebservice/item.md)
- [ExecuteWorkflow](../00.manual/05.wfrlqsat/item.md#executeworkflow-operation)
- [executeBusinessAction](../../../05.configuration-tools/03.business-actions/05.webservice_ba/item.md)
- [addProductImages](../03.docenhance/item.md#product-multi-image-field)

## How to define a web service operation as idempotent

To mark a supported operation as idempotent we have to send an additional parameter with the call: `cbwsOptions`. This parameter is an array in which we can define the `ClientRequestIdentifier`. This option can have two values:

- `generate` or empty: in this case, coreBOS will generate the ID for the operation so it can do the tracking of the repeated calls internally
- any string identifier for the operation. If the ID is present in the application, it will consider the operation as repeated and return the previous result, if not, it will use the given ID as the idempotent identifier for the operations internal tracking. This permits the user of the API to determine what a repeated call looks like.

## Examples

We do a normal update call but setting the `ClientRequestIdentifier` parameter to the empty string so coreBOS can do the internal control of the operation. The description field is updated.

![idempotent revise](IdempotentRevise.png?width=100%)

Now we update the description field from inside the application

![updated description](AppUpdate.png?width=100%)

We do the call again and get the exact same result as the first call. The description field is NOT updated, the web service update call was detected as already executed and ignored.

## References

- [Making retries safe with idempotent APIs](making-retries-safe-with-idempotent-apis-malcolm-featonby.pdf)
- [Idempotent Writes to Delta Lake Tables](https://towardsdatascience.com/idempotent-writes-to-delta-lake-tables-96f49addd4aa)
- [How to make data pipelines idempotent · Start Data Engineering](https://www.startdataengineering.com/post/why-how-idempotent-data-pipeline/)
- [Building Resilient Systems with Idempotent APIs - DEV Community](https://dev.to/karishmashukla/building-resilient-systems-with-idempotent-apis-5e5p)

<br>
------------------------------------------------------------------------

[Next](../../02.coreboswsbrowser)| Chapter 15: coreBOS Web Service Developer Tool.

------------------------------------------------------------------------
