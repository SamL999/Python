import csv

oldf =r"C:\Users\user\Desktop\Python\input.csv"
newf =r"C:\Users\user\Desktop\Python\output.csv"


with open(oldf, encoding="utf8") as f:      
    oldf = csv.reader(f)
    data = list(oldf)
    
with open(newf, 'w', newline='', encoding="utf8") as f2:
    nf = csv.writer(f2)
    for row in data :
        nf.writerow(row)
    nf.writerow(["----------"])
    for row in data :
        nf.writerow(row)
    nf.writerow(["花茶", "15"])
    nf.writerow(["蜜茶", "10"])


