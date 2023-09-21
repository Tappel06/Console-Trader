'''This file contains all the methods that connects and manipulates data of the stock_table in console_trader_db'''

#=====Imports=====#
from Processors.cards import Cards
from DB_Communicator.Stock_table import Stock_table

#=====Classes======#

class Stock_processors():

    def __init__(self, simulator_id):
        # The simulator in use's id
        self.simulator_id = simulator_id

        # Creates stock object of Cards
        self.cards = Cards()
        # Creates stock table object
        self.stock_table = Stock_table()

    
    def add_stock_records_to_stock_table(self):
        """Stores the stocks to stock_table the moment a new simulator is created"""
        
        # Gets the list of stocks to be stored to database
        stock_list = self.cards.stocks

        # Stores each stock in the database
        for stock in stock_list:
            self.stock_table.create_stock_record(self.simulator_id, stock[0], stock[1], stock[2])


    def get_all_stock_records(self):
        """Gets all the records of the stocks
        
            :returns: a list of records of the stocks from database

            :rtype: list
        """
        # Gets list
        list = self.stock_table.get_all_stock_records(self.simulator_id)
        return list
    

    def get_stock_price(self, stock_name):
        """Gets the current price of a stock
        
            :param string stock_name: The name of the stock

            :returns: current price

            :rtype: float
        """
        # Get list of stocks
        list = self.get_all_stock_records()

        # find specific stock
        for stock in list:
            if stock[2] == stock_name:
                return stock[5]





    