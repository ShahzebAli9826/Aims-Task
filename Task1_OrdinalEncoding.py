import pandas as pd
import numpy as np

data = {
    "Name" : ["Ram","Shyam","Harry","Vikesh","Sonu","Nitin","Salman"],
    "Age":[10,45,23,np.nan,18,np.nan,23],
    "City": ["Delhi","Mumbai","Chennai","Mumbai","Delhi","Delhi","Chennai"]
}

df = pd.DataFrame(data)


City_mapping = {"Delhi":1,"Mumbai":2,"Chennai":3}
df["City_Encoded"] = df["City"].map(City_mapping)
print(df)

