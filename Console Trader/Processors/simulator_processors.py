'''This file contains all the method that process the data from the simulator table in the database'''

#=====Imports=====#
from DB_Communicator.simulator_table import Simulator_table


#=====Classes=====#
class Simulator_processors():

    def __init__(self):
        self.sim_table = Simulator_table()


    def create_new_simulator(self, simulator_name):
        """Creates a new record in the simulator table.
        
            :param string simulator_name: The simulator being created's name
        """

        self.sim_table.create_simulator_record(simulator_name)


    def get_all_simulator_records(self):
        """Gets all the simulator records.
        
            :returns: A list of all the simulator records.

            :rtype: list.
        """
        list = self.sim_table.get_all_simulator_records()
        return list


    def get_simulator_id(self, simulator_name):
        """Gets the id of a specific simulator.
        
            :param string simulator_name: The name of the simulator.

            :returns: The id of the simulator.

            :rtype: int
        """
        # Gets list of simulators
        list = self.get_all_simulator_records()

        # Checks if simulator_name matches with the record name, returns the id if so
        for record in list:
            if record[1] == simulator_name:
                return record[0]
            

    def get_simulator_name(self, simulator_id):
        """Gets the id of a specific simulator.
        
            :param string simulator_name: The name of the simulator.

            :returns: The id of the simulator.

            :rtype: int
        """
        # Gets list of simulators
        list = self.get_all_simulator_records()

        # Checks if simulator_name matches with the record name, returns the id if so
        for record in list:
            if record[0] == simulator_id:
                return record[1]
            

    def simulator_name_exists(self, simulator_name):
        """Checks wether a simulator name exists, return true if so.
        
            :param string simulator_name: The name of the simulator.

            :returns: True if it exists, False if not

            :rtype: boolean
        """
        # Gets list of simulator records
        list = self.get_all_simulator_records()

        # Checks wether simulator name exists
        for record in list:
            if simulator_name == record[1]:
                return True

        # Return false if no name matched in for loop    
        return False
    

    def delete_simulator(self, id):
        """Deletes all trace of simulator.
        
            :param int id: The id of the simulator.
        """
        self.sim_table.delete_record_by_id(id)