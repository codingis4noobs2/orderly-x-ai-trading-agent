# AlphaWaveTrader - Machine Learning Crypto Trading Strategy

## Overview
**AlphaWaveTrader** is a machine learning-based trading strategy that executes trades on the **ETH/USDT** pair. The strategy integrates technical indicators, historical market data, and a pre-trained machine learning model to predict market trends and make automated buy/sell decisions. It aims to maximize returns while managing risk through the use of technical analysis indicators.

This repository contains the necessary code, models, and resources to set up and deploy the trading strategy, along with backtesting results.

## Team Members
- **codingis4noobs2** (Owner)
---

## Project Setup

### Step 1: Create a Virtual Environment
First, create and activate a virtual environment to manage project dependencies:

```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On Windows:
env\Scripts\activate

# On macOS/Linux:
source env/bin/activate
```

### Step 2: Install Dependencies
Once the virtual environment is activated, install all required dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
Run the `setup_account.py` script to generate the `.env` file, which will contain the necessary environment variables:

```bash
python setup_account.py
```

This will create a `.env` file that holds the GCP project ID and the path to the Google Cloud service account credentials.

### Step 4: Configure Google Cloud Project
1. Obtain your **Google Cloud Project ID**.
2. Create a **service account** in your GCP project with the role: **Basic -> Owner**.
3. Make sure you have enabled BigQuery API.
4. Download the service account JSON file and place it in the project directory.
5. Update the `.env` file with the following fields:

```env
GCP_PROJECT_ID=your_gcp_project_id
GOOGLE_APPLICATION_CREDENTIALS=path_to_your_service_account.json
```

Make sure the `.env` file has correct values to ensure successful integration with Google Cloud.

### Step 5: Train the Model
To train the machine learning model, open and run the `model_training.ipynb` Jupyter notebook. This notebook fetches historical data, computes technical indicators, and trains the Random Forest Classifier model. The trained model is then stored in **Google Cloud Storage** for later use by the trading strategy.

### Step 6: Execute the Strategy and Backtest
Run the `trading_strategy.ipynb` Jupyter notebook to execute the strategy and perform backtesting. This notebook simulates the strategy using historical data, evaluates its effectiveness, and outputs the performance metrics (e.g., returns, Sharpe ratio, drawdown). For 2 weeks testing, Please change the lookback value to 14 and Interval to 30m.

---

## Core Logic of the Strategy

The trading strategy leverages a combination of technical indicators and a machine learning model (Random Forest Classifier) to predict price movements and generate buy/sell signals. Key technical indicators used are:

- **Simple Moving Averages (SMA)**: 10-period and 20-period moving averages.
- **RSI (Relative Strength Index)**: Momentum oscillator to identify overbought/oversold conditions.
- **MACD (Moving Average Convergence Divergence)**: Measures momentum and trend direction.
- **Bollinger Bands**: Volatility-based indicator to identify overbought/oversold levels.
- **ATR (Average True Range)**: Volatility indicator measuring the range of price movement.
- **Momentum (MOM)**: Measures the rate of price change.
- **Rate of Change (ROC)**: Percentage change between the current price and the price a number of periods ago.

The **Random Forest Classifier** takes these technical indicators as input features and predicts whether to buy or sell based on historical price action.

### Intended Market Behavior
The strategy is designed to capture trends and avoid significant drawdowns. It performs best in trending markets and adjusts its risk based on real-time technical analysis.

---

## Backtesting & Simulation Results

### Performance Metrics
Backtesting was performed on the **ETH/USDT** pair from **August 14, 2024** to **October 13, 2024** (approximately 60 days). Initial capital was set to $4000, and the results were compared to a simple buy-and-hold strategy.

| Metric                         | Value          |
| ------------------------------- | -------------- |
| **Equity Final [$]**             | 5229.52        |
| **Return [%]**                   | 30.74          |
| **Buy & Hold Return [%]**        | -10.41         |
| **Return (Ann.) [%]**            | 387.55         |
| **Sharpe Ratio**                 | 2.70           |
| **Sortino Ratio**                | 31.55          |
| **Calmar Ratio**                 | 53.32          |
| **Max Drawdown [%]**             | -7.27          |
| **Avg. Drawdown [%]**            | -1.50          |
| **Max. Drawdown Duration**       | 17 days 16:00  |
| **Profit Factor**                | 2.78           |
| **Number of Trades**             | 53             |
| **Win Rate [%]**                 | 54.72          |
| **Best Trade [%]**               | 12.17          |
| **Worst Trade [%]**              | -4.15          |
| **Max. Trade Duration**          | 7 days 08:00   |

### Key Performance Indicators (KPIs)
- **Sharpe Ratio**: A measure of risk-adjusted return. A Sharpe ratio above 2 is generally considered excellent.
- **Max Drawdown**: The maximum observed loss from a peak to a trough in the strategy’s equity curve.
- **Profit Factor**: The ratio of gross profit to gross loss, with a value greater than 2 indicating high profitability.

The trading strategy outperformed the buy-and-hold approach significantly, achieving a return of **30.74%** compared to **-10.41%** for buy-and-hold. The risk-adjusted metrics (Sharpe ratio and Sortino ratio) also indicate strong performance with relatively low risk.

---

## Data Feeds & Machine Learning Algorithms

### Data Feeds
The strategy ingests historical and live OHLCV data (Open, High, Low, Close, Volume) for the **ETH/USDT** pair, fetched from cryptocurrency exchanges using the **ccxt** library. This data is used to compute technical indicators and train the machine learning model.

### Machine Learning Algorithms
The strategy uses a **Random Forest Classifier** to predict price movements. The model is trained on historical data and generates buy/sell signals in real-time based on technical indicators.

---

## Tokens Focused on Trading

The primary asset pair traded by this strategy is **ETH/USDT**. The strategy can be adapted to trade other pairs like **BTC/USDT** or **BNB/USDT** by adjusting the data sources and retraining the model with the corresponding asset data.

---

## Notable Points

- **Google Cloud Integration**: Data is stored in **BigQuery**, and the trained model is saved in **Google Cloud Storage**. This allows for scalable storage and remote access.
- **Risk Management**: The strategy ensures only one position (long or short) is active at any time, reducing exposure to volatile markets.
---

## Future Improvements

- **Sentiment Analysis**: Future versions could incorporate sentiment data from news sources or social media platforms to improve the model’s predictive power during volatile markets.
- **Reinforcement Learning**: Exploring reinforcement learning to allow the model to adapt to changing market conditions in real-time.
- **Extended Asset Coverage**: Expanding the strategy to cover more cryptocurrency pairs like **BTC/USDT**, **BNB/USDT**, and other high-liquidity assets.
