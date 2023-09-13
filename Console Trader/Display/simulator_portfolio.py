'''This file contains all the methods related to the simulator portfolio, identifying the portfolio'''

#=====Imports=====#
import os


#=====Classes=====#

class Simulator_portfolio():

    def __init__(self, simulator_id):
        self.simulator_id = simulator_id

        self.simulator_portfolio_options()


    def simulator_portfolio_options(self):
        """"The display options for simulator portfolio"""

        # Clear console
        os.system("cls || clear")

        fff = input(f"Welcome to simulator portfilio. id: {self.simulator_id}")

