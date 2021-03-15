# 使用者輸入字元
c = input("請輸入一個字元: ")
 
# 使用者輸入ASCII碼，並將輸入的數值轉為整型
a = int(input("請輸入一個ASCII碼: "))
 
 
print( c + " 的ASCII 碼為", ord(c))
print( a , " 對應的字元為", chr(a))