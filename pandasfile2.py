import pandas as pd

df = pd.read_csv("nba.csv")


print (df.sort_values("Salary", ascending=False).head(3))
print ("-"*70)

mask = df["Age"] >= 25
print (df[mask].head(3))
print ("-"*70)

mask2 = df["Age"].between(28,30)
print (df[mask2].head(3))
print ("-"*70)

mask3 = df["Age"].isin([27,28,29])
print (df[mask3].head(3))
print ("-"*70)

mask4 = df["Salary"].isnull()
print (df[mask4])

