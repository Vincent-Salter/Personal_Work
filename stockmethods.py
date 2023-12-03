import matplotlib.pyplot as plt
import os
from pandas import DataFrame
from datetime import timedelta

class trading_bot_methods():

    def plot_trades(stock_data, trades):
        # Create a figure and a set of subplots
        fig, ax1 = plt.subplots()

        # Plotting stock price
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Price')
        ax1.plot(stock_data['Close'], color='tab:blue', label='Stock Price')
        ax1.tick_params(axis='y')

        # Highlighting trade dates
        buy_dates = [trade[0] for trade in trades]
        sell_dates = [trade[2] for trade in trades]
        ax1.scatter(buy_dates, stock_data.loc[buy_dates, 'Close'], color='green', label='Buy Points')
        ax1.scatter(sell_dates, stock_data.loc[sell_dates, 'Close'], color='red', label='Sell Points')

        # Instantiating a second y-axis to plot cumulative profit
        ax2 = ax1.twinx()
        ax2.set_ylabel('Cumulative Profit')
        cumulative_profit = [sum(t[4] for t in trades if t[0] <= date) for date in stock_data.index]
        ax2.plot(stock_data.index, cumulative_profit, color='tab:orange', label='Cumulative Profit')
        ax2.tick_params(axis='y')

        fig.tight_layout()
        fig.legend(loc='upper left')
        plt.show()


    def export_trades_to_csv(trades, directory, filename):
        if not filename.endswith(".csv"):
            filename += ".csv"
        filepath = os.path.join(directory, filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        trades_df = DataFrame(trades, columns=['Buy Date', 'Buy Price', 'Sell Date', 'Sell Price', 'Long Profit'])
        trades_df.to_csv(filepath, index=False)

    def backtest_strategy(stock_data, drawdown_percent, day_range):
        trades = []
        for index, row in stock_data.iterrows():
            open_price = row['Open']
            low_price = row['Low']
            if low_price <= open_price * (1 - drawdown_percent / 100):
                buy_price = low_price
                sell_date = index + timedelta(days=day_range)
                if sell_date in stock_data.index:
                    sell_price = stock_data.loc[sell_date]['Close']
                    profit = sell_price - buy_price
                    trades.append((index, buy_price, sell_date, sell_price, profit))
                else:
                    print(f"Target sell date is out of range for the data: {sell_date}")
        
        # This return statement should be outside the for loop
        return trades