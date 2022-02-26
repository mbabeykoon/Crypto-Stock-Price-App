#import libraries
import streamlit as st
import yfinance as yf
from pandas_datareader import data
from datetime import datetime, timedelta

#heading 
st.write("""
# Simple Stock/Crypto Price App
""")

#define the ticker symbol according to the asset type
AsType = st.radio(
     "Asset type you need to check:",
     ('Stock', 'Cryptocurency'))

if AsType == 'Stock':
    tickerSymbol = st.text_input("Enter tickerSymbol : ","")
else:
    tickerSymbol = st.text_input("Enter Crypto pair: (Eg:BTC-USD) ","")



#get data on selected ticker
tickerData = yf.Ticker(tickerSymbol)

#get period from user
period = st.radio(
     "Time:",
     ('1w', '1d','1h','1m'))

#get number of dates from user
option = st.slider("How many days of data would you like to see?",1,3655,1)



tickerDf = tickerData.history(period, start = (datetime.today() - timedelta(option)).strftime('%Y-%m-%d'), end = datetime.today().strftime('%Y-%m-%d'))
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.markdown(f"""
Shown are the stock **closing price** and ***volume*** of:{tickerSymbol} !
""")

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)


st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)

