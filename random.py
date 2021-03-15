import random

ranint = int(input("請輸入欲產生的亂數個數 : \n"))

items = [random.randint(1,100) for i in range(ranint)]

print (items)

print (tuple(items))

print (set(items))


