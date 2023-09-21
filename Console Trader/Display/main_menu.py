'''This file contains all the methods regarding the main menu for Console Trader'''

#=====Imports=====#
from Processors.simulator_processors import Simulator_processors
from Processors.stock_processors import Stock_processors
from Display.simulator_portfolio import Simulator_portfolio
from Processors.portfolio_processors import Portfolio_processors
import os


#=====Class=====#

class Main_menu():

    def __init__(self):
        # Creates object of Simulator_processors
        self.sim_process = Simulator_processors()
        # Creates Portfolio processor object
        self.portfolio_processor = Portfolio_processors()

    def menu_options(self):
        """Displays the options of the menu"""

        # Prints logo
        self.logo()

        # Loop options
        while True:
            # Prints the menu options
            self.print_menu_Options()

            option = input("Option: ")

            # If option equals "1", run new_simulator method
            if option == "1":
                # Adds new simulator record
                self.new_simulator()
                # Prints logo
                self.logo()
                
            # If option equals "2", run load_simulator method
            elif option == "2":
                self.load_simulator()
                # Prints logo
                self.logo()

            # If option equals "3", run delete_simulator method
            elif option == "3":
                self.delete_simulators()
                # Prints logo
                self.logo()

            # If option equals "4", run about_console_trader
            elif option == "4":
                self.about_console_trader()
                # Prints logo
                self.logo()

            # If option equals "5", exit program
            elif option == "5":
                exit()

            # Else, print that an given option was not entered
            else:
                # Prints logo
                self.logo()

                # print incorrect option
                print("\n\033[31m***** YOU DID NOT ENTER A GIVEN OPTION! *****\033[0m")



    def print_menu_Options(self):
        """Print the options of the main menu"""

        print('''
1. New Simulator
2. Load Simulator
3. Delete Simulator
4. About Console Trader
5. Exit
''')


    def new_simulator(self):
        """Display menu options to create new simulator"""
        # Clear console
        os.system("cls || clear")

        # Loop
        while True:
            # Print instructions
            print("Insert the name of your new simulator, or just press \"Enter\" to cancel.\n")

            new_name = input("New simulator name: ")

            # Checks if new_name is equal to blank
            if new_name == "":
                break

            # Checks if name alread exists
            if self.sim_process.simulator_name_exists(new_name) == True:
                os.system("cls || clear")
                print("\033[31m***** This name already exists, try another! *****\033[0m\n")
                continue

            # Clear console
            os.system("cls || clear")

            # Loop
            while True:
                choice = input(f"Are you sure you want to create {new_name}? (Y/N)")

                # Checks if correct options inputed
                if choice.upper() == "Y":
                    self.sim_process.create_new_simulator(new_name)
                    # Creates object of stock_processors
                    stock_processors = Stock_processors(self.sim_process.get_simulator_id(new_name))
                    # Add stocks for specific simulator in  stock_table in db
                    stock_processors.add_stock_records_to_stock_table()
                    # Create portfolio record
                    self.portfolio_processor.create_portfolio_record(self.sim_process.get_simulator_id(new_name)
                                                                     , 2000)
                    # Enter simulator by id
                    simulator = Simulator_portfolio(self.sim_process.get_simulator_id(new_name))
                    # exits method
                    return
                
                elif choice.upper() == "N":
                    # Clears console
                    os.system("cls || clear")
                    # Exits current loop
                    break

                else: 
                    # Clear console
                    os.system("cls || clear")
                    print("\033[31m***** YOU DID NOT INSERT A CHOICE! *****\033[0m\n")


    def load_simulator(self):
        """Displays options to load simulator"""

        # Gets list of simulators
        list = self.sim_process.get_all_simulator_records()

        # Clears console
        os.system("cls || clear")

        while True:
            # Index number to be displayed
            index = 1
            # Prints list of simulators
            for record in list:
                print(f"{index}. {record[1]}")
                index += 1

            print(f"\n{index}. Return to main menu")

            try:
                # Option input
                option = int(input("\nWhich simulator do you wish to load: "))

                if option == index:
                    break

                # If option is more tha zero and less or equal to the length of list
                if option > 0 and option <= len(list):
                    # opens simulator portfolio
                    portfolio = Simulator_portfolio(self.sim_process.get_simulator_id(list[option - 1][1]))
                    break

                else: 
                    # Clears console
                    os.system("cls || clear")
                    print("\033[31m***** You did not enter a given option! ******\033[0m\n")
                

            except Exception:
                # Clears console
                os.system("cls || clear")
                print("\033[31m***** You did not insert a given option! *****\033[0m")


    def delete_simulators(self):
        """Displays options to delete a simulator"""

        # Gets list of simulators
        list = self.sim_process.get_all_simulator_records()

        # Clears console
        os.system("cls || clear")

        while True:
            # Index number to be displayed
            index = 1
            # Prints list of simulators
            for record in list:
                print(f"{index}. {record[1]}")
                index += 1

            print(f"\n{index}. Return to main menu")

            try:
                # Option input
                option = int(input("\nWhich simulator do you wish to delete: "))

                if option == index:
                    break

                # If option is more tha zero and less or equal to the length of list
                if option > 0 and option <= len(list):
                    # opens simulator portfolio
                    
                    # loop choice
                    while True:
                        # CLear console
                        os.system("cls || clear")
                        choice = input(f"Are you sure you want to delete {list[option - 1][1]}? (Y/N):")

                        if choice.upper() == "Y":
                            self.sim_process.delete_simulator(list[option - 1][0])
                            # Update list
                            list = self.sim_process.get_all_simulator_records()
                            # Clear Console
                            os.system("cls || clear")
                            break
                        
                        elif choice.upper() == "N":
                            # Clear Console
                            os.system("cls || clear")
                            break

                        else:
                            # Clears console
                            os.system("cls || clear")
                            print("\033[31m***** You did not choose Y/N! *****\033[0m\n")


                else: 
                    # Clears console
                    os.system("cls || clear")
                    print("\033[31m***** You did not enter a given option! ******\033[0m\n")
                
            except Exception:
                # Clears console
                os.system("cls || clear")
                print("\033[31m***** You did not insert a given option! *****\033[0m")


    def about_console_trader(self):
        """Displays the about of console trader"""

        # Loops options
        while True:
            # Clear console
            os.system("cls || clear")
            # Print information
            print('''About:
                  
Console Trader
                  
Version:        0.0.1 (released 2023/09/12)
                  
Created by:     Theuns Robert Pretorius, 
                founder of Ghost Software Productions
                  
Description:    The \"Console Trader\" is written in Python, and is meant to always be
                an application that runs on the Console of an operating system.
                The Application is a simulator that simulates a virtual stock market with
                fictional stocks. This application is solely meant for educational purposes,
                for people learning how the stock market works.
                  
''')
            option = input("Press enter to go back to previous menu: ")

            # If option equals ""
            if option == "":
                break


    def logo(self):
        """The logo of the program"""

        # Resets Console
        os.system("cls || clear")

        # Prints the logo
        print("\033[32mConsole Trader\033[0m. V 0.0.1\nMade by \033[33mGhost Software Productions\033[0m")