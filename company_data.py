import yfinance as yf

def get_stock (ticker):
    return yf.Ticker(ticker)

def get_company_info (stock):

    info = stock.info

    if not info:
        return None

    return info

def get_stock_data (stock):

    data = stock.history(period="5y")

    data["MA_5"] = data["Close"].rolling(window=5).mean()
    data["MA_20"] = data["Close"].rolling(window=20).mean()

    return data