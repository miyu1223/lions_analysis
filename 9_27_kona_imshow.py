import japanize_matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('9_27_kona.csv')

location = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
total = 0

heatmap_data = df.pivot_table(
    index='縦', columns='横', values='球種', aggfunc='count', fill_value=0
)

plt.figure(figsize=(8, 8))
plt.imshow(heatmap_data, cmap='OrRd')

plt.colorbar()
plt.title('9月27日高橋光成投手のコース別投球割合')
plt.xticks([0, 1, 2], ['一塁側', '真ん中', '三塁側'])
plt.yticks([0, 1, 2], ['高め', '真ん中', '低め'])
plt.show()