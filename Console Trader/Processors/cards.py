'''This file contains all the cards, such as stocks, and market influence'''

#=====Imports=====#


#=====Classes=====#

class Cards():

    def __init__(self):
        self.day_cards = day_cards
        self.industry_cards = industry_cards
        self.stock_cards = stock_cards


#=====Functions======#

# = = = Stock cards = = = #

# List for stock cards
stocks = []

# = = 1. Energy stocks
energy_stocks = [["Energize", "Energy", 53.23]
                 ["Eskom", "Energy", 20.33]
                ]

# = = 2. Materials
material

# = = 3. Industrials
# = = 4. Consumer discretionary
# = = 5. Consumer staples
# = = 6. Healthcare
# = = 7. Financials
# = = 8. Information technology
# = = 9. Utilities


# = = = Day cards = = = #

# List of Day cards
day_cards = [-0.10, -0.20, -0.25, -0.50, -0.75, -1.00, -1.25, -1.50, -1.75, -2.00,
            -2.50, -3.00, -3.50, -4.00, -5.00, -6.00, -7.00, -8.00, -9.00, -10.00,
            0.10, 0.20, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00,
            2.50, 3.00, 3.50, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]

# List of Industry cards
industry_cards = [-0.10, -0.20, -0.25, -0.50, -0.75, -1.00, -1.25, -1.50, -1.75, -2.00,
                  -2.25, -2.50, -2.75, -3.00, -3.25, -3.50, -3.75, -4.00, -4.25, -5.00,
                  0.10, 0.20, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00,
                  2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 3.75, 4.00, 4.25, 5.00]

# List of Stock cards
stock_cards = [-0.10, -0.20, -0.25, -0.50, -0.75, -1.00, -1.25, -1.50, -1.75, -2.00,
                  -2.25, -2.50, -2.75, -3.00, -3.25, -3.50, -3.75, -4.00, -4.25, -5.00,
                  0.10, 0.20, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00,
                  2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 3.75, 4.00, 4.25, 0]