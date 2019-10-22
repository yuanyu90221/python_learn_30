import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_1 = pd.read_excel('D://TimeseriesData.xlsx', index='Time', sheet_name='Sheet1')
df_2 = pd.read_excel('D://TimeseriesData.xlsx', sheet_name='Sheet2')

# print(df_1.head(5))
# df_1.plot()
# plt.show()

plt.plot(df_2['Time'].astype(str), df_2['Amount Produced'], label='Amount Produced')

plt.show()