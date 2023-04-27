from tkinter import *
from tkinter import ttk
import csv

#
def validate_entry(text):
    if len(text) <=18:
        return True
    else:
        return False

root = Tk()

#
root.title('บันทึกค่าใช้จ่าย')
root.config(bg='white')

#
width = (root.winfo_screenwidth()//4)
height = (root.winfo_screenheight()//2)
x = (root.winfo_screenwidth()//3)
y = (root.winfo_screenheight()//4)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#
Font1 = ('TH Sarabun New',18,'bold')

#
I1 = PhotoImage(file='3\LogoCat.png')
I1 = I1.subsample(4)

#
F1 = Frame(root,bg='white')

#
IL1 = Label(F1,image=I1,bg="white",)
L1 = Label(F1,text='รายการค่าใช้จ่าย',bg="white",font=Font1)
A1 = Entry(F1,font=Font1,validate="key")
L2 = Label(F1,text='จำนวนเงิน',bg="white",font=Font1)
A2 = Entry(F1,font=Font1,validate="key")
S1 = ttk.Button(F1,text='บันทึก',command='')

#
A1['validatecommand']=(A1.register(validate_entry),'%P')
A2['validatecommand']=(A2.register(validate_entry),'%P')

#
IL1.grid(row=0,column=1,pady=5)
L1.grid(row=1,column=0,pady=5)
A1.grid(row=1,column=2)
L2.grid(row=2,column=0,pady=5)
A2.grid(row=2,column=2,)
S1.grid(row=3,column=1,pady=5)

#
F1.pack(padx=0,pady=10)

root.mainloop()