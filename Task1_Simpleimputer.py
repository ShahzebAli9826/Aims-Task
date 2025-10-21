import pandas as pd
import numpy as np

data = {
    "Name" : ["Ram","Shyam","Harry","Vikesh","Sonu","Nitin","Salman"],
    "Age":[10,45,23,np.nan,18,np.nan,23],
    "City": ["Delhi","Mumbai","Chennai","Mumbai","Delhi","Delhi","Chennai"]
}

df = pd.DataFrame(data)

#imputer

#Mean
mean_value = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_value)
print(df)

#Median
median_value = df["Age"].median()
df['Age'] = df['Age'].fillna(median_value)
print(df)

#mode
mode_value = df["Age"].mode()[0]
df['Age'] = df['Age'].fillna(mode_value)
print(df)
