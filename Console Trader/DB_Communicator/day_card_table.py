'''THis file contains all the methods that works with the day_card table'''

#=====Imports=====#
import sqlite3


#=====Classes=====#
class Day_card_table():

    def __init__(self):
        self.database_directory = "Database/console_trader_db"


    def day_card_table_exists(self):
        """Checks wether the day card table exists.
        
            :returns: True if exists, False if not.

            :rtype: Boolean
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM day_card_table''')
                return True
            except Exception:
                return False


    def stock_table_exists(self):
        """Checks wether the day card table exists.
        
            :returns: True if exists, False if not.

            :rtype: Boolean
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM day_card_table''')
                return True
            except Exception:
                return False
            

    def create_day_card_table(self):
        """Creates a day card table in console_trader_db"""

        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Execute query
                cursor.execute('''CREATE TABLE day_card_table(
                                Day_card_id INT(7),
                                Simulator_id INT(2),
                                Percentage DECIMAL(3, 2),
                                PRIMARY KEY(Day_card_id)
                                )''')
                # Commit the query
                db.commit()
            
            except Exception:
                # Rollback the query
                db.rollback()
                print("Could not create the day_card_table in the console_trader_db")

            finally:
                cursor.close()


    def auto_assign_id(self):
        """Finds an id that has not yet been used in the day_card_table
        
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
                    cursor.execute('''SELECT * FROM day_card_table
                                    WHERE Day_card_id = ?''', (id,))
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
                    print("Could not assign a available id for day_card_table")

                finally:
                    cursor.close()


    def create_day_card_record(self, simulator_id, percentage):
        """Creates a new record in day_card_table.
        
            :param string simulator_id: The ID of the simulator.
            :param float percentage: The percentage of the the card
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Create cursor
            cursor= db.cursor()

            try:
                # Executes query
                cursor.execute('''INSERT INTO day_card_table
                                VALUES(?, ?, ?);''',
                                (self.auto_assign_id(), simulator_id,
                                 percentage,))
                # Commits changes
                db.commit()

            except Exception:
                db.rollback()
                print("Could not add new record to the day_card_table")

            finally:
                cursor.close()


    def get_all_day_card_records(self, simulator_id):
        """Returns a list of all the day card records.

            :param int simulator_id: The simulator's id.
        
            :returns: list of day card records.

            :rtype: list.
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM day_card_table
                               WHERE Simulator_id = ?;''',
                               (simulator_id,))
                # Gets list
                list = cursor.fetchall()
                return list
            
            except Exception:
                print("Could not retrieve a list from day_card_table")


    def delete_day_card_record(self, simulator_id, card_percentage):
        """Deletes a day card record from the table.
        
            :param int simulator_id: The simulator Id of the card being deleted
            :param float card_percentage: The percentage of the card being deleted.
            """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''DELETE FROM day_card_table
                                WHERE Simulator_id = ?
                                AND Percentage = ?''',
                                (simulator_id, card_percentage,))
                db.commit()
            
            except Exception:
                db.rollback()
                print("Could not delete record from day_card_table")