import yfinance as yf
import plotly.graph_objs as go

TOP_STOCKS = [
    "ITUB4.SA",
    "VALE3.SA",
    "PETR4.SA",
    "BBAS3.SA",
    "MGLU3.SA"
]

def get_top_stocks():
    stocks = []

    for ticker in TOP_STOCKS:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="5d")

        if len(hist) < 2:
            continue

        close_today = hist["Close"].iloc[-1]
        close_yesterday = hist["Close"].iloc[-2]
        variation = ((close_today - close_yesterday) / close_yesterday) * 100

        stocks.append({
            "ticker": ticker.replace(".SA", ""),
            "price": round(close_today, 2),
            "variation": round(variation, 2)
        })

    return stocks


def get_stock_data(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    info = stock.fast_info

    return {
        "price": round(info["last_price"], 2),
        "open": round(info["open"], 2),
        "high": round(info["day_high"], 2),
        "low": round(info["day_low"], 2),
        "volume": info.get("volume", 0),
        "currency": info.get("currency", "USD")
    }

def generate_chart(ticker, period="1d", interval="5m"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist["Close"],
        mode="lines",
        fill="tozeroy",
        line=dict(color="#00c853", width=2)
    ))

    fig.update_layout(
        template="plotly_dark",
        height=420,
        margin=dict(l=30, r=30, t=20, b=20),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True),
    )

    return fig.to_html(full_html=False)