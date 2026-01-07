import numpy as py
import pandas as pd
import math
import matplotlib.pyplot as plt
pd.options.display.max_columns = None
pd.options.display.max_rows = None

df=pd.read_csv("/Users/sangeetha/Downloads/MTA_Daily_Ridership_Data__2020_-_2025_20250414.csv")
print(df.head())

null_counts = df.isnull().sum()
print(null_counts)
print("#########################################################")
print(df.describe())

#df['Date'] = pd.to_datetime(df['Date'])

print(df.dtypes)

df['Buses: Total Estimated Ridership'] = df['Buses: Total Estimated Ridership'].str.replace(',', '').astype(int)
df['Buses: Total Estimated Ridership'] = df['Buses: Total Estimated Ridership'].astype(int)
df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)

print(df.dtypes)
 
x = df['Subways: Total Estimated Ridership']  # or whatever your x column is called
#y = df['Date']  # or your y column name

# Plot a trend line for a column, e.g., 'Sales'
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Buses: Total Estimated Ridership'], marker='o', linestyle='-', label='Amount of Riders', color='purple')
plt.title('Amount of Bus Riders Over Time')
plt.xlabel('Year')
plt.ylabel('Amount of Riders')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Format x-axis to show only years
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
