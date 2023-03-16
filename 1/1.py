from tkinter import *

tk = Tk()
tk.title('1st Step')
tk.geometry('1000x200')

font1 = ('TH Sarabun New',100,'bold')
L1 = Label(tk,text='Happy New Year!',font=font1,fg='red')
L1.pack()

tk.mainloop()
