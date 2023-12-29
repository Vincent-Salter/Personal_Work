import yfinance as yf
from datetime import datetime, timedelta
from stockmethods_clone import trading_bot_methods

# Copyright Vincent Salter 02/12/23 2nd of December 2023

class StockAlgorithm:

    def __init__(self, drawdown_percent, day_range):
        pass
        ## Constructor code available upon request

    def fetch_stock_data(self, stock_symbol, start_date, end_date):
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
        return stock_data
    
    def set_drawdown_percent(self, new_drawdown_percent):
        self.drawdown_percent = new_drawdown_percent

    def set_day_range(self, new_day_range):
        self.day_range = new_day_range

    def set_date_range(self, new_start_date, new_end_date):
        self.start_date = new_start_date
        self.end_date = new_end_date

    def add_list(self, ticker):
        #add tickers to a list
        self = []
        pass
    #can i add here a method that would add a list to the object if you wanted to pull multiple tickers add them to a list then process them all

    def process_stock(self, ticker):
                # Main method code available upon request
                print(f"File saved to directory: {directory}")#how do i print a new line above here

print("Please input your parameters here.\n")
initial_drawdown_percent = float(input("Enter drawdown percent (e.g., 5 for 5%) here: "))
initial_day_range = int(input("How many days until you would like to sell?: "))

#stock_algo is the self, the self. is just changing the properties or attributes of the object
stock_algo = StockAlgorithm(initial_drawdown_percent, initial_day_range) #how is this row here assigned\\\\ creating an instance of the class to use it in the program
print("If you would like to change your parameters please type 'change' or type 'done' to finish.\n")

while True:
    ticker_input = input('Input ticker here: ') #assign this ticker_input object a property

    if ticker_input.lower() == 'change': #check if the object has the property 'change'
        new_drawdown_percent = float(input("Input new drawdown percentage: "))  # Ensure conversion to float ##
        stock_algo.set_drawdown_percent(new_drawdown_percent)

        new_day_range = int(input("Input new day range: "))  # Ensure conversion to int
        stock_algo.set_day_range(new_day_range)

    elif ticker_input.lower() == 'done':
        break

    else:
        stock_algo.process_stock(ticker_input) #run this part of the stock_algo opbject IN ITS CURRENT STATE with the ticker_input object as a parameter
