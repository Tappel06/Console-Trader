'''This file contains all the methods related to the simulator portfolio, identifying the portfolio'''

#=====Imports=====#
from Display.stock_market_menu import Stock_market_menu
import os


#=====Classes=====#

class Simulator_portfolio():

    def __init__(self, simulator_id):
        self.simulator_id = simulator_id

        # Creates stock market object
        self.stock_market_menu = Stock_market_menu(self.simulator_id)

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
                pass

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

        # Clears console
        os.system("cls || clear")

        # Print header
        print(f'''Simulator: simname
Available Funds: 0.00 coins
Portfolio value: 0.00 coins
-----------------------------              
              ''')

