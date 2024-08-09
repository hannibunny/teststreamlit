import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
import numpy as np

def get_stock_data(symbol, period="1y"):
    stock = yf.Ticker(symbol)
    df = stock.history(period=period)
    return df, stock.info

def plot_stock_data(df):
    st.line_chart(df['Close'], width=0, height=0, use_container_width=True)
    st.bar_chart(df['Volume'], width=0, height=0, use_container_width=True)

def plot_moving_averages(df):
    df['20d MA'] = df['Close'].rolling(window=20).mean()
    df['50d MA'] = df['Close'].rolling(window=50).mean()
    st.line_chart(df[['Close', '20d MA', '50d MA']], width=0, height=0, use_container_width=True)

st.title("Visualizing Stock Data")

# Input field for stock symbol
stock_symbol = st.text_input("Enter stock symbol", value="NVDA").upper()

# Fetch stock data
df, stock_info = get_stock_data(stock_symbol)
# Display company name and current price
st.markdown(f"**{stock_info['longName']}**")
st.markdown(f"**Current Price: ${stock_info['currentPrice']}**")

#st.write(df)
st.dataframe(df.style.highlight_max(axis=0))

# Display stock data charts
st.subheader("Closing Prices")
plot_stock_data(df)

st.subheader("Volume of Trades")
plot_stock_data(df)

st.subheader("Closing Price and Moving Averages")
plot_moving_averages(df)

st.subheader("More Experiments from streamlit tutorials")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [48.70, 9.11],
    columns=['lat', 'lon'])
st.map(map_data)
