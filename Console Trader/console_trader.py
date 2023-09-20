'''This file contains the startup code for the console trader program'''

#=====Imports=====#
from Display.main_menu import Main_menu
from Processors.db_manager import Db_manager


#=====Run Program=====#

# Creates Db_maneger object
db_manager = Db_manager()
# Checks that tables and paths exist
db_manager.manage_db()

# Create Main_menu object
main_menu = Main_menu()
# Launch Program
main_menu.menu_options()


#=====Test Program=====#



