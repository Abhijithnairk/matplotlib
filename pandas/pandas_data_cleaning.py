import pandas as pd

df=pd.read_csv('data.csv')

# x=df.to_string()

# print(x)

print(df.dropna())

x=df['Calories'].mean()

print(f'the mean calories {x}')