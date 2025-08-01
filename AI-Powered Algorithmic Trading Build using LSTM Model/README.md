---
## Disclaimer

This course is intended **purely for educational purposes**.

The examples, models, and predictions used in this course are designed to teach how AI and LSTM models can be applied to financial data.  
They are **not meant to provide investment advice**, nor should they be used as a basis for real-world trading.

Always consult a certified financial advisor before making any financial decisions.

---

# LSTM-Based Algorithmic Trading Demo

This project demonstrates how to build, train, and use an LSTM model for predicting stock trading signals using historical price and technical indicators.

---

## Requirements

Ensure you have Python 3.7 or higher installed.

Install required libraries using:

```bash
pip install -r requirements.txt
```

Note: Standard libraries like `datetime`, `random`, and `collections` are used but **do not need to be installed separately**.

---

## Included Files

- `LSTM_Part1_Training.ipynb` – Main notebook for training and backtesting
- `LSTM_Part2_Live_Prediction.ipynb` – Live prediction and simulated trading
- `lstm_model.h5` – Pre-trained LSTM model
- `scaler.pkl` – Trained MinMaxScaler for preprocessing
- `requirements.txt` – List of minimal required Python libraries
- `README.md` – This file

---

## Running the Notebooks

1. Start with **Part I**:
   - Train the LSTM model and evaluate its performance.
   - Save the trained model and scaler for future use.

2. Continue with **Part II**:
   - Load the saved model and scaler.
   - Fetch live stock data using `yfinance`.
   - Engineer features and perform prediction.
   - Simulate trade actions using a mock broker.

---

## Live Prediction Notes

- The model uses a **15-day window** of historical data.
- Features used: `Close`, `Volume`, `High_Low_Range`, `Momentum_5`, `Volatility_5`, `SMA_10`, `SMA_50`
- Ensure that data preprocessing (scaling and shaping) is **identical** to training.

---

## Tips

- If you face errors like `ModuleNotFoundError`, manually install the missing package:
  ```bash
  pip install yfinance joblib
  ```
- Run the notebooks in the same environment to avoid compatibility issues.

---

Happy Learning!
