import japanize_matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('9_27_kona.csv')

Fastball = df[df['球種']=='ストレート']
Fork = df[df['球種']=='フォーク']
Slider = df[df['球種']=='縦スライダー']
Cutter = df[df['球種']=='カットボール']
Curve = df[df['球種']=='カーブ']

x = ['ストレート', 'フォーク', '縦スライダー', 'カットボール', 'カーブ']
y = [Fastball['球速'].mean(), Fork['球速'].mean(), Slider['球速'].mean(), Cutter['球速'].mean(), Curve['球速'].mean()]

plt.bar(x, y)
plt.title('9/27 高橋光成投手の球種ごとの平均球速')
plt.ylim(110, 160)
plt.show()