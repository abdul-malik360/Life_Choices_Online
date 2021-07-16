from tkinter import *
import mysql.connector
from tkinter import messagebox
from datetime import datetime

root = Tk()
root.geometry("650x650")
root.title("Sign In/Out Page")
root.config(bg="#0F0F0F")

calender = StringVar()
clock = StringVar()
lc_icon = PhotoImage(file="images/lc academy.png")
canvas = Canvas(root, width=150, height=60, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=lc_icon)
canvas.place(x=240, y=20)

log_frame = LabelFrame(root, padx=130, pady=40, bg="#89db33")
log_frame.place(x=95, y=100)
time_frame = LabelFrame(root, width=440, height=50, bg="#0F0F0F")
time_frame.place(x=100, y=100)

Label(time_frame, text="Date ", bg="#0F0F0F", foreground="#89db33").place(x=10, y=10)
Label(time_frame, text="Time ", bg="#0F0F0F", foreground="#89db33").place(x=300, y=10)
now = datetime.now()
Label(time_frame, textvariable=calender, foreground="#FFFFFF", bg="#0F0F0F").place(x=50, y=10)
calender.set(now.strftime("%d-%m-%Y "))
Label(time_frame, textvariable=clock, foreground="#FFFFFF", bg="#0F0F0F").place(x=350, y=10)
clock.set(now.strftime("%H:%M:%S"))


log_icon = PhotoImage(file="images/login logo.png")
canvas = Canvas(log_frame, width=119, height=105, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=log_icon)
canvas.grid(column=2, row=1, padx=0, pady=20)


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
password_ent.grid(column=2, row=5, padx=10, pady=10)


def show_pass():
    if tick.get() == 1:
        password_ent.configure(show="")
    if tick.get() == 0:
        password_ent.configure(show="*")


tick = IntVar()
Checkbutton(root, variable=tick, onvalue=1, offvalue=0, command=show_pass, bg="#89db33", borderwidth=0, highlightthickness=0,).place(x=403, y=343)


def sign_in():
    my_db = mysql.connector.connect(user="abdul-malik", password="@8-2fermENt2020", host="127.0.0.1", database="LCA_Online", auth_plugin="mysql_native_password", buffered=True)
    my_cursor = my_db.cursor()
    my_cursor.execute("select * from Register")

    for i in my_cursor:
        if name_ent.get() == i[3] and password_ent.get() == i[5]:
            date = datetime.now().date().strftime("%Y-%m-%d")
            time = datetime.now().time().strftime("%H:%M:%S")
            insert = "INSERT INTO Log (UserName, Password, Date, TimeIn) VALUES (%s, %s, %s, %s)"
            entries = (name_ent.get(), password_ent.get(), date, time,)
            my_cursor.execute(insert, entries)
            my_db.commit()
            messagebox.showinfo("Login Successful", "Enjoy your day")

            break

    if name_ent.get() == "" or password_ent.get() == "":
        messagebox.showerror("No Entries", "Please enter Username and Password")
    elif name_ent.get() != i[3] or password_ent.get() != i[5]:
        messagebox.showerror("Login Unsuccessful", "Incorrect Username or Password")
        name_ent.delete(0, END)
        password_ent.delete(0, END)


in_btn = Button(log_frame, text="Sign in", command=sign_in, foreground="#89db33", bg="#0F0F0F")
in_btn.grid(column=2, row=6, padx=10, pady=10)


def sign_out():
    if name_ent.get() == "" or password_ent.get() == "":
        messagebox.showerror("No Entries", "Please enter Username and Password")
    else:
        messagebox.showinfo("Logout", "You have signed out")
        my_db = mysql.connector.connect(user="abdul-malik", password="@8-2fermENt2020", host="127.0.0.1", database="LCA_Online", auth_plugin="mysql_native_password")
        my_cursor = my_db.cursor()
        date = datetime.now().date().strftime("%Y-%m-%d")
        time = datetime.now().time().strftime("%H:%M:%S")
        insert = "UPDATE Log SET Date = %s, TimeOut = %s WHERE UserName = %s"
        entries = (date, time, name_ent.get())
        my_cursor.execute(insert, entries)
        my_db.commit()


out_btn = Button(log_frame, text="Sign Out", command=sign_out, foreground="#89db33", bg="#0F0F0F")
out_btn.grid(column=2, row=7, padx=10, pady=10)


def admin_go(event):
    root.withdraw()
    root.destroy()
    import admin_log


root.bind("<Control-a>", admin_go)


def register():
    root.destroy()
    import register


reg_btn = Button(log_frame, text="Register New User", command=register, foreground="#89db33", bg="#0F0F0F")
reg_btn.grid(column=2, row=8, padx=10, pady=10)


root.mainloop()
