import pandas as pd
import numpy as np

"""
df = pd.DataFrame(np.random.rand(5,3),\
     index=list("ABCDE"), columns=list("XYZ"))
    
print (df)
print ("-"*30)    
print (df.loc["A","X"])
print ("-"*30)   
print (df.loc["B":"D",:])
print (df.loc[:,"Y":"Z"])
print (df.loc["A":"C","X":"Y"])
print (df.loc[["B","E"],["Y","Z"]])  """

df2 = pd.DataFrame(np.random.randint(1,101,9).reshape(3,3),\
     index=list("xyz"), columns=list("XYZ"))

print (df2)
print ("-"*30) 
print (df2.iloc[0,1])
print (df2.iloc[0:2,:])
print (df2.iloc[:,1:2])
print (df2.iloc[0:2,0:2])
print (df2.iloc[[0,2],[0,2]])
print (df2.iloc[2,2])