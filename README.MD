# Simple Stock Analysis Tool (SSAT)

## Overview

The Simple Stock Analysis Tool (SSAT) is a graphical user interface (GUI) application that performs technical analysis on ETFs or stocks using a CSV file as input. The application calculates key technical indicators such as Simple Moving Averages (SMA), Relative Strength Index (RSI), and Moving Average Convergence Divergence (MACD). Based on these indicators, the application provides a recommendation to buy, hold, or sell the ETF/stock. The results and plots are displayed in a modern and user-friendly interface.

## Features

- **Load CSV File**: Users can load a CSV file containing historical price data.
- **Technical Indicators**: Calculates 50-day SMA, 200-day SMA, RSI, MACD, and Signal Line.
- **Recommendation**: Provides a recommendation (buy, hold, or sell) based on the latest data.
- **Visualization**: Displays the price chart with SMAs, RSI, and MACD in a modern and interactive plot.

## Requirements

- Python 3.x
- pandas
- matplotlib
- tk

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/simple-stock-analysis-tool.git
    cd simple-stock-analysis-tool
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python stock_analysis.py
    ```

2. Load your CSV file:
    - Click the "Load CSV File" button and select the CSV file containing your ETF or stock data.
    - The application will automatically analyze the data and display the results and plots.

## CSV File Format

The CSV file should have the following columns:

- `Date`: The date of the price data (YYYY-MM-DD format).
- `Open`: The opening price.
- `High`: The highest price.
- `Low`: The lowest price.
- `Close`: The closing price.
- `Adj Close`: The adjusted closing price.
- `Volume`: The trading volume.

Example:
```csv
Date,Open,High,Low,Close,Adj Close,Volume
2023-01-01,100,110,90,105,105,1000000
2023-01-02,106,115,95,110,110,1500000
...
## Explanation of Technical Indicators

- **Simple Moving Average (SMA)**: The average price over a specified period. The 50-day SMA and 200-day SMA are commonly used to identify trends.
- **Relative Strength Index (RSI)**: A momentum oscillator that measures the speed and change of price movements. An RSI above 70 indicates overbought conditions, while an RSI below 30 indicates oversold conditions.
- **Moving Average Convergence Divergence (MACD)**: A trend-following momentum indicator that shows the relationship between two moving averages of a security’s price. The MACD line is the difference between the 12-day EMA and the 26-day EMA. The Signal Line is the 9-day EMA of the MACD line.

### Decision Criteria for Recommendation

- **Buy**: The latest closing price is above both the 50-day SMA and the 200-day SMA, the RSI is below 70, and the MACD is above the Signal Line.
- **Sell**: The latest closing price is below both the 50-day SMA and the 200-day SMA, the RSI is above 70, or the MACD is below the Signal Line.
- **Hold**: Any other condition.

### Example

After loading the CSV file, the application will display:
- A plot with the price and moving averages.
- A plot with the RSI.
- A plot with the MACD and Signal Line.
- A recommendation to buy, hold, or sell based on the latest data.

### Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to improve the application.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
``
