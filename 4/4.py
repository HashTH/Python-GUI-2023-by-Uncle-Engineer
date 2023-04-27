from tkinter import *
from tkinter import ttk
import csv
import datetime


def validate_entry(text):
    if len(text) <=18:
        return True
    else:
        return False

def validate_int(value):
    if value.isdigit():
        return True
    elif value == "":
        return True
    else:
        return False
    

def saveCSV():
    A1get = A1.get()
    A2get = A2.get()
    TimeUpdate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = (A1get,A2get,TimeUpdate)
    with open('data.csv','a',newline='',encoding='UTF8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def readCSV():
    with open('data.csv','r',newline='',encoding='UTF8') as Ocsvfile:
        reader = csv.reader(Ocsvfile)
        data2 = []
        for row in reader:
            data2.append(row)
    return data2

def fillTable(treeview,data2):
    treeview.delete(*treeview.get_children())
    for row in data2:
        treeview.insert('',END,values=row)


        

root = Tk()

#
tabs = ttk.Notebook(root)
tabs.pack(ipadx=10,ipady=20)


###EP3
root.title('บันทึกค่าใช้จ่าย')
root.config(bg='white')

#
width = (root.winfo_screenwidth()//4)
height = (root.winfo_screenheight()//3)
x = (root.winfo_screenwidth()//3)
y = (root.winfo_screenheight()//4)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#
Font1 = ('TH Sarabun New',18,'bold')

#
Style1 = ttk.Style()
Style1.configure('TButton',font=Font1)
Style2 = ttk.Style()
Style2.configure('TFrame', background='white')

#
I1 = PhotoImage(file='3\LogoCat.png')
I1 = I1.subsample(4)

#
F1 = ttk.Frame(tabs)

#
IL1 = Label(F1,image=I1,bg="white",)
L1 = Label(F1,text='รายการค่าใช้จ่าย',bg="white",font=Font1)
A1 = Entry(F1,font=Font1,validate="key")
L2 = Label(F1,text='จำนวนเงิน',bg="white",font=Font1)
A2 = Entry(F1,font=Font1,validate='key')
S1 = ttk.Button(F1,text='บันทึก',command=saveCSV)

#
A1['validatecommand']=(A1.register(validate_entry),'%P')
A2['validatecommand']=(A2.register(validate_entry),'%P')
A2['validatecommand']=(A2.register(validate_int),'%P')

#
IL1.grid(row=0,column=1,pady=5)
L1.grid(row=1,column=0,pady=5)
A1.grid(row=1,column=2)
L2.grid(row=2,column=0,pady=5)
A2.grid(row=2,column=2,)
S1.grid(row=3,column=1,pady=5)

#
F1.pack(padx=0,pady=10)
##EP3

#EP4
F2 = ttk.Frame(tabs)

#
treeview = ttk.Treeview(F2,column=('รายการ','ค่าใช้จ่าย','เวลาทำรายการ'),show='headings',height=2)
treeview.heading('รายการ',text='รายการ')
treeview.heading('ค่าใช้จ่าย',text='ค่าใช้จ่าย')
treeview.heading('เวลาทำรายการ',text='เวลาทำรายการ')

treeview.column('รายการ',minwidth=0,width=180,stretch=NO)
treeview.column('ค่าใช้จ่าย',minwidth=0,width=120,stretch=NO)
treeview.column('เวลาทำรายการ',minwidth=0,width=160,stretch=NO)
treeview.pack()

#
data2 = readCSV()
fillTable(treeview, data2)

#
F2.pack(padx=0,pady=10)

#
tabs.add(F1,text='บันทึกข้อมูล')
tabs.add(F2,text='รายงาน')
##EP4

root.mainloop()