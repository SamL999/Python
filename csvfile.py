import csv

oldf =r"C:\Users\user\Desktop\Python\test\test_utf8.csv"
newf =r"C:\Users\user\Desktop\Python\test\testnew.csv"
cpf =r"C:\Users\user\Desktop\Python\test\testcp.csv"

with open(oldf,encoding="utf8") as f:
    csvf = csv.reader(f)
    data = list(csvf)
    print (data, "\n")

print("-"*50, "\n")
print(data[4][3])

with open(newf, 'w', newline='', encoding="utf8") as f2:
    wf = csv.writer(f2)
    wf.writerow(["ID", "姓名", "電話"])
    wf.writerow(["A1", "Sam", "0988666222"])
    wf.writerow(["A2", "David", "0966333111"])
    wf.writerow(["A3", "Mary", "0977555777"])
    
with open(cpf, 'w', newline='', encoding="utf8") as f3:
    copyf = csv.writer(f3)
    for row in data :
        copyf.writerow(row)