#ส่งการบ้าน EP.3 จ้าาา 
#แคปเจอร์โปรแกรมบันทึกค่าใช้จ่าย+ csv
# Source Code: https://github.com/UncleEngineer/PythonGUI2023

from tkinter import *

tk = Tk()
tk.title('โปรแกรมบันทึกค่าใช้จ่าย')

#
width = 500
height = 500
x = (tk.winfo_screenwidth()//4)
y = (tk.winfo_screenheight()//4)
tk.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#
pic = Frame(tk, width=100, height=100)
head = Frame(tk)
middle = Frame(tk)
bottom = Frame(tk)

#
head = ('TH Sarabun New',30,'bold')
content = ('TH Sarabun New',24)

#
imgHead = ImageTk.PhotoImage(Image.open("3\LogoCat.jpg"))

#
    #head
    L1 = Label(pic, image = imgHead)
    L1.pack()
    #content


#
pic.pack()
head.pack()
middle.pack()
bottom.pack()

tk.mainloop()