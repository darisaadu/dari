import numpy as np 
import pandas as pd

l = [1,2,3,4,5,6]

s = np.array(l)
# print(s)

df = pd.Series(s)
print(df)
