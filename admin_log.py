from tkinter import *
import mysql.connector
from tkinter import messagebox

root = Tk()
root.geometry("650x650")
root.title("Admin Login Page")
root.config(bg="#89db33")

lc_icon = PhotoImage(file="images/lc academy.png")
canvas = Canvas(root, width=162, height=60, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=lc_icon)
canvas.place(x=240, y=20)

log_frame = LabelFrame(root, padx=130, pady=40, bg="#0F0F0F")
log_frame.place(x=85, y=145)

font_style = ("Sans Serif", 25, "bold", "italic")
Label(log_frame, text="Admin Only", bg="#0F0F0F", foreground="#FFFFFF", font=font_style).grid(column=2, row=1)

log_icon = PhotoImage(file="images/admin logo.png")
canvas = Canvas(log_frame, width=94, height=117, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=log_icon)
canvas.grid(column=2, row=2, padx=0, pady=20)


name_check = False
pass_check = False


def name_text(event):
    name_ent.configure(state=NORMAL)
    name_ent.delete(0, END)
    name_check = True


def pass_text(event):
    password_ent.configure(state=NORMAL)
    password_ent.delete(0, END)
    pass_check = True


name_ent = Entry(log_frame)
name_ent.insert(0, 'Username')
name_ent.configure(state=DISABLED)
name_ent.bind('<Button-1>', name_text)
name_ent.grid(column=2, row=3, padx=10, pady=10)

password_ent = Entry(log_frame, show="*")
password_ent.insert(0, 'Password')
password_ent.configure(state=DISABLED)
password_ent.bind('<Button-1>', pass_text)
password_ent.grid(column=2, row=4, padx=10, pady=10)


def show_pass():
    if tick.get() == 1:
        password_ent.configure(show="")
    if tick.get() == 0:
        password_ent.configure(show="*")


tick = IntVar()
Checkbutton(root, variable=tick, onvalue=1, offvalue=0, command=show_pass, bg="#0F0F0F", borderwidth=0, highlightthickness=0,).place(x=410, y=443)


def login():
    my_db = mysql.connector.connect(user="abdul-malik", password="@8-2fermENt2020", host="127.0.0.1", database="LC_Online", auth_plugin="mysql_native_password")
    my_cursor = my_db.cursor()
    xy = my_cursor.execute("select * from Admin")

    for i in my_cursor:
        if name_ent.get() == i[0] and password_ent.get() == i[1]:
            messagebox.showinfo("Login Successful", "Access Granted")
            root.destroy()
            import admin

            break

    if name_ent.get() == "" and password_ent.get() == "":
        messagebox.showerror("No Entries", "Please Insert your name and password")
    elif name_ent.get() != i[0] or password_ent.get() != i[1]:
        messagebox.showerror("Access Denied", "Incorrect Name or Password")
        name_ent.delete(0, END)
        password_ent.delete(0, END)


log_btn = Button(log_frame, text="Login", command=login, width=15, bg="#89db33")
log_btn.grid(column=2, row=5, padx=10, pady=10)
root.mainloop()
