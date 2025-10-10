import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("9_6_yutarou.csv")

plt.title("9月6日　渡邊勇太郎　イニング別投球数")
plt.xlabel("回")
plt.ylabel("投球数")
plt.plot(df["回"], df["投球数"], marker="o", linestyle="-")
plt.xticks(df["回"])
plt.grid(True)
plt.show()