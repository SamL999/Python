import re

key = "SABCDXYGGF DSBCCJJCCCX XDDCCVVDDDWERTXX"

p1 = "X[Y]{1}"
pattern1 = re.compile(p1)
print (pattern1.findall(key))

p2 = "A[BC]{2}"
pattern2 = re.compile(p2)
print (pattern2.findall(key))

p3 = "[CDE]{2}"
pattern3 = re.compile(p3)
print (pattern3.findall(key))

