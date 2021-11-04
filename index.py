import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
from Models.Date import Date
from Models.MovingAverage import MovingAverage
from Models.EMAManager import EMAManager

yf.pdr_override()

# Input a ticker
stock = input("Enter a stock ticker symbol: ")
print(stock)

# Start Date Object
startDate = Date(2019, 1, 1)

# Analytics from time period for inputed ticker
df = pdr.get_data_yahoo(
    stock,
    dt.datetime(startDate.year, startDate.month, startDate.day),
    dt.datetime.now()
)

emaManager = EMAManager(15, [3, 5, 8, 10, 12, 15, 30, 35, 40, 45, 50, 60])

# Appends each different EMA to the end of our data frame
for ema in emaManager.Emas:
    df[emaManager.getDisplay(ema)] = round(
        df.iloc[:, 4].ewm(span=ema, adjust=False).mean(), 2)

print(df.tail())
print(emaManager.getShortCollection())
print(emaManager.getLongCollection())

# for i in df.index:
#     cmin = min()
