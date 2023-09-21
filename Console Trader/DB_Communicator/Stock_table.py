'''This file contains all the methods regarding the stock_table in console_trader_db'''

#=====Imports=====#
import sqlite3


#=====Classes=====#

class Stock_table():

    def __init__(self):
        self.database_directory = "Database/console_trader_db"
        pass


    def stock_table_exists(self):
        """Checks wether the stock table exists.
        
            :returns: True if exists, False if not.

            :rtype: Boolean
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM stock_table''')
                return True
            except Exception:
                return False
            

    def create_stock_table(self):
        """Creates a stock table in console_trader_db"""

        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Execute query
                cursor.execute('''CREATE TABLE stock_table(
                                Stock_id INT(7),
                                Simulator_id INT(7),
                                Name VARCHAR(30),
                                Industry VARCHAR(30),
                                Default_price DECIMAL(10, 2),
                                Current_price DECIMAL(10, 2),
                                PRIMARY KEY(Stock_id)
                                );''')
                # Commit the query
                db.commit()
            
            except Exception:
                # Rollback the query
                db.rollback()
                print("Could not create the stock_table in the console_trader_db")

            finally:
                cursor.close()


    def auto_assign_id(self):
        """Finds an id that has not yet been used in the stock_table
        
            :returns: An available ID number

            :rtype: int
        """
        # current id
        id = 1
        # Loop
        while True:
            # Opens Database
            with sqlite3.connect(self.database_directory) as db:
                # Creates cursor
                cursor = db.cursor()

                try:
                    #Executes query
                    cursor.execute('''SELECT * FROM stock_table
                                    WHERE Stock_id = ?''', (id,))
                    # Gets a list of records from cursor
                    list = cursor.fetchall()
                    
                    # Checks if list length is less than 1
                    if len(list) < 1:
                        # Break loop and return value
                        return id
                    
                    else:
                        # Id plus 1
                        id += 1
                    
                except Exception:
                    print("Could not assign a available id for stock_table")

                finally:
                    cursor.close()


    def create_stock_record(self, simulator_id, stock_name, stock_industry, default_price):
        """Creates a new record in stock_table.
        
            :param string simulator_name: Name of the simulator.
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Create cursor
            cursor= db.cursor()

            try:
                # Executes query
                cursor.execute('''INSERT INTO stock_table
                                VALUES(?, ?, ?, ?, ?, ?);''',
                                (self.auto_assign_id(), simulator_id,
                                 stock_name, stock_industry,
                                 default_price, default_price,))
                # Commits changes
                db.commit()

            except Exception:
                db.rollback()
                print("Could not add new record to the stock_table")

            finally:
                cursor.close()


    def get_all_stock_records(self, simulator_id):
        """Returns a list of all the stock records.

            :param int simulator_id: The simulator's id.
        
            :returns: list of stock records.

            :rtype: list.
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM stock_table
                               WHERE Simulator_id = ?;''',
                               (simulator_id,))
                # Gets list
                list = cursor.fetchall()
                return list
            
            except Exception:
                print("Could not retrieve a list from stock_table") 


    def reset_stock_price(self, simulator_id, stock_name):
        """Resets a stock's price back to its default price.
        
            :param int simulator_id: The simulator's id.
            :param string stock_name: The stock's name.
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''UPDATE stock_table
                                SET Current_price = Default_price
                                WHERE Simulator_id = ?
                                AND Name = ?;''',
                                (simulator_id, stock_name,))
                db.commit()
            
            except Exception:
                db.rollback()
                print("Could not update stock to default price in stock_table")


    def update_stock_current_price(self, simulator_id, stock_name, new_price):
        """Updates a stock's current price back to its default price.
        
            :param int simulator_id: The simulator's id.
            :param string stock_name: The stock's name.
            :param string new_price: The new price for the stock.
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''UPDATE stock_table
                               SET Current_price = ?
                                WHERE Simulator_id = ?
                                AND Name = ?;''',
                                (new_price, simulator_id, stock_name,))
                db.commit()
            
            except Exception:
                db.rollback()
                print("Could not update stock to default price in stock_table")