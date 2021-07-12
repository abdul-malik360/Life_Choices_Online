import tkinter
from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()
root.geometry("650x650")
root.title("Admin Page")
root.config(bg="#0F0F0F")


lc_icon = PhotoImage(file="images/lc academy.png")
canvas = Canvas(root, width=150, height=60, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=lc_icon)
canvas.place(x=10, y=10)
font_style = ("Sans Serif", 25, "bold", "italic")
Label(root, text="Admin Account", bg="#0F0F0F", foreground="#FFFFFF", font=font_style).place(x=180, y=50)


def table_reg():
    my_db = mysql.connector.connect(user="abdul-malik", password="@8-2fermENt2020", host="127.0.0.1", database="LC_Online", auth_plugin="mysql_native_password")
    my_cursor = my_db.cursor()
    my_cursor.execute("select * from Register")

    table = ttk.Treeview(root)
    table["show"] = "headings"

    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure(".", font=("sans serif", 11))
    style.configure("Treeview.Heading", foreground="#89db33", bg="#0F0F0F", font=("sans serif", 11, "bold"))
    table["columns"] = ("ID", "Name", "Surname", "UserName", "Role", "Password", "Cell", "Next_Of_Kin", "NextOfKin_Cell")

    table.column("ID", width=150, minwidth=150, anchor=tkinter.CENTER)
    table.column("Name", width=150, minwidth=150, anchor=tkinter.CENTER)
    table.column("Surname", width=150, minwidth=150, anchor=tkinter.CENTER)
    table.column("UserName", width=100, minwidth=100, anchor=tkinter.CENTER)
    table.column("Role", width=100, minwidth=100, anchor=tkinter.CENTER)
    table.column("Password", width=150, minwidth=150, anchor=tkinter.CENTER)
    table.column("Cell", width=120, minwidth=120, anchor=tkinter.CENTER)
    table.column("Next_Of_Kin", width=150, minwidth=150, anchor=tkinter.CENTER)
    table.column("NextOfKin_Cell", width=150, minwidth=150, anchor=tkinter.CENTER)

    table.heading("ID", text="ID Number", anchor=tkinter.CENTER)
    table.heading("Name", text="Name", anchor=tkinter.CENTER)
    table.heading("Surname", text="Surname", anchor=tkinter.CENTER)
    table.heading("UserName", text="Username", anchor=tkinter.CENTER)
    table.heading("Role", text="Role", anchor=tkinter.CENTER)
    table.heading("Password", text="Password", anchor=tkinter.CENTER)
    table.heading("Cell", text="Cell Number", anchor=tkinter.CENTER)
    table.heading("Next_Of_Kin", text="Next of Kin", anchor=tkinter.CENTER)
    table.heading("NextOfKin_Cell", text="Next of Kin Cell", anchor=tkinter.CENTER)

    i = 0
    for row in my_cursor:
        table.insert("", i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        i = i + 1

    scrollh = ttk.Scrollbar(root, orient="horizontal")
    scrollh.configure(command=table.xview)
    table.configure(xscrollcommand=scrollh.set)
    scrollh.pack(fill=X, side=BOTTOM)

    scrollv = ttk.Scrollbar(root, orient="vertical")
    scrollv.configure(command=table.yview)
    table.configure(yscrollcommand=scrollv.set)
    scrollv.pack(fill=Y, side=RIGHT)

    table.pack(side=BOTTOM)


rt_btn = Button(root, text="Registered Users", width=14, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33", command=table_reg)
rt_btn.place(x=10, y=250)

add_btn = Button(root, text="Add User", command=None, width=14, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
add_btn.place(x=10, y=150)
remove_btn = Button(root, text="remove User", command=None, width=14, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
remove_btn.place(x=10, y=200)
edit_btn = Button(root, text="edit User", command=None, width=14, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
edit_btn.place(x=10, y=100)
log_btn = Button(root, text="Logged Users", command=None, width=14, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
log_btn.place(x=10, y=300)
q_btn = Button(root, text="Quit", command=None, width=14, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
q_btn.place(x=10, y=350)

root.mainloop()
