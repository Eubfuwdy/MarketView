import yfinance as yf

def get_dollar():
    ticker = yf.Ticker("USDBRL=X")  
    data = ticker.history(period="1d")
    return round(data["Close"].iloc[-1], 2)

def get_euro():
    ticker = yf.Ticker("EURBRL=X")
    data = ticker.history(period="1d")
    return round(data["Close"].iloc[-1], 2)