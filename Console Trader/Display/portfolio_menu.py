'''This file contains all the methods regarding the portfolio menu'''

#=====Imports=====#
from Processors.stock_processors import Stock_processors
from Processors.stock_market_engine import Stock_market_engine
from Processors.simulator_processors import Simulator_processors
from Processors.portfolio_processors import Portfolio_processors
from Display.sell_menu import Sell_menu
import os

#=====Classes=====#

class Portfolio_menu():

    def __init__(self, simulator_id):
        self.simulator_id = simulator_id
        # Create object of stock processors
        self.stock_processors = Stock_processors(self.simulator_id)
        # Create Stock Market engine onject
        self.stock_engine = Stock_market_engine(self.simulator_id)
        # Create portfolio processor object
        self.portfolio_processor = Portfolio_processors()
        # Creates simulator object
        self.simulator = Simulator_processors()
        

    def portfolio_options(self):
        """Displays the portfolio options"""
        # get stock list of portfolio
        stock_list = self.portfolio_processor.get_portfolio_stock_records(self.simulator_id)

        self.portfolio_header()

        while True:
            self.print_portfolio_options()

            # Print next turn and return to previous menu option
            print(f"{len(stock_list) + 1}. Next turn"
                  + f"\n{len(stock_list) + 2}. Return to previous menu")
            
            try:
                # input option
                option = int(input("\nOption: "))

                # checks if option is in range with stock_list length
                if option > 0 and option <= len(stock_list):
                    # Checks which number in range was selected
                    for i in range(len(stock_list)):
                        if option == i + 1:
                            # Creates Object for buying
                            sell_menu = Sell_menu(self.simulator_id, stock_list[i][1])
                            # Run Buy options method
                            sell_menu.sell_menu_options()
                            # clears console
                            os.system("cls || clear")
                            break
                
                elif option == len(stock_list) + 1:
                    self.stock_engine.next_turn()
                    self.portfolio_header()

                elif option == len(stock_list) + 2:
                    break

                else:
                    # Clears console
                    os.system("cls || clear")
                    print(f"\033[31m***** You did not enter a given option! *****\033[0m")
            
            except Exception:
                # Clears console
                os.system("cls || clear")
                print(f"\033[31m***** You did not enter a given option! *****\033[0m")


    def print_portfolio_options(self):
        """Prints the stock market options"""

        # Prints the stock headers
        print(f'''
Current turn: ?

Stock Name = NME
Total Shares = TS
Value = V

#    NME{" " * 17}TS{" " * 8}V{" " * 7}
{"-" * 50}''')
        self.stock_display()
        
    
    def stock_display(self):
        """Display all stocks and their details"""

        # Gets stock list
        list = self.portfolio_processor.get_portfolio_stock_records(self.simulator_id)

        # Highlight colours
        colour_1_highlight = "\033[41m\033[30m"
        colour_2_highlight = "\033[42m\033[30m"
        default_colour = "\033[0m"

        stock_current_price_colour = ""

        # Index number
        index = 1
        for stock in list:

            # Stock current price
            current_price = round(self.stock_processors.get_stock_price(stock[1]), 2)

            # Print
            print(f"{index}.{' ' * (4 - len(str(index)))}" # Index
                  + f"{stock[1]}{' ' * (20- len(str(stock[1])))}"    # Stock name
                  + f"{stock[2]}{' ' * (10- len(str(stock[2])))}"    # Total Shares
                  + f"{stock[2] * current_price}"
                )
            
            # Index plus 1
            index += 1
        
        print(f"{'-' * 50}")


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
            value = self.stock_processors.get_stock_price(stock[1])
            current_shares = self.portfolio_processor.get_stock_total_shares(self.simulator_id, stock[1])
            total_value = current_shares * value
            stocks_value += total_value

        # Print header
        print(f'''Simulator: {self.simulator.get_simulator_name(self.simulator_id)}
Available Funds: {round(record[0][2], 2)} coins
Portfolio value: {round(stocks_value + record[0][2], 2)} coins
-----------------------------             
              ''')
