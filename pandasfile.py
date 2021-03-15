import pandas as pd

df = pd.read_csv("csvsample.csv")
print ("此檔案是幾維陣列 : ",df.ndim)
print ("此檔案的欄位資訊 : ",df.shape)
print ("-"*20)
print ("此檔案的資料型態 :\n",df.dtypes)

print (df.head(5))
print (df.tail(3))
print (df.info())

x = [["Amy","F",80],["Tom","M",60],["Jenny","F",40],["Sam","M",50]]
y = pd.DataFrame(x, columns=["Name","Sex","Age"])

print (y)
print (y["Name"])
print (y["Name"].values)
print (y["Name"][1])

df1 = pd.read_csv("nba.csv")
print (df1.head())
print (df1["Name"][0:10])
print (df1[["Name","Team"]].head(3))

df2 = pd.read_csv("nba.csv")
df2.insert(1,"Sport", value="checked")
print (df2.head())

df2 = df2.drop("Sport", axis=1)
print (df2.head())

df2 = df2.drop(0, axis=0)
print (df2.head())

df2 = df2.dropna()
print (df2.head(10))  

df3 = pd.read_csv("nba.csv")
df3 = df3.fillna(10000)
print (df3.head(10))


