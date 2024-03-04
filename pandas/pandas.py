import pandas as pd

data ={
    'calories':[420,380,390],
    'duration': [50,40,45]
}

df=pd.DataFrame(data)

print(df)
print(df.loc[0])

df=pd.DataFrame(data,index=["day1","day2","day3"])

df=pd.read_csv('data.csv')

print(df)

print(df.head(10))

print(df.info())