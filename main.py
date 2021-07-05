from tkinter import *
import mysql.connector
from tkinter import messagebox

root = Tk()
root.geometry("500x300")
root.title("Login Page")

my_db = mysql.connector.connect(user="abdul-malik", password="@8-2fermENt2020", host="127.0.0.1", database="Life_Choices_Online", auth_plugin="mysql_native_password")
my_cursor = my_db.cursor()
xy = my_cursor.execute("select * from Lecturers")

for i in my_cursor:
    print(i)


root.mainloop()
