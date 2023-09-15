'''This file manages the database files, makes sure that the directory exists and the table's are created'''

#=====Imports=====#
from DB_Communicator.simulator_table import Simulator_table
from DB_Communicator.Stock_table import Stock_table
import os

#=====Classes=====#

class Db_manager():

    def __init__(self):
        # Creates Simulator_table object
        self.sim_table = Simulator_table()
        # Creates Stock_table object
        self.stock_table = Stock_table()


    def create_database_directory(self):
        """Creates the directory of the database if it does not exist"""

        # Check if directory exist
        if os.path.exists("Database/") == True:
            print("The directory for the database exists.")

        else:
            print("Creating database directory...")
            os.system("mkdir Database")
            print("Database directory created")


    def create_tables(self):
        """Checks if tables exist in database, creates it if they do not exist"""

        # Creates simulator table
        if self.sim_table.simulator_table_exists() == True:
            print("simulator table exists.")
        else:
            print("creating simulator table...")
            self.sim_table.create_simulator_table()
            print("simulator table created.")

        # Creates stock table
        if self.stock_table.stock_table_exists() == True:
            print("stock table exists.")
        else:
            print("creating stock table...")
            self.stock_table.create_stock_table()
            print("stock table created.")


    def manage_db(self):
        """Creates the paths and tables if necassary"""

        # Creates path
        self.create_database_directory()

        # Creates tables
        self.create_tables()



            