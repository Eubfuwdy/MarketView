from flask import Flask, render_template, request
from services.currency import get_dollar, get_euro
from services.stocks import get_top_stocks, get_stock_data, generate_chart

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template(
        "dashboard.html",
        dollar=get_dollar(),
        euro=get_euro(),
        stocks=get_top_stocks()
    )

@app.route("/cotacoes")
def quotes():
    ticker = request.args.get("ticker")
    data = None
    chart = None

    if ticker:
        ticker = ticker.upper()
        data = get_stock_data(ticker)
        chart = generate_chart(ticker)

    return render_template(
        "quotes.html",
        ticker=ticker,
        data=data,
        chart=chart
    )

@app.route("/carteira")
def portfolio():
    return render_template("portfolio.html")


if __name__ == '__main__':
    app.run(debug=True)
