import pandas as pd

col = ["class","name","bd"]
data = [["class A", "小明","1985-08-02"],
          ["class B", "小美","1995-10-09"],
          ["class C", "小黃","1995-06-06"],
          ["class C", "小陳","1993-11-29"],
          ["class A", "小花","1996-01-13"],
          ["class B", "小雨","1992-02-22"]]

frame = pd.DataFrame(data,columns=col)
print (frame)
print ("-"*50)
frame_class = frame.groupby("class")
print (frame_class.groups)
print ("-"*50)
print (frame_class.get_group("class A"))

