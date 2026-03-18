import yfinance as yf

def getPrice(url):
    ticker = url.split("quote/")[1].split("?")[0]
    stock = yf.Ticker(ticker)
    price = stock.fast_info["last_price"]
    return round(price, 2)

