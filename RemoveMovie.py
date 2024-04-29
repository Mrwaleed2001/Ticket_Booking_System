import os
import tkinter.messagebox

import mysql.connector as c
from tkinter import *

db=c.connect(host="localhost",user="root",password="Rockstar2",port="3306")
executioner=db.cursor()

def bk():
    global movie
    movie.destroy()
    os.system("show_movies.py")

def submit():
    global id_entry
    global executioner
    global movie
    movie_id=id_entry.get()
    if movie_id != "":
        found=False
        executioner.execute("select movie_id from cinema_management.movie")
        ids=executioner.fetchall()
        for l in ids:
            if int(movie_id) in l:
                found=True
        if found == True:
            executioner.execute(f"delete from cinema_management.movie where movie_id = {int(movie_id)}")
            executioner.execute("commit")
            tkinter.messagebox.showinfo(title="Success",message="Deleted Successfully")
            movie.destroy()
            os.system("show_movies.py")
        else:
            tkinter.messagebox.showerror(title="Error",message="ID NOT FOUND!!!")
            movie.destroy()
            os.system("show_movies.py")
    else:
        tkinter.messagebox.showerror(title="ERROR!!",message="Enter a valid ID!!!")

movie=Tk()
movie.title("ID")
movie.geometry("300x250")
movie["bg"]="black"

id_label=Label(movie,text="ENTER MOVIE ID",fg="white",bg="black",font="Times 12 bold")
id_label.pack()

id_entry=Entry(movie)
id_entry.pack()

enter_btn=Button(movie,text="Enter",fg="red",bg="yellow",font="Times 20 bold",command=submit)
enter_btn.pack()
bk_btn = Button(movie, text="Back", fg="red", bg="Yellow", font="Times 20 bold",command=bk)
bk_btn.pack()

movie.mainloop()