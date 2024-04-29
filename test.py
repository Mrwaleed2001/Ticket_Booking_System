import datetime

import mysql.connector as c
db = c.connect(host="localhost",user="root",password="Rockstar2",port="3306")
executioner = db.cursor()

data1=(int(1),'K-000')
executioner.execute("select available_seats from cinema_management.screen where screen_id IN(%s) and cinema_id IN(%s)",data1)
l=executioner.fetchall()
print(l)