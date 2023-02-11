import pandas as pd
import numpy as np
s=pd.Series(np.random.random(5))
print(s)
print( s.argmax(),s.argmin())
print(s.argsort())
print(s.cumsum())
