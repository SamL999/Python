from tkinter import *
from tkinter import messagebox

def showMsg() :
    result = ''
    for i in checkvalue :
        if checkvalue[i].get() == True :
            result = result + dessert[i] + "\t"
    messagebox.showinfo("選餐結果 :", result)

def showMsg2() :
    i = radiovalue.get()
    messagebox.showinfo("選餐結果 :", dessert[i])


window = Tk()

label1 = Label(window, text="請選取你喜歡的甜點 :", fg="blue").pack()

dessert = { 0 : "馬卡龍", 1 : "舒芙蕾", 2 : "草莓塔", 3 : "蘋果派", } 

# checkvalue = {}

# for i in range(len(dessert)) :
#     checkvalue[i] = BooleanVar()
#     Checkbutton(window, variable=checkvalue[i], text=dessert[i]).pack()

# Button(window, text = "確定", command = showMsg).pack()


radiovalue = IntVar()
radiovalue.set(0)

for i in range(len(dessert)) :
    Radiobutton(window, text=dessert[i], variable=radiovalue, value = i).pack()

Button(window, text = "確定", command = showMsg2).pack()

window.mainloop()

