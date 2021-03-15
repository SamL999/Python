import pandas as pd

data = {"國語":[75,91,71,69],
        "數學":[62,53,88,53],
        "英文":[85,56,51,87],
        "自然":[73,63,69,74],
        "社會":[60,65,87,70]}

df = pd.DataFrame(data, index=("小林","小黃","小陳","小美"))

print (df)

print (df.iloc[2:4,:])

print ("-"*20)

print (df["自然"].sort_values(ascending=False))

print (df.iloc[[0,2],[1,3]])
