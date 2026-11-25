import japanize_matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('9_27_kona.csv')

Fastball = df[df['球種']=='ストレート']
Fork = df[df['球種']=='フォーク']
Slider = df[df['球種']=='縦スライダー']
Cutter = df[df['球種']=='カットボール']
Curve = df[df['球種']=='カーブ']

border = [120, 125, 130, 135, 140, 145, 150, 155]

plt.hist(Fastball['球速'], alpha = 0.7, hatch = '/', label = 'ストレート', bins = border)
plt.hist(Fork['球速'], alpha = 0.7, hatch = 'o', label = 'フォーク', bins = border)
plt.hist(Slider['球速'], alpha = 0.7, hatch = '.', label = '縦スライダー', bins = border)
plt.hist(Cutter['球速'], alpha = 0.7, hatch = '-', label = 'カットボール', bins = border)
plt.hist(Curve['球速'], alpha = 0.7, hatch = '*', label = 'カーブ', bins = border)

plt.title('球種ごとの球速分布')
plt.xlabel('球速(km/h)')
plt.ylabel('投球数')
plt.legend(loc='upper left')
plt.show()
