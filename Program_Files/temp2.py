import pandas as pd
 
df = pd.read_csv('Record.csv')
temp_l = list(df['UName'])
username = temp_l[len(temp_l)-1]
print(temp_l)
