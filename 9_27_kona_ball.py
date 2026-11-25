import japanize_matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('9_27_kona.csv')

counts = df['球種'].value_counts()
plt.pie(counts, labels = counts.index, counterclock = False, startangle = 90)
plt.title('9/27 高橋光成投手の球種割合')
plt.show()