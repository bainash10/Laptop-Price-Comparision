import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the random seed for reproducibility
np.random.seed(42)

# Generate random data
months = pd.date_range(start='2023-01-01', periods=12, freq='M')
prices_usd = np.random.uniform(low=800, high=1500, size=len(months))

# Conversion rates (as of a specific date)
usd_to_npr = 125.5  # 1 USD = 125.5 NPR
usd_to_inr = 74.5   # 1 USD = 74.5 INR

# Convert prices to NPR and INR
prices_npr = prices_usd * usd_to_npr
prices_inr = prices_usd * usd_to_inr

# Create a DataFrame
data = pd.DataFrame({'Month': months, 'Price_USD': prices_usd, 'Price_NPR': prices_npr, 'Price_INR': prices_inr})

# Set the style for seaborn
sns.set(style='whitegrid')

# Line Graph
plt.figure(figsize=(10, 6))
# plt.plot(data['Month'], data['Price_USD'], marker='o', linestyle='-', color='b', label='Price (USD)')
plt.plot(data['Month'], data['Price_NPR'], marker='o', linestyle='-', color='r', label='Price (NPR)')
plt.plot(data['Month'], data['Price_INR'], marker='o', linestyle='-', color='g', label='Price (INR)')
plt.title('Currency Value Comparison - Laptop Prices', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
