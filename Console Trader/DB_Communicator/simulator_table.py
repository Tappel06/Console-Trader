'''This file contains all the methods regarding the simulator_table in console_trader_db'''

#=====Imports=====#
import sqlite3


#=====Classes=====#

class Simulator_table():

    def __init__(self):
        self.database_directory = "Database/console_trader_db"


    def simulator_table_exists(self):
        """Checks wether the simulator table exists.
        
            :returns: True if exists, False if not.

            :rtype: Boolean
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM simulator_table''')
                return True
            except Exception:
                return False


    def create_simulator_table(self):
        """Creates a simulator table in console_trader_db"""

        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Execute query
                cursor.execute('''CREATE TABLE simulator_table(
                                Simulator_id INT(7),
                                Simulator_name,
                                PRIMARY KEY(Simulator_id)
                                )''')
                # Commit the query
                db.commit()
            
            except Exception:
                # Rollback the query
                db.rollback()
                print("Could not create the simulator_table in the console_trader_db")

            finally:
                cursor.close()


    def auto_assign_id(self):
        """Finds an id that has not yet been used in the simulator_table
        
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
                    cursor.execute('''SELECT * FROM simulator_table
                                    WHERE Simulator_id = ?''', (id,))
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
                    print("Could not assign a available id for simulator_table")

                finally:
                    cursor.close()


    def create_simulator_record(self, simulator_name):
        """Creates a new record in simulator_table.
        
            :param string simulator_name: Name of the simulator.
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Create cursor
            cursor= db.cursor()

            try:
                # Executes query
                cursor.execute('''INSERT INTO simulator_table
                                VALUES(?, ?);''',
                                (self.auto_assign_id(), simulator_name,))
                # Commits changes
                db.commit()

            except Exception:
                db.rollback()
                print("Could not add new record to the simulator_table")

            finally:
                cursor.close()


    def get_all_simulator_records(self):
        """Returns a list of all the simulator records.
        
            :returns: list of simulator records.

            :rtype: list.
        """
        # Opens database
        with sqlite3.connect(self.database_directory) as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM simulator_table;''')
                # Gets list
                list = cursor.fetchall()
                return list
            
            except Exception:
                print("Could not retrieve a list from simulator_table") 


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
                cursor.execute('''DELETE FROM simulator_table
                                WHERE Simulator_id = ?;''', (id,))
                db.commit()
            
            except Exception:
                db.rollback()
                print("Could not delete record from simulator_table")

            