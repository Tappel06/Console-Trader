'''This file contains all the methods regarding the buy menu for Console Trader'''

#=====Imports=====#

import os
from Processors.portfolio_processors import Portfolio_processors
from Processors.simulator_processors import Simulator_processors
from Processors.stock_processors import Stock_processors


#=====Classes=====#

class Sell_menu():

    def __init__(self, simulator_id, stock_name):
        self.simulator_id = simulator_id
        self.stock_name = stock_name

        # Creates Portfolio processor object
        self.portfolio_processor = Portfolio_processors()
        # Creates simulator process object
        self.simulator = Simulator_processors()
        # Creates stock processor object
        self.stock_processor = Stock_processors(self.simulator_id)


    def sell_menu_options(self):
        """Options for the buy menu"""

        # Record of the portfolio
        record = self.portfolio_processor.get_portfolio_record(self.simulator_id)

        # Prints header
        self.portfolio_header()

        while True:
            try:
                shares = int(input("Enter \'0\" to cancel\nAmount of shares to sell: "))

                if shares == 0:
                    return
                
                if shares > self.portfolio_processor.get_stock_total_shares(self.simulator_id, self.stock_name):
                    self.portfolio_header()
                    print(f"\033[31m***** You don't have that much shares! *****\033[0m\n")

                else:
                    # Print header
                    self.portfolio_header()
                    while True:

                        choice = input(f"\nAre you sure you want to sell {shares} shares? (Y/N): ")

                        if choice.upper() == "Y":
                            # update(sell) / delete record
                            self.portfolio_processor.sell_delete_or_update_stock_record(self.simulator_id, self.stock_name, shares)
                            return
                    
                        elif choice.upper() == "N":
                            return
                    
                        else:
                            # Print header
                            self.portfolio_header()
                            print(f"\033[31m***** You did not insert a choice! *****\033[0m\n")

            except Exception:
                self.portfolio_header()
                print(f"\033[31m***** You did not enter an amount of shares! *****\033[0m\n")


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
Sell {self.stock_name} shares

Price per share: {self.stock_processor.get_stock_price(self.stock_name)}

You can sell up to {self.portfolio_processor.get_stock_total_shares(self.simulator_id, self.stock_name)} shares
              ''')