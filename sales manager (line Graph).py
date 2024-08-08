import matplotlib.pyplot as plt
import numpy as np

# Data
months = np.arange(1, 13)
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10), sharex=True, sharey=True)
fig.suptitle('Sales Performance of Product Categories Over Time', fontsize=16)

# Electronics Sales
axs[0, 0].plot(months, electronics_sales, marker='o', color='b')
axs[0, 0].set_title('Electronics')
axs[0, 0].set_ylabel('Sales ($)')
axs[0, 0].grid(True)

# Clothing Sales
axs[0, 1].plot(months, clothing_sales, marker='o', color='g')
axs[0, 1].set_title('Clothing')
axs[0, 1].grid(True)

# Home & Garden Sales
axs[1, 0].plot(months, home_garden_sales, marker='o', color='r')
axs[1, 0].set_title('Home & Garden')
axs[1, 0].set_xlabel('Month')
axs[1, 0].set_ylabel('Sales ($)')
axs[1, 0].grid(True)

# Sports & Outdoors Sales
axs[1, 1].plot(months, sports_outdoors_sales, marker='o', color='m')
axs[1, 1].set_title('Sports & Outdoors')
axs[1, 1].set_xlabel('Month')
axs[1, 1].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
