from tkinter  import *
from tkinter import  messagebox
import mysql.connector as m1
con=m1.connect(host='localhost',database='bankdata',user='root',password='')
root= Tk()
root.title('Bank Application')
root.configure(bg='cyan')
root.geometry('750x350+100+100')

def submit():
    a=int(e1.get())
    b=e2.get()
    c=e3.get()
    d=int(e4.get())
    cursor = con.cursor()
    qry = "insert into employee values({},'{}','{}',{})".format(a, b, c,d)
    cursor.execute(qry)
    con.commit()
    messagebox.showinfo(message = 'data added successfully')

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)




l1=Label(root, text='Employee-ID', bg='black',padx=28,pady=10, fg='red',font=('Arial','15'))
l1.grid(row=0,column=0,padx=10,pady=10)

l2=Label(root, text='Employee Name', bg='black',padx=28,pady=10, fg='red',font=('Arial','15'))
l2.grid(row=1,column=0,padx=10,pady=10)

l3=Label(root, text='Employee Department', bg='black',padx=14,pady=10, fg='red',font=('Arial','15'))
l3.grid(row=2,column=0,padx=10,pady=10)

l4=Label(root, text='Employee Salary', bg='black',padx=28,pady=10, fg='red',font=('Arial','15'))
l4.grid(row=3,column=0,padx=10,pady=10)

e1=Entry(root, font=('Arial','25'))
e1.grid(row=0, column=1,padx=10,pady=10)

e2=Entry(root, font=('Arial','25'))
e2.grid(row=1, column=1,padx=10,pady=10)

e3=Entry(root, font=('Arial','25'))
e3.grid(row=2, column=1,padx=10,pady=10)

e4=Entry(root, font=('Aerial','25'))
e4.grid(row=3, column=1,padx=10,pady=10)

b1=Button(root, text='Clear', fg='red',font=('Agency FB','15'),padx=20,command=clear)
b1.grid(row=4,column=0, padx=0,pady=20)

var1=StringVar()
b2=Button(root, text='Submit', fg='red',font=('Agency FB','15'),padx=20,command=submit)
b2.grid(row=4,column=1, padx=0,pady=20)

b3=Button(root, text='Exit', fg='red',font=('Agency FB','15'),padx=20,command=root.destroy)
b3.grid(row=4,column=3, padx=0,pady=20)


root.mainloop()
