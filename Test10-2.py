import json

fname =r"C:\Users\user\Desktop\Python\drugstore.json"
count = 0


with open(fname, encoding="utf8") as f:
    data = json.load(f)
    for item in data :
        if item[2]['地址縣市別'] == "新北市" and item[0]['機構狀態'] == "開業" :
            count = count + 1
            if count > 10 and count <21 :
                print (item[1]['機構名稱'], "  ", item[2]['地址縣市別'], item[3]['地址鄉鎮市區'], item[4]['地址街道巷弄號'], sep='')


