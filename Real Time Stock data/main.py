import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
from sklearn.metrics import mean_absolute_error

# Step 1: Choose Stock Ticker (Indian or Global)
ticker = "RELIANCE.NS"  # Change to any stock, e.g., "AAPL", "INFY.NS", "TATAMOTORS.NS"
stock = yf.Ticker(ticker)
df = stock.history(period="max")
df.reset_index(inplace=True)

# Step 2: Preprocess the Data
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Close'] = df['Close'].astype(float)

# Step 3: Plot Yearly Average Close Price
yearly_avg = df.groupby('Year')['Close'].mean().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(data=yearly_avg, x='Year', y='Close', marker='o')
plt.title(f"{ticker} - Yearly Average Closing Price", fontsize=14)
plt.xlabel("Year"); plt.ylabel("Avg Close Price")
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 4: Prepare Data for Prophet Forecasting
prophet_df = df[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'})
model = Prophet(daily_seasonality=False)
model.fit(prophet_df)

# Step 5: Predict Future Prices
future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)

# Step 6: Plot the Forecast
model.plot(forecast)
plt.title(f"{ticker} - Forecast for Next Year", fontsize=14)
plt.xlabel("Date"); plt.ylabel("Predicted Price")
plt.tight_layout()
plt.show()

# Step 7: Evaluate Accuracy (Optional)
if len(prophet_df) >= 365:
    actual = prophet_df['y'].values[-365:]
    predicted = forecast['yhat'].values[-365:]
    mae = mean_absolute_error(actual, predicted)
    print("Mean Absolute Error (Last 1 Year):", round(mae, 2))
