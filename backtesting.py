import backtrader as bt
import datetime
from sma import SMA
import yfinance as yf

data_df = yf.download("AAPL", start="2018-01-01", end="2024-01-01")


data_df = data_df[['Open', 'High', 'Low', 'Close', 'Volume']]  
data_df.columns = ['open', 'high', 'low', 'close', 'volume']  
data_df.index = data_df.index.tz_localize(None)

data = bt.feeds.PandasData(dataname=data_df)  # Ensure this is a DataFrame, not a tuple


cerebro = bt.Cerebro()
cerebro.addstrategy(SMA)
cerebro.adddata(data)
cerebro.broker.set_cash(10000)

cerebro.run()
cerebro.plot()