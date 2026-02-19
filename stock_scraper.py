
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# List of tickers to track
tickers = ["AAPL", "GOOGL", "MSFT", "AMZN"]

# Date range
start_date = "2023-01-01"
end_date = "2023-12-31"

data = {}

for ticker in tickers:
    print(f"Fetching data for {ticker}...")
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        if not stock_data.empty:
            data[ticker] = stock_data
            
            # Save to CSV
            filename = f"{ticker}_stock_data.csv"
            stock_data.to_csv(filename)
            print(f"Saved {filename}")
            
            # Plot Closing Price
            plt.figure(figsize=(12, 6))
            plt.plot(stock_data['Close'], label=f"{ticker} Close Price")
            plt.title(f"{ticker} Stock Price Trend ({start_date} to {end_date})")
            plt.xlabel("Date")
            plt.ylabel("Price ($)")
            plt.legend()
            plt.grid(True)
            plt.savefig(f"{ticker}_price_trend.png")
            print(f"Saved {ticker}_price_trend.png")
            plt.close() # Close figure to free memory
            
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")

print("\nData scraping and visualization complete.")
