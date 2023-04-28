import pandas as pd
import numpy as np
d={"age" :[1,2,3],"salary": [122,133,144]}
print(type(d))
data =pd.DataFrame(d)
print(data.iloc[0])
data.loc[3]=[4,155]
print(data)
