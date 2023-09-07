# Convert the 'date' column to a datetime object (if not already done)
data['date'] = pd.to_datetime(data['date'])

# Set 'date' as the index
data.set_index('date', inplace=True)

acf_values = sm.tsa.acf(data['close'], fft=False)

# Create a lag range for the x-axis
lag_range = np.arange(0, len(acf_values))

# Create the ACF plot
plt.figure(figsize=(10, 5))
plt.bar(lag_range, acf_values)
plt.xlabel('Lag')
plt.ylabel('ACF Value')
plt.title('Autocorrelation Function (ACF) Plot')
plt.grid(True)
plt.show()
