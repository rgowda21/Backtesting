import backtrader as bt


class SMA(bt.Strategy):  
    params = (("sma_short", 10), ("sma_long", 200))

    def __init__(self):
        self.sma_short = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.sma_short)
        self.sma_long = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.sma_long)

    def next(self):
        if self.position:  
            if self.sma_short[0] < self.sma_long[0]: 
                self.close()

        if self.sma_short[0] > self.sma_long[0]:
            self.buy()
