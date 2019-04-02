import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('C:\\Users\\...\\spybot.csv', quoting=0)
data.hist(bins=15)

plt.title("Price/Owner Comparison of Video Games")
plt.xlabel("Price ($)")
plt.ylabel("Owners (Millions)")
plt.show()
