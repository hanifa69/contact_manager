from collections import*
from tkinter import*
from tkinter.ttk import*
from tkinter import messagebox
w = Tk()
w.geometry('600x400')
w.title('دفترچه تلفن')
w.config(bg='lightgreen')
w.config(cursor='hand2')
## exchange , hand1 , hand2 ,dot,...
#w.withdraw()          مخفي کردن پنجره
#icon=PhotoImage(file='icon.png')
#w.iconphoto(True,icon)


#توابع
#تابع سيو کاربر جديد
def add():
    contact=Contact(n_fname.get(),n_lname.get(),n_mobal.get())
    contacts.append(contact)
    show(tree,contact)
# واسه فريم 3تابع اضافه کردن
def show_add_form():
    w = Tk()
#فریم ها
    lf=Frame(w)
    lf.pack(side=TOP)
    rf=Frame(w)
    rf.pack(side=TOP)
    fnf=Frame(lf)
    fnf.pack(side=TOP)
    lnf=Frame(lf)
    lnf.pack(side=TOP)
    mf=Frame(lf)
    mf.pack(side=TOP)

    global n_fname
    global n_lname
    global n_mobal
    n_fname=StringVar(fnf)
    n_lname=StringVar(fnf)
    n_mobal=StringVar(fnf)
    
    a=Label(fnf,text="اسم")
    a.pack(side=TOP)
    a1=Entry(fnf,textvariable=n_fname)
    a1.pack(side=TOP)
    a2=Label(fnf,text="فاميل")
    a2.pack(side=TOP)
    a3=Entry(fnf,textvariable=n_lname)
    a3.pack(side=TOP)
    a4=Label(fnf,text="شماره")
    a4.pack(side=TOP)
    a5=Entry(fnf,textvariable=n_mobal)
    a5.pack(side=TOP)
    #
    a6=Button(rf,text="افزودن",command=add)                                   
    a6.pack()
    w.mainloop()
def show(tree,contacts):
##    for contact in contacts:
    tree.insert('',END,values=(.0))
    
    