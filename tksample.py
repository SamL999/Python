from tkinter import *
import tkinter.font as tkFont

def increase_label_font():
    fontsize = fontStyle['size']
    labelExample['text'] = fontsize+2
    fontStyle.configure(size=fontsize+2)

def decrease_label_font():
    fontsize = fontStyle['size']
    labelExample['text'] = fontsize-2
    fontStyle.configure(size=fontsize-2)


def showMsg() :
    label4["text"] = "Welcom to Python GUI !!!" 

def add() :
    result.set(num1.get()+num2.get())
       

window = Tk()
num1 = DoubleVar()
num2 = DoubleVar()
result = DoubleVar()

fontStyle = tkFont.Font(family="Lucida Grande", size=20)

window.title("Python 視窗")

window.geometry("600x600")
window.maxsize(800,800)

btn1 = Button(window, text="確定")
btn1.config(fg="purple", bg="lightblue")
btn1.place(x=280, y=550)

btn2 = Button(window, text="Show Message", command=showMsg)
btn2.config(fg="purple", bg="lightgreen")
btn2.place(x=5, y=200)

label1 = Label(window, text="Python 會員系統", width=30, fg="blue") 
label2 = Label(window, text="會員帳號 : ", width=15, bg="lightblue") 
label3 = Label(window, text="密碼 : ", width=15, bg="lightpink") 
label4 = Label(window, fg="brown")


label1.pack()
label2.place(x=5, y=50)
label3.place(x=5, y=100)
label4.place(x=150, y=200)

Entry(window, width=10, textvariable = num1).pack(side=LEFT)
Label(window, width=5, text = "+").pack(side=LEFT)
Entry(window, width=10, textvariable = num2).pack(side=LEFT)
Button(window, width=10, text = "=", command=add).pack(side=LEFT)
Entry(window, width=10, textvariable = result).pack(side=LEFT)

messagebox.askokcancel("歡迎訊息", "Welcome !")

window.mainloop()

