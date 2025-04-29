import numpy as np

# Sample Bitcoin closing prices for the last 5 days
closing_prices = np.array([65230.50, 64780.90, 65310.20, 64890.00, 65520.75])

# Print the array and its type
print("\nBitcoin Closing Prices (Last 5 Days):")
print(closing_prices)
print("\nArray Type:", type(closing_prices))
print("Array Shape:", closing_prices.shape)

# This array structure is useful for various trading calculations, such as:
# - Moving averages
# - Price momentum
# - Volatility calculations
# - Technical indicators