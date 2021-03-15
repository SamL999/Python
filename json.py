import json

objf =r"C:\Users\user\Desktop\Python\object.json"
aryf =r"C:\Users\user\Desktop\Python\array.json"

with open(objf) as objfile:
    data = json.load(objfile)
    print(data)
    print(type(data))

with open(aryf) as aryfile:
    data2 = json.load(aryfile)
    print(data2)
    print(type(data2))

