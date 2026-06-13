import pandas as py
import matplotlib.pyplot as plt
import japanize_matplotlib

df = py.read_csv("yutarou_out.csv")

plt.pie(df["数"], labels=df["種類"], autopct="%1.1f%%", startangle=90)

plt.title("9月6日　渡邊勇太郎　アウトの内訳")
plt.show()