import pandas as pd

series_a = pd.Series(data=[1,2,3,4,5], dtype=int, name="Sample")

print(series_a)

g = {"key1": [1,2,3,4,5], "key2":[6,7,8,9,10]}

df = pd.DataFrame(data=g)
print(df)