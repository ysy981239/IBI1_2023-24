import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


os.chdir("D:\IBI1_2023-24\practical7")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print(dalys_data.head(5))

print(dalys_data.info())

print(dalys_data.describe())

print(dalys_data.iloc[0, 3])

afghanistan_dalys = dalys_data.loc[dalys_data['Entity'] == 'Afghanistan', 'DALYs']
print(afghanistan_dalys)

china_data = dalys_data[dalys_data['Entity'] == 'China'][['Entity', 'Year', 'DALYs']]

mean_dalys_china = np.mean(china_data['DALYs'])
print(f"Mean DALYs in China: {mean_dalys_china}")

china_dalys_2019 = china_data.loc[china_data['Year'] == 2019, 'DALYs'].values[0]
print(f"DALYs in China for 2019: {china_dalys_2019}")
print("2019 was above the mean." if china_dalys_2019 > mean_dalys_china else "2019 was below the mean.")

plt.plot(china_data['Year'], china_data['DALYs'], 'b+')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs in China Over Time')
plt.xticks(rotation=-90)  
plt.show()