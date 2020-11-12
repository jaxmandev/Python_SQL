
# This lesson will include connection to our SQL DB from Python using PYODBC

# pyodbc driver from microsoft helps us to connect to SQL instance
# we will connect to our Northwind DB which you have already used in SQL week

import pyodbc

server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# server name - database name - username and password is required to connecto to pyodbc

# cursor is location of your mouse/current path
cursor = northwind_connection.cursor()

cursor.execute("SELECT @@VERSION")
# select the version of current DB
# row = cursor.fetchone()
# print(row)

# in our DB we have table called Customers 
# that has customers data available
cust_row = cursor.execute("SELECT * FROM Customers;").fetchall()
for records in cust_row:
    print(records)

# we have another table in the DB called Products
product_rows = cursor.execute("SELECT * FROM Products").fetchall()
for product_records in product_rows:
    print(product_records.UnitPrice)

product_rows = cursor.execute("SELECT * FROM Products")

# combination of loop and control flow to ensure 
# we only iterate through data when data is available
while True:
    records = product_rows.fetchone()
    if records is None:
        # when no records are left, None is remaining
        break
    print(records.UnitPrice)