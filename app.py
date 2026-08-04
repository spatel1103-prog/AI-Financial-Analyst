import streamlit as st

from company_data import get_company_info, get_stock_data
from display import display_company_info, display_chart
from ai_analysis import generate_business_summary, generate_investment_recommendation, valuation_analysis, risks, growth_opportunities, ask_ai

st.title("AI Financial Analyst")
st.caption("Analyze any publicly traded company using financial data and AI generated insights.")

ticker = (st.text_input("Enter a stock ticker: ")).upper()

if st.button("Analyze"):

    st.header(f"{ticker} Analysis")

    try:
        info = get_company_info(ticker)
        data = get_stock_data(ticker)

    except Exception as e:
        st.exception(e)
        st.stop()


    # validate the ticker the user inputted
    if info is None:
        st.error("Invalid ticker.")
        st.stop()

    # fetch data from 5 years
    data = get_stock_data(ticker)

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
            risks_analysis = risks (ticker, data)
            st.write(risks_analysis)

        with st.expander ("Growth Opportunities"):
            growth = growth_opportunities(ticker)
            st.write(growth)


        st.subheader("Ask the AI")

        question = st.text_area(
         "Ask a question about this company:",
            placeholder = "Example: Is this company overvalued?"
        )

        if st.button("Ask AI"):
            answer = ask_ai(question, info, data)
            st.write(answer)