from tkinter import *
import mysql.connector
from tkinter import messagebox

root = Tk()
root.geometry("650x650")
root.title("Register Page")
root.config(bg="#0F0F0F")

lc_icon = PhotoImage(file="images/lc academy.png")
canvas = Canvas(root, width=150, height=60, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=lc_icon)
canvas.place(x=470, y=550)

lc_logo = PhotoImage(file="images/rsz_lc_logo.png")
canvas = Canvas(root, width=85, height=52, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=lc_logo)
canvas.place(x=30, y=20)

reg_logo = PhotoImage(file="images/reg logo.png")
canvas = Canvas(root, width=100, height=100, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=reg_logo)
canvas.place(x=250, y=100)

font_style = ("Sans Serif", 25, "bold", "italic")
Label(root, text="Create Your Account", bg="#0F0F0F", foreground="#FFFFFF", font=font_style).place(x=120, y=50)

Label(root, text="ID Number", bg="#0F0F0F", foreground="#89db33").place(x=110, y=230)
Label(root, text="Name", bg="#0F0F0F", foreground="#89db33").place(x=110, y=280)
Label(root, text="Surname", bg="#0F0F0F", foreground="#89db33").place(x=110, y=330)
Label(root, text="Username", bg="#0F0F0F", foreground="#89db33").place(x=110, y=380)
Label(root, text="Role", bg="#0F0F0F", foreground="#89db33").place(x=330, y=230)
Label(root, text="Password", bg="#0F0F0F", foreground="#89db33").place(x=110, y=430)
Label(root, text="Cell Number", bg="#0F0F0F", foreground="#89db33").place(x=330, y=280)
Label(root, text="Next of kin", bg="#0F0F0F", foreground="#89db33").place(x=330, y=330)
Label(root, text="Next of Kin Cell Number", bg="#0F0F0F", foreground="#89db33").place(x=330, y=380)

idcheck = False
namecheck = False
snamecheck = False
unamecheck = False
rolecheck = False
passcheck = False
cellcheck = False
kincheck = False
kcellcheck = False


def id_text(event):
    id_ent.configure(state=NORMAL)
    id_ent.delete(0, END)
    idcheck = True


def name_text(event):
    name_ent.configure(state=NORMAL)
    name_ent.delete(0, END)
    namecheck = True


def sname_text(event):
    surname_ent.configure(state=NORMAL)
    surname_ent.delete(0, END)
    snamecheck = True


def uname_text(event):
    username_ent.configure(state=NORMAL)
    username_ent.delete(0, END)
    unamecheck = True


def role_text(event):
    role_ent.configure(state=NORMAL)
    role_ent.delete(0, END)
    rolecheck = True


def pass_text(event):
    password_ent.configure(state=NORMAL)
    password_ent.delete(0, END)
    passcheck = True


def cell_text(event):
    cell_ent.configure(state=NORMAL)
    cell_ent.delete(0, END)
    cellcheck = True


def kin_text(event):
    next_kin_ent.configure(state=NORMAL)
    next_kin_ent.delete(0, END)
    kincheck = True


def kcell_text(event):
    kin_cell_ent.configure(state=NORMAL)
    kin_cell_ent.delete(0, END)
    kcellcheck = True


id_ent = Entry(root, width=24)
id_ent.insert(0, 'eg. 0002035200084')
id_ent.configure(state=DISABLED)
id_ent.bind("<Button>", id_text)
id_ent.place(x=110, y=250)


name_ent = Entry(root, width=24)
name_ent.insert(0, 'eg. Achmat')
name_ent.configure(state=DISABLED)
name_ent.bind('<Button-1>', name_text)
name_ent.place(x=110, y=300)


surname_ent = Entry(root, width=24)
surname_ent.insert(0, 'eg. Breda')
surname_ent.configure(state=DISABLED)
surname_ent.bind('<Button-1>', sname_text)
surname_ent.place(x=110, y=350)


username_ent = Entry(root, width=24)
username_ent.insert(0, 'eg. Achmat28')
username_ent.configure(state=DISABLED)
username_ent.bind('<Button-1>', uname_text)
username_ent.place(x=110, y=400)


role_ent = Entry(root, width=24)
role_ent.insert(0, 'Staff/Lecturer/Student/Visitor')
role_ent.configure(state=DISABLED)
role_ent.bind('<Button-1>', role_text)
role_ent.place(x=330, y=250)


password_ent = Entry(root, width=24)
password_ent.insert(0, 'eg. uthmaan or 0000')
password_ent.configure(state=DISABLED)
password_ent.bind("<Button>", pass_text)
password_ent.place(x=110, y=450)


cell_ent = Entry(root, width=24)
cell_ent.insert(0, 'eg. 0842567852')
cell_ent.configure(state=DISABLED)
cell_ent.bind('<Button-1>', cell_text)
cell_ent.place(x=330, y=300)


next_kin_ent = Entry(root, width=24)
next_kin_ent.insert(0, 'eg. Parent/Sibling/Spouse')
next_kin_ent.configure(state=DISABLED)
next_kin_ent.bind('<Button-1>', kin_text)
next_kin_ent.place(x=330, y=350)


kin_cell_ent = Entry(root, width=24)
kin_cell_ent.insert(0, 'eg. 0725684526')
kin_cell_ent.configure(state=DISABLED)
kin_cell_ent.bind('<Button-1>', kcell_text)
kin_cell_ent.place(x=330, y=400)


def register():
    if id_ent.get() == "" or name_ent.get() == "" or surname_ent.get() == "" or username_ent.get() == "" or password_ent.get() == "" or cell_ent.get() == "" or next_kin_ent.get() == "" or kin_cell_ent.get() == "":
        messagebox.showerror("No Entries", "Please fill all fields")
    else:
        messagebox.showinfo("Register", "You have been Registered")
        my_db = mysql.connector.connect(user="abdul-malik", password="@8-2fermENt2020", host="127.0.0.1", database="LC_Online", auth_plugin="mysql_native_password")
        my_cursor = my_db.cursor()
        insert = "INSERT INTO Register (ID, Name, Surname, UserName, Role, Password, Cell, Next_Of_Kin, NextOfKin_Cell) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        entries = (id_ent.get(), name_ent.get(), surname_ent.get(), username_ent.get(), role_ent.get(), password_ent.get(), cell_ent.get(), next_kin_ent.get(), kin_cell_ent.get())
        my_cursor.execute(insert, entries)
        my_db.commit()


reg_btn = Button(root, text="Register", command=register, bg="#89db33", width=21)
reg_btn.place(x=330, y=441)


def login():
    root.destroy()
    import main


log_btn = Button(root, text="Sign In", command=login, bg="#89db33", width=48)
log_btn.place(x=112, y=500)

root.mainloop()
