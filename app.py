# yfinance to fetch historical stock data. It fetches historical market data from Yahoo Finance
import yfinance as yf

import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the **opening** and **closing** stock prices of Apple!

""")

# define the ticker symbol
tickerSymbol = 'AAPL'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
# fetching historical stock data for the spocified period from May 31st 2010 to May 31st 2020
# period = '1d' means daily
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open, High, Low, Close, Volume, Dividends, Stock Splits are the columns in the tickerDf

st.write("""
## Opening Price
""")
st.line_chart(tickerDf.Open)

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
