from tkinter import *
from tkinter import messagebox

def newFile() :
    messagebox.showinfo("建立新檔案", "建立一個新檔案")

def openFile() :
    messagebox.showinfo("開啟新檔案", "開啟一個舊檔案")
    
def about() :
    messagebox.showinfo("關於我們", "Python程式設計初學者，正在學習道路上，不斷往前邁進 ！")
    
window = Tk()
menu = Menu(window)
window["menu"]= menu

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="檔案", menu=filemenu)
filemenu.add_command(label="建立新檔案", command=newFile)
filemenu.add_command(label="開啟舊檔", command=openFile)
filemenu.add_separator()
filemenu.add_command(label="離開", command=window.destroy)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="說明", menu=helpmenu)
helpmenu.add_command(label="關於我們", command=about)
window.mainloop()