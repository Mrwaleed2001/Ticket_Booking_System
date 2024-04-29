from tkinter import *
from tkinter import ttk
import mysql.connector as c
import os


db=c.connect(host="localhost",user="root",password="Rockstar2",port="3306")
executioner=db.cursor()
def bk():
    global movies
    movies.destroy()
    os.system("Admin_interface.py")

def add_movie():
    global movies
    movies.destroy()
    os.system("MovieAdd.py")


def remove_movie():
    global movies
    movies.destroy()
    os.system("RemoveMovie.py")

movies=Tk()
movies.title("Movies")
movies.geometry("600x600")
movies["bg"] = "black"
header=Label(movies,text="MOVIES",font="Times 30 bold",fg="White",bg="black")
header.pack()
header1=Label(movies,text="ALL",font="Times 30 bold",fg="White",bg="black")
header1.pack()

mov_tree=ttk.Treeview(movies)
mov_tree['columns']=("MovieID","Movie Name","DOR","RELEASED")
mov_tree.column("#0",width=90,minwidth=25)
mov_tree.column("MovieID",anchor="center",width=120)
mov_tree.column("Movie Name",anchor="w",width=120)
mov_tree.column("DOR",anchor="center",width=120)
mov_tree.column("RELEASED",anchor="center",width=120)
mov_tree.heading("#0",text="SERIAL",anchor="center")
mov_tree.heading("MovieID",text="Movie ID",anchor="center")
mov_tree.heading("Movie Name",text="Movie Name",anchor="w")
mov_tree.heading("DOR",text="Date of release",anchor="center")
mov_tree.heading("RELEASED",text="Released",anchor="center")

executioner.execute("select * from cinema_management.movie")
MOVIES=executioner.fetchall()
y=0
for x in range(0,len(MOVIES)):
    mov=MOVIES[y]
    if mov[2] == 1:
        release=True
    elif mov[2] == 0:
        release=False
    mov_tree.insert(parent='',index='end',iid=x,text='Movie'+str(x),values=(mov[0],mov[1],mov[-1],release))
    y+=1

mov_tree.pack()

addmov_btn = Button(movies, text="ADD-MOVIE", fg="red", bg="Yellow", font="Times 15 bold",command=add_movie)
addmov_btn.place(x=50,y=400)
remmov_btn = Button(movies, text="REMOVE-MOVIE", fg="red", bg="Yellow", font="Times 15 bold",command=remove_movie)
remmov_btn.place(x=400, y=400)

bk_btn = Button(movies, text="Back", fg="red", bg="Yellow", font="Times 15 bold",command=bk)
bk_btn.place(x=275, y=400)

movies.mainloop()