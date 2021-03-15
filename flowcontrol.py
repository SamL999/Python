a = eval(input("請輸入一個整數 : \n"))
b = 5
c = 8

e = a % b
f = a % c

if (e == 0) and (f == 0) :
    print(a,"是", b, "的倍數, 也是", c, "的倍數",)
elif (e != 0) and (f != 0) :
    print(a,"不是", b, "的倍數, 也不是", c, "的倍數",)
elif e == 0:
    print(a,"是", b, "的倍數")
elif f == 0:
    print(a,"是", c, "的倍數")




