'''THis file contains all the methods that works with the industry_card table'''

#=====Imports=====#
import sqlite3


#=====Classes=====#
class Industry_card_table():

    def __init__(self, Industry_name):
        self.database_directory = "Database/console_trader_db"
        self.industry_name = Industry_name
            

    def industry_card_table_exists(self):
        """Checks wether the industry card table exists.
        
            :returns: True if exists, False if not.

            :rtype: Boolean
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM industry_card_table''')
                return True
            except Exception:
                return False
            

    def create_industry_table(self):
        """Creates a industry card table in console_trader_db"""

        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Execute query
                cursor.execute('''CREATE TABLE industry_card_table(
                                Industry_card_id INT(7),
                                Simulator_id INT(7),
                                Industry_name VARCHAR(30),
                                Percentage DECIMAL(3, 2),
                                PRIMARY KEY(Industry_card_id)
                                )''')
                # Commit the query
                db.commit()
            
            except Exception:
                # Rollback the query
                db.rollback()
                print("Could not create the industry_card_table in the console_trader_db")

            finally:
                cursor.close()


    def auto_assign_id(self):
        """Finds an id that has not yet been used in the industry_card_table
        
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
                    cursor.execute('''SELECT * FROM industry_card_table
                                    WHERE Industry_card_id = ?''', (id,))
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
                    print("Could not assign a available id for industry_card_table")

                finally:
                    cursor.close()


    def create_industry_card_record(self, simulator_id, percentage):
        """Creates a new record in industry_card_table.
        
            :param int simulator_id: The ID of the simulator.
            :param float percentage: The percentage of the the card
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Create cursor
            cursor= db.cursor()

            try:
                # Executes query
                cursor.execute('''INSERT INTO industry_card_table
                                VALUES(?, ?, ?, ?);''',
                                (self.auto_assign_id(), simulator_id, 
                                 self.industry_name, percentage,))
                # Commits changes
                db.commit()

            except Exception:
                db.rollback()
                print("Could not add new record to the industry_card_table")

            finally:
                cursor.close()


    def get_all_industry_card_records(self, simulator_id):
        """Returns a list of all the industry card records.

            :param int simulator_id: The simulator's id.
        
            :returns: list of industry card records.

            :rtype: list.
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM industry_card_table
                               WHERE Simulator_id = ?
                               AND Industry_name = ?;''',
                               (simulator_id, self.industry_name,))
                # Gets list
                list = cursor.fetchall()
                return list
            
            except Exception:
                print("Could not retrieve a list from industry_card_table")


    def delete_industry_card_record(self, simulator_id, industry_name, card_percentage):
        """Deletes a industry card record from the table.
        
            :param int simulator_id: The simulator Id of the card being deleted.
            :param string industry_name: The name of the industry
            :param float card_percentage: The percentage of the card being deleted.
            """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''DELETE FROM industry_card_table
                                WHERE Simulator_id = ?
                                AND Industry_name = ?
                                AND Percentage = ?''',
                                (simulator_id, industry_name, card_percentage,))
                db.commit()
            
            except Exception:
                db.rollback()
                print("Could not delete record from industry_card_table")