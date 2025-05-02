---
title: 'Putting operations in the queue'
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

As of May 2022, there is a set of web service operations that can be sent to the coreBOS queue system for deferred execution. What happens in this case is that instead of directly executing the operation and returning the result, the operation is sent to the queue system where it is put on hold and a unique `operationTrackingID` is returned instead. With the tracking ID you can consult the status of the operation until it is finished.

## Supported Operations

The exact list of supported operations can be obtained by executing this SQL command in the database:

`SELECT name FROM vtiger_ws_operation where queable=1`

As of the moment of writing this article, they are:

- [create](../08.methodreference/item.md#create)
- [update](../08.methodreference/item.md#update)
- [revise](../08.methodreference/item.md#revise)
- [upsert](../08.methodreference/item.md#upsert)
- [MassCreate](../08.methodreference/item.md#masscreate-massupsert)
- [MassUpdate](../08.methodreference/item.md#massupdate)
- [MassDelete](../08.methodreference/item.md#massdelete)
- [describe](../08.methodreference/item.md#describe)
- [getRelatedModulesInfomation](../08.methodreference/item.md#other-information)
- [ExecuteWorkflow](../00.manual/05.wfrlqsat/item.md#executeworkflow-operation)
- [ExecuteWorkflowWithContext](../00.manual/05.wfrlqsat/item.md#executeworkflowwithcontext-operation)
- [convertlead](../01.convertleadwebservice/item.md)
- [gendoc_convert](../05.getpdfdata/item.md)

## How to put an operation in the queue

To put a supported operation in the queue we have to send an additional parameter with the call: `cbwsOptions`. This parameter is an array in which we can define two options:

- `launchfromqueue` is a boolean value that indicates if the operation should be enqueued or not
- `queuedelay` is an integer value that defines the delay, in seconds, which the operation will wait in the queue to be executed

![Describe in queue](DescribeQueue.png?width=100%)

## How to consult the status of queued operation

To get the status of a queued operation we can use the `getQueuedOperationResult` endpoint. This GET operation requires one parameter which is the `operationTrackingID` obtained from the call where we put the operation in the queue.

![Describe in queue](GetStatusQueue.png?width=100%)

The call will either return the string "Operation not queued or not finished yet" or the response if the operation has been executed.

**Important note:** The response can only be returned once. After reading the result of the queued operation the response is lost.

![Describe in queue](GetStatusQueueExecuted.png?width=100%)

The complete result of the operation will be held in the `result` response property, it is NOT the standard web service response, that response is now inside the ` result` property.

## How to execute the operations in the queue

The operations that have been put into the queue need to be read and processed. The script in charge of that is `include/Webservices/executeOperationsFromQueue.php` which must be executed in a cron from your operating system exactly like the `vtigercron.php` script.

```shell
cd /your/corebos/install/directory
/usr/bin/php include/Webservices/executeOperationsFromQueue.php
```

This script reads the pending web service operation messages from the queue and processes them.

<br>
------------------------------------------------------------------------

[Next](../15.wsidempotent/item.md)| Idempotent operations

------------------------------------------------------------------------
