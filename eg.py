from tkinter import *
import mysql.connector
from tkinter import messagebox

root = Tk()
root.geometry("500x300")
root.title("Login Page")
root.config(bg="#1def8c")

name = StringVar()
password = StringVar()

Label(root, text="Please Enter Username", bg="#1def8c").place(x=30, y=50)
Label(root, text="Please Enter Password", bg="#1def8c").place(x=30, y=100)

name_ent = Entry(root)
name_ent.place(x=250, y=50)
password_ent = Entry(root, show="*")
password_ent.place(x=250, y=100)


def login():
    my_db = mysql.connector.connect(user="abdul-malik", password="@8-2fermENt2020", host="127.0.0.1", database="mydb", auth_plugin="mysql_native_password")
    my_cursor = my_db.cursor()
    xy = my_cursor.execute("select * from Login")

    for i in my_cursor:
        if name_ent.get() == i[0] and password_ent.get() == i[1]:
            messagebox.showinfo("Login Successful", "Access Granted")

            break

    if name_ent.get() == "" and password_ent.get() == "":
        messagebox.showerror("No Entries", "Please Insert your name and password")
    elif name_ent.get() != i[0] or password_ent.get() != i[1]:
        messagebox.showerror("Access Denied", "Incorrect Name or Password")
        name_ent.delete(0, END)
        password_ent.delete(0, END)


def register():
    if name_ent.get() == "" and password_ent.get() == "":
        messagebox.showerror("No Entries", "Please Insert your name and password")
    else:
        messagebox.showinfo("Register", "You have been Registered")
        my_db = mysql.connector.connect(user="abdul-malik", password="@8-2fermENt2020", host="127.0.0.1", database="mydb", auth_plugin="mysql_native_password")
        my_cursor = my_db.cursor()
        insert = "INSERT INTO Login (user, password) VALUES (%s, %s)"
        entries = (name_ent.get(), password_ent.get())
        my_cursor.execute(insert, entries)
        my_db.commit()


log_btn = Button(root, text="Login", command=login)
log_btn.place(x=350, y=150)
reg_btn = Button(root, text="Register New User", command=register)
reg_btn.place(x=265, y=200)

root.mainloop()
