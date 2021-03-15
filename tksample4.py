from tkinter import *
from tkinter import messagebox


def showMsg() :
    i = radiovalue.get()
    if i == 0 :
        messagebox.showinfo("選取結果", "牡丹花")
    else :
        messagebox.showinfo("選取結果", "繡球花")

window = Tk()

image1 = PhotoImage(file = "flower1.png")
image2 = PhotoImage(file = "flower2.png")

label1 = Label(window, text="請選取你喜歡的花 :", fg="purple").pack()
radiovalue = IntVar()
radiovalue.set(0)
Radiobutton(window, image = image1, variable=radiovalue, value = 0).pack()
Radiobutton(window, image = image2, variable=radiovalue, value = 1).pack()
Button(window, text = "確定", command = showMsg).pack()

window.mainloop()