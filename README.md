
# 📈 Real-Time Stock Market Data Scraper & Tracker

An automated tool to fetch, analyze, and visualize real-time stock market data using the Yahoo Finance API (`yfinance`).

## 🚀 Overview
This script automates the process of retrieving historical stock data for major tech companies (AAPL, GOOGL, MSFT, AMZN). It saves the raw data for further analysis and generates trend visualizations.

## 🔑 Key Features
- **Automated Data Retrieval**: Fetches 1 year of historical data for multiple tickers.
- **Data Storage**: Saves daily OHLCV (Open, High, Low, Close, Volume) data to CSV files.
- **Trend Visualization**: Automatically generates and saves closing price trend charts.
- **Error Handling**: Robust error handling for network issues or invalid tickers.

## 🛠️ Tech Stack
- **Python 3.x**
- **yfinance** (Yahoo Finance API Wrapper)
- **Pandas** (Data Management)
- **Matplotlib** (Visualization)

## 📦 Installation
1.  Clone the repository:
    ```bash
    git clone https://github.com/sololeveling-01/stock-market-scraper.git
    cd stock-market-scraper
    ```
2.  Install dependencies:
    ```bash
    pip install yfinance pandas matplotlib
    ```

## 🏃‍♂️ Usage
Run the scraper:
```bash
python stock_scraper.py
```
This will:
1.  Download data for AAPL, GOOGL, MSFT, AMZN.
2.  Save `[TICKER]_stock_data.csv` files.
3.  Generate `[TICKER]_price_trend.png` charts.

## 📝 Future Improvements
- Add technical indicators (RSI, MACD).
- Implement a simple email alert system for price thresholds.
