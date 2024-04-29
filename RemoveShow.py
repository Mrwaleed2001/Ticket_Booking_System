import os
import tkinter.messagebox

import mysql.connector as c
from tkinter import *

db=c.connect(host="localhost",user="root",password="Rockstar2",port="3306")
executioner=db.cursor()


def bk():
    global s_main
    s_main.destroy()
    os.system("Show_shows.py")
def screen_rem():
    def bk1():
        scrn_wind.destroy()
        os.system("RemoveShow.py")
    def sub_scrn():
        global executioner
        scrn_id=e.get()
        if scrn_id == "":
            tkinter.messagebox.showerror(title="ERROR101",message="Enter ID")
        else:
            found=False
            executioner.execute("select cinema_id from cinema_management.screen_show")
            ids = executioner.fetchall()
            for l in ids:
                if int(scrn_id) in l:
                    found = True
            if found==True:
                scrn_id=(int(scrn_id),)
                executioner.execute("delete from cinema_management.screen_show where screen_id IN(%s)",scrn_id)
                executioner.execute("commit")
                tkinter.messagebox.showinfo(title="INFO", message="Deleted all shows of screen id entered")
                scrn_wind.destroy()
                os.system("Show_shows.py")
            else:
                tkinter.messagebox.showerror(title="Error", message="ID NOT FOUND!!!")
                scrn_wind.destroy()
                os.system("Show_shows.py")
    global s_main
    s_main.destroy()
    scrn_wind=Tk()
    scrn_wind.title("Remove Shows on a Screen")
    scrn_wind.geometry("250x250")
    scrn_wind["bg"]="black"

    l=Label(scrn_wind,text="Enter Screen ID of SHOW to remove",fg="white",bg="black",font="Times 10 bold")
    l.pack()
    e=Entry(scrn_wind)
    e.pack()
    sub_btn=Button(scrn_wind,text="Enter",fg="red",bg="yellow",font="Times 15 bold",command=sub_scrn)
    sub_btn.pack()
    bk_btn = Button(scrn_wind, text="Back", fg="red", bg="yellow", font="Times 20 bold", command=bk1)
    bk_btn.pack()
    scrn_wind.mainloop()
def cin_show_rem():
    def bk1():
        scrn_wind.destroy()
        os.system("RemoveShow.py")
    def sub_cin():
        global executioner
        cin_id = e.get()
        if cin_id == "":
            tkinter.messagebox.showerror(title="ERROR101", message="Enter ID")
        else:
            found=False
            executioner.execute("select cinema_id from cinema_management.screen_show")
            ids=executioner.fetchall()
            for l in ids:
                if cin_id in l:
                    found= True
            if found==True:
                cin_id = (cin_id,)
                executioner.execute("delete from cinema_management.screen_show where cinema_id IN(%s)", cin_id)
                executioner.execute("commit")
                tkinter.messagebox.showinfo(title="INFO", message="Deleted all shows of cinema id entered")
                scrn_wind.destroy()
                os.system("Show_shows.py")
            else:
                tkinter.messagebox.showerror(title="Error", message="ID NOT FOUND!!!")
                scrn_wind.destroy()
                os.system("Show_shows.py")
    global s_main
    s_main.destroy()
    scrn_wind = Tk()
    scrn_wind.title("Remove Shows in a CINEMA")
    scrn_wind.geometry("250x250")
    scrn_wind["bg"] = "black"

    l = Label(scrn_wind, text="Enter Cinema ID of SHOW to remove", fg="white", bg="black", font="Times 10 bold")
    l.pack()
    e = Entry(scrn_wind)
    e.pack()
    sub_btn = Button(scrn_wind, text="Enter", fg="red", bg="yellow", font="Times 15 bold", command=sub_cin)
    sub_btn.pack()
    bk_btn = Button(scrn_wind, text="Back", fg="red", bg="yellow", font="Times 20 bold", command=bk1)
    bk_btn.pack()
    scrn_wind.mainloop()
def mov_show_rem():
    def bk1():
        scrn_wind.destroy()
        os.system("RemoveShow.py")
    def sub_mov():
        global executioner
        mov_id = e.get()
        if mov_id == "":
            tkinter.messagebox.showerror(title="ERROR101", message="Enter ID")
        else:
            found=False
            executioner.execute("select movie_id from cinema_management.screen_show")
            ids=executioner.fetchall()
            for l in ids:
                if int(mov_id) in l:
                    found=True
            if found==True:
                mov_id = (int(mov_id),)
                executioner.execute("delete from cinema_management.screen_show where movie_id IN(%s)", mov_id)
                executioner.execute("commit")
                tkinter.messagebox.showinfo(title="INFO", message="Deleted all shows of Movie id entered")
                scrn_wind.destroy()
                os.system("Show_shows.py")
            else:
                tkinter.messagebox.showerror(title="ERROR",message="ID NOT FOUND")
                scrn_wind.destroy()
                os.system("Show_shows.py")
    global s_main
    s_main.destroy()
    scrn_wind = Tk()
    scrn_wind.title("Remove Shows in a CINEMA")
    scrn_wind.geometry("250x250")
    scrn_wind["bg"] = "black"

    l = Label(scrn_wind, text="Enter Movie ID of SHOW to remove", fg="white", bg="black", font="Times 10 bold")
    l.pack()
    e = Entry(scrn_wind)
    e.pack()
    sub_btn = Button(scrn_wind, text="Enter", fg="red", bg="yellow", font="Times 15 bold", command=sub_mov)
    sub_btn.pack()
    bk_btn = Button(scrn_wind, text="Back", fg="red", bg="yellow", font="Times 20 bold", command=bk1)
    bk_btn.pack()
    scrn_wind.mainloop()

s_main=Tk()
s_main.title("Remove show")
s_main.geometry("300x450")
s_main["bg"]="black"


rsid_btn=Button(s_main,text="Remove By Screen ID",fg="red",bg="yellow",font="Times 20 bold",command=screen_rem)
rsid_btn.place(x=0,y=0)

csid_btn=Button(s_main,text="Remove By Cinema ID",fg="red",bg="yellow",font="Times 20 bold",command=cin_show_rem)
csid_btn.place(x=0,y=100)

msid_btn=Button(s_main,text="Remove By Movie ID",fg="red",bg="yellow",font="Times 20 bold",command=mov_show_rem)
msid_btn.place(x=0,y=200)

bk_btn=Button(s_main,text="Back",fg="red",bg="yellow",font="Times 20 bold",command=bk)
bk_btn.place(x=140,y=350)
s_main.mainloop()