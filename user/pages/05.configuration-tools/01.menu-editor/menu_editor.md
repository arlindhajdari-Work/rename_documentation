---
title: 'Menu Editor'
metadata:
    description: 'Menu Editor'
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
        - adminmanual
    tag:
        - menu
        - menueditor
---

The coreBOS Menu Editor is a tool within the coreBOS application that allows users to customize and manage the menu structure and entries. It provides a user-friendly interface for organizing and configuring the application's menu.

===

Here are the key aspects of the coreBOS Menu Editor:

1. **Action Panel and Tree View**: The menu editor interface consists of two main panels. The panel on the right side is the action panel, where any changes made will immediately take effect and reflect in the menu tree displayed on the left side.

2. **Menu Tree**: The tree view on the left side displays the menu elements in a hierarchical structure. It allows users to see all the menu entries, including those that are not currently visible, and provides the ability to order them by dragging and dropping. To save the changes made to the menu structure, users must click the save button.

3. **Visibility Control**: Users can add new menu elements without making them visible to others until they are ready. By creating an element with the "visible" property unchecked, users can work on it privately and then check the visibility when they have finished placing it in the desired location.

In addition to the standard features, there are a few hidden features available for debugging and fixing purposes:

- **Debug Mode**: Adding "&menudebug=1" to the URL activates the debug mode, which shows the order of the menu entries. This can be helpful for troubleshooting or understanding the menu structure.

- **Reorder Menu Action**: Using the action "Save" and the module "evvtMenu" with the parameter "evvtmenudo=fixOrder" in the URL, users can reorder the menu entries by assigning them incremental consecutive numbering. This can be useful if there is a need to reorganize the menu systematically.

- **Fixing Orphaned Entries**: In rare cases where the left menu tree fails to load, possibly due to a JavaScript error and a message saying "loading" but no progress, it could be caused by a menu entry not having a parent menu. To fix this issue, a utility function can be executed by visiting the following URL: `http://your_server/your_corebos/index.php?action=Save&module=evvtMenu&evvtmenudo=fixOrphaned`. This utility function sets all orphaned entries to the top level, allowing users to enter and organize them as required.

The coreBOS Menu Editor provides users with a convenient way to customize and manage the application's menu structure, enabling them to tailor the menu to their specific needs and preferences.

### Design

The design of the menu editor is like this:

-   The panel on the right is an action panel, anything you do there will take effect immediately and reflect on the left panel tree.
-   The tree on the left is so you can see all the elements, even the non-visible ones and order them by drag and drop. Once you have ordered the entries as you need you must click the save button to make those changes permanent.
-   If you want to add an element but not have it seen by anyone until you have it in place, create it with the "visible" property unchecked and then check it when you are finished placing it.

### - [Menu Selection](../01.menu-editor/01.menuselection)