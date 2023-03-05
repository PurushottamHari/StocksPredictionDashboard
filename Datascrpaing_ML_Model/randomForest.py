import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from datetime import timedelta
import pickle
from pathlib import Path
import os

def saveModelsForAllSavedCsvFiles():
    basepath = 'D:\Purushottam\Stuff\\reactProjects\DataScraping\dataset\\'
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            saveModelForStockCsvFile(basepath + entry)
            




def saveModelForStockCsvFile(csvPath):
    # First check if a model has been saved already, if not train it
    stockSymbol = Path(csvPath).stem

    if os.path.isfile('D:\Purushottam\Stuff\\reactProjects\DataScraping\models\\' + stockSymbol + '.pickle'):
        print('Model already saved for ' + stockSymbol + '!')
        return

    df = pd.read_csv(csvPath)

    df['Date']= pd.to_datetime(df['Date'])

    temporal_data = df[['Date','Low']]

    X = []
    y_true = []
    dates = []

    window_size = 14

    for i in range(0, len(temporal_data)-window_size, window_size):
        X.append(temporal_data['Low'][i:i+window_size])
        y_true.append(temporal_data['Low'][i+window_size])
        
        dates.append(temporal_data['Date'][i+window_size])


    regr = RandomForestRegressor(max_depth=3, random_state=0)

    try:
        regr.fit(X, y_true)
    except:
        print("Exception with " + stockSymbol) 


    pickle.dump(regr, open('D:\Purushottam\Stuff\\reactProjects\DataScraping\models\\' + stockSymbol + '.pickle', 'wb'))

    # y_pred = regr.predict(X)

    # mean_absolute_error(y_true, y_pred)

    # future_predictions = df[['Date','Low']][-1*window_size:]
    # future_predictions.reset_index(drop=True, inplace = True)


    # future_predictions['Date']= pd.to_datetime(future_predictions['Date'])

    # for pred in range(4):
        
    #     future_predictions = future_predictions.append(
    #         {
    #             'Date' : future_predictions.at[len(future_predictions)-1,'Date'] + timedelta(days=1), 
    #             'Low' : regr.predict([future_predictions['Low'][-1*window_size:]])[0]
    #         }, 
    #         ignore_index=True
    #     )



saveModelsForAllSavedCsvFiles()
