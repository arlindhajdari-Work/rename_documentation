---
title: 'How to add expression functions'
metadata:
    description: 'How to add expression functions inside the expression picker.'
    author: 'Arlind Ismalaja'
content:
    items:
        - '@self.children'
    order:
        by: date
        dir: desc
    url_taxonomy_filters: true
taxonomy:
    category:
        - webservice
        - application
    tag:
        - howto
---

The article provides a guide on adding new expression functions inside the expression picker. 
Below you can find the necessary steps and considerations for integrating custom functions.

===

!! **Note:** Please consider the current implementations before proceeding.

---

The files you need to change are:
* **`modules/com_vtiger_workflow/expression_functions/[file].php`**
    * Here, you have to define the logic of the function.
        
        ```php
            function __cb_functionname($arr) {
                // Your Logic Here ...
            }
        ```
    * There are a few standards you have to follow:
        * It is recommended that your function starts with **`__cb_`**.
        * Your function should have **only one parameter** called **`$arr`**, regardless of how many inputs your implementation actually has. As named, your input at this point is going to come as an array (of your parameters).
        * **[file]** is a placeholder for the category function. For example, if your function does string manipulation, it belongs to the file `strings.php`; if it's a math operation, it belongs to `math.php`, etc. Your function can belong to any file in this directory, otherwise is highly advised to create a new one.

* **`modules/com_vtiger_workflow/expression_engine/VTExpressionEvaluater.inc`**
    * Here, you link the function with an abstract name. This referral name is going to be used in the expression picker.

        ```php
            $this->[category] = array(
                ...
                'FunctionName' => '__cb_functionname'
            )
        ```
    * There is something to take into consideration before adding the entry inside this file. There are a few **[categories]** your function should fall into depending on the parameters it expects.
        * **Operators:** This array holds basic operations (ex. sum, sub, mul, etc.)
        * **Functions:** This holds a list of all the available functions
        * **operationsSQL:** This holds a list of all the functions that are available for the scheduled task conditions
        * **rawparams:** This holds a list of functions where their parameters are *NOT* evaluated.
        * **needscontext:** This holds a list of functions that need the context of the module that is calling them. Essentially what this does is add the entity as an additional parameter in the array, along the already defined parameters.
* **`modules/com_vtiger_workflow/expression_engine/VTExpressionsManager.inc`**

    * Here, you have to define the **name** and the **declaration** of the function as such:

        ```php
                public function expressionFunctions() {
                    global $adb;
                    return array(
                        ...
                        'FunctionName' => 'FunctionName(parameters...)'
                    );
                }
        ```

* **`modules/com_vtiger_workflow/language/[lang].fndefs.php`**
    * This part has language support, and as such you would need to modify multiple files (ex. **en_us.fndefs.php**)
    * Here, you define the function help description as shown below.

        ![workflow expression](workflowexpression.png?width=100%)

    * Follow the previous examples, but the main line of logic is this:
        ```php
        'function name' => array( // see functions in modules/com_vtiger_workflow/expression_engine/VTExpressionsManager.inc
            'name' => usually the same as the function name but may be different, will be shown to the user,
            'desc' => description of the function,
            'params' => parameters of the function, array(
                array(
                    'name' => 'param name',
                    'type' => String | Boolean | Integer | Float | Date | DateTime | Multiple | Field,
                    'optional' => true/false,
                    'desc' => 'description of the parameter',
                )
            ),
            'categories' => array of categories the function belongs to
            'examples' => array of one-line examples,
        )
        ```
---
This is pretty much all you need. You can find an example commit [here](https://code.spike.studio/EvolutivoCode/EvolutivoFW/commit/6ba209b894ad7af2d98d79d1a60caa778093b3a2).

