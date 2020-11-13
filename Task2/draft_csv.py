# import pyodbc that will facilitate accessing the database management system
import pyodbc
# # import pyodbc that will facilitate accessing csv file
import csv

class Connect:
    # the connect method will start the connection
    def __init__(self):
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
        
        # the block of code that may cause an exception is nested,
        # inside the try scope. The except block only runs if try does not
        try:
            # executes the query, and if successful prints the prompt
            with self.cursor.execute(query):
                print("Table Created!")

            # .commit() is used to save the changes and upload them to DB
            self.connection.commit()
        except:
            # concise exception handling 
            print("Encoutered an error while attempting to create {table} table.")
    
    # drop a table
    def delete_table(self, table):

        # format in order to abide by SQL syntax rules
        query = f"DROP TABLE {table};"

        try:
            # executes the query, and if successful prints the prompt
            with self.cursor.execute(query):
                print("Table Dropped!")
    
            # .commit() is used to save the changes and upload them to DB
            self.connection.commit()
        
        except:
            print("Encoutered an error while attempting to drop {table} table.")

        # update a table
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


        # display a table
        display_table(self):

        # format in order to abide by SQL syntax rules
        query = f"SELECT * FROM {table}".fetchall
        
        try:
            # executes the query, and if successful prints the prompt
            for i in cust_row:
                print(records)

def main():
    print('Available Options: C=Create, R=Read, U=Update, D=Delete ')
    choice = input('Choose your option = ')
    action = Crud()
    while True:
        if choice == 'C':
            action.create_table()
        elif choice == 'R':
            action.read_table()
        elif choice == 'U':
            action.update_table()
        elif choice == 'D':
            action.delete_table()
        else:
            print('Wrong choice.')

# call the main function
if __name__ = "__main__":
    main()