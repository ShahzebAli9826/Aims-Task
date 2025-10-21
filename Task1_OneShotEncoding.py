import pandas as pd
import numpy as np

data = {
    "Name" : ["Ram","Shyam","Harry","Vikesh","Sonu","Nitin","Salman"],
    "Age":[10,45,23,np.nan,18,np.nan,23],
    "City": ["Delhi","Mumbai","Chennai","Mumbai","Delhi","Delhi","Chennai"]
}

df = pd.DataFrame(data)

Cities = df["City"].unique()
for city in Cities:
    val = []
    for c in df["City"]:
        if city == c:
            val.append(1)
        else:
            val.append(0)
    df[f"City_{city}"]=pd.DataFrame(val)

print(df)
