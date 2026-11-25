import japanize_matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('9_27_kona.csv')

Fastball = df[df['球種']=='ストレート']

x ,y = [], []

for i in  range(1, 6):
    inning = Fastball[Fastball['回']==i]
    x.append(i)
    y.append(inning['球速'].mean())

plt.plot(x, y)
plt.title('イニングごとのストレート平均球速')
plt.xlabel('イニング(回)')
plt.ylabel('ストレートの平均球速(km/h)')
plt.xticks([1, 2, 3, 4, 5])
plt.show()