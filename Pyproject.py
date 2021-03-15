import pandas as pd
import numpy as np
import os
import csv
import glob
from matplotlib import pyplot as plt
from pandas import Series, DataFrame
import math

# 資料來源檔案欄位說明
# district(鄉鎮市區)            rps01(交易標的)           rps02(土地區段位置建物區段門牌)
# rps03(土地移轉總面積平方公尺)  rps04(都市土地使用分區)    rps05(非都市土地使用分區)
# rps06(非都市土地使用編定)      rps07(交易年月日)         rps08(交易筆棟數)
# rps09(移轉層次)               rps10(總樓層數)           rps11(建物型態)
# rps12(主要用途)               rps13(主要建材)           rps14(建築完成年月)
# rps15(建物移轉總面積平方公尺)  rps16(建物現況格局-房)     rps17(建物現況格局-廳)
# rps18(建物現況格局-衛)         rps19(建物現況格局-隔間)   rps20(有無管理組織)
# rps21(總價元)                 rps22(單價元平方公尺)      rps23(車位類別)
# rps24(車位移轉總面積平方公尺)  rps25(車位總價元)          rps26(備註)
# rps27(編號)                   rps28(主建物面積)         rps29(附屬建物面積)
# rps30(陽台面積)               rps31(電梯)

def myautopct(data):
   def inner_myautopct(pct):
       total=sum(data)
       val=int(round(pct*total/100.0))
       return '{p:.0f}% ({v:d})'.format(p=pct,v=val)
   return inner_myautopct


def showlinevalue(label, value) :
    for a, b in zip(label, value):
        plt.text(a, b, b, ha='left', va='bottom', color="black", fontsize=12)

def showbarvalue(label, value) :
    for a1,b1 in zip(label,value):
        plt.text(a1, b1+0.05, '%.0f' % b1, ha='center', va='bottom', fontsize=14, color="red")


files = glob.glob('csvfiles/*.csv')
df = pd.concat([pd.read_csv(x, low_memory=False).assign(New=os.path.basename(x)) for x in files])

files2 = glob.glob('csvfiles2/*.csv')
df2 = pd.concat([pd.read_csv(x, low_memory=False).assign(New=os.path.basename(x)) for x in files2])

files3 = glob.glob('csvfiles3/*.csv')
df3 = pd.concat([pd.read_csv(x, low_memory=False).assign(New=os.path.basename(x)) for x in files3])

df_total = len(df)

df_district = df.groupby("district")["district"].count()

# 土城區 資料
dftc =  df[df.district == "土城區"]
dftc1 =  dftc[dftc.rps01 == "房地(土地+建物)"]
dftc2 =  dftc[dftc.rps01 == "房地(土地+建物)+車位"]
dftc3 = pd.concat([dftc1,dftc2])
     
colors = ["#2E86AB", "#424B54", "#00A6A6", "#F24236", "#9E643C", "#f7bb5f", "#EDE6F2","#E9D985", "#8C4843", "#90d595", 
          "#e48381", "#090446", "#f7bb5f", "#eafb50","#adb0ff", "#ffb3ff", "#90d595", "#e48381", "#aafbff",'#746D75']

plt.rcParams["font.family"]="Microsoft Yahei"

"""
# 101~110 年新北市不動產交易 折線圖分析

df_date = df.rps07.tolist()
dfyear = []
for i in range(len(df_date)):
    tempy = str(df_date[i])[0:3]
    dfyear.append(tempy)

x = ["101", "102", "103", "104", "105", "106", "107", "108", "109", "110"]

y = [dfyear.count("101"), dfyear.count("102"), dfyear.count("103"), dfyear.count("104"),
     dfyear.count("105"), dfyear.count("106"), dfyear.count("107"), dfyear.count("108"),
     dfyear.count("109"), dfyear.count("110")]

plt.figure(figsize=(14,10), facecolor="#f7bb5f") 

showlinevalue(x, y)   
 
plt.plot(x,y, "o-", linewidth=2, markerfacecolor='blue', color="#e48381", label="民國101~110年新北市不動產交易數")
plt.xlabel('年 度', fontsize=20, color="blue")
plt.ylabel('不動產交易數', fontsize=20, color="blue")
plt.legend(loc = "best", fontsize=16)
plt.tick_params(labelsize=14)

plt.savefig("newtp1.jpg")

plt.show()
plt.close()


# 101~110 新北市鄉鎮市區不動產交易量 橫條圖分析

df1 = dict(df_district.sort_values(ascending=False))
x1 = df1.keys()
y1 = df1.values()

fig, ax = plt.subplots(figsize=(16, 9))

y_pos = np.arange(len(x1))

ax.barh(y_pos, y1, color=colors)

for a,b in zip(y1,y_pos):
      ax.text(a, b, '%.0f' % a, ha='left', va='center', fontsize=12, color="black")


ax.text(0.59, 0.3, "不動產交易總數 : "+str(df_total), transform=ax.transAxes, size=24, color='#000000',ha='left')

ax.set_yticks(y_pos)
ax.set_yticklabels(x1, fontsize=10, color="blue")
ax.invert_yaxis()
# ax.set_xlabel('不動產交易數', fontsize=12, color="blue")
ax.set_title("民國101~110年新北市鄉鎮市區不動產交易量", fontsize=14,  loc="Center", color="brown")
ax.grid(which='major', axis='x', linestyle='-')  # 增加格線
ax.xaxis.set_ticks_position('top')  # 將橫軸放到頂端
plt.box(False)  # 去掉箱線

plt.savefig("newtp2.jpg", bbox_inches='tight', pad_inches=0.0)
plt.show()
plt.close()


# 101~110 新北市鄉鎮市區不動產交易 圓餅圖分析

dft2 = dict(df_district.sort_values(ascending=False).head(18))
x2 = dft2.keys()
y2 = dft2.values()


plt.figure(figsize=(14,10))                # 顯示圖框架大小

labels = x2                              # 圓餅圖標籤來源
sizes = y2                               # 圓餅圖數值來源
explodes = (0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0,
            0, 0, 0, 0, 0, 0, 0, 0) # 依據類別數量，分別設定要突出的區塊

plt.pie(sizes,                          # 數值
        labels = labels,                # 標籤
        autopct = "%1.1f%%",            # 將數值百分比並留到小數點一位
        explode = explodes,             # 設定分隔的區塊位置
        pctdistance = 0.6,              # 數字距圓心的距離
        textprops = {"fontsize" : 12}, 
        # colors = colors,
        shadow=True)                    # 設定陰影
 
plt.axis('equal')                       # 圓餅圖比例相等
plt.title("民國101~110年新北市鄉鎮市區不動產交易分析", fontsize=14,  loc="Center", color="brown") 
plt.legend(loc = "best")                # 設定圖例及其位置為最佳

plt.savefig("newtp3.jpg",   
              bbox_inches='tight',      # 去除座標軸占用的空間
              pad_inches=0.0)           # 去除所有白邊
plt.show()
plt.close()


# 101~110 新北市鄉鎮市區不動產交易 直條圖分析

dft3 = dict(df_district.sort_values(ascending=False).head(10))
x3 = dft3.keys()
y3 = dft3.values()

plt.figure(figsize=(10,8))
plt.bar(x3, y3, color=colors)


showbarvalue(x3,y3)
   
plt.title("民國101~110年新北市不動產交易排名前 10", fontsize=14,  loc="Center", color="brown")
plt.xlabel('鄉 鎮 市 區', fontsize=12, color="blue")
plt.ylabel('不 動 產 交 易 數', fontsize=12, color="blue")

plt.savefig("newtp4.jpg", pad_inches=0.0)

plt.show()
plt.close()


# 101~110 新北市鄉鎮市區人口成長 折線圖分析

df2a = df2[df2.隸屬區 == "淡水區"]
df2b = df2[df2.隸屬區 == "板橋區"]
df2c = df2[df2.隸屬區 == "新莊區"]
df2d = df2[df2.隸屬區 == "中和區"]
df2e = df2[df2.隸屬區 == "新店區"]
df2f = df2[df2.隸屬區 == "土城區"]

x = ["101", "102", "103", "104", "105", "106", "107", "108", "109", "110"]
y = df2a["合計"].values
y1 = df2b["合計"].values
y2 = df2c["合計"].values
y3 = df2d["合計"].values
y4 = df2e["合計"].values
y5 = df2f["合計"].values

plt.figure(figsize=(14,10))

for a, b in zip(x, y2):
    plt.text(a, b, b, ha='right', va='top', color="purple", fontsize=12)

showlinevalue(x, y)
showlinevalue(x, y1)
showlinevalue(x, y3)
showlinevalue(x, y4)
showlinevalue(x, y5)

plt.plot(x, y, "o-", linewidth=2, markerfacecolor="red", color="purple", label="淡水區")
plt.plot(x, y1, "o--", linewidth=2, markerfacecolor="red", color="green", label="板橋區")
plt.plot(x, y2, "o-.", linewidth=2, markerfacecolor="red", color="blue", label="新莊區")
plt.plot(x, y3, "o-", linewidth=2, markerfacecolor="red", color="brown", label="中和區")
plt.plot(x, y4, "p--", linewidth=2, markerfacecolor="red", color="orange", label="新店區")
plt.plot(x, y5, "p-", linewidth=2, markerfacecolor="red", color="black", label="土城區")

plt.title('民國101~110年新北市鄉鎮市區人口成長分析', fontsize=18, color="brown")
plt.xlabel('年     度', fontsize=16, color="blue")
plt.ylabel('人  口  數', fontsize=16, color="blue")
plt.legend(loc="upper left", fontsize=12)
plt.tick_params(labelsize=14)

plt.savefig("newtp5.jpg", pad_inches=0.0)

plt.show()
plt.close()


# 101~110 新北市土城區 不動產交易分析

dftc_asset = dftc.groupby("rps01")["rps01"].count()

df4 = dict(dftc_asset.sort_values())
x4 = df4.keys()
y4 = df4.values()

plt.figure(figsize=(14,10)) 

labels = x4                             
sizes = y4                             
explodes = (0.05, 0.05, 0.05, 0.05, 0.05)

plt.pie(sizes, labels = labels, autopct = myautopct(y4), explode = explodes,             
        pctdistance = 0.6, textprops = {"fontsize" : 14})                    
 
plt.axis('equal')                      
plt.title("民國101~110年 土城區 不動產交易分析", fontsize=16,  loc="Center", color="brown") 
plt.legend(loc = "best")               

plt.savefig("tc01.jpg", bbox_inches='tight', pad_inches=0.0)
plt.show()
plt.close()


# 101~110 新北市土城區 不動產交易金額  雙折線分析  

dftc_temp1 = dftc1.rps21.tolist()
dftc_temp2 = dftc2.rps21.tolist()

x = 0 
x1 = 0 
x2 = 0
x3 = 0
x4 = 0
y = 0
y1 = 0 
y2 = 0
y3 = 0
y4 = 0

for i in range(len(dftc_temp1)) :
    if int(dftc_temp1[i]) < 5000000 :
        x = x + 1
    elif int(dftc_temp1[i]) > 5000000 and int(dftc_temp1[i]) < 10000001 :
        x1 = x1 + 1
    elif int(dftc_temp1[i]) > 10000000 and int(dftc_temp1[i]) < 20000001 :
        x2 = x2 + 1
    elif int(dftc_temp1[i]) > 20000000 and int(dftc_temp1[i]) < 30000001 :
        x3 = x3 + 1
    else :
        x4 = x4 + 1    

for i in range(len(dftc_temp2)) :
    if int(dftc_temp2[i]) < 5000000 :
        y = y + 1
    elif int(dftc_temp2[i]) > 5000000 and int(dftc_temp2[i]) < 10000001 :
        y1 = y1 + 1
    elif int(dftc_temp2[i]) > 10000000 and int(dftc_temp2[i]) < 20000001 :
        y2 = y2 + 1
    elif int(dftc_temp2[i]) > 20000000 and int(dftc_temp2[i]) < 30000001 :
        y3 = y3 + 1
    else :
        y4 = y4 + 1  

label1 = ["500萬以下", "500~1000萬", "1000萬~2000萬", "2000萬~3000萬", "3000萬以上"]
value1 = [x, x1, x2, x3, x4]
value2 = [y, y1, y2, y3, y4]

plt.figure(figsize=(14,10), facecolor="#adb0ff") 


showlinevalue(label1, value1)
showlinevalue(label1, value2)

plt.plot(label1,value1, "o-", linewidth=2, markerfacecolor='blue', color="orange", label="房地(土地+建物)")
plt.plot(label1,value2, "o--", linewidth=2, markerfacecolor='brown', color="#2E86AB", label="房地(土地+建物)+車位")


plt.title('民國101~110年土城區房屋交易分析', fontsize=24, color="brown")
plt.xlabel('房 屋 交 易 金 額', fontsize=20, color="blue")
plt.ylabel('房 屋 成 交 數 量', fontsize=20, color="blue")
plt.legend(loc = "best", fontsize=16)
plt.tick_params(labelsize=14)

plt.savefig("tc02.jpg", pad_inches=0.0)

plt.show()
plt.close()


# 101~110 新北市土城區 房屋交易區域分析 (只用 "房地(土地+建物)" 及 "房地(土地+建物)+車位")

dftc_temp3 = dftc3.rps02.tolist() 
dftc_addr = []
for i in range(len(dftc_temp3)):
    temp = str(dftc_temp3[i])[6:9]
    dftc_addr.append(temp)

temp5 = dict((i, dftc_addr.count(i)) for i in dftc_addr)

dftemp5 = Series(temp5)

df5 = (dftemp5.sort_values(ascending=False)).head(10)

x5 = df5.keys()
y5 = df5[df5.notnull()].values

clrs = ["#ffb3ff", "#90d595", "#e48381", "#aafbff",'#746D75', "#F24236", "#9E643C", "#f7bb5f", "#EDE6F2", "#E9D985"]

plt.figure(figsize=(14,10))
plt.bar(x5, y5, color=clrs)

showbarvalue(x5,y5)
    
plt.title("民國101~110年土城區房屋交易區域分析", fontsize=24,  loc="Center", color="brown")
plt.xlabel('土 城 區 街 道 路 名', fontsize=20, color="blue")
plt.ylabel('房屋交易數量', fontsize=20, color="blue")
plt.tick_params(labelsize=14)

plt.savefig("tc03.jpg", pad_inches=0.0)

plt.show()
plt.close()


# 101~110 土城區人口成長 折線圖分析

df3a = df3[df3.里名 == "裕生里"]
df3b = df3[df3.里名 == "日新里"]
df3c = df3[df3.里名 == "員仁里"]
df3d = df3[df3.里名 == "廣福里"]
df3e = df3[df3.里名 == "廣興里"]
df3f = df3[df3.里名 == "樂利里"]
df3g = df3[df3.里名 == "學士里"]

x = ["101", "102", "103", "104", "105", "106", "107", "108", "109", "110"]
y = df3a["合計"].values
y1 = df3b["合計"].values
y2 = df3c["合計"].values
y3 = df3d["合計"].values
y4 = df3e["合計"].values
y5 = df3f["合計"].values
y6 = df3g["合計"].values

plt.figure(figsize=(14,8))

for a, b in zip(x, y):
    plt.text(a, b, b, ha='right', va='top', color="purple", fontsize=12)
        
showlinevalue(x, y1)
showlinevalue(x, y2)
showlinevalue(x, y3)
showlinevalue(x, y4)
showlinevalue(x, y5)
showlinevalue(x, y6)

plt.plot(x, y, "o-", linewidth=2, markerfacecolor="red", color="green", label="中央路 - 裕生里")
plt.plot(x, y1, "o-", linewidth=2, markerfacecolor="red", color="green", label="中央路 - 日新里")
plt.plot(x, y2, "o-", linewidth=2, markerfacecolor="red", color="green", label="中央路 - 員仁里")
plt.plot(x, y3, "o--", linewidth=2, markerfacecolor="red", color="brown", label="學府路 - 廣福里")
plt.plot(x, y4, "o--", linewidth=2, markerfacecolor="red", color="brown", label="學府路 - 廣興里")
plt.plot(x, y5, "o--", linewidth=2, markerfacecolor="red", color="brown", label="學府路 - 樂利里")
plt.plot(x, y6, "o--", linewidth=2, markerfacecolor="red", color="brown", label="學府路 - 學士里")

plt.title('民國101~110年土城區人口成長分析', fontsize=18, color="brown")
plt.xlabel('年      度', fontsize=16, color="blue")
plt.ylabel('人 口 數', fontsize=16, color="blue")
plt.legend(loc="best", fontsize=12)
plt.tick_params(labelsize=14)

plt.savefig("tc03.jpg", pad_inches=0.0)

plt.show()
plt.close()



# 101~110 土城區 房屋交易坪數  折線圖分析  

dftc3_temp1 = dftc3.rps15.tolist()

x = 0 
x1 = 0 
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0
x8 = 0

for i in range(len(dftc3_temp1)) :
    if int(dftc3_temp1[i]) < 66.116 :
        x = x + 1
    elif int(dftc3_temp1[i]) >= 66.116 and int(dftc3_temp1[i]) < 99.174 :
        x1 = x1 + 1
    elif int(dftc3_temp1[i]) >= 99.174 and int(dftc3_temp1[i]) < 132.232 :
        x2 = x2 + 1
    elif int(dftc3_temp1[i]) >= 132.232 and int(dftc3_temp1[i]) < 165.29 :
        x3 = x3 + 1
    elif int(dftc3_temp1[i]) >= 165.29 and int(dftc3_temp1[i]) < 198.348 :
        x4 = x4 + 1    
    elif int(dftc3_temp1[i]) >= 198.34 and int(dftc3_temp1[i]) < 231.406 :
        x5 = x5 + 1 
    elif int(dftc3_temp1[i]) >= 231.406 and int(dftc3_temp1[i]) < 264.464 :
        x6 = x6 + 1 
    elif int(dftc3_temp1[i]) >= 264.464 and int(dftc3_temp1[i]) < 297.522 :
        x7 = x7 + 1 
    else :
        x8 = x8 + 1    


label1 = ["20坪以下", "20~30坪", "30~40坪", "40~50坪", "50~60坪", "60~70坪", "70~80坪", "80~90坪","100坪以上"]
value1 = [x, x1, x2, x3, x4, x5, x6, x7, x8]

plt.figure(figsize=(14,10), facecolor="lightyellow") 

showlinevalue(label1, value1)

plt.plot(label1,value1, "o-", linewidth=2, markerfacecolor='red', color="orange", label="房地(土地+建物) 及 房地+車位")

plt.title('民國101~110年土城區房屋交易坪數分析', fontsize=24, color="brown")
plt.xlabel('交 易 坪 數', fontsize=20, color="blue")
plt.ylabel('房 屋 交 易 數', fontsize=20, color="blue")
plt.legend(loc = "best", fontsize=16)
plt.tick_params(labelsize=14)

plt.savefig("tc04.jpg", pad_inches=0.0)

plt.show()
plt.close()



# 101~110 土城區 交易房屋使用年限 折線圖分析  

dftc3_temp2 = dftc3.rps14.fillna(0).tolist()

dftc3year = []

for i in range(len(dftc3_temp2)):
    temp = str(dftc3_temp2[i])
    dftc3year.append(temp)

temp6 = dict((i, dftc3year.count(i)) for i in dftc3year)
temp6 = Series(temp6)
df6 = (temp6.sort_values(ascending=False))

with open('df6.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in df6.items():
        writer.writerow([key, value])

"""

df6 = pd.read_csv("df6.csv")

y = 0
y1 = 0
y2 = 0
y3 = 0
y4 = 0
y5 = 0
y6 = 0
y7 = 0
y8 = 0
for i in range(len(df6)) :
        if  df6["date"][i] < 19710101 : 
              y = y + df6["count"][i]
        elif df6["date"][i] >= 19710101 and df6["date"][i] < 19810101 :
            y1 = y1 + df6["count"][i]
        elif df6["date"][i] >= 19810101 and df6["date"][i] < 19910101 :
            y2 = y2 + df6["count"][i]
        elif df6["date"][i] >= 19910101 and df6["date"][i] < 20010101 :
            y3 = y3 + df6["count"][i]
        elif df6["date"][i] >= 20010101 and df6["date"][i] < 20110101 :
            y4 = y4 + df6["count"][i]
        elif df6["date"][i] >= 20110101 and df6["date"][i] < 20160101 :
            y5 = y5 + df6["count"][i]
        elif df6["date"][i] >= 20160101 and df6["date"][i] < 20180101 :
            y6 = y6 + df6["count"][i]
        elif df6["date"][i] >= 20180101 and df6["date"][i] < 20200101 :
            y7 = y7 + df6["count"][i]
        else :
            y8 = y8 + df6["count"][i]

label2 = ["50年以上", "50~40年", "40~30年", "30~20年", "20~10年", "10~5年", "5~4年", "3~2年", "1年"]

value2 = [y, y1, y2, y3, y4, y5, y6, y7, y8]

plt.figure(figsize=(14,10), facecolor="lightpink") 

showlinevalue(label2, value2)   
 
plt.plot(label2, value2, "o-", linewidth=2, markerfacecolor='blue', color="#e48381", label="民國101~110年土城區交易房屋屋齡")
plt.xlabel('屋     齡', fontsize=20, color="blue")
plt.ylabel('房 屋 交 易 數', fontsize=20, color="blue")
plt.legend(loc = "best", fontsize=16)
plt.tick_params(labelsize=14)

plt.savefig("tc05.jpg")

plt.show()
plt.close()
