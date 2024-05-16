import yfinance as yf

stocks = []
st = input("Hisse adı giriniz: ")
stocks.append(st)

for stock in stocks:
    stock_info = yf.Ticker(stock)
    hist = stock_info.history(period="1d")
    print(f"Hisse: {stock}")
    print("Şu anki Fiyat:", hist['Close'].iloc[-1])  # Son kapanış fiyatı
    print("---")