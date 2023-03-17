from tkinter import *

tk = Tk()
tk.title('คำนวณ BMI')

# กำหนดขนาดและตำแหน่งหน้าต่าง GUI ให้อยู่ตรงกลางจอ
width = (tk.winfo_screenwidth()//2)
height = (tk.winfo_screenheight()//2)
x = (tk.winfo_screenwidth()//4)
y = (tk.winfo_screenheight()//4)
tk.geometry('{}x{}+{}+{}'.format(width, height, x, y))

FHead = ('TH Sarabun New',30,'bold')
FContent = ('TH Sarabun New',22)

Head = Label(tk,text='โปรแกรมคำนวณหาค่าดัชนีมวลกาย',font=FHead)

Question = Frame(tk)
WQuest = Label(Question,text='น้ำหนักตัว (kg.)',font=FContent)
HQuest = Label(Question,text='ส่วนสูง (cm.)',font=FContent)
WAns = Entry(Question,font=FContent)
HAns = Entry(Question,font=FContent)
WQuest.pack()
WAns.pack()
HQuest.pack()
HAns.pack()

def submitResult():
    Weight = float(WAns.get())
    Height = float(HAns.get())
    BMI = float(Weight/((Height/100)**2))
    BMIResult.config(text=(f'ค่าดัชนีมวลกายของคุณคือ \n {BMI:.2f}'))

SubMit = Button(Question,text='คำนวณ \u2193',font=FContent,command=submitResult)
SubMit.pack(pady=20)

BMIResult = Label(tk,text='',font=FContent)

Head.pack(pady=20)
Question.pack()
BMIResult.pack()

tk.mainloop()

