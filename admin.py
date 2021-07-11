import tkinter
from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()
root.geometry("650x650")
root.title("Admin Page")
root.config(bg="#89db33")

admin_frame = LabelFrame(root, width=550, height=300, padx=130, pady=40, bg="#0F0F0F")
admin_frame.place(x=50, y=80)

my_db = mysql.connector.connect(user="abdul-malik", password="@8-2fermENt2020", host="127.0.0.1", database="LC_Online", auth_plugin="mysql_native_password")
my_cursor = my_db.cursor()
my_cursor.execute("select * from Register")

table = ttk.Treeview(root)
table["show"] = "headings"

style = ttk.Style(root)
style.theme_use("clam")

style.configure(".", font=("sans serif", 11))
style.configure("Treeview.Heading", foreground="green", font=("sans serif", 11, "bold"))
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

scroll = ttk.Scrollbar(root, orient="horizontal")
scroll.configure(command=table.xview)
table.configure(xscrollcommand=scroll.set)
scroll.pack(fill=X, side=BOTTOM)

table.pack(side=BOTTOM)

root.mainloop()
