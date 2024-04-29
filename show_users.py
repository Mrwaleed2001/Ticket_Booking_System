import os
import mysql.connector as c
from tkinter import *
from tkinter import ttk

db=c.connect(host="localhost",user="root",password="Rockstar2",port="3306")
executioner=db.cursor()

def bk():
    global user_wind
    user_wind.destroy()
    os.system("Admin_interface.py")

def add_user():
    pass
    global user_wind
    user_wind.destroy()
    os.system("UserAdd.py")


def remove_user():
    global user_wind
    user_wind.destroy()
    os.system("RemoveUser.py")

user_wind=Tk()
user_wind.title("Movies")
user_wind.geometry("800x800")
user_wind["bg"] = "black"
header=Label(user_wind,text="USERS",font="Times 30 bold",fg="White",bg="black")
header.pack()
header1=Label(user_wind,text="ALL",font="Times 30 bold",fg="White",bg="black")
header1.pack()

user_tree=ttk.Treeview(user_wind)
user_tree['columns']=("ID","Pass","fn","ln","s","h","city")
user_tree.column("#0",anchor="center",width=60,minwidth=50)
user_tree.column("ID",anchor="center",width=80,minwidth=50)
user_tree.column("Pass",anchor="center",width=80,minwidth=50)
user_tree.column("fn",anchor="w",width=100,minwidth=80)
user_tree.column("ln",anchor="w",width=100,minwidth=80)
user_tree.column("s",anchor="w",width=100,minwidth=70)
user_tree.column("h",anchor="center",width=80,minwidth=50)
user_tree.column("city",anchor="center",width=80,minwidth=50)
user_tree.heading("#0",text="Serial",anchor="center")
user_tree.heading("ID",text="User ID",anchor="center")
user_tree.heading("Pass",text="Password",anchor="center")
user_tree.heading("fn",text="FirstName",anchor="center")
user_tree.heading("ln",text="LastName",anchor="center")
user_tree.heading("s",text="STREET",anchor="center")
user_tree.heading("h",text="House",anchor="center")
user_tree.heading("city",text="CITY",anchor="center")

executioner.execute("select * from cinema_management.customer_data")
custs=executioner.fetchall()
y=0
for x in range(0,len(custs)):
    cust=custs[y]
    user_tree.insert(parent='',index='end',iid=x,text='USER'+str(x),values=(cust[0],cust[1],cust[2],cust[3],cust[4],cust[5],cust[-1]))
    y+=1

user_tree.pack()
add_btn = Button(user_wind, text="ADD-USER", fg="red", bg="Yellow", font="Times 15 bold",command=add_user)
add_btn.place(x=50,y=400)
remmov_btn = Button(user_wind, text="REMOVE-USER", fg="red", bg="Yellow", font="Times 15 bold",command=remove_user)
remmov_btn.place(x=600, y=400)
bk_btn = Button(user_wind, text="Back", fg="red", bg="Yellow", font="Times 15 bold",command=bk)
bk_btn.place(x=275, y=400)
user_wind.mainloop()