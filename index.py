import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
from Models.Date import Date
from Models.MovingAverage import MovingAverage

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

ma = MovingAverage(50)


print(ma.getMABeatsClosePercetage(df))
