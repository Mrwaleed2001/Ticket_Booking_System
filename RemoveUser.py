import mysql.connector as c
from tkinter import *
import os
import tkinter.messagebox
db=c.connect(host="localhost",user="root",password="Rockstar2",port="3306")
executioner=db.cursor()
def bk():
    global window
    window.destroy()
    os.system("show_users.py")
def submission():
    global executioner
    global window
    global e
    user_id=e.get()
    if user_id == "":
        tkinter.messagebox.showerror(title="ERROR101",message="Kindly enter ID")
    else:
        found=False
        executioner.execute("select Cust_ID from cinema_management.customer_data")
        ids=executioner.fetchall()
        for l in ids:
            if user_id in l:
                found=True
        if found==True:
            user_id=(user_id,)
            executioner.execute("delete from cinema_management.customer_data where Cust_ID IN(%s)",user_id)
            executioner.execute("commit")
            tkinter.messagebox.showinfo(title="INFO",message="DELETED SUCCESSFULLY")
            window.destroy()
            os.system("show_users.py")
        else:
            tkinter.messagebox.showerror(title="ERROR101", message="ID NOT FOUND")
            window.destroy()
            os.system("show_users.py")

window=Tk()
window.title("Removing User!!!")
window.geometry("300x300")
window["bg"]="black"

labl=Label(window,text="Enter User-ID you need to remove from the list",fg="white",bg="black",font="Times 9 bold")
labl.pack()
e=Entry(window)
e.pack()
b=Button(window,text="Enter",fg="red",bg="yellow",font="Times 14 bold",command=submission)
b.pack()
bk_btn = Button(window, text="Back", fg="red", bg="Yellow", font="Times 20 bold",command=bk)
bk_btn.pack()
window.mainloop()