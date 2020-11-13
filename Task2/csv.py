# import pyodbc that will facilitate accessing the database management system
import pyodbc
# # import pyodbc that will facilitate accessing csv file
import pandas

# create a class with methods to establish connection with database
class Movie:

    # the connect method will start the connection
    def __init__(self):
        self.connect()
        self.menu()
    
    # create a method that connects to database using default arguments
    def connect(self, server = "databases1.spartaglobal.academy", database = "Northwind", username = "**", password = "**"):

        # initiate connection with server using pyodbc module
        self.database_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        # create a cursor to traverse the records in the database
        self.cursor = self.database_connection.cursor()

        # saving the movie file into a python variable
        self.movies_csv = pandas.read_csv(r'main/Users/main/Desktop/Python_SQL/Task2/imdbtitles.csv')
        # to display the file in python
        self.data_frame = pandas.DataFrame(self.movies_csv,
                                       columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult',
                                                'startYear', 'endYear', 'runtimeMinutes', 'genres'])

    def create_table_sql(self):
        # method creates imdb with all the columns provided in the csv file
        self.cursor.execute("CREATE TABLE matt_movies_table (titleType VARCHAR(255), primaryTitle VARCHAR(255), "
               "originalTitle VARCHAR(255), isAdult INT, startYear INT, endYear VARCHAR(255), runtimeMinutes VARCHAR(255), genres VARCHAR(255))")

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
            print("Encoutered an error while attempting to create table.")    
    
    def import_from_csv(self):
        # inserts data into the SQL table with the use of pandas i.e. csv -> Python -> SQL Table
        for row in self.data_frame.itertuples():
            self.cursor.execute("""
                            INSERT INTO imdb_list (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                           row.titleType,
                           row.primaryTitle,
                           row.originalTitle,
                           row.isAdult,
                           row.startYear,
                           row.endYear,
                           row.runtimeMinutes,
                           row.genres)
            self.connect.commit()
    
    def search_movie(self):
        # search the Table for a specific movie
        movie = input("What movie would you like to search for?\n -> ")
        query = pandas.read_sql_query(f""" SELECT * FROM imdb_table WHERE primaryTitle = '{movie}' """, self.connect)
        pd = pandas.DataFrame(query)
        # print table in python with all queried results
        print(pd)

    
    
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