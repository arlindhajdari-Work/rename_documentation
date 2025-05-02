---
title: '246: speed optimization: calls to getParentTab'
metadata:
    description: '246: speed optimization: calls to getParentTab'
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
        - documentation
    tag:
        - issue
---

## Speed Optimization
### Before/After optimization: HelpDesk List view
![](optimize_getparenttab_pre_hd.png?width=100%)
![](optimize_getparenttab_pst_hd.png?width=100%)

### Before/After optimization: Accounts List view
![](optimize_getparenttab_pre_acc.png?width=100%)
![](optimize_getparenttab_pst_acc.png?width=100%)

### Conclusion
As can be seen in the images above the time spent by the getParentTab() method has been reduced significantly. This optimization won't have a big impact in the overall usage of the application, specially because we aren't optimizing the real bottle neck which is elsewhere, but all in all, every little bit helps.