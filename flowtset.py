a = int(input("請輸入一個正整數 : \n"))

sum=0  
i=1
        
while i<a:
    i=i+1
    if i%7 !=0:
        continue
    sum= sum+i

print("從 1 到", a, "的總和是 : ", sum)


for i in range(0, i<=a, 7):
    sum=sum+i

print("從 1 到", a, "的總和是 : ", sum)