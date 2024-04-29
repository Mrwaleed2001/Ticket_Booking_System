import os
from tkinter import *
def bk():
    global admin_wind
    admin_wind.destroy()
    os.system("Login_Interface.py")
def show_movies():
    global admin_wind
    admin_wind.destroy()
    os.system("show_movies.py")
def show_users():
    global admin_wind
    admin_wind.destroy()
    os.system("show_users.py")
def show_shows():
    global admin_wind
    admin_wind.destroy()
    os.system("Show_shows.py")


admin_wind=Tk()
admin_wind.title("ADMIN WINDOW")
admin_wind.geometry("300x300")
admin_wind["bg"] = "black"

header=Label(admin_wind,text="ADMIN",font="Times 30 bold",fg="White",bg="black")
header.pack()

#buttons
show_moviebtn=Button(admin_wind,text="Show Movies", fg="red", bg="Yellow", font="Times 15 bold",command=show_movies)
show_moviebtn.pack()
show_userbtn=Button(admin_wind,text="Show Users", fg="red", bg="Yellow", font="Times 15 bold",command=show_users)
show_userbtn.pack()
show_showsbtn=Button(admin_wind,text="Show Shows", fg="red", bg="Yellow", font="Times 15 bold",command=show_shows)
show_showsbtn.pack()
bk_btn = Button(admin_wind, text="Log-OUT", fg="red", bg="Yellow", font="Times 20 bold",command=bk)
bk_btn.pack()
admin_wind.mainloop()