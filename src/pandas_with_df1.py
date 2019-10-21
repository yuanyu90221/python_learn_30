import pandas as pd

csv_file = 'D://crimes-in-boston/crime.csv'

df = pd.read_csv(csv_file, encoding='iso-8859-1')
print(df.columns)
print(df.index)

df2 = df['OFFENSE_CODE']
df2.to_excel("output.xlsx")