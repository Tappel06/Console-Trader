'''This file contains all the cards, such as stocks, and market influence'''

#=====Imports=====#


#=====Classes=====#

class Cards():

    def __init__(self):
        # Cards
        self.day_cards = day_cards
        self.industry_cards = industry_cards
        self.stock_cards = stock_cards

        # List of all the stocks and their details
        self.stocks = []

        # Calss the method to append all stocks
        self.append_stocks()


    def append_stocks(self):
        """appends all the stock cards into stocks list"""

        # Appends energy stocks
        for list in energy_stocks:
            self.stocks.append(list)

        # Appends material stocks
        for list in material_stocks:
            self.stocks.append(list)

        # Appends industrial stocks
        for list in industrial_stocks:
            self.stocks.append(list)

        # Appends consumer discretionary stocks
        for list in consumer_discretionary_stocks:
            self.stocks.append(list)

        # Appends consumer staple stocks
        for list in consumer_staple_stocks:
            self.stocks.append(list)

        # Appends healtcare stocks
        for list in healthcare_stocks:
            self.stocks.append(list)

        # Appends financial stocks
        for list in financial_stocks:
            self.stocks.append(list)

        # Appends information technology stocks
        for list in information_technology_stocks:
            self.stocks.append(list)

        # Appends utility stocks
        for list in utility_stocks:
            self.stocks.append(list)


#=====Functions======#

# = = = Stock cards = = = #

# = = 1. Energy stocks
energy_stocks = [["Energize", "Energy", 53.23],
                 ["Eskom", "Energy", 20.33]]

# = = 2. Materials
material_stocks = [["Cement", "Materials", 15.22],
                  ["Steel", "Materials", 10.55]]

# = = 3. Industrials
industrial_stocks = [["Logistics", "Industrial", 93.22],
                     ["Air Freight", "Industrial", 46.66]]

# = = 4. Consumer discretionary
consumer_discretionary_stocks = [["Retail", "Consumer discretionary", 35],
                   ["Travel", "Consumer discretionary", 102.00]]

# = = 5. Consumer staples
consumer_staple_stocks = [["Tobacco", "Consumer staples", 64],
                    ["Personal care", "Consumer staples", 549]]

# = = 6. Healthcare
healthcare_stocks = [["Biogen", "Healthcare", 123.23],
              ["John and sons", "Healthcare", 12.32]]

# = = 7. Financials
financial_stocks = [["Bank", "Financial", 456.00],
                    ["Insurance", "Financial", 321.22]]

# = = 8. Information technology
information_technology_stocks = [["Software", "Information technology", 222.22],
                                 ["Hardware", "Information technology", 111.11]]

# = = 9. Utilities
utility_stocks = [["Electricity", "Utilities", 66.66],
                  ["Water", "Utilities", 44.33]]


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