from tkinter import *

tk = Tk()
tk.title('โปรแกรมหารจ่าย')
# กำหนดขนาดและตำแหน่งหน้าต่าง GUI ให้อยู่ตรงกลางจอ
tk.update_idletasks()
width = (tk.winfo_screenwidth()//2)
height = (tk.winfo_screenheight()//2)
x = (tk.winfo_screenwidth()//4)
y = (tk.winfo_screenheight()//4)
tk.geometry('{}x{}+{}+{}'.format(width, height, x, y))

Head = Label(tk,text='โปรแกรมหารจ่าย',font=('TH Sarabun New',30,'bold'),fg='red')

Question = Frame(tk)
E1 = Label(Question,text='ค่าอาหารทั้งหมด (บาท)',font=('TH Sarabun New',20))
E2 = Label(Question,text='มีทั้งหมดกี่คน',font=('TH Sarabun New',20))
A1 = Entry(Question,font=('TH Sarabun New',20))
A2 = Entry(Question,font=('TH Sarabun New',20))
E1.pack()
A1.pack()
E2.pack()
A2.pack()

def showResult():
    A1 = str(A1.get())
    A2 = str(A2.get())

Submit1 = Button(Question,text='คำนวณ',font=('TH Sarabun New',20),command=showResult)
Submit1.pack(pady=10)

Head.pack(padx=10,pady=10)
Question.pack()

tk.mainloop()