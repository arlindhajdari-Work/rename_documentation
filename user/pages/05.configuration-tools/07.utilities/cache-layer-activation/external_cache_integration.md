---
title: 'External Cache Integration'
metadata:
    description: 'How to use External Cache Integration'
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
        - cache
        - development
---

One of the many features in coreBOS is an external cache integration, which allows you to improve the performance and scalability of the CRM system.

===

## Cache Integration

External cache integration in coreBOS involves using an external caching system to store frequently accessed data, reducing the need to retrieve it from the database on every request. This can significantly enhance the overall system performance by reducing the load on the database server.

By integrating an external cache system with coreBOS, you can achieve significant performance improvements. The caching system acts as a middle layer between the CRM system and the database, reducing the number of database queries and improving response times. It is especially useful in scenarios with high user concurrency and heavy database usage.

It's worth noting that while external cache integration can greatly enhance performance, it also introduces some considerations. Care must be taken to properly configure and manage the cache system to ensure data consistency and minimize the risk of serving stale information.

Overall, coreBOS's external cache integration feature provides a scalable and efficient solution to optimize the performance of the CRM system by leveraging external caching mechanisms.

Here's how the external cache integration works in coreBOS:

### Configuration

coreBOS supports multiple caching systems, including Memcached and Redis. You need to configure the CRM system to connect and communicate with the chosen caching system. This typically involves specifying the cache server's host, port, and any required authentication credentials.

This can be done in Utilities > Cache layer activation section.

![Utilities Cache](UtilitiesCache.png?width=100%)

### Cache Storage

Once the configuration is set up, coreBOS can store various types of data in the cache. This includes database query results, module-specific data, user sessions, and other frequently accessed information. When data is requested, we first must check if it exists in the cache. If found, it retrieves it from the cache, bypassing the need to query the database.

### Cache Invalidation

To ensure data consistency, coreBOS implements cache invalidation mechanisms. When a relevant record is modified or deleted, the corresponding cache entries are invalidated or cleared. This ensures that the CRM system always retrieves the most up-to-date information.

### Cache Expiration

To prevent stale data from being served indefinitely, coreBOS also supports cache expiration. You can define a time-to-live (TTL) for cache entries, after which they are automatically removed from the cache. This ensures that data is periodically refreshed from the database.

## Usage

Once the connection to the cache server is configured and activated, we will be able to use the global cache object wherever we need it in the code. This object is named `$cbAppCache`. This object is [PSR-16 compliant](https://www.php-fig.org/psr/psr-16/) and based on the [Laminas Cache library](https://docs.laminas.dev/laminas-cache/) so we support all the functionalilty they give us. We have also enhanced it with some specific coreBOS methods. In general, you can use these methods:

- **isActive**() true or false depending on the activation of the cache integration in the utilities section
- **isUsable**() true or false depending on isActive() and the health of the connection with the external cache service
- **getCacheClient**() if the integration isUsable() return the cache object we can work with. This object supports these methods
  - **get**('someKey', $defaultValue)
  - **set**('someKey', $value) When setting values, whether single values or multiple, you can also optionally provide a Time To Live (TTL) value.
  - **setMultiple**(['key1' => $value1, 'key2' => $value2])
  - **delete**('someKey')
  - **deleteMultiple**(['key1', 'key2'])
  - **has**('someKey')
  - **hasWithModuleCheck**($key, $module, $id = 0)
  - **hasWithQueryCheck**($key, $query, $queryParams = [])

The methods are very straightforward, so let's look at the two specific coreBOS methods

### hasWithModuleCheck

This method returns if a key exists based on the last modified time of modules or records in the application. It requires two parameters and a third optional one:

- $key is the key we are asking about, the key we want to know whether it is in the cache or not
- $module is the module that can invalidate the key value
- $id is the record that can invalidate the key value

The idea is that if we have a module that changes very little, for example, Business Maps, which, once the application is configured and in production, the business map module will change very little, then we can set the key value to invalidate automatically based on the last modified time of any record in the module. So, when the value is set in the cache, our cache system will write also the last modified time of the module. When you try to retrieve the key it will check that last modified time and if no record in the module has changed then the key value will be considered valid.

The same idea happens when you give the CRMID of a record but it will check only the last modified time of that specific record instead of all the records in the module.

### hasWithQueryCheck

This method returns if a key exists based on a query that you give it. It requires two parameters and a third optional one:

- $key is the key we are asking about, the key we want to know whether it is in the cache or not
- $query the query we must execute to determine if the key exists or not
- $queryParams array of parameters for the query: will be given directly to pquery

The best example to understand this usage is a Condition Expression or Query Business map. Let's suppose a business map that calculates some expression based on Sales Order records. We can use the `hasWithModuleCheck` method to invalidate the cache when the business map record changes, but we also have to consider that the expression itself, even if it hasn't changed may return a different result whenever records in the Sales Order module change. So we have to give our function a specific query that determines both conditions: if Sales Order records have changed or the business map itself has changed.

## Examples

Some code examples you can study:

- Cache library:
  - [cbCache](http://code.spike.studio:3000/EvolutivoCode/EvolutivoFW/src/branch/master/include/utils/cbCache.php)
  - [Integration cache](http://code.spike.studio:3000/EvolutivoCode/EvolutivoFW/src/branch/master/include/integrations/cache/cache.php)
- [get_user_array](http://code.spike.studio:3000/EvolutivoCode/EvolutivoFW/src/branch/master/include/utils/utils.php#L216-L217)
- [coreBOS Rule](http://code.spike.studio:3000/EvolutivoCode/EvolutivoFW/src/branch/master/modules/cbMap/cbRule.php#L23)
- Also used in Picklist extension

## Conclusion

The coreBOS cache layer is a development tool that is being used in various parts of the application already and should be extended to optimize many other parts.

Ideally, we should migrate the current memory-based cache to this library and eliminate the usage of static cache wherever we use it. To do that we must first have a solid performance and quality assurance testing infrastructure in place as the usage of cache in the application right now is widespread.

Besides the pending task of moving the existing cache to the new library, this library is completely functional and can be used, from the code, wherever we need it.

We could also design new projects like permitting the admin user to activate the cache in different parts of the application or based on some conditions and business logic. As usual, start using and keep going.
