# 引入日曆模組
import calendar
 
# 輸入指定年月
yy = int(input("輸入年份: "))
mm = int(input("輸入月份: "))
 
# 顯示日曆
print(calendar.month(yy,mm))