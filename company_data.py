import yfinance as yf
import streamlit as st


@st.cache_data(ttl=3600)
def get_company_info(ticker):
    stock = yf.Ticker(ticker)

    return dict(stock.fast_info)

@st.cache_data(ttl=3600)
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)

    data = stock.history(period="5y")
    data["MA_5"] = data["Close"].rolling(window=5).mean()
    data["MA_20"] = data["Close"].rolling(window=20).mean()

    return data