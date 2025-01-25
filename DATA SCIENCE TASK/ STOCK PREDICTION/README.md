# Stock Price Prediction Using LSTM

## Project Overview
This project demonstrates how to use Long Short-Term Memory (LSTM) networks for stock price prediction. Using historical stock data fetched via the `yfinance` library, the model predicts future stock prices based on patterns in the closing price.

The project focuses on the following key steps:
1. Data Collection (using Yahoo Finance API)
2. Data Preprocessing (normalization and sequence creation)
3. Model Building (LSTM neural network)
4. Model Training and Evaluation
5. Visualization of Predicted vs. Actual Stock Prices

---

## Features
- Fetches historical stock price data using the `yfinance` API.
- Prepares time-series data for LSTM input.
- Builds and trains a sequential LSTM model with Dropout regularization.
- Visualizes the results by comparing predicted stock prices against actual values.

---

## Prerequisites
To run this project, you need:
- **Python 3.x**: Ensure Python is installed on your machine.
- Required Libraries: Install the dependencies using the following command:
  ```bash
  pip install numpy pandas matplotlib yfinance scikit-learn tensorflow

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/your-username/cloud-based-photo-gallery.git
cd cloud-based-photo-gallery
```

## Install Dependencies
```bash
pip install numpy pandas matplotlib yfinance scikit-learn tensorflow

```
## Run the Script



```bash
python stock_price_prediction.py

```


