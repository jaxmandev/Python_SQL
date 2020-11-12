# import a module that will facilitate accessing the database management system
import pyodbc

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

    # create a function that create a table in the DB
    def create_table(self):
        self.connect()
        self.table_name = input(" Enter table name: --> ")
        number_columns = int(input(" Enter how many columns? --> "))
        
        self.column_dict = {}
      
        # each for loop iteration is a database table column definition stored,
        # in the inner_query string variable
        for i in range(1, number_columns + 1):
            column_name = input(f"Enter column {i} name: ")
            column_data_type = input(f"Enter column {i} datatype: ")
            inner_query = inner_query + column_name + " " + column_data_type + ", "
            
            # created for later use, when data will be input
            self.column_dict[column_name] = column_data_type

        # inne_query string requires syntax formatting of the extra ","
        inner_query2 = inner_query[:-1]
        final_query = f"CREATE TABLE {self.table_name} ({inner_query2});"

        # execute the above and commit queries to databse
        self.cursor.execute(final_query)
        self.database_connection.commit()
        print("Table created!")

        # create a function that prompts user to input data in that table
    def input_data_to_table(self):
        data = []
        # input data into the table
        for key, value in self.column_dict:
            data.append(input(f"Enter in {key} a {value} type variable: "))
        
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

# instantiate the class
if __name__ == "__main__":
    test1 = Connector()
    test1.connect()
    test1.create_table()
    test1.input_data_to_table()