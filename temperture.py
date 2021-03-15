a = (input('攝氏轉華氏,請按 1\n華氏轉攝氏 請按 2\n'))

while a != "1" and a != "2":
    a = (input('你輸入不正確，請重新輸入 !!\n攝氏轉華氏,請按 1\n華氏轉攝氏 請按 2\n'))
    print()
if a == "1":
    celsius = float(input('請輸入攝氏溫度:'))
    fahrenheit = (celsius*1.8)+32
    print('攝氏 %.1f 轉為華氏溫度為 %.1f' %(celsius,fahrenheit))
else:
    fahrenheit = float(input('請輸入華氏溫度:'))
    celsius = (fahrenheit - 32)/1.8
    print('華氏 %.1f 轉為攝氏溫度為 %.1f' %(fahrenheit,celsius))
