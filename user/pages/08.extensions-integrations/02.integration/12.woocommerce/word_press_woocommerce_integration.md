---
title: 'WordPress Woocommerce Integration'
metadata:
    description: 'WooCommerce is an ecommerce plugin for WordPress. It makes creating and managing an online store simple, with reasonable levels of flexibility and several vital features such as inventory and tax management, secure payments, and shipping integration.'
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
        - woocommerce 
---

This integration supports a two-way synchronization of products and customers between the two applications and a one-way synchronization of orders from the WordPress website to your coreBOS. So we will be able to automatically receive all our website orders inside coreBOS where we can manage them in our business logic while triggering all our workflows and business processes.

===

Once configured the integration just works transparently in the background.

The configuration has two parts, one in coreBOS and the other in WooCommerce.

**In WooCommerce**

1. go to WooCommerce &gt; Settings &gt; Advanced &gt; REST API
    ![](woocommercerestapi1.png?width=100%)

2. set a name for the access
3. select a user (admin)
4. give Read/Write permission
5. click next to see the consumer key and secret. Copy these values as you will need to give them to coreBOS
6. select the "webhooks" option (next to REST API)
   ![](woocommercenot.png?width=90%)

7. add new web hooks for
    1.  Product Create, Update, Delete and Restore
    2.  Customer Create, Update, Delete and Restore
    3.  Order Create, Update, Delete and Restore
8. give them names and make them Active
9. set the URL to `https://your_corebos_server/your_corebos/notifications.php?type=wcintegration`
10. define a strong secret and copy it to save it in coreBOS later
11. use the latest API version (3 minimum)
12. now activate and define the taxes for your website

**In coreBOS**

1.  go to the Integrations page in Utilities `https://your_corebos_server/your_corebos/index.php?module=Utilities&action=index`
2.  Click on the WooCommerce section
    ![](cbwoocommerceconfig.png?width=100%)

3. set the consumer key, the consumer secret, and the notifications secret which you set in WooCommerce
4. set the WordPress URL
5. select the default modules we will sync with. WooCommerce has three entities: Products, Customers, and Orders. In coreBOS, we can map Customers to Accounts or Contacts, Products to Products or Services, and Orders to SalesOrders or Invoices. You must define the modules you want to work with by default. Despite this selection, you can still synchronize the other modules for Customers and Products.
6.  If you have different taxes for each product on your site, yo have to define the same taxes on corebos and after you have to create two business maps to indicate each corebos tax is on woocommerce.
    
    1.  Go to a product in your woocommerce and look available taxes that you have.
    
    ![](product_taxes_list.png?width=50%)
    
    2.  Check that you have the sames taxes on your coreBOS
    ![](corebos-taxes.png?width=100%)

    3. Set global variable **Inventory_Tax_Type_Default** in corebos to value equal to **individual**
    
    4. Found the internal values for each tax on you woocommerce, inspecting code on the picklist that we showed you in step 1.
    ![](inspect-taxes-picklist-to-know-names.png?width=100%)
    Standar tax, always will be an empty value. Don't worry we have controlled on our corebos code integration if you indicate the name standart.
    
    5. Go to Business Maps module in your corebos and create a new map to indicate tax names in woocommerce what tax are in corebos, with the next name.

    **WC2ProductsTaxes**

```xml
<map>
  <originmodule>
    <originname>woocommerce</originname>
  </originmodule>
  <targetmodule>
    <targetname>Products</targetname>
  </targetmodule>
  <fields>
    <field>
      <fieldname>tax1</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>standard</OrgfieldName>
          <OrgfieldID>21.000</OrgfieldID>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>tax2</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>reducido-10</OrgfieldName>
          <OrgfieldID>10.000</OrgfieldID>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>tax3</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>super-reducido-4</OrgfieldName>
          <OrgfieldID>4.000</OrgfieldID>
        </Orgfield>
      </Orgfields>
    </field>
  </fields>
</map>
```
  6. Now just you need to create an ohter map but in the other way with the next name.

  **Products2WCTaxes**

```xml
<map>
  <originmodule>
    <originname>Products</originname>
  </originmodule>
  <targetmodule>
    <targetname>woocommerce</targetname>
  </targetmodule>
  <fields>
    <field>
      <fieldname>standard</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>tax1</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>reducido-10</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>tax2</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>super-reducido-4</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>tax3</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
  </fields>
</map>
```
7.  finally, you have to activate the message queue processor which is done in the operating system with the command `php include//cbmqtm/run.php` you have to make sure this process is running continuously for the integration to work

Here you have a video presentation of the steps and the functionality.

* <a href="https://www.youtube.com/watch?v=eUhGmZK4zlQ&t=30s">coreBOS-WooCommerce Integration</a>

These are the two maps I used for testing:

**WC2Products**

```xml
<map>
  <originmodule>
    <originname>woocommerce</originname>
  </originmodule>
  <targetmodule>
    <targetname>Products</targetname>
  </targetmodule>
  <fields>
    <field>
      <fieldname>productsheet</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>slug</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
    <field>
      <fieldname>description</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>description</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
  </fields>
</map>
```

**Products2WC**

```xml
<map>
  <originmodule>
    <originname>Products</originname>
  </originmodule>
  <targetmodule>
    <targetname>woocommerce</targetname>
  </targetmodule>
  <fields>
    <field>
      <fieldname>stock_quantity</fieldname>
      <Orgfields>
        <Orgfield>
          <OrgfieldName>qtyinstock</OrgfieldName>
        </Orgfield>
      </Orgfields>
    </field>
  </fields>
</map>
```

<div class="notices blue">
We have created a module named <strong>wcProductImage</strong> which is supported natively by this integration. It permits you to save images with meta information that will be sent to WooCommerce. Contact us if you are interested.
</div>

### Links

- [WordPress Woocommerce](https://woocommerce.com/)
- [WooCommerce API - PHP Client](https://github.com/woocommerce/wc-api-php)
- [Woocommerce REST API](http://woocommerce.github.io/woocommerce-rest-api-docs/?php)
- This integration uses the [coreBOS Message Queue](../../../10.developer-guide/04.development_framework/11.develtutorials/24.corebos_mqtm)

### Frequently Asked Questions

<strong> How can we send HTML descriptions to WooCommerce and back </strong>

In WooCommerce the description will be stored in the **wp\_posts** table inside **post\_content** column. In general WordPress uses some filters to encode and decode the value of **post\_content** before saving and displaying it. You need to use Wordpress **wp\_insert\_post\_data** hook to modify the passed value of **post\_content** before saving it to the database.

You can modify that hook like this:

```php
add_filter( 'wp_insert_post_data' , 'filter_post_data' , '99', 2 );

function filter_post_data( $data , $postarr ) {
  // Change post content
  $data['post_content'] = html_entity_decode($data['post_content']);
  return $data;
}
```


The goal is to save the raw data with html tags on the database. That script can be added to your child theme’s **functions.php** file or via a plugin that allows custom functions to be added.
