import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date

today = date.today()
currentDate = today.strftime("%Y-%m-%d")

st.write("""
# Stock price application
- Anurag Bandyopadhyay


Shown are the Stock Closing prices and Volume of **NVIDIA**

""")

tickerSymbol='NVDA' # Getting the symbol for this ticker

tickerData=yf.Ticker(tickerSymbol) #Getting the historical prices for this ticker
tickerDf=tickerData.history(period='1d',start='2010-05-31',end=currentDate) #Open high low close dividends and stock splits
st.write("""
## Closing price

""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume

""")
st.line_chart(tickerDf.Volume)




#St.write follows markdown syntax!
