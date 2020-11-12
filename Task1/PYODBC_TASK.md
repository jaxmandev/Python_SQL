## Pre-requisites
- pip install pyodbc
- import pyodbc to use it

```
# import a module that will facilitate accessing the database management system
import pyodbc
```

## Script desciption
- Connection with the server is made and it is initialised for
- every Class object creation
```
# create a class with methods to establish connection with database
class Connector:

    # the connect method will start the connection
    def __init__(self):
        self.connect()
    
    # create a method that connects to database using default arguments
    def connect(self, server = "databases1.spartaglobal.academy", database = "Northwind", username = "**", password = "**"):

        # initiate connection with server using pyodbc module
        self.database_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        # create a cursor to traverse the records in the database
        self.cursor = self.database_connection.cursor()
```
- the cursor used to traverse the database is made in 
- the final line from the block of code above
-----
- a class method will enable the creation of tables
- the user inputs the name of the table and number of columns
``` 
    # create a method that create a table in the DB
    def create_table(self):
        self.connect()
        self.table_name = input(" Enter table name: --> ")
        number_columns = int(input(" Enter how many columns? --> "))
```
- for loop will iterate over each column to name it and 
- declare the variable type expected
```
        self.column_dict = {}
        # each for loop iteration is a database table column definition stored,
        # in the inner_query string variable
        for i in range(1, number_columns + 1):
            column_name = input(f"Enter column {i} name: ")
            column_data_type = input(f"Enter column {i} datatype: ")
            inner_query = inner_query + column_name + " " + column_data_type + ", "
```
- store the new column names and datatypes for data input (see further down)
```   
            # created for later use, when data will be input
            self.column_dict[column_name] = column_data_type
```
- notice the inner_query variable in the for loop just above has a "," as to,
- continue building the sql query. The charcater must be deleted from the end of our string variable
```
        # inne_query string requires syntax formatting of the extra ","
        inner_query2 = inner_query[:-1]
        final_query = f"CREATE TABLE {self.table_name} ({inner_query2});"

        # execute the above and commit queries to databse
        self.cursor.execute(final_query)
        self.database_connection.commit()
        print("Table created!")
```
- input_data_to_table method will prompt user to input in a given format
- input is stored in empty list
```
        # create a function that prompts user to input data in that table
    def input_data_to_table(self):
        data = []
        # input data into the table
        for key, value in self.column_dict:
            data.append(input(f"Enter in {key} a {value} type variable: "))
```       
- can insert the data into the table column of choice with INSERT INTO statement
- the control flow is a SQL query formater
```
        # insert input data into the table
        # due to python's auto string format, we need to do
        # smart formatting or the queries will not be correct
        self.list_columns_names = list(self.column_dict)
        self.list_datatypes = list(self.column_dict.values())
        for j in range(len(self.list_columns_names)):
            if 'CHAR' in self.list_datatypes:
                self.cursor.execute(f"""
                INSERT INTO {self.table_name} ({self.list_columns_names[j]})
                VALUES ('{data[j]}');
                """)
            else:
                self.cursor.execute(f"""
                INSERT INTO {self.table_name} ({self.list_columns_names[j]})
                VALUES ({data[j]});
                """)
```
- test all the methods
```
# instantiate the class
if __name__ == "__main__":
    test1 = Connector()
    test1.connect()
    test1.create_table()
    test1.input_data_to_table()
```
---------

- import the class and module needed to connect and query the database
```
# import pyodbc that will facilitate accessing the database management system
import pyodbc

# import module containing parent class
from nw_products import Connector
```
- child class inherits all the methods and attributes from parent class
```
# create child class
class Runner(Connector):
    def __init__(self):
        def super().__init__():
```        
- perform an operation in python with the data from connected database
```
            # define a function that finds the average UnitStock price
            def average_price(self):
                sql_object = self.cursor.execute("SELECT UnitsInStock FROM Products;").fetchall()
                
                # convert the python dictionary to integers
                avg_price = list()
    
                for stock in sql_object:
                    avg_price.append(int(stock[]))
                # returns the average from the integer avg list
                return sum(avg_price)/len(avg_price)

# instantiate the class with test2 object
if __name__ = "__main__":
    test2 = Runner()
    print(test2.average_price())
```