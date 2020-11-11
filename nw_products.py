# SQL OOP
# 
# OOP task using pyodbc
# An sql manager for the products table
# create an object that relates only to the products table in the Northwind database. 
# The reason for creating a single object for any table within the database would be to ensure that all functionality we build into this relates to what could be defined as a 'business function'.
# 
# As an example the products table, although relating to the rest of the company, will service a particular area of the business in this scenario we will simply call them the 'stock' department.
# 
# The stock department may have numerous requirements and it makes sense to contain all the requirements a code actions within a single object.
# 
# Create two files nw_products.py & nw_runner.py and then we will move into creating our object.
# 
# Our first requirement...
# We've had a requirement for the stock department to print out the average value of all of our stock items.
# 
# Away we go....
# 
# !!!Important Note!!! It would be more efficient to write the SQL query to find the data and compute the value and simply return the value in Python.

import pyodbc

server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = northwind_connection.cursor()

def average1(any_list):
    sum(any_list) / len(any_list)

sql_object = cursor.execute("SELECT * FROM Products").fetchall()
list1 = []
for i in sql_object:
    list1.append(i.UnitPrice)
print(average1(list1))


