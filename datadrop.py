import pandas as pd
import numpy as np
d={"age":[1,2,3],"salary":[122,133,144]}
print(type(d))
data =pd.DataFrame(d)
data.loc[3]=[4,155]
data.drop(columns=['salary'],axis=1,inplace=True)
print(data) 
#machine learning 
