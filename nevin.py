import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("nevin_month.csv")

plt.plot(df["月"], df["長打率"], marker="o")
plt.title("ネビン 月別長打率")
plt.xlabel("月")
plt.ylabel("長打率")
plt.ylim(0.2, 0.6)
plt.grid(True)
plt.show()