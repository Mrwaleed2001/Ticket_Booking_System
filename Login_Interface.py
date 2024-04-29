import os
import tkinter.messagebox
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as c

db = c.connect(host="localhost",user="root",password="Rockstar2",port="3306")
executioner = db.cursor()

def sign_in():
    global executioner
    global login
    global id_entry
    global pass_entry
    password= pass_entry.get()
    user_id= id_entry.get()
    if user_id=="" or password=="":
        tkinter.messagebox.showerror(title="EMPTY",message="Kindly fill all fields!!!")
    elif user_id[0].upper()=="A":
        executioner.execute("select * from cinema_management.admin_data")
        admins=executioner.fetchall()
        id_found=False
        pass_found=False
        for admin in admins:
            if admin[0] == user_id:
                id_found=True
                if admin[1] == password:
                    pass_found=True
                    break

        if id_found == True and pass_found == True:
            login.destroy()
            os.system("Admin_interface.py")
        else:
            tkinter.messagebox.showerror(title="ERROR",message="Incorrect ID or PASS!!!")
    elif user_id[0].upper() == "C":
        executioner.execute("select * from cinema_management.customer_data")
        customers = executioner.fetchall()
        id_found = False
        pass_found = False
        for customer in customers:
            if customer[0] == user_id:
                id_found = True
                if customer[1] == password:
                    pass_found = True
                    break

        if id_found == True and pass_found == True:
            with open("User_Log.txt","w+") as f:
                f.write(user_id)
            login.destroy()
            os.system("Customer_interface.py")
        else:
            tkinter.messagebox.showerror(title="ERROR", message="Incorrect ID or PASS!!!")


def sign_up():
    global login
    login.destroy()
    os.system("Sign_up_interface.py")


login=Tk()
login.title("MOVIEPLEX CINEMAS")
login.geometry("430x608")
login["bg"] = "black"


#header
header=Label(login,text="Movie Plex",font="Times 30 bold",fg="White",bg="black")
header.pack()
#ID and Pass
id_label=Label(login,text="ID",font="Times 10 bold",fg="White",bg="black")
id_label.place(x=130,y=250)

id_entry=Entry(login,width=30,relief="groove")
id_entry.place(x=150,y=250)

pass_label=Label(login,text="Password",font="Times 10 bold",fg="White",bg="black")
pass_label.place(x=90,y=270)

pass_entry=Entry(login,width=30,relief="groove")
pass_entry.place(x=150,y=270)
#Buttons

signin_btn=Button(login,text="SIGN-IN",fg="red",bg="Yellow",font="Times 20 bold",command=sign_in)
signin_btn.place(x=80,y=330)

signup_btn=Button(login,text="SIGN-UP",fg="red",bg="Yellow",font="Times 20 bold",command=sign_up)
signup_btn.place(x=250,y=330)

login.mainloop()