'''This file contains all the methods to running the stock market engine'''

#=====Imports=====#
import random

from DB_Communicator.Stock_table import Stock_table
from DB_Communicator.day_card_table import Day_card_table
from DB_Communicator.stock_card_table import Stock_card_table
from DB_Communicator.industry_cards import Industry_card_table
from Processors.cards import Cards

import os

#=====Classes=====#

class Stock_market_engine():

    def __init__(self, simulator_id):
        # Gets simulator id
        self.simulator_id = simulator_id

        # Create stock table object
        self.stock_table = Stock_table()
        # Creates day card object
        self.day_card = Day_card_table()
        # Creates stock card object
        self.stock_card = Stock_card_table()

        # Creates Cards object
        self.cards = Cards()

        # Createas object for each industry
        self.energy_cards = Industry_card_table("Energy")
        self.material_cards = Industry_card_table("Materials")
        self.industrial_cards = Industry_card_table("Industrial")
        self.consumer_discretionary_cards = Industry_card_table("Consumer discretionary")
        self.consumer_staple_cards = Industry_card_table("Consumer staples")
        self.healthcare_cards = Industry_card_table("Healthcare")
        self.financial_cards = Industry_card_table("Financial")
        self.information_technology_cards = Industry_card_table("Information technology")
        self.utility_cards = Industry_card_table("Utilities")

        # Creates industry list
        self.industry_list = {self.energy_cards, self.material_cards, self.industrial_cards, 
                              self.consumer_discretionary_cards, self.consumer_staple_cards, 
                              self.healthcare_cards, self.financial_cards, 
                              self.information_technology_cards, self.utility_cards}


    def load_cards_if_none(self):
        """Insert card record to database if none exist.
        
            :param int simulator_id: the simulator's id.
        """
        # Total cards to calculate
        total_cards = self.total_cards()
        # Total records calculated
        total_cards_calculated = 0

        # Print progress bar
        self.print_progress_bar(total_cards_calculated, total_cards)

        # = = Day Cards = = #

        # Gets list
        day_card_list = self.day_card.get_all_day_card_records(self.simulator_id)

        # Checks if  day cards length is 0, If so, add new day cards
        if len(day_card_list) < 1:
            # Gets list of day cards that needs to be inserted to table
            day_card_list = self.cards.day_cards
            # Insert Day card records to table
            for day in day_card_list:
                self.day_card.create_day_card_record(self.simulator_id, day)
                # Add to total cards calculated
                total_cards_calculated += 1
                # Print progress bar
                self.print_progress_bar(total_cards_calculated, total_cards)


        # = = Stock Cards = = #

        # Get all stock names
        stock_list = self.stock_table.get_all_stock_records(self.simulator_id)
        
        # Alternate through stocks
        for stock in stock_list:
            stock_card_list = self.stock_card.get_all_stock_card_records(self.simulator_id, stock[2])
            if len(stock_card_list) < 1:
                # Get list of stock cards
                stock_card_list = self.cards.stock_cards
                # Insert Stock Card Records to table
                for card in stock_card_list:
                    self.stock_card.create_stock_card_record(self.simulator_id, stock[2], card)
                    # Add to total cards calculated
                    total_cards_calculated += 1
                    # Print progress bar
                    self.print_progress_bar(total_cards_calculated, total_cards)
            
        # = = Industry Cards = = #
        
        for industry in self.industry_list:
            in_list = industry.get_all_industry_card_records(self.simulator_id)
            if len(in_list) < 1:
                # Get list of industry cards
                in_list = self.cards.industry_cards

                for in_card in in_list:
                    # Insert industry card records into into industry table
                    industry.create_industry_card_record(self.simulator_id, in_card)
                    # Add to total cards calculated
                    total_cards_calculated += 1
                    # Print progress bar
                    self.print_progress_bar(total_cards_calculated, total_cards)

        # Print final progress bar
        self.print_progress_bar(total_cards, total_cards)


    def total_cards(self):
        """The total cards in all the decks.
        
            :returns: The total number of cards from all the decks.

            :rtype: int.
        """
        # Variable for cards
        total_cards = 0

        # Counts the total day cards
        day_card_list = self.cards.day_cards
        total_cards += len(day_card_list)

        # Gets the total of stocks, and multiplies it with the total stock cards
        total_cards += len(self.cards.stocks) * len(self.cards.stock_cards)

        # Gets the total industry cards, and multiplies is with 9 (The total number of industries)
        total_cards += len(self.cards.industry_cards) * 9

        return total_cards
    

    def print_progress_bar(self, total_complete, total):
        """Prints the progress bar.
        
            :param int total_complete: The number of functions complete.
            :param int total: The actual number that should be complete.
        """
        # Calculate Percentage
        percent = round(((total_complete / total)*100), 2)
        # The total character in a load bar
        bar_char = 20
        # The total Load bar char to print
        total_print_char = int((percent / 100) * 20)

        # Clears console
        os.system("cls || clear")

        # Prints Progress
        print(f"Loading: [\033[42m{' ' * total_print_char}\033[0m{' ' * (bar_char - total_print_char)}]" 
              + f" {percent}%")
        

    def calculate_and_delete_cards(self):
        """Calculate and update stocks, then delete cards"""
        
        ##### Day Cards #####

        # List of available day cards
        day_cards = self.day_card.get_all_day_card_records(self.simulator_id)
        # gets random index number for day_cards
        random_day_card_index = random.randint(0, len(day_cards) - 1)
        # Stores day card value in variable
        day_card_value = day_cards[random_day_card_index][2]
        #print(f"day card: {day_card_value}")

        ##### Industry Cards ######

        # Dictionary for each industry
        industry_dictionary = {"Energy" : 0, "Materials" : 0, "Industrial" : 0,
                               "Consumer discretionary" : 0, "Consumer staples" : 0, "Healthcare" : 0,
                               "Financial" : 0, "Information technology" : 0, "Utilities" : 0}
        
        for industry in self.industry_list:
            # Gets list of cards in industry
            ind_list = industry.get_all_industry_card_records(self.simulator_id)
            # Gets random index number for industry cards
            random_industry_card_index = random.randint(0, len(ind_list) - 1)
            # Stores industry value in dictionary
            industry_dictionary[industry.industry_name] = ind_list[random_industry_card_index][3]

        ##### Stock Cards #####

        # Gets list of stocks
        stock_list = self.stock_table.get_all_stock_records(self.simulator_id)

        # Go through each stock individualy
        for stock in stock_list:
            # Get list of cards of specific stock
            stock_card_list = self.stock_card.get_all_stock_card_records(self.simulator_id, stock[2])
            # Gets random index number of specific stock_card_list
            rndm_stck_crd_lst = random.randint(0, len(stock_card_list) - 1)
            # Stock_card_value
            stock_card_value = stock_card_list[rndm_stck_crd_lst][3]
            
            # Total perecentage of all cards comined
            total_card_percentage = day_card_value + industry_dictionary[stock[3]] + stock_card_value
            # Resets stock if stock_card_value equals 0
            if stock_card_value == 0:
                self.stock_table.reset_stock_price(self.simulator_id, stock[2])
            else:
                # Calculate new price:
                new_price = round((stock[5] * (total_card_percentage / 100)) + stock[5], 2)
                # Update stocks in table
                self.stock_table.update_stock_current_price(self.simulator_id, stock[2], new_price)

            # Delete stock cards from stock card table
            self.stock_card.delete_stock_card_record(self.simulator_id, stock[2], stock_card_value)

        # Delete Day Card and Industry cards from table
        self.day_card.delete_day_card_record(self.simulator_id, day_card_value)

        for industry in self.industry_list:
            industry.delete_industry_card_record(self.simulator_id, industry.industry_name, 
                                                 industry_dictionary[industry.industry_name])


    def next_turn(self):
        """Implements all the required functions and calculations to update information for next turn"""

        # Checks if there are cards left in the database, Insert new ones if not.
        self.load_cards_if_none()

        self.calculate_and_delete_cards()





