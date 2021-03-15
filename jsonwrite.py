import json

objf =r"C:\Users\user\Desktop\Python\object.json"
aryf =r"C:\Users\user\Desktop\Python\array.json"

adddict = {"Key" : "Golden", "S":123}
addlist = [7,8,9,10,"元宵節"]


with open(objf, 'w') as objfile:
    json.dump(adddict, objfile)


with open(aryf, 'w') as aryfile:
    json.dump(addlist, aryfile, ensure_ascii=False)
