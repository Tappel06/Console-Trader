'''Contains all the methods regarding the portfolio and portfolio stock tables'''

#=====Imports=====#
from DB_Communicator.portfolio_table import Portfolio_table
from DB_Communicator.portfolio_stock_table import Portfolio_stock_table
from Processors.stock_processors import Stock_processors

#=====Classes=====#

class Portfolio_processors():

    def __init__(self):
        # Creates portfolio object
        self.portfolio = Portfolio_table()
        # Creates Portfolio stock object
        self.portfolio_stock = Portfolio_stock_table()

    
    def create_portfolio_record(self, simulator_id, cash_available):
        """Creates a portfolio record
        
            :param int simulator_id: The ID of the simulator.
            :param float cash_available: The total amount of cash that will be available
        """

        self.portfolio.create_portfolio_record(simulator_id, cash_available)

    
    def get_portfolio_record(self, simulator_id):
        """Gets the record of the portfolio.
        
            :param int simulator_id: The id of the simulator.

            :returns: a record of the portfolio.

            :rtype: list.
        """
        list = self.portfolio.get_portfolio_record(simulator_id)

        return list
    

    def get_portfolio_stock_records(self, simulator_id):
        """Gets all records from the portfolio_stock_table
        
            :param int simulator_id: The id of the simulator
        """
        # Get list from table
        list = self.portfolio_stock.get_portfolio_stock_records(simulator_id)

        return list
    

    def stock_exists(self, simulator_id, stock_name):
        """Checks if a stock exists in the portfolio_stock_table.
        
            :param int simulator_id: The id of the simulator.
            :param string stock_name: The name of the stock.

            :returns: True if it exists, false if not.

            :rtype: boolean.
        """
        list = self.get_portfolio_stock_records(simulator_id)
        for record in list:
            if record[1] == stock_name:
                return True

        return False
    

    def get_stock_total_shares(self, simulator_id, stock_name):
        """Gets the total shares of a specific stock.
        
            :param int simulator_id: The id of the simulator.
            :param string stock_name: The name of the stock.

            :returns: The total amount of shares.

            :rtype: int.
        """
        list = self.get_portfolio_stock_records(simulator_id)
        for record in list:
            if record[1] == stock_name:
                return record[2]
    

    def buy_create_or_update_stock_record(self, simulator_id, stock_name, total_shares):
        """Creates or update a stock record in the portfolio_stock_table
        
            :param int simulator_id: The simulator's ID.
            :param string stock_name: The stock's name.
            :param int total_shares: The total shares being bought
        """
        # Creates stock processor object
        stock_processor = Stock_processors(simulator_id)
        
        # Checks if if record exists or not, creates or updates acoordingly
        if self.stock_exists(simulator_id, stock_name) == False:
            # Create record
            self.portfolio_stock.create_portfolio_stock_record(simulator_id, stock_name, total_shares)

            # deduct amount from portfolio Available cash
            record = self.get_portfolio_record(simulator_id)
            old_amount = round(record[0][2], 2)
            new_amount = round(old_amount - (total_shares * stock_processor.get_stock_price(stock_name)), 2)
            self.portfolio.update_available_cash(simulator_id, new_amount)

        else:
            # Calculates new shares
            new_total_shares = self.get_stock_total_shares(simulator_id, stock_name) + total_shares
            
            # Updates shares
            self.portfolio_stock.update_stock_shares(simulator_id, stock_name, new_total_shares)

            # deduct amount from portfolio Available cash
            record = self.get_portfolio_record(simulator_id)
            old_amount = round(record[0][2], 2)
            new_amount = round(old_amount - (total_shares * stock_processor.get_stock_price(stock_name)), 2)
            self.portfolio.update_available_cash(simulator_id, new_amount)


    def sell_delete_or_update_stock_record(self, simulator_id, stock_name, total_shares):
        """Deletes or update a stock record in the portfolio_stock_table
        
            :param int simulator_id: The simulator's ID.
            :param string stock_name: The stock's name.
            :param int total_shares: The total shares being sold
        """
        # Creates stock processor object
        stock_processor = Stock_processors(simulator_id)
        
        current_total_shares = self.get_stock_total_shares(simulator_id, stock_name)
        # Checks if total shares are equal to current share, then deletes if so
        
        if current_total_shares == total_shares:

            # Update add to portfolio available cash
            record = self.get_portfolio_record(simulator_id)
            old_amount = round(record[0][2], 2)
            new_amount = round(old_amount + (total_shares * stock_processor.get_stock_price(stock_name)), 2)
            self.portfolio.update_available_cash(simulator_id, new_amount)

            # Delete record
            self.portfolio_stock.delete_record(simulator_id, stock_name)

        else:
            # Calculates new shares
            new_total_shares = self.get_stock_total_shares(simulator_id, stock_name) - total_shares
            
            # Updates shares
            self.portfolio_stock.update_stock_shares(simulator_id, stock_name, new_total_shares)

            # Update add to portfolio available cash
            record = self.get_portfolio_record(simulator_id)
            old_amount = round(record[0][2], 2)
            new_amount = round(old_amount + (total_shares * stock_processor.get_stock_price(stock_name)), 2)
            self.portfolio.update_available_cash(simulator_id, new_amount)