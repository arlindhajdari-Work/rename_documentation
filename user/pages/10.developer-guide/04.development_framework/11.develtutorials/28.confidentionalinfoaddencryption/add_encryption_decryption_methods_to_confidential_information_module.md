---
title: 'Add Encryption/Decryption methods to Confidential Information module'
metadata:
    description: 'Add Encryption/Decryption methods to Confidential Information module'
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
    tag:
        - encryption
        - decryption
---

These are the steps that need to be taken in order to implement a new encryption/decryption method:

- Add your new method to the switch case in encryptFields defining your encryption method function
- Add your new method to the switch case in decryptFields defining your decryption method function
- Add your new NONCE method to the switch case in getNONCE defining your method function to obtain the unique encryption code
- Define the methods themselves following the code examples of the ones that already exist
- Add your method to configuration
- Add any functionality you may require
- Check and adjust the migrate to new password method: most probably you will not have to do anything here

[You can find the PKI implementation commit here](https://github.com/tsolucio/Confidential-Information/commit/d927bc6442af4f074ccd2c886635d227f6013072)
