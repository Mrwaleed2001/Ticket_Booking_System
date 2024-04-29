import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import mysql.connector as c
import os
import datetime

db=c.connect(host="localhost",user="root",password="Rockstar2",port="3306")
executioner=db.cursor()

def bk():
    global root
    root.destroy()
    os.system("Customer_interface.py")
def mov_selected(event):


    def cin_selected(event):


        def scrn_selected(event):

            def seat_selected(event):
                def dt_select(event):

                    def t_select(event):


                        def book():
                            with open("User_Log.txt","r+") as f:
                                user_id=f.read()
                            d= dat_combo.get()
                            t=t_combo.get()
                            c = cin_combo.get()
                            scrn = scrn_combo.get()
                            data=(int(scrn),c)
                            executioner.execute("update cinema_management.screen set available_seats=available_seats-1 where screen_id IN(%s) and cinema_id IN(%s)",data)
                            executioner.execute("commit")
                            data=(int(scrn),c,seat_row,seat_no)
                            executioner.execute("update cinema_management.seat set is_booked=true where screen_id IN(%s) and cinema_id IN(%s) and row_letter IN(%s) and seat_NO IN(%s)",data)
                            executioner.execute("commit")
                            data=(user_id,int(scrn),c,movie_id,seat_row,seat_no)
                            executioner.execute("insert into cinema_management.booking values(%s,%s,%s,%s,%s,%s)",data)
                            executioner.execute("commit")
                            data=(user_id,movie_id,int(scrn),c)
                            executioner.execute("select * from cinema_management.booking_history")
                            hist=executioner.fetchall()
                            if data not in hist:
                                executioner.execute("insert into cinema_management.booking_history values(%s,%s,%s,%s)",data)
                                executioner.execute("commit")
                            executioner.execute("select * from cinema_management.screen")
                            screens1=executioner.fetchall()
                            for s in screens1:
                                if s[0] == int(scrn) and s[1]==c and s[-1]==0:
                                    is_full=True
                                    # d=d("-")
                                    # t=t.split(":")
                                    # y=int(d[0])
                                    # m1 = int(d[1])
                                    # day1 = int(d[-1])
                                    # h=int(t[0])
                                    # min1= int(t[1])
                                    # sec = int(t[-1])
                                    # d=datetime.date(y,m1,day1)
                                    # t=datetime.time(h,min1,sec)
                                    data=(int(scrn),c,movie_id,d,t)
                                    executioner.execute("update cinema_management.screen_show set isfull=1 where screen_id IN(%s) and cinema_id IN(%s) and movie_id IN(%s) and date_of_show IN(%s) and time_of_show IN(%s)",data)
                                    executioner.execute("commit")
                            tkinter.messagebox.showinfo(title="INFO",message=f"Your movie has been booked for date {d} and time {t} (NO REFUND NO EXCHANGE)")
                            root.destroy()
                            os.system("Customer_interface.py")

                        global executioner
                        global root
                        t= t_combo.get()
                        t_label = Label(root, text=t + " selected", fg="white", bg="black",
                                         font="Times 10 bold").pack()
                        header5 = Label(root, text="Confirm Booking", fg="white", bg="black", font="Times 11 bold").pack()
                        confirm_btn=Button(root,text="CONFIRM",fg="red",bg="yellow",font="Times 15 bold",command=book)
                        confirm_btn.pack()
                    global executioner
                    global root
                    dt=dat_combo.get()
                    dt_label = Label(root, text=dt + " selected", fg="white", bg="black", font="Times 10 bold").pack()
                    header5 = Label(root, text="Select Time", fg="white", bg="black", font="Times 11 bold").pack()
                    dt=dt.split("-")
                    year=int(dt[0])
                    month = int(dt[1])
                    day = int(dt[2])
                    date_of_show=datetime.date(year,month,day)
                    c = cin_combo.get()
                    scrn = scrn_combo.get()
                    movie_id = mov_id
                    shows = now_showing_movies
                    times=[]
                    for x in shows:
                        if x[-1]==0 and x[0] == int(scrn) and x[1] == c and x[2] == movie_id and x[3]==date_of_show and x[4] not in times:
                            times.append(x[4])
                    t_combo=ttk.Combobox(root,value=times)
                    t_combo.current(0)
                    t_combo.bind("<<ComboboxSelected>>",t_select)
                    t_combo.pack()
                global executioner
                global root
                st=st_combo.get()
                st_label = Label(root, text=st + " selected", fg="white", bg="black", font="Times 10 bold").pack()
                header4 = Label(root, text="Select Date", fg="white", bg="black", font="Times 11 bold").pack()
                s=[]
                for b in st:
                    s.append(b)
                seat_row=s[0]
                seat_no=int(s[-1])
                c = cin_combo.get()
                scrn = scrn_combo.get()
                movie_id=mov_id
                shows=now_showing_movies
                dates_show=[]
                for x in shows:
                    if x[-1]==0 and x[0] == int(scrn) and x[1]==c and x[2]==movie_id and x[3] not in dates_show:
                        dates_show.append(x[3])
                dat_combo=ttk.Combobox(root,value=dates_show)
                dat_combo.current(0)
                dat_combo.bind("<<ComboboxSelected>>",dt_select)
                dat_combo.pack()



            global executioner
            global root
            c=cin_combo.get()
            scrn = scrn_combo.get()
            scrn_label = Label(root, text="Screen "+str(scrn) + " selected", fg="white", bg="black", font="Times 10 bold").pack()
            header1 = Label(root, text="Select Seat", fg="white", bg="black", font="Times 11 bold").pack()
            executioner.execute("select * from cinema_management.seat")
            seats=executioner.fetchall()
            available_seats=[]
            for seat in seats:
                if seat[0] == int(scrn) and seat[1] == c and seat[-1]==0:
                    x=seat[2]+str(seat[3])
                    available_seats.append(x)
            st_combo=ttk.Combobox(root,value=available_seats)
            st_combo.current(0)
            st_combo.bind("<<ComboboxSelected>>",seat_selected)
            st_combo.pack()

        global root
        cinema=cin_combo.get()
        c_label = Label(root, text=cinema + " selected", fg="white", bg="black", font="Times 10 bold").pack()
        header1 = Label(root, text="Select Screen", fg="white", bg="black", font="Times 11 bold").pack()
        global now_showing_movies
        screens=[]
        for mov in now_showing_movies:
            if mov[1] == cinema and mov[2]==mov_id:
                if mov[0] not in screens:
                    screens.append(mov[0])
        scrn_combo=ttk.Combobox(root,value=screens)
        scrn_combo.current(0)
        scrn_combo.bind("<<ComboboxSelected>>",scrn_selected)
        scrn_combo.pack()

    global root
    s_movie=mov_combo.get()
    s_label=Label(root,text=s_movie+" selected",fg="white",bg="black",font="Times 10 bold").pack()
    header1 = Label(root, text="Select Cinema", fg="white", bg="black", font="Times 11 bold").pack()
    global all_movies
    cinemas=[]
    mov_id=0
    for mov in all_movies:
        if mov[1] == s_movie:
            mov_id=mov[0]
    global now_showing_movies
    for x in now_showing_movies:
        if x[2] == mov_id:
            if x[1] not in cinemas:
                cinemas.append(x[1])
    cin_combo=ttk.Combobox(root,value=cinemas)
    cin_combo.current(0)
    cin_combo.bind("<<ComboboxSelected>>",cin_selected)
    cin_combo.pack()

root=Tk()
root.title("MOVIE-PLEX   CINEMAS")
root.geometry("400x600")
root["bg"]="black"

header=Label(root,text="NOW-SHOWING",fg="white",bg="black",font="Times 10 bold")
header.pack()
header1=Label(root,text="Select Movie",fg="white",bg="black",font="Times 11 bold").pack()

executioner.execute("select * from cinema_management.screen_show ")
now_showing_movies=executioner.fetchall()
movies_id=[]
for x in now_showing_movies:
    if x[2] not in movies_id:
        movies_id.append(x[2])

executioner.execute("select * from cinema_management.movie ")
all_movies=executioner.fetchall()
now_showing_movies2=[]
for movie in all_movies:
    if movie[0] in movies_id:
        now_showing_movies2.append(movie[1])

mov_combo=ttk.Combobox(root,value=now_showing_movies2)
mov_combo.current(0)
mov_combo.bind("<<ComboboxSelected>>",mov_selected)
mov_combo.pack()
Back_btn=Button(root,text="Back",fg="red",bg="Yellow",font="Times 20 bold",command=bk).place(x=0,y=0)
root.mainloop()