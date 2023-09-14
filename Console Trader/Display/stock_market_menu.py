'''This file contains all the methods regarding the stock market menu'''

#=====Imports=====#
import os

#=====Classes=====#

class Stock_market_menu():

    def __init__(self):
        self.simulator_id = 0


    def stock_market_options(self, simulator_id):
        """Displays the stock market options"""
        
        # Stores Simulator id
        self.simulator_id = simulator_id

        # CLears console
        os.system("cls || clear")

        while True:
            self.print_stock_market_options()
            f = input()


    def print_stock_market_options(self):
        """Prints the stock market options"""

        # Prints the stock headers
        print(f'''
Current turn: ?

Stock Name = NME
Current Price = CP
Last Price = LP
Price change since beginnining = P%B

NME{" " * 17}CP{" " * 8}LP{" " * 8}P%B{" " * 7}
{"-" * 50}''')

