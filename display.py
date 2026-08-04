import streamlit as st

import matplotlib.pyplot as plt

def display_chart (data, ticker):
    # create graph

    fig = plt.figure(figsize=(12, 6))

    # draws lines on the graph
    plt.plot(data.index, data["Close"], label="Closing Price")
    plt.plot(data.index, data["MA_5"], label="5-Day Moving Average")
    plt.plot(data.index, data["MA_20"], label="20-Day Moving Average")

    plt.title(f"{ticker} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")

    # display graph and legend
    plt.legend()

    st.pyplot(fig)

def display_company_info (ticker, info):
    # display info about company
    st.subheader(ticker)
    #st.write(f"Sector: {info['sector']}")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"Current Price:")
        st.write(f"${info['lastPrice']:.2f}")

        # not all companies have trailing pe and dividend yield so check first then print
        pe = info.get("trailingPE")

        if pe is not None:
            st.write(f"Trailing PE:")
            st.write(f"{pe:.2f}")
        else:
            st.write("Trailing PE:")
            st.write("N/A")

        st.write("52 Week High:")
        st.write(f"${info['yearHigh']:.2f}")

    with col2:
        st.write(f"Market Cap:")
        st.write(f"${(info['marketCap'] / 1_000_000_000):.2f} Billion")

        dividend = info.get("dividendYield")

        if dividend is not None:
            st.write(f"Dividend Yield:")
            st.write(f" {dividend:.2f}%")
        else:
            st.write("Dividend Yield:")
            st.write("N/A")

        st.write(f"52 Week Low")
        st.write(f"${info['yearLow']:.2f}")


