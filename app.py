import streamlit as st

from company_data import  get_stock, get_company_info, get_stock_data
from display import display_company_info, display_chart
from ai_analysis import generate_business_summary, generate_investment_recommendation, valuation_analysis, risks

st.title("AI Financial Analyst")
st.caption("AI Financial Analyst description")

ticker = (st.text_input("Enter a stock ticker: ")).upper()

if st.button("Analyze"):

    st.header(f"{ticker} Analysis")

    stock = get_stock(ticker)

    info = get_company_info(stock)

    # validate the ticker the user inputted
    if info is None:
        st.error("Invalid ticker.")
        st.stop()

    # fetch data from 5 years
    data = get_stock_data(stock)

    # create tabs for organization
    tab1, tab2, tab3 = st.tabs([
        "Company Information",
        "Stock Chart",
        "AI Analysis"
    ])

    with tab1:
        display_company_info(info)

    with tab2:
        display_chart(data, ticker)

    with tab3:

        with st.expander ("Business Summary"):
            summary = generate_business_summary(info["longName"])
            st.write(summary)

        with st.expander ("Investment Recommendation"):
            recommendation = generate_investment_recommendation(ticker, data)
            st.write(recommendation)

        with st.expander ("Valuation Analysis"):
            valuation = valuation_analysis ( ticker, data )
            st.write(valuation)

        with st.expander ("Business Risks") :
            risks = risks (ticker, data)
            st.write(risks)

        with st.expander ("Growth Opportunities"):
            st.write()