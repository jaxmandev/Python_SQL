# import pyodbc that will facilitate accessing the database management system
import pyodbc

class Connect:
    # the connect method will start the connection
    def __init__(self, server, database, username, password):
        self.connection = self.connected(server, database, username, password)
        
        # create a cursor to traverse the records in the database
        self.cursor = self.connection.cursor()

    # class method to connect to 
    def connected(self, server, database, username, password):
        
        # initiate connection with server using pyodbc module
        connection = pyodbc.connect(f"""
                DRIVER=ODBC Driver 17 for SQL Server;
                SERVER={server};
                DATABASE={database};
                UID={username};
                PWD={password}""")
        return connection

class Crud(Connect):
    # create a table
    def create_table(self, table, columns):
        query = f"CREATE TABLE {table} ({', '.join(columns)});"
       
        # executes the query, and if successful prints the prompt
        with self.cursor.execute(query):
            print("Table Created!")

        # .commit() is used to save the changes and upload them to DB
        self.connection.commit()
    
    # drop a table
    def delete_table(self, table):
        query = f"DROP TABLE {table};"

        # executes the query, and if successful prints the prompt
        with self.cursor.execute(query):
            print("Table Dropped!")
        
        # .commit() is used to save the changes and upload them to DB
        self.connection.commit()
    
    # update a table
    

    # display a table