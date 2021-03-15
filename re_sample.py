"""
import re

pattern = re.compile(r"\d+")

r1 = pattern.findall("runoob 123 google 456")

r2 = pattern.findall("run88oob123google456",0 ,10)

print (r1)

print (r2)  """

import re

key = "abcde@abc.edu.tw"

p1 = "@.+."
pattern1 = re.compile(p1)
print (pattern1.findall(key))

p2 = "@.+\."
pattern2 = re.compile(p2)
print (pattern2.findall(key))

p3 = "@.+?\."
pattern3 = re.compile(p3)
print (pattern3.findall(key))