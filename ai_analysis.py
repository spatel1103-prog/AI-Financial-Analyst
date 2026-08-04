from openai import OpenAI
import streamlit as st

client = OpenAI (api_key = st.secrets["OPENAI_API_KEY"])

def generate_business_summary ( company_name ):
    response = client.responses.create(

        model = "gpt-5",
        input = f"""""
        You are a professional financial analyst.
        
        Write a concise business summary for {company_name}.
        
        Include:
        - What the company does
        - How it makes money
        - Its primary products or services
        
        Limit the response to about 150 words
        """""
    )

    return response.output_text

def generate_investment_recommendation ( ticker, data ):
    response = client.responses.create(

        model="gpt-5",
        input=f"""""
          You are a professional financial analyst.
          
          Determine whether the stock {ticker} is a buy, sell or hold right now based on previous data and indicators {data}
          
          Write a response around 150 words explaining strengths, weaknesses, previous data and indicators and how this all contributes to the recommendation.
          """""
    )

    return response.output_text

def valuation_analysis ( ticker, data ):

    response = client.responses.create(

        model = "gpt-5",
        input=f"""
        You are a professional financial analyst.
        
        Write a few sentences explaining how the technical indicators of stock {ticker} with data {data} determine if the stock is overpriced, undervalued, etc.
        
        """
    )

    return response.output_text


def risks (ticker, data):
    response = client.responses.create(

        model="gpt-5",
        input=f"""
        You are a professional financial analyst.

        Explain the biggest risks investors should know before investing in {ticker} using {data}
        Use bullets and be concise
        """
    )


    return response.output_text

def growth_opportunities ( ticker ):
    response = client.responses.create(

        model = "gpt-5",
        input = f"""

        You are a professional financial analyst.
        Identify growth opportunities for {ticker} stock in a bulleted list.
        Make these growth opportunities based on technical indicators and fundamental analysis 
        """


    )

    return response.output_text


def ask_ai ( question, info, data ):
    response = client.responses.create(

        model="gpt-5",
        input=f"""

            You are a professional financial analyst.
            
            Company: {info["longName"]}
            Sector: {info["sector"]}
            Current Price: {info["currentPrice"]}
            MarketCap: {info["marketCap"]}
            Other Stock data: {data}
            Question: {question}
                    
            Answer in a clear way for an investor.
            If the question is unrelated to the company, or ivnveting, politely explaing that you only answer financial questions.

            """

    )

    return response.output_text