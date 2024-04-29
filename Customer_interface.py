import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import mysql.connector as c
import os
import datetime

def bk():
    global root
    tkinter.messagebox.showinfo(title="GOOD BYE!!!",message="SEE YOU NEXT TIME!!!")
    root.destroy()
    os.system("Login_Interface.py")
def book_mov():
    global root
    root.destroy()
    os.system("BookMovie.py")
def show_hist():
    global root
    root.destroy()
    os.system("show_history.py")

root=Tk()
root.title("MOVIE-PLEX   CINEMAS")
root.geometry("500x500")
root["bg"]="black"

header=Label(root,text="WELCOME TO MOVIEPLEX CINEMAS",bg="black",fg="White",font="Times 20 bold")
header.pack()

book_btn=Button(root,text="BOOK TICKET",fg="red",bg="yellow",font="Times 15 bold",command=book_mov).place(x=170,y=130)
bookh_btn=Button(root,text="SHOW HISTORY",fg="red",bg="yellow",font="Times 15 bold",command=show_hist).place(x=160,y=230)
backk_btn=Button(root,text="LOG-OUT",fg="red",bg="yellow",font="Times 15 bold",command=bk).place(x=190,y=330)


root.mainloop()