
import yfinance as yf

ticker = yf.Ticker("AAPL")
history = ticker.history(period="1y")

if history.empty:
    print("No stock data found.")
else:
    start_price = history["Close"].iloc[0]
    end_price = history["Close"].iloc[-1]

    total_return = (
        (end_price / start_price) - 1
    ) * 100

    print("Company: Apple")
    print(f"Starting price: {start_price:.2f}")
    print(f"Ending price: {end_price:.2f}")
    print(f"Total return: {total_return:.2f}%")
