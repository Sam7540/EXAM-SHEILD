import pandas as pd

df = pd.read_csv('Record.csv')
print(df.iloc[-1,1])