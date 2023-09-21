'''This file manages the database files, makes sure that the directory exists and the table's are created'''

#=====Imports=====#
from DB_Communicator.simulator_table import Simulator_table
from DB_Communicator.Stock_table import Stock_table
from DB_Communicator.day_card_table import Day_card_table
from DB_Communicator.stock_card_table import Stock_card_table
from DB_Communicator.industry_cards import Industry_card_table
from DB_Communicator.portfolio_table import Portfolio_table
from DB_Communicator.portfolio_stock_table import Portfolio_stock_table
import os

#=====Classes=====#

class Db_manager():

    def __init__(self):
        # Creates Simulator_table object
        self.sim_table = Simulator_table()
        # Creates Stock_table object
        self.stock_table = Stock_table()
        # Creates Day_card object
        self.day_card = Day_card_table()
        # Creates stock card table
        self.stock_card_table = Stock_card_table()
        # Creates an object for Industry table
        self.energy = Industry_card_table("Energy")
        # Creates a portfolio table object
        self.portfolio = Portfolio_table()
        # Creates a portfolio stock table object
        self.portfolio_stocks = Portfolio_stock_table()


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

        # Creates day card table
        if self.day_card.day_card_table_exists() == True:
            print("day card table exists.")
        else:
            print("creating day card table...")
            self.day_card.create_day_card_table()
            print("day card table created.")

        # Creates stock card table
        if self.stock_card_table.stock_card_table_exists() == True:
            print("stock card table exists.")
        else:
            print("creating stock card table...")
            self.stock_card_table.create_stock_card_table()
            print("stock card table created.")

        # Creates Industry table. only need to create it once
        if self.energy.industry_card_table_exists() == True:
            print("industry card table exists.")
        else:
            print("creating industry card table...")
            self.energy.create_industry_table()
            print("industry card table created.")

        # Creates portfolio table. only need to create it once
        if self.portfolio.portfolio_table_exists() == True:
            print("portfolio table exists.")
        else:
            print("creating portfolio table...")
            self.portfolio.create_portfolio_table()
            print("portfolio table created.")

        # Creates portfolio stock table. only need to create it once
        if self.portfolio_stocks.portfolio_stock_table_exists() == True:
            print("portfolio stock table exists.")
        else:
            print("creating portfolio table...")
            self.portfolio_stocks.create_portfolio_stock_table()
            print("portfolio stock table created.")


    def manage_db(self):
        """Creates the paths and tables if necassary"""

        # Creates path
        self.create_database_directory()

        # Creates tables
        self.create_tables()



            