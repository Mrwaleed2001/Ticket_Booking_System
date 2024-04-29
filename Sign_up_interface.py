import os
import tkinter.messagebox
from tkinter import *
import mysql.connector as connection

db = connection.connect(host="localhost",user="root",password="Rockstar2",port="3306")
executioner = db.cursor()

def bk():
    global wind_sign_up
    wind_sign_up.destroy()
    os.system("Login_Interface.py")

def submit():
    global wind_sign_up
    global P_entry
    global RP_entry
    global FirstN_entry
    global LastN_entry
    global STREET_entry
    global CITY_entry
    global HOUSE_entry
    password=P_entry.get()
    l_name = LastN_entry.get()
    f_name = FirstN_entry.get()
    house_no = HOUSE_entry.get()
    street = STREET_entry.get()
    city = CITY_entry.get()
    Rpassword = RP_entry.get()
    if (password != "") and (Rpassword != "") and (street != "") and (house_no != "") and (city != "") and (f_name != "") and (l_name != ""):
        if password == Rpassword:
            cust_ids=[]
            global executioner
            executioner.execute("select * from cinema_management.customer_data")
            all_cust=executioner.fetchall()
            for cust in all_cust:
                cust_ids.append(cust[0])
            max_cust_id=max(cust_ids)
            max_cust_id=max_cust_id.split("-")
            max_int=int(max_cust_id[-1])
            new_cust=max_int+1
            cust_id = "C-" + str(new_cust)
            if len(cust_id) < 5:
                zeroes = 5 - len(cust_id)
                customer_id = "C-" + "0"*zeroes + str(new_cust)
            executioner.execute("insert into cinema_management.customer_data values(%s,%s,%s,%s,%s,%s,%s)",(customer_id,password,f_name,l_name,street,house_no,city))
            executioner.execute("commit")
            tkinter.messagebox.showinfo(title="Success",message=f"Data stored Successfully your id is {customer_id}")
            wind_sign_up.destroy()
            os.system("Login_Interface.py")
        else:
            tkinter.messagebox.showerror(title="MIS-MATCH", message="ENTER SAME PASSWORDS IN PASSWORD RELATED FIELDS!!!")
    else:
        tkinter.messagebox.showerror(title="EMPTY", message="ENTER DATA IN ALL FIELDS!!!")


wind_sign_up = Tk()
wind_sign_up.title("Sign-Up Window")
wind_sign_up.geometry("430x500")
wind_sign_up["bg"] = "black"

# SIGN-UP header
header1 = Label(wind_sign_up, text="SIGN-UP", font="Times 30 bold", fg="White", bg="black")
header1.pack()

# sign Up fields
P_entry = Entry(wind_sign_up, width=50, relief="groove")
P_entry.place(x=60, y=80)

RP_entry = Entry(wind_sign_up, width=50, relief="groove")
RP_entry.place(x=120, y=120)

FirstN_entry = Entry(wind_sign_up, width=50, relief="groove")
FirstN_entry.place(x=90, y=160)

LastN_entry = Entry(wind_sign_up, width=50, relief="groove")
LastN_entry.place(x=90, y=200)

STREET_entry = Entry(wind_sign_up, width=50, relief="groove")
STREET_entry.place(x=60, y=240)

HOUSE_entry = Entry(wind_sign_up, width=50, relief="groove")
HOUSE_entry.place(x=60, y=280)

CITY_entry = Entry(wind_sign_up, width=50, relief="groove")
CITY_entry.place(x=60, y=320)

label_p = Label(wind_sign_up, text="Password", fg="white", bg="black", font="Times 10 bold")
label_p.place(x=0, y=80)

label_rp = Label(wind_sign_up, text="Re-enter Password", fg="white", bg="black", font="Times 10 bold")
label_rp.place(x=0, y=120)

label_fn = Label(wind_sign_up, text="First Name", fg="white", bg="black", font="Times 10 bold")
label_fn.place(x=0, y=160)

label_ln = Label(wind_sign_up, text="Last Name", fg="white", bg="black", font="Times 10 bold")
label_ln.place(x=0, y=200)

label_strt = Label(wind_sign_up, text="Street", fg="white", bg="black", font="Times 10 bold")
label_strt.place(x=0, y=240)

label_h = Label(wind_sign_up, text="House.No", fg="white", bg="black", font="Times 10 bold")
label_h.place(x=0, y=280)

label_city = Label(wind_sign_up, text="City", fg="white", bg="black", font="Times 10 bold")
label_city.place(x=0, y=320)

# submit
submit_btn = Button(wind_sign_up, text="SUBMIT", font="Times 25 bold", relief="groove", fg="red", bg="yellow",command=submit)
submit_btn.place(x=150, y=350)
bk_btn=Button(wind_sign_up,text="BACK",font="Times 20 bold",fg="red",bg="Yellow",command=bk)
bk_btn.place(x=150,y=450)

wind_sign_up.mainloop()