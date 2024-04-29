import os
import tkinter.messagebox

import mysql.connector as c
from tkinter import *
db = c.connect(host="localhost",user="root",password="Rockstar2",port="3306")
executioner = db.cursor()

def bk():
    global movie
    movie.destroy()
    os.system("show_movies.py")

def insert():
    global movie
    global moviereleased_entry
    global id_movie
    global movieN_entry
    global moviedate_entry
    global executioner
    is_release=moviereleased_entry.get()
    movie_name=movieN_entry.get()
    movie_date=moviedate_entry.get()
    if (movie_date != "") and (movie_name != "") and (is_release != ""):
        if is_release[0].upper() == 'T':
            release=True
        elif is_release[0].upper() == 'F':
            release=False
        executioner.execute("insert into cinema_management.movie values(%s,%s,%s,%s)",(id_movie,movie_name,release,movie_date))
        executioner.execute("commit")
        tkinter.messagebox.showinfo(title='INFO',message='Data saved')
        movie.destroy()
        os.system("show_movies.py")
    else:
        tkinter.messagebox.showerror(title='ERROR',message='Fill all data fields')


movie=Tk()
movie.title("ID")
movie.geometry("400x400")
movie["bg"]="black"

executioner.execute("select * from cinema_management.movie")
movies=executioner.fetchall()
ids=[]
for l in movies:
    ids.append(l[0])
id_movie=max(ids)+1


movieN_label=Label(movie,text="Movie Name",fg="white",bg="black")
movieN_label.pack()
movieN_entry=Entry(movie)
movieN_entry.pack()

moviereleased_label=Label(movie,text="T or F",fg="white",bg="black")
moviereleased_label.pack()
moviereleased_entry=Entry(movie)
moviereleased_entry.pack()

moviedate_label=Label(movie,text="Release Date(YYYY-MM-DD)",fg="white",bg="black")
moviedate_label.pack()
moviedate_entry=Entry(movie)
moviedate_entry.pack()

enter_btn=Button(movie,text="Enter",fg="red",bg="yellow",font="Times 20 bold",command=insert)
enter_btn.pack()
bk_btn = Button(movie, text="Back", fg="red", bg="Yellow", font="Times 20 bold",command=bk)
bk_btn.pack()

movie.mainloop()