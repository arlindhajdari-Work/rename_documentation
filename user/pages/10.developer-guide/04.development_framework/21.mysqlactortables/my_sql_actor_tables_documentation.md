---
title: 'MySQL Actor Tables documentation'
body_classes: title-center title-h1h2
metadata:
    description: 'How to configure the application to access an internal or external MySQL table as if it were an internal module.'
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

How to configure the application to access internal or external flat MySQL tables as if they were internal modules

===

  [TOC]

## Prerequisites

!! **Note**: The table you are referring to must always have a **Primary Key** or an **autoincrement** field named **`id`**!

#### For Users

1. You need to be logged in as **`admin`**.
2. There are entries that **have to be present** for the installation to work normally. The core ones are protected by deletion, but either way, mind your footing.
3. The implementation is very delicate and everything you define has to be accurate.
4. There are multiple fail-safes implemented to make the work as smooth as possible. Otherwise, the main indication of a bad configuration is in the **`Home`** module, where it fails to load.
5. When using foreign modules, don't forget to **define their permissions**.
6. Normally when everything goes right, the page will reload. If it doesn't, try hard-reloading by using **`CTRL + Shift + R`**. If there is an issue, there is a message that will tell you which module failed to insert and where. Otherwise, look out for things that misbehave.

#### For developers
!! **Note:** If you are getting any errors related to mssql, be sure that both the container and the database are built correctly. The script for inserting the **`unit test data`** for MSSQL is called **`insertMssqlEntries.sh`** and can be located in the root directory of the folder. Since this integration is optional, **THE SCRIPT IS NOT RUN BY DEFAULT !**

1. On **`foreign modules`**, be mindful that the first thing to check for is the necessary drivers for the connection to be established. One indication of this is this error: **```Uncaught Error: Call to undefined function 'driverHandler'_query()```**.
2. The main database tables that this implementation inserts into are:
  * **cb_ws_permissiontables**: Here resides the permission mapping.
  * **vtiger_ws_entity**: For the **`WS`** to refer to the new table, the new entry has to be present here.
  * **vtiger_ws_entity_tables**: This links the **`WS Entity`** insert with its corresponding table.
  * **vtiger_ws_entity_name**: This links the **`WS Entity`** insert with the name that youre defining it as.
3. The table **`cb_ws_permissiontables`** needs to be loaded along with the menu, thus is not present as a changeset. It is defined and created in **`evvtMenuUtils.php`**.

## How to access

Once you land on the home page of any (CoreBOS, Evolutivo) install:

1. Visit `Utilities`.
2. Go to `Permission Mapping`.
3. Navigate the configuration.

## How to use

!!! * You can start working only after the **`no errors found`** prompt.
!!! * On window load, the feature checks the current DB configuration. This can also be done manually using the **`Check DB Configuration`** button.
!!! * Please refer to the **`Known Issues`** section if any unexpected behavior occurs, otherwise report it to the assigned person.
!!! * If there is any error, please refer **`Prerequisites > For Developers > No. 2`** on how to fix it.

* You can use the implementation to create new **`Actor`** modules which are represented by flat tables. There are two scenarios:
    - The flat table is local, in the same environment.
    - The flat table is foreign, in a remote environment.

#### Local Environment Actor Tables:

**Defining a new local `Actor`**:
1. Click on the **`Add Row`** button.
2. The fields presented are as follows:
  - **`Alias`**: This field represents the name of the new **Actor**. You are going to use this name whenever you refer to the **Actor**.
  - **`Real Module`**: This dropdown represents the module where the **actor** should take the permissions from. If set to **`--None--`**, you are allowed to define custom permissions.
  - **`Table Name`**: This field is the DB table the **actor** represents .
  - **`Name Fields`**: This field represents the name of the **`Primary Column`** of the DB Table. If unsure, leave it empty.
  - **`Handler Path`**: This field represents the path of the **Handler File**.
  > This field is autocompleted in all cases, **don't edit unless necessary**.
  - **`Handler Class`**: This field represents the working class inside the **Handler Path**.
  > This field is autocompleted in all cases, **don't edit unless necessary**.
  - **`Is Module`**: This boolean is required only if the entry represents a **`Module`** and not an **`Actor`**.
  - **`Is Foreign`**: This boolean is required only if the entry represents a table in a remote environment. When foreign, the user is prompted to provide the necessary DB configuration to create a connection.
  - **`A C R W`**: This boolean group represents the permissions of the **Actor** module. Corresponding to: **Access**, **Create**, **Read**, **Write**.
      > This group is only available if the **`Real Module`** is set to **`--None--`**.
  - **`Actions`**: This button is used to remove the configuration entry.
         > Can only be done if there are no present errors.
1. Click **`Save`**, the window should reload. The user is prompted If there is any error during the procedure.

#### Remote Environment Actor Tables:

!!! It is not necessary to fill the **`Table Name`** field when defining remote actors.

**Defining a new remote `Actor`**:

1. Fill in the:
  - **`Alias`** field.
  - Define the permissions using either the **`Real Module`** dropdown, or the **`Permissions`** grouping.
2. Tick the **`Is Foreign`** box and fill in the DB Configuration. Once done, click **`Save`**. The window will close.
3. Click **`Save`** to update the permission mapping. The window should reload if the process was completed successfully.

## Connecting to a Remote Database Server

!!! * Please refer to **`Prerequisites`** before navigating this section.
!!! * The supported PearDB types are:
!!!    `fbsql, ibase, informix, msql, mssql, mysql, mysqli, oci8, odbc, pgsql, sqlite and sybase`
!!! * Currently only MySQL and MSSQL have been implemented and tested.

! * Take note of the hostname you're using and what environment the install is running on.

#### Connecting to a MySQL Server

To connect to a **`MySQL Server`**, use **`mysqli`** as the **`database type`** when defining the DB Configuration of a foreign module. It's fully compatible with all **`CRUD`** operations. **No additional driver install is required**.

#### Connecting to an MSSQL Server

! **MSSQL requires an additional driver to work with PHP.**
! You can find the documentation (Ubuntu, MacOS) in the links below:
! > https://learn.microsoft.com/en-us/sql/connect/php/installation-tutorial-linux-mac?view=sql-server-ver16
!
! > https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-! for-sql-server?view=sql-server-ver16&tabs=alpine18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline
! 
! Test your installation using this snippet:
! ```php=
! <?php
! $serverName = "yourServername";
! $connectionOptions = array(
!     "database" => "yourDatabase",
!     "uid" => "yourUsername",
!     "pwd" => "yourPassword"
! );
! 
! function exception_handler($exception) {
!     echo "<h1>Failure</h1>";
!     echo "Uncaught exception: " , $exception->getMessage();
!     echo "<h1>PHP Info for troubleshooting</h1>";
!     phpinfo();
! }
! 
! set_exception_handler('exception_handler');
! 
! // Establishes the connection
! $conn = sqlsrv_connect($serverName, $connectionOptions);
! if ($conn === false) {
!     die(formatErrors(sqlsrv_errors()));
! }
! 
! // Select Query
! $tsql = "SELECT @@Version AS SQL_VERSION";
! 
! // Executes the query
! $stmt = sqlsrv_query($conn, $tsql);
! 
! // Error handling
! if ($stmt === false) {
!     die(formatErrors(sqlsrv_errors()));
! }
! ?>
! 
! <h1> Success Results : </h1>
! 
! <?php
! while ($row = sqlsrv_fetch_array($stmt, SQLSRV_FETCH_ASSOC)) {
!     echo $row['SQL_VERSION'] . PHP_EOL;
! }
! 
! sqlsrv_free_stmt($stmt);
! sqlsrv_close($conn);
! 
! function formatErrors($errors)
! {
!     // Display errors
!     echo "<h1>SQL Error:</h1>";
!     echo "Error information: <br/>";
!     foreach ($errors as $error) {
!         echo "SQLSTATE: ". $error['SQLSTATE'] . "<br/>";
!         echo "Code: ". $error['code'] . "<br/>";
!         echo "Message: ". $error['message'] . "<br/>";
!     }
! }
! ?>
! ```
! 
! > **Note**: You can find this script also in `build/HelperScripts` as `testMSSQLConnection.php`. Configure the connection as below, and run it.
! ```php=2
! $serverName = "hostname";
! $connectionOptions = array(
!     "database" => "database",
!     "uid" => "username",
!     "pwd" => "password"
! );
! ```

To connect to a **`MSSQL Server`**, use **`mssqlnative`** as the **`database type`** when defining the DB Configuration of a foreign module. As of this date, only **`SELECT`** operations are supported.

The following queries have been tested to be working correctly:

1. **Nested SELECT**:
```sql
SELECT (SELECT id_num from new_employees WHERE id_num = 1)
FROM new_employees
WHERE id_num = 1;
```
2. **ORDER BY**:
```sql
SELECT id_num FROM new_employees ORDER BY fname ASC, lname ASC;
```
3. **LIKE**
```sql
SELECT id_num FROM new_employees WHERE fname LIKE '%a%';
```
4. **LIMIT**
```sql
SELECT id_num FROM new_employees WHERE id_num = 1 LIMIT 1;
```

Other operations are not supported due to **Microsoft SQL Engine** syntax differentiation.
> Refer to **What's Next** section for more information.

#### Using the test environment

!!! **Note**: We created a MSSQL container in the **`yaml`** file of the dockerized CoreBOS. The credentials are **`username: sa`** and **`password: 121212AbAbAb`**. The main reason is to be able to support unit testing for the feature.

When using the feature in the **test** environment, set the hostname as the container name. Be sure to confirm if you have trouble connecting.

As of 2023, the install's DB container is called **`db`**, while the **`Microsoft SQL Server`** is called **`mssql`**.

## Known Issues

* The installation will crash if there is at least one wrong configuration. You can notice it in the **`Home`** module, or **`Webservice Playground (CBWSDev)`**. There are no apparent Apache logs, so keep that in mind.
* ~~If you have a foreign module and then select **`--None--`** as the **`Real Module`**, the **`Is Foreign`** box will be disabled.~~
* **`Handler Path`** and **`Handler Class`** columns will be removed on a future update and instead added as optional settings in **`Actions`**.
* Sometimes the window will not reload. You can try hard-reloading it using **`CTRL + Shift + R`**. Notice if there are configuration issues.

## What's Next

### How was MSSQL Supported

Inside **`VtigerActorOperation`** there is a function called **`query($q)`**. This executes the generated query. We further enhanced the functionality to translate the query before executing. We have laid the ground to allow support for DB Engines other than MySQL. Below you can have a look at the code. Using **SQL Parser** is highly appreciated.

```php
public function query($q) {
    $mysql_query = $this->wsVTQL2SQL($q, $meta, $queryRelatedModules);
    $mysql_query = $this->translateQuery($mysql_query, $this->dbDriverType);
    return $this->querySQLResults($mysql_query, $q, $meta, $queryRelatedModules);
}

private function translateQuery($q, $dbDriverType) {
    switch ($dbDriverType) {
        case 'mssqlnative':
            return $this->translateMSSQL($q);
            break;

        default:
            return $q;
            break;
    }
}

private function translateMSSQL($q) {
    /* MSSQL support for LIMIT, ORDER BY and LIKE stay the same */
    if (preg_match('/limit\s+(\d+)/i', $q, $matches)) {
        $limit = $matches[1];
        $q = preg_replace('/LIMIT\s+(\d+)/i', '', $q);
        $q = preg_replace('/SELECT\s+/i', 'SELECT TOP '.$limit.' ', $q);
    }
    return $q;
}
```

Secondly, encryption is **mandatory** for MSSQL. We disabled it by modifying the **`connect($dieOnError = false)`** function inside **`PearDatabase.php`**, which poses a security flaw. There is support for SSL inside of CoreBOS, but adding it for MSSQL is a challenge for another time. 

```php
public function connect($dieOnError = false) {
    global $dbconfig;
    if (!isset($this->dbType)) {
        $this->println('DB Connect: DBType not specified');
        return;
    }
    $this->database = ADONewConnection($this->dbType);
    $this->database->setConnectionParameter('Encrypt', 'no');
```
!!! **Note**: You will have a notice in the `DEBUG` logs regarding the encryption. That is not crashing anything, but regardless is there.

When the **WS** tries to describe the remote table, MSSQL doesn't return a **`Primary Key`** attribute. We used **`auto_increment`** instead.

```php
$dataKey = (isset($dbField->primary_key) && $dbField->primary_key)  || (isset($dbField->auto_increment) && $dbField->auto_increment);

if (($dbField->not_null && !$dataKey) || (isset($dbField->unique_key) && $dbField->unique_key == 1)) {
    $typeOfData = $fieldType.'~M';
} else {
    $typeOfData = $fieldType.'~O';
}
```

Lastly, the queries inside the **`CBForeignActorOperation`** have been adjusted. For reliability concerns, the handler tests the DB connection before instantiating the class. To support the **MSSQL**, the following `switch / case` has been implemented.

```php
switch ($dbtype) {
	case 'mssqlnative':
	case 'mysqli':
		$result = $edb->pquery('SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME=?', [$tableName]);
		break;
	default:
		throw new WebServiceException(WebServiceErrorCode::$UNKNOWNOPERATION, 'Unsupported database type');
		break;
}
```

## Further support for MSSQL operations

The main issue remains the syntax incompatibility. At no point were we able to get the rest of the **`CRUD`** operations working smoothly since the **WS** is built ground-up using MySQL. As mentioned in the section above, you **CAN** use a query translator to pick up the work.
