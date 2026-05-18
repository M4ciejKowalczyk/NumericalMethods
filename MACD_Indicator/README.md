# MACD Indicator: Algorithmic Trading Simulation

## Overview
This project implements the MACD (Moving Average Convergence/Divergence) indicator from scratch to analyze financial markets and simulate an automated trading strategy. Developed as part of a Numerical Methods university course, the script calculates exponential moving averages (EMA) without relying on high-level financial libraries, generating buy and sell signals based on MACD and Signal line crossovers. 

## Features
* **Custom EMA & MACD Implementation:** Calculates the 12-period and 26-period EMAs to derive the MACD line, and a 9-period EMA for the Signal line using a recursive mathematical formula.
* **Signal Generation:** Automatically identifies transaction points (Buy: MACD crosses Signal from below; Sell: MACD crosses Signal from above).
* **Trading Simulation:** Includes a backtesting environment that starts with an initial capital of 1000 units of a given asset, executing trades based solely on the generated signals.
* **Data Visualization:** Generates comprehensive charts using `matplotlib` to visualize asset price changes, MACD/Signal crossovers, and portfolio value over time.

## Data Sources & Technologies
* **Language:** Python 
* **Libraries:** `pandas` (for data manipulation), `matplotlib` (for plotting)
* **Datasets Tested:** Historical market data for PKN Orlen (Polish stock) and Gold (XAU/USD) from January 2021 to March 2025.

## Key Findings
The simulation evaluated the effectiveness of the MACD indicator against a standard "Buy and Hold" strategy:
* **PKN Orlen:** The MACD strategy generated a profit of +6.70% (18 profitable trades, 26 loss trades), slightly outperforming the buy-and-hold approach (+5.39%).
* **Gold:** The MACD strategy yielded a significant profit of +47.74% (21 profitable, 18 loss), though it slightly underperformed the buy-and-hold strategy (+50.43%) due to extreme market volatility in late 2024.

**Conclusion:** While the MACD indicator is a robust tool for identifying long-term market trends, its reliance on moving averages introduces a lag. This delay can sometimes result in poorly timed trades during periods of rapid, short-term price fluctuations or market consolidation. 

## How to Run
1. Ensure you have Python installed along with the `pandas` and `matplotlib` libraries.
2. Provide a `.csv` file with historical price data.
3. Run `main.py` to view the analysis charts and simulation results.
