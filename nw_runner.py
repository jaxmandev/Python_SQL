# import pyodbc that will facilitate accessing the database management system
import pyodbc

# import module containing parent class
from nw_products import Connector

# create child class
class Runner(Connector):
    def __init__(self):
        def super().__init__():
        
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