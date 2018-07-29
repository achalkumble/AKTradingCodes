import numpy as np
import pandas as pd
import quandl
import talib
import os

os.chdir('C://Users//achal//Documents//GitHub//AKTradingCodes')


quandl.ApiConfig.api_key = '2382uQe_AhAsFNx-V96p'
tickers = pd.read_csv('nse_quandl_tickers.csv',header=None)
tickers = tickers[0].tolist()

start = '2017-01-01'
end = '2018-07-27'


stock_prices = pd.DataFrame()

for i in range(len(tickers)):
    if i == 0:
        print(tickers[i])
        stock_prices = quandl.get(tickers[i],start_date=start,end_date=end,column_index=5)
    else:
        print(tickers[i])
        stock_prices = stock_prices.join(quandl.get(tickers[i], start_date=start, end_date=end,
                                                    column_index=5),rsuffix=tickers[i])

stock_prices.columns = tickers

# UNDER RSI VALUES > 70 INDICATE OVERVALUED STOCKS AND RSI < 30 INDICATE UNDERVALUED STOCKS

rsi_values = pd.DataFrame(index=stock_prices.index,columns=tickers)

for i in tickers:
    rsi_values[i] = talib.RSI(stock_prices[i])

overvalued = 80
undervalued = 20

rsi_values.dropna(inplace=True)
rsi_values.shape

# IMPLEMENT TRADING STRATEGY

rsi_indicators = pd.DataFrame(np.zeros(rsi_values.shape),index=rsi_values.index, columns=tickers)

for i in range(len(rsi_indicators.index)):
    for j in range(len(tickers)):
        if i == 0:
            pass
        elif sum(rsi_indicators.iloc[:i,j]) == 1:
            if rsi_values.iloc[i,j] >= overvalued:
                rsi_indicators.iloc[i,j] = -1
            else:
                pass
        else:
            if rsi_values.iloc[i,j] <= undervalued:
                rsi_indicators.iloc[i, j] = 1
            else:
                pass

rsi_indicators.to_csv('rsi_indicators.csv')









