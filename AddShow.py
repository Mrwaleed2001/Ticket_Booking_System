import os
import tkinter.messagebox
import datetime
import mysql.connector as c
from tkinter import *

db=c.connect(host="localhost",user="root",password="Rockstar2",port="3306")
executioner=db.cursor()
def bk():
    global s_main
    s_main.destroy()
    os.system("Show_shows.py")
def submit():
    global s_main
    global s_entry
    global sd_entry
    global st_entry
    global m_entry
    global c_entry
    global executioner
    scrn_id=s_entry.get()
    cin_id=c_entry.get()
    mov_id=m_entry.get()
    show_date=sd_entry.get()
    show_time=st_entry.get()
    if show_time=="" or scrn_id=="" or mov_id=="" or cin_id=="" or show_date=="":
        tkinter.messagebox.showerror(title="ERROR",message="Kindly fill all fields!!!")
    else:
        is_full=False
        executioner.execute("insert into cinema_management.screen_show values(%s,%s,%s,%s,%s,%s)",(int(scrn_id),cin_id,int(mov_id),show_date,show_time,is_full))
        executioner.execute("commit")
        tkinter.messagebox.showinfo(title="INFO",message="Inserted.")
        s_main.destroy()
        os.system("Show_shows.py")
s_main=Tk()
s_main.title("Add show")
s_main.geometry("300x300")
s_main["bg"]="black"

scrnid_label=Label(s_main,text="Enter Screen ID",fg="white",bg="black",font="Times 10 bold")
scrnid_label.pack()
s_entry=Entry(s_main)
s_entry.pack()
cinid_label=Label(s_main,text="Enter Cinema ID",fg="white",bg="black",font="Times 10 bold")
cinid_label.pack()
c_entry=Entry(s_main)
c_entry.pack()
m_label=Label(s_main,text="Enter Movie ID",fg="white",bg="black",font="Times 10 bold")
m_label.pack()
m_entry=Entry(s_main)
m_entry.pack()
sd_label=Label(s_main,text="Show Date (YYYY-MM-DD)",fg="white",bg="black",font="Times 10 bold")
sd_label.pack()
sd_entry=Entry(s_main)
sd_entry.pack()
st_label=Label(s_main,text="Show Time(HH:MM:SS)",fg="white",bg="black",font="Times 10 bold")
st_label.pack()
st_entry=Entry(s_main)
st_entry.pack()

sub_btn=Button(s_main,text="Enter",fg="red",bg="yellow",font="Times 20 bold",command=submit)
sub_btn.pack()
bk_btn=Button(s_main,text="Back",fg="red",bg="yellow",font="Times 20 bold",command=bk)
bk_btn.pack()

s_main.mainloop()