import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import mysql.connector as c
import os
import datetime

db = c.connect(host="localhost",user="root",password="Rockstar2",port="3306")
executioner = db.cursor()

def bk():
    global root
    root.destroy()
    os.system("Customer_interface.py")
def remove_hist():
    global root
    global executioner
    global user_id
    data=(user_id,)
    executioner.execute("delete from cinema_management.booking_history where ID=%s",data)
    executioner.execute("commit")
    tkinter.messagebox.showinfo(title="Success",message="Your history has been cleared")
    root.destroy()
    os.system("Customer_interface.py")

root=Tk()
root.title("Movies")
root.geometry("600x600")
root["bg"] = "black"
with open("User_Log.txt","r+") as file:
    user_id=file.read()
header=Label(root,text="HISTORY FOR ID",font="Times 30 bold",fg="White",bg="black")
header.pack()
header1=Label(root,text=user_id,font="Times 30 bold",fg="White",bg="black")
header1.pack()
executioner.execute("select * from cinema_management.booking_history")
HISTORY=executioner.fetchall()
if HISTORY==[]:
    tkinter.messagebox.showinfo(title="INFO", message="YOU HAVE NO BOOKING-HISTORY YET!!!")
    root.destroy()
    os.system("Customer_interface.py")

mov_tree=ttk.Treeview(root)
mov_tree['columns']=("ID","MovieID","S","C")
mov_tree.column("#0",width=100,minwidth=25)
mov_tree.column("ID",anchor="center",width=120)
mov_tree.column("MovieID",anchor="center",width=120)
mov_tree.column("S",anchor="center",width=120)
mov_tree.column("C",anchor="center",width=120)
mov_tree.heading("#0",text="SERIAL",anchor="center")
mov_tree.heading("ID",text="Your ID",anchor="center")
mov_tree.heading("MovieID",text="Movie-ID",anchor="center")
mov_tree.heading("S",text="Screen-ID",anchor="center")
mov_tree.heading("C",text="Cinema-ID",anchor="center")

y=0
for x in range(0,len(HISTORY)):
    hist=HISTORY[y]
    mov_tree.insert(parent='',index='end',iid=x,text='BOOKING '+str(x),values=(hist[0],hist[1],hist[2],hist[3]))
    y+=1
mov_tree.pack()
remmov_btn = Button(root, text="CLEAR-ALL", fg="red", bg="Yellow", font="Times 30 bold",command=remove_hist)
remmov_btn.pack()

bk_btn = Button(root, text="Back", fg="red", bg="Yellow", font="Times 25 bold",command=bk)
bk_btn.pack()

root.mainloop()