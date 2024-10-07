# AlphaWaveTrader

## Team Members
- **codingis4noobs2** (Owner)

## Project Overview
AlphaWaveTrader is an algorithmic trading strategy designed to generate consistent returns through short-term trading on the BNB/USDT trading pair. The strategy leverages machine learning models to predict market trends and make informed buy/sell decisions based on various technical indicators. The goal is to capitalize on quick price movements and optimize profitability while maintaining risk management through strategic entry and exit points.

## Core Strategy Logic and Market Behavior
AlphaWaveTrader employs a **trend-following** approach by analyzing technical indicators and patterns to identify potential price movements. The core logic of the strategy includes:

1. **Technical Indicator Analysis**: The strategy uses a combination of moving averages, relative strength index (RSI), MACD, and Bollinger Bands to assess price trends, volatility, and momentum.
2. **Machine Learning Predictions**: The strategy's machine learning model generates predictions based on historical price patterns and technical indicator values. These predictions determine whether the strategy should enter a long (buy) or short (sell) position.
3. **Position Management**: The strategy automatically closes opposing positions (e.g., closing a short position when a buy signal is generated) to maintain a single directional trade at any given time.
4. **Short-term Focus**: The strategy aims to capture small profits over shorter timeframes, making it well-suited for short trading scenarios. It seeks to minimize drawdowns and maximize risk-adjusted returns by timing entries and exits effectively.

### Market Behavior
- **Short-term Market Reactions**: The strategy attempts to take advantage of short-term price movements in the BNB/USDT market. It reacts to changes in momentum and volatility, making it suitable for periods of increased market activity or low liquidity.

## Trading Strategy Specifications

### Market Focus
- **Trading Pair**: BNB/USDT

### Time Horizon
- **Strategy Type**: Short-term trading (30m timeframe)

### Data Feeds and Inputs
The strategy ingests the following data feeds for analysis and decision-making:
1. **OHLCV Data**: Open, High, Low, Close, and Volume data at 30m intervals. Data received from KuCoin
2. **Technical Indicators**: 
   - **Simple Moving Averages (SMA)**: Short-term (10-period) and medium-term (20-period).
   - **Relative Strength Index (RSI)**: Measures the speed and change of price movements.
   - **MACD**: Used to identify changes in the strength, direction, momentum, and duration of a trend.
   - **Bollinger Bands (BB)**: Indicates volatility and potential price reversals.
   - **Average True Range (ATR)**: Measures volatility.
   - **Momentum (MOM)**: Measures the rate of change in price movements.
   - **Rate of Change (ROC)**: Percentage change in price over a specified period.

### Machine Learning Algorithms Used
The strategy utilizes the following machine learning models for making predictions:
- **Random Forest Classifier**:
  - A robust ensemble model that creates multiple decision trees and combines their predictions to classify price movements.
  - Trained on historical price data and technical indicators to predict the likelihood of a positive or negative price movement.

### Performance Metrics
The following metrics summarize the results of backtesting the strategy over a 5-day period:

- **Start**: 2024-10-02 03:30:00
- **End**: 2024-10-07 03:00:00
- **Duration**: 4 days 23:30:00
- **Exposure Time [%]**: 99.17
- **Equity Final [$]**: 1024.65
- **Equity Peak [$]**: 1025.71
- **Return [%]**: 2.46
- **Buy & Hold Return [%]**: 3.40
- **Return (Annualized) [%]**: 617.94
- **Volatility (Annualized) [%]**: 42.35
- **Sharpe Ratio**: 14.59
- **Sortino Ratio**: Inf
- **Calmar Ratio**: 344.57
- **Max. Drawdown [%]**: -1.79
- **Avg. Drawdown [%]**: -0.41
- **Max. Drawdown Duration**: 2 days 04:30:00
- **Avg. Drawdown Duration**: 0 days 08:37:00
- **Number of Trades**: 5
- **Win Rate [%]**: 40.0
- **Best Trade [%]**: 6.64
- **Worst Trade [%]**: -1.82
- **Avg. Trade [%]**: 0.88
- **Max. Trade Duration**: 4 days 06:30:00
- **Avg. Trade Duration**: 0 days 23:42:00
- **Profit Factor**: 2.88

## Project Setup

### Step 1: Create a Virtual Environment
First, create and activate a virtual environment:

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
Install all required libraries from the requirements.txt file:
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
Run the setup_account.py file to generate the .env file, which will contain the necessary environment variables:
```bash
python setup_account.py
```

### Step 4: Configure Google Cloud Project
- Obtain your **GCP Project ID** and create a **service account** with the role: `Basic -> Owner`.
- Download the service account JSON file and add it to your project directory.

Update the `.env` file with the following fields:
- `GCP_PROJECT_ID` : Your GCP Project ID.
- `GOOGLE_APPLICATION_CREDENTIALS` : Path to the downloaded service account JSON file.

Example `.env` file:

```
GCP_PROJECT_ID=your_gcp_project_id
GOOGLE_APPLICATION_CREDENTIALS=path_to_your_service_account.json
```

### Step 5: Train the Model
Run the `model_training.ipynb` Jupyter notebook to train the machine learning model and store it in Google Cloud Storage

### Step 6: Execute the Strategy and Backtest
Run the `trading_strategy.ipynb` Jupyter notebook to execute the strategy and perform backtesting

This notebook will simulate the trading strategy using historical data and provide performance metrics to evaluate its effectiveness.

## GCP Tools Used
1. **Cloud Storage**: For storing the trained machine learning model and scaler.
2. **BigQuery**: For storing and analyzing historical trading data.
