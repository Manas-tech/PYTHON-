import pandas as pd
import numpy as np
d={"age":[1,2,3],"salary":[122,133,144]}
d["exp"]=[5,6,9]
print(type(d))
data =pd.DataFrame(d)
data.loc[3]=[3,144,9]
data.drop_duplicates(inplace=True)
print(data)
