---
title: 'Module Import Permission Call Stack'
metadata:
    description: 'Module Import Permission Call Stack'
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
        - vtlib
        - module
---

### Call trace when a new module is imported

- import module
- import_sharingaccess
- module -> setDefaultSharing
- Access: syncSharingAccess
  - recalculateSharingRules
  - flushAllPrivileges(roleid)
    - recalculateSharingFile
    - foreach user
      - setUserPrivilege
      - setSharingPrivileges

- setUserPrivilege
  - createUserFile

- setSharingPrivileges
  - createSharingPrivilegeFile
    - populateSharingTmpTables
    - foreach module
      - populateSharingPrivileges (user/group read/write)
    - foreach related module share
      - populateRelatedSharingPrivileges (user/group read/write)
