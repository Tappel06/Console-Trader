'''This file contains all the methods regarding with the trade portfolio'''

#=====Imports=====#
import sqlite3


#=====Classes=====#

class Portfolio_table():

    def __init__(self):
        self.database_directory = "Database/console_trader_db"


    def portfolio_table_exists(self):
        """Checks wether the portfolio table exists.
        
            :returns: True if exists, False if not.

            :rtype: Boolean
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM portfolio_table''')
                return True
            except Exception:
                return False
            

    def create_portfolio_table(self):
        """Creates a portfolio table in console_trader_db"""

        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Execute query
                cursor.execute('''CREATE TABLE portfolio_table(
                                Simulator_id INT(7),
                                Total_turns INT(7),
                                Cash_available DECIMAL(15, 2),
                                PRIMARY KEY(Simulator_id)
                                )''')
                # Commit the query
                db.commit()
            
            except Exception:
                # Rollback the query
                db.rollback()
                print("Could not create the portfolio_table in the console_trader_db")

            finally:
                cursor.close()


    def create_portfolio_record(self, simulator_id, cash_available):
        """Creates a new record in portfolio_table.
        
            :param int simulator_id: Uses the ID of the simulator.
            :param string simulator_id: The Simulator's id.
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Create cursor
            cursor= db.cursor()

            try:
                # Executes query
                cursor.execute('''INSERT INTO portfolio_table
                                VALUES(?, ?, ?);''',
                                (simulator_id, 0, cash_available))
                # Commits changes
                db.commit()

            except Exception:
                db.rollback()
                print("Could not add new record to the portfolio_table")

            finally:
                cursor.close()


    def update_available_cash(self, simulator_id, updated_amount):
        """Updates the value of cash available in portfolio.
        
            :param int simulator_id: Uses the ID of the simulator. 
            :param float updated_amount: The new amount of the cash available
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try: 
                # Executes query
                cursor.execute('''UPDATE portfolio_table
                                SET Cash_available = ?
                                WHERE Simulator_id = ?;''', (updated_amount, simulator_id,))
                db.commit()

            except Exception:
                db.rollback()
                print("Could not update record to the portfolio_table")


    def update_turns(self, simulator_id, turns):
        """Updates the value of cash available in portfolio.
        
            :param int simulator_id: Uses the ID of the simulator.
            :param float turns: The new amount of turns taken
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try: 
                # Executes query
                cursor.execute('''UPDATE portfolio_table
                                SET Total_turns = ?
                                WHERE Simulator_id = ?;''', (turns, simulator_id,))
                db.commit()

            except Exception:
                db.rollback()
                print("Could not update record to the portfolio_table")


    def get_portfolio_record(self, simulator_id):
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
                cursor.execute('''SELECT * FROM portfolio_table
                                WHERE Simulator_id = ?;''', (simulator_id,))
                # Gets list
                list = cursor.fetchall()
                return list
            
            except Exception:
                print("Could not retrieve a list from portfolio_table")


    def delete_record_by_id(self, id):
        """Deletes the record by id.
        
            :param int id: The id of the simulator.
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''DELETE FROM portfolio_table
                                WHERE Simulator_id = ?;''', (id,))
                db.commit()
            
            except Exception:
                db.rollback()
                print("Could not delete record from portfolio_table")