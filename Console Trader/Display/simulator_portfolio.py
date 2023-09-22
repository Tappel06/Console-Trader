'''This file contains all the methods related to the simulator portfolio, identifying the portfolio'''

#=====Imports=====#
from Display.stock_market_menu import Stock_market_menu
from Display.portfolio_menu import Portfolio_menu
from Processors.simulator_processors import Simulator_processors
from Processors.portfolio_processors import Portfolio_processors
from Processors.stock_processors import Stock_processors
import os


#=====Classes=====#

class Simulator_portfolio():

    def __init__(self, simulator_id):
        self.simulator_id = simulator_id

        # Creates stock market menu object
        self.stock_market_menu = Stock_market_menu(self.simulator_id)
        # Creates portfolio menu object
        self.portfolio_menu = Portfolio_menu(self.simulator_id)

        # Creates simulator object
        self.simulator = Simulator_processors()
        # Creates Portfolio processor object
        self.portfolio_processor = Portfolio_processors()
        # Creates stock_processor object
        self.stock_processor = Stock_processors(self.simulator_id)

        self.simulator_portfolio_options()


    def simulator_portfolio_options(self):
        """The display options for simulator portfolio"""

        # Print header, and clears console
        self.portfolio_header()

        # Loop options
        while True:
            # Prints options
            self.print_portfolio_options()

            option = input("\nOption: ")

            # If option equals "1" run stocks_menu() (Seperate class)
            if option == "1":
                self.stock_market_menu.stock_market_options()
                # Print header, and clears console
                self.portfolio_header()

            # If option equals "2" run My_Portfolio_menu() (Seperate class)
            if option == "2":
                self.portfolio_menu.portfolio_options()
                # Print header, and clears console
                self.portfolio_header()

            # If option equals "3", Break.
            if option == "3":
                break

            # If option equals "4", Exit.
            if option == "4":
                exit()


    def print_portfolio_options(self):
        """Prints the options for the portfolio"""
        
        print('''1. Stocks
2. My Portfolio
3. Main Menu
4. Exit''')


    def portfolio_header(self):
        """Displays the header of the portfolio"""

        # Record of the portfolio
        record = self.portfolio_processor.get_portfolio_record(self.simulator_id)

        # Gets list of records in portfolio_stock_table
        records = self.portfolio_processor.get_portfolio_stock_records(self.simulator_id)

        # Clears console
        os.system("cls || clear")

        # Calculates the value of of current shares
        stocks_value = 0
        for stock in records:
            value = self.stock_processor.get_stock_price(stock[1])
            current_shares = self.portfolio_processor.get_stock_total_shares(self.simulator_id, stock[1])
            total_value = current_shares * value
            stocks_value += total_value

        # Print header
        print(f'''Simulator: {self.simulator.get_simulator_name(self.simulator_id)}
Available Funds: {round(record[0][2], 2)} coins
Portfolio value: {round(stocks_value + record[0][2], 2)} coins
-----------------------------             
              ''')

