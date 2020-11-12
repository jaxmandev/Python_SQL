# Python with SQL and pyodbc module

### Introduction
```
1. We can use a database with Python to meet customer needs.
2. Connection is achieved via API calls.
```
### Using PYODBC
```
PYODBC - Python Open Database Connectivity
- We use this to connect to SQL from our Python program
```

### What is cursor
```
In computer science, a database cursor is a control structure that enables over the records in a database. 
```

### Functioms to know
- Steps
- Installation
1. Install the pyodbc package:
2. pip install pyodbc
3. Install Drivers Use the following commands to install drivers required for compatibility with MacOS
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
HOMEBREW_NO_ENV_FILTERING=1 ACCEPT_EULA=Y brew install msodbcsql17 mssql-tools
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
```
4. Homebrew installation of MS ODB
```
brew install msodbcsql17 mssql-tools
Once installed, create a python_sql.py file.
```
5. Setting up a connection
- Test the pyodbc module has been imported
- Define the server properties i.e. server, database, username and password. Store these as variables.
```
import pyodbc
server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "*****"
password = "******"
```
- Establish a connection with the following command.
```
# server name - database name - username and password is required to connect to pyodbc
northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
```
- Use the cursor function to execute queries. Cursor is location of your mouse/current path
```
cursor = northwind_connection.cursor()
```
- Running Queries

- We have now established a connection, we can access the database.
- We know that we have a table called Customers that has customer data available.
- Using fetchall() method, we can get all the data available in the customers table.
```
cust_row=cursor.execute("SELECT * FROM Customers").fetchall()
for records in cust_row:
    print(records)
```
- We have another table in the DB called Products
```
product_rows = cursor.execute("SELECT * FROM Products").fetchall()
```
- As with SQL, we can fetch a particular column using control flow.

```
# for each row in the database, print the UnitPrice
for x in product_rows:
    print(x.UnitPrice)
```

- We can use a while loops to ensure we only iterate through the data as long as the data is available.
```
product_row=cursor.execute("SELECT * FROM Products")
while True:
    # Returns one row at a time
    records= product_row.fetchone()
    # When no records left (value is None), stops
    if records is None:
        break
    print(records.UnitPrice)
    ```
