import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("test_results.csv", header=None, names=["Time", "Line", "Status"])
df["Issue"] = df["Status"].apply(lambda x: 1 if "⚠️" in x else 0)

plt.plot(df["Issue"], marker="o")
plt.title("Device Health Over Time")
plt.xlabel("Log Entry")
plt.ylabel("Issue Detected")
plt.show()
