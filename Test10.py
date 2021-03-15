import json

newf =r"C:\Users\user\Desktop\Python\jsonoutput.json"
adddict = {"breakfast":50, "lunch":80, "dinner":100}

with open(newf, 'w') as f1:
    json.dump(adddict, f1)

with open(newf) as f2:
    data = json.load(f2)
    print("早餐費用 :",data['breakfast'],"元")
    print("午餐費用 :",data['lunch'],"元")
    print("晚餐費用 :",data['dinner'],"元")
