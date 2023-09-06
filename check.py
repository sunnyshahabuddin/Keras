import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt

# Load the Apple share price dataset
data = pd.read_csv('apple_share_prices.csv')

# Convert the 'date' column to a datetime object
data['date'] = pd.to_datetime(data['date'])

# Set 'date' as the index
data.set_index('date', inplace=True)

# Group data by week and take the closing price as the target variable
weekly_data = data['close'].resample('W').mean()

# Split data into train and test sets
train_size = int(0.8 * len(weekly_data))
train, test = weekly_data[:train_size], weekly_data[train_size:]

# Define SARIMA hyperparameters (p, d, q, P, D, Q, S)
p, d, q = 1, 1, 1  # Non-seasonal parameters
P, D, Q, S = 1, 1, 1, 4  # Seasonal parameters (weekly data)

# Fit the SARIMA model
sarima_model = SARIMAX(train, order=(p, d, q), seasonal_order=(P, D, Q, S))
sarima_result = sarima_model.fit(disp=False)

# Forecast using the trained model
forecast = sarima_result.get_forecast(steps=len(test))

# Calculate MAPE
mape = np.mean(np.abs((test - forecast.predicted_mean) / test)) * 100

# Calculate RMSE
rmse = sqrt(mean_squared_error(test, forecast.predicted_mean))

# Plot the actual vs. forecasted values
plt.figure(figsize=(12, 6))
plt.plot(train.index, train.values, label='Train Data')
plt.plot(test.index, test.values, label='Test Data')
plt.plot(forecast.predicted_mean.index, forecast.predicted_mean.values, label='Forecast')
plt.legend()
plt.title(f'SARIMA Forecast\nMAPE: {mape:.2f}% | RMSE: {rmse:.2f}')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.show()

# Print MAPE and RMSE
print(f'MAPE: {mape:.2f}%')
print(f'RMSE: {rmse:.2f}')
