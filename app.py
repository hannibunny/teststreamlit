import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

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

# Display stock data charts
st.subheader("Closing Prices")
plot_stock_data(df)

st.subheader("Volume of Trades")
plot_stock_data(df)

st.subheader("Closing Price and Moving Averages")
plot_moving_averages(df)
