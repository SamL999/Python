import pandas as pd
'''
x = pd.Series([5,-4,9,-2],index=["a", "b", "c", "d"])

print (x)
print (x.values)
print (x.index)
print (x["a"])
print ("a" in x)
print (5 in x)
print (5 in x.values)

print ("-"*20)

a = ["A",123,"B",456,"C",789]
b = pd.Series(a)
print (b)

print ("-"*20)

c = {"A":123,"B":456,"C":789}
d = pd.Series(c)
print (d)

print ("-"*20)
'''

y = {"Name":["Sam","Vincent","Mary"], "Age":[50,45,30], "Birth":[1971,1976,1991]}
z = pd.DataFrame(y)
z2 = pd.DataFrame(y, columns=["Name","Age","Birth","ABC"], index=["a","b","c"])
print (z)
print (z2)