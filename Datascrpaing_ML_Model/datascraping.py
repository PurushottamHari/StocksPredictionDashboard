import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
from yahoo_fin import stock_info as si
import os

# nifty50Ticker = pd.DataFrame( si.tickers_nifty50() )
nasdaqDf = pd.read_csv('D:\Purushottam\Stuff\\reactProjects\DataScraping\stockSymbols\\nasdaq_screener_1677928122370.csv')

# sym1 = set( symbol for symbol in nifty50Ticker[0].values.tolist() )

for index, row in nasdaqDf.iterrows():
    stockSymbol = row['Symbol']
    if os.path.isfile('D:\Purushottam\Stuff\\reactProjects\DataScraping\dataset\\' + stockSymbol + '.csv'):
        print('CSV already saved for ' + stockSymbol + '!')
        pass

    try:
        df = yf.download(stockSymbol)
        if(len(df) == 0): 
            print('Data empty for ' + stockSymbol)
        else:     
            df.to_csv('D:\Purushottam\Stuff\\reactProjects\DataScraping\dataset\\' + stockSymbol + '.csv')
    except:
        print("Exception with " + stockSymbol)