'''This file contains all the methods regarding the stock market menu'''

#=====Imports=====#
from Processors.stock_processors import Stock_processors
from Processors.stock_market_engine import Stock_market_engine
import os

#=====Classes=====#

class Stock_market_menu():

    def __init__(self, simulator_id):
        self.simulator_id = simulator_id
        # Create object of stock processors
        self.stock_processors = Stock_processors(self.simulator_id)
        # Create Stock Market engine onject
        self.stock_engine = Stock_market_engine(self.simulator_id)
        


    def stock_market_options(self):
        """Displays the stock market options"""
        # get stock list
        stock_list = self.stock_processors.get_all_stock_records()

        # CLears console
        os.system("cls || clear")
        while True:
            self.print_stock_market_options()

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
                            # clears console
                            f = input(f"option {i + 1} was selected.")
                            os.system("cls || clear")
                            break
                
                elif option == len(stock_list) + 1:
                    self.stock_engine.next_turn()
                    # clears console
                    os.system("cls || clear")

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


    def print_stock_market_options(self):
        """Prints the stock market options"""

        # Prints the stock headers
        print(f'''
Current turn: ?

Stock Name = NME
Current Price = CP
Price change since beginnining = P%B

#    NME{" " * 17}CP{" " * 8}P%B{" " * 7}
{"-" * 50}''')
        self.stock_display()
        
    
    def stock_display(self):
        """Display all stocks and their details"""

        # Gets stock list
        list = self.stock_processors.get_all_stock_records()

        # Highlight colours
        colour_1_highlight = "\033[41m\033[30m"
        colour_2_highlight = "\033[42m\033[30m"
        default_colour = "\033[0m"

        stock_current_price_colour = ""
        percentage_colour = ""

        # index number
        index = 1
        for stock in list:
            
            # Decides stock current price colour
            if stock[5] > stock[4]:
                stock_current_price_colour = colour_2_highlight
            
            elif stock[5] < stock[4]:
                stock_current_price_colour = colour_1_highlight

            else:
                stock_current_price_colour = default_colour

            # Print
            print(f"{index}.{' ' * (4 - len(str(index)))}"
                  + f"{stock[2]}{' ' * (20- len(str(stock[2])))}"    # Stock name
                  + f"{stock_current_price_colour}{stock[5]}{' ' * (10- len(str(stock[5])))}\033[0m"  # Stock current price
                  + f"{stock_current_price_colour}{self.calculate_percentage(stock[4], stock[5])}%\033[0m" # Percentage
                )
            
            # Index plus 1
            index += 1
        
        print(f"{'-' * 50}")
            

    def calculate_percentage(self, default_stock, current_stock):
        """Calculates the percentage.
        
            :param float default_stock: The default stock price
            :param float current_stock: The current stock price

            :returns: Percentage

            :rtype: float
        """
        # If current stock price is smaller than beginning
        if current_stock < default_stock:
            percentage = ((current_stock - default_stock) / default_stock) * 100
            return round(percentage, 2)
        
        # If current stock price is bigger than beginning
        elif current_stock > default_stock:
            percentage = ((current_stock / default_stock) - 1) * 100
            return round(percentage, 2)
        
        else:
            return 0


