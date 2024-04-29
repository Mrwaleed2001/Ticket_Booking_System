import mysql.connector as c
from tkinter import *
import os
from tkinter import ttk

db=c.connect(host="localhost",user="root",password="Rockstar2",port="3306")
executioner=db.cursor()

def bk():
    global show_wind
    show_wind.destroy()
    os.system("Admin_interface.py")

def add_show():
    global show_wind
    show_wind.destroy()
    os.system("AddShow.py")
def remove_show():
    global show_wind
    show_wind.destroy()
    os.system("RemoveShow.py")


show_wind=Tk()
show_wind.title("Movies")
show_wind.geometry("600x600")
show_wind["bg"] = "black"
header=Label(show_wind,text="ALL",font="Times 30 bold",fg="White",bg="black")
header.pack()
header1=Label(show_wind,text="SHOWS",font="Times 30 bold",fg="White",bg="black")
header1.pack()

show_tree=ttk.Treeview(show_wind)
show_tree['columns']=("Screen.no","CinemaID","MovieID","Show Date","Show Time","Full")
show_tree.column("#0",width=60,minwidth=50)
show_tree.column("Screen.no",anchor="center",width=60)
show_tree.column("CinemaID",anchor="center",width=60)
show_tree.column("MovieID",anchor="center",width=60)
show_tree.column("Show Date",anchor="center",width=70)
show_tree.column("Show Time",anchor="center",width=70)
show_tree.column("Full",anchor="center",width=40)
show_tree.heading("#0",text="Serial",anchor="center")
show_tree.heading("Screen.no",text="ScreenID",anchor="center")
show_tree.heading("CinemaID",text="CinemaID",anchor="center")
show_tree.heading("MovieID",text="MovieID",anchor="center")
show_tree.heading("Show Date",text="Show Date",anchor="center")
show_tree.heading("Show Time",text="Show Time",anchor="center")
show_tree.heading("Full",text="Full",anchor="center")

executioner.execute("select * from cinema_management.screen_show")
SHOWS=executioner.fetchall()
y=0
for x in range(0,len(SHOWS)):
    show=SHOWS[y]
    if show[-1] == 1:
        is_full=True
    elif show[-1] == 0:
        is_full=False
    show_tree.insert(parent='',index='end',iid=x,text='Show'+str(x),values=(show[0],show[1],show[2],show[3],show[4],is_full))
    y+=1
show_tree.pack()

addshow_btn = Button(show_wind, text="ADD-SHOW", fg="red", bg="Yellow", font="Times 15 bold",command=add_show)
addshow_btn.place(x=50,y=400)
remshow_btn = Button(show_wind, text="REMOVE-SHOW", fg="red", bg="Yellow", font="Times 15 bold",command=remove_show)
remshow_btn.place(x=400, y=400)

bk_btn = Button(show_wind, text="Back", fg="red", bg="Yellow", font="Times 15 bold",command=bk)
bk_btn.place(x=275, y=400)
show_wind.mainloop()