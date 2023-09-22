'''This file contains all the methods regarding with the trade portfolio'''

#=====Imports=====#
import sqlite3


#=====Classes=====#

class Portfolio_stock_table():

    def __init__(self):
        self.database_directory = "Database/console_trader_db"


    def portfolio_stock_table_exists(self):
        """Checks wether the portfolio stock table exists.
        
            :returns: True if exists, False if not.

            :rtype: Boolean
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM portfolio_stock_table''')
                return True
            except Exception:
                return False
            

    def create_portfolio_stock_table(self):
        """Creates a portfolio table in console_trader_db"""

        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Execute query
                cursor.execute('''CREATE TABLE portfolio_stock_table(
                                Simulator_id INT(7),
                                Stock_name VARCHAR(30),
                                Total_stocks INT(10),

                                );''')
                # Commit the query
                db.commit()
            
            except Exception:
                # Rollback the query
                db.rollback()
                print("Could not create the portfolio_stock_table in the console_trader_db")

            finally:
                cursor.close()


    def create_portfolio_stock_record(self, simulator_id, stock_name, total_stocks):
        """Creates a new record in portfolio_stock_table.
        
            :param int simulator_id: Uses the ID of the simulator.
            :param string stock_name: The stocks name.
            :param int total_stocks: The total amount of shares in the stock
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Create cursor
            cursor= db.cursor()

            try:
                # Executes query
                cursor.execute('''INSERT INTO portfolio_stock_table
                                VALUES(?, ?, ?);''',
                                (simulator_id, stock_name, total_stocks,))
                # Commits changes
                db.commit()

            except Exception:
                db.rollback()
                print("Could not add new record to the portfolio_stock_table")

            finally:
                cursor.close()


    def update_stock_shares(self, simulator_id, stock_name, total_shares):
        """Updates the value of cash available in portfolio.
        
            :param int simulator_id: Uses the ID of the simulator. 
            :param string stock_name: The name of the stock.
            :param int total_shares: The new amount of the cash available.
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try: 
                # Executes query
                cursor.execute('''UPDATE portfolio_stock_table
                                SET Total_stocks = ?
                                WHERE Simulator_id = ?
                                AND Stock_name = ?;''', (total_shares, simulator_id, stock_name,))
                db.commit()

            except Exception:
                db.rollback()
                print("Could not update record to the portfolio_stock_table")


    def get_portfolio_stock_records(self, simulator_id):
        """Returns a list of the portfolio record.

            :param int simulator_id: Uses the ID of the simulator.
        
            :returns: list of simulator records.

            :rtype: list.
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM portfolio_stock_table
                                WHERE Simulator_id = ?;''', (simulator_id,))
                # Gets list
                list = cursor.fetchall()
                return list
            
            except Exception:
                print("Could not retrieve a list from portfolio_stock_table")


    def delete_record(self, simulator_id, stock_name):
        """Deletes the record by id.
        
            :param int simulator_id: The id of the simulator.
            :param string stock_name: The name of the stock.
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''DELETE FROM portfolio_stock_table
                                WHERE Simulator_id = ?
                                AND Stock_name = ?;''', (simulator_id, stock_name,))
                db.commit()
            
            except Exception:
                db.rollback()
                print("Could not delete record from portfolio_stock_table")