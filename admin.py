import tkinter
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

root = Tk()
root.geometry("650x650")
root.title("Admin Page")
root.config(bg="#0F0F0F")

clicked = True
un_clicked = False

lc_icon = PhotoImage(file="images/lc academy.png")
canvas = Canvas(root, width=150, height=60, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=lc_icon)
canvas.place(x=10, y=10)
font_style = ("Sans Serif", 25, "bold", "italic")
Label(root, text="Admin Account", bg="#0F0F0F", foreground="#FFFFFF", font=font_style).place(x=180, y=50)

table = ttk.Treeview(root)
my_db = mysql.connector.connect(user="abdul-malik", password="@8-2fermENt2020", host="127.0.0.1", database="LCA_Online", auth_plugin="mysql_native_password")
my_cursor = my_db.cursor()


def table_reg():
    add_btn.config(state=DISABLED)
    log_btn.config(state=DISABLED)
    rt_btn.config(state=DISABLED)
    admin_btn.config(state=DISABLED)
    search_btn.config(state=DISABLED)
    my_cursor.execute("select * from Register")

    table = ttk.Treeview(root)
    table["show"] = "headings"

    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure(".", font=("sans serif", 11))
    style.configure("Treeview.Heading", foreground="#89db33", bg="#0F0F0F", font=("sans serif", 11, "bold"))
    table["columns"] = ("ID", "Name", "Surname", "UserName", "Role", "Password", "Cell", "Next_Of_Kin", "NextOfKin_Cell")

    table.tag_configure("odd", background="#89db33")
    table.tag_configure("even", background="#0F0F0F", foreground="white")

    count = 0
    for i in my_cursor:
        if count % 2 == 0:
            table.insert("", 'end', iid= count, values = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]), tags=("even",))
        else:
            table.insert("", 'end', iid= count, values = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]), tags=("odd",))
        count += 1

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

    def close():
        log_btn.config(state=NORMAL)
        add_btn.config(state=NORMAL)
        rt_btn.config(state=NORMAL)
        admin_btn.config(state=NORMAL)
        search_btn.config(state=NORMAL)
        remove_btn.config(state=DISABLED)
        scrollv.destroy()
        scrollh.destroy()
        table.destroy()
        edit_btn.destroy()
        remove_btn.destroy()
        close_btn.destroy()

    def remove():
        try:
            selected = table.selection()[0]
            print(table.item(selected)['values'])
            uid = table.item(selected)['values'][0]
            delete = 'DELETE FROM Register where ID=%s'
            sel_data = (uid,)
            my_cursor.execute(delete, sel_data)
            my_db.commit()
            table.delete(selected)
            messagebox.showinfo("User removed", "Successfully removed a User")
        except IndexError:
            messagebox.showerror("Nothing Selected", "Please Select a User")

    edit_btn = Button(root, text="Edit User", command=None, width=14, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
    edit_btn.place(x=305, y=370)
    remove_btn = Button(root, text="Remove User", command=remove, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
    remove_btn.place(x=450, y=370)
    close_btn = Button(root, text="Close", command=close, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
    close_btn.place(x=570, y=370)


rt_btn = Button(root, text="Registered Users", width=14, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33", command=table_reg)
rt_btn.place(x=10, y=100)


def search():
    add_btn.config(state=DISABLED)
    log_btn.config(state=DISABLED)
    rt_btn.config(state=DISABLED)
    admin_btn.config(state=DISABLED)
    search_btn.config(state=DISABLED)
    search_frame = LabelFrame(root, width=450, height=280, bg="#89db33")
    search_frame.place(x=160, y=100)

    name_ent = Entry(search_frame, width=24)
    name_ent.place(x=10, y=10)
    # surname_ent = Entry(search_frame, width=24)
    # surname_ent.place(x=10, y=30)
    id_numb = StringVar()
    name = StringVar()
    surname = StringVar()
    username = StringVar()
    password = StringVar()
    role = StringVar()
    cell = StringVar()
    kin = StringVar()
    kincell = StringVar()

    def find():
        Label(search_frame, textvariable=id_numb, bg="#0F0F0F", foreground="#89db33").place(x=10, y=50)
        Label(search_frame, textvariable=name, bg="#0F0F0F", foreground="#89db33").place(x=10, y=100)
        Label(search_frame, textvariable=surname, bg="#0F0F0F", foreground="#89db33").place(x=10, y=150)
        Label(search_frame, textvariable=username, bg="#0F0F0F", foreground="#89db33").place(x=10, y=200)
        Label(search_frame, textvariable=password, bg="#0F0F0F", foreground="#89db33").place(x=200, y=50)
        Label(search_frame, textvariable=role, bg="#0F0F0F", foreground="#89db33").place(x=10, y=250)
        Label(search_frame, textvariable=cell, bg="#0F0F0F", foreground="#89db33").place(x=200, y=100)
        Label(search_frame, textvariable=kin, bg="#0F0F0F", foreground="#89db33").place(x=200, y=150)
        Label(search_frame, textvariable=kincell, bg="#0F0F0F", foreground="#89db33").place(x=200, y=200)

        my_cursor.execute("select * from Register where Name=%s", name_ent.get())

        row = my_cursor.fetchall()

        id_numb.set(row[0])
        name.set(row[1])
        surname.set(row[2])
        username.set(3)
        role.set(row[4])
        password.set(row[5])
        cell.set(row[6])
        kin.set(row[7])
        kincell.set(row[8])

        my_db.commit()
    find_btn = Button(search_frame, text="Search", command=find, foreground="#89db33", bg="#0F0F0F", width=7)
    find_btn.place(x=355, y=10)

    def close():
        log_btn.config(state=NORMAL)
        add_btn.config(state=NORMAL)
        rt_btn.config(state=NORMAL)
        admin_btn.config(state=NORMAL)
        search_btn.config(state=NORMAL)
        search_frame.destroy()

    close_btn = Button(search_frame, text="Quit", command=close, foreground="#89db33", bg="#0F0F0F", width=7)
    close_btn.place(x=355, y=240)


search_btn = Button(root, text="Search User", command=search, width=14, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
search_btn.place(x=10, y=200)


def add():
    add_btn.config(state=DISABLED)
    log_btn.config(state=DISABLED)
    rt_btn.config(state=DISABLED)
    admin_btn.config(state=DISABLED)
    search_btn.config(state=DISABLED)
    add_frame = LabelFrame(root, width=450, height=280, bg="#89db33")
    add_frame.place(x=160, y=100)
    Label(add_frame, text="ID Number", bg="#89db33", foreground="#0F0F0F").place(x=10, y=10)
    Label(add_frame, text="Name", bg="#89db33", foreground="#0F0F0F").place(x=10, y=60)
    Label(add_frame, text="Surname", bg="#89db33", foreground="#0F0F0F").place(x=10, y=110)
    Label(add_frame, text="Username", bg="#89db33", foreground="#0F0F0F").place(x=10, y=160)
    Label(add_frame, text="Role", bg="#89db33", foreground="#0F0F0F").place(x=230, y=10)
    Label(add_frame, text="Password", bg="#89db33", foreground="#0F0F0F").place(x=10, y=210)
    Label(add_frame, text="Cell Number", bg="#89db33", foreground="#0F0F0F").place(x=230, y=60)
    Label(add_frame, text="Next of kin", bg="#89db33", foreground="#0F0F0F").place(x=230, y=110)
    Label(add_frame, text="Next of Kin Cell Number", bg="#89db33", foreground="#0F0F0F").place(x=230, y=160)

    id_ent = Entry(add_frame, width=24)
    id_ent.place(x=10, y=30)
    name_ent = Entry(add_frame, width=24)
    name_ent.place(x=10, y=80)
    surname_ent = Entry(add_frame, width=24)
    surname_ent.place(x=10, y=130)
    username_ent = Entry(add_frame, width=24)
    username_ent.place(x=10, y=180)
    password_ent = Entry(add_frame, width=24)
    password_ent.place(x=10, y=230)
    role_ent = Entry(add_frame, width=24)
    role_ent.place(x=230, y=30)
    cell_ent = Entry(add_frame, width=24)
    cell_ent.place(x=230, y=80)
    next_kin_ent = Entry(add_frame, width=24)
    next_kin_ent.place(x=230, y=130)
    kin_cell_ent = Entry(add_frame, width=24)
    kin_cell_ent.place(x=230, y=180)

    def register():
        if id_ent.get() == "" or name_ent.get() == "" or surname_ent.get() == "" or username_ent.get() == "" or password_ent.get() == "" or cell_ent.get() == "" or next_kin_ent.get() == "" or kin_cell_ent.get() == "":
            messagebox.showerror("No Entries", "Please fill all fields")
        else:
            messagebox.showinfo("Register Successful", "You have registered a new user")

            insert = "INSERT INTO Register (ID, Name, Surname, UserName, Role, Password, Cell, Next_Of_Kin, NextOfKin_Cell) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            entries = (id_ent.get(), name_ent.get(), surname_ent.get(), username_ent.get(), role_ent.get(), password_ent.get(), cell_ent.get(), next_kin_ent.get(), kin_cell_ent.get())
            my_cursor.execute(insert, entries)
            my_db.commit()
            add_frame.destroy()

    reg_btn = Button(add_frame, text="Register", command=register, foreground="#89db33", bg="#0F0F0F", width=10)
    reg_btn.place(x=230, y=220)

    def close():
        log_btn.config(state=NORMAL)
        add_btn.config(state=NORMAL)
        rt_btn.config(state=NORMAL)
        admin_btn.config(state=NORMAL)
        search_btn.config(state=NORMAL)
        add_frame.destroy()

    close_btn = Button(add_frame, text="Quit", command=close, foreground="#89db33", bg="#0F0F0F", width=7)
    close_btn.place(x=345, y=220)


add_btn = Button(root, text="Add User", command=add, width=14, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
add_btn.place(x=10, y=250)


def table_log():
    log_btn.config(state=DISABLED)
    add_btn.config(state=DISABLED)
    rt_btn.config(state=DISABLED)
    admin_btn.config(state=DISABLED)
    search_btn.config(state=DISABLED)
    my_cursor.execute("select * from Log")

    table2 = ttk.Treeview(root)
    table2["show"] = "headings"

    style2 = ttk.Style(root)
    style2.theme_use("clam")

    style2.configure(".", font=("sans serif", 11))
    style2.configure("Treeview.Heading", foreground="#89db33", bg="#0F0F0F", font=("sans serif", 11, "bold"))
    table2["columns"] = ("LogNumber", "UserName", "Password", "Date", "TimeIn", "TimeOut")

    table2.tag_configure("odd", background="#89db33")
    table2.tag_configure("even", background="#0F0F0F", foreground="white")

    count = 0
    for i in my_cursor:
        if count % 2 == 0:
            table2.insert("", 'end', iid= count, values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=("even",))
        else:
            table2.insert("", 'end', iid= count, values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=("odd",))
        count += 1

    table2.column("LogNumber", width=150, minwidth=150, anchor=tkinter.CENTER)
    table2.column("UserName", width=150, minwidth=150, anchor=tkinter.CENTER)
    table2.column("Password", width=150, minwidth=150, anchor=tkinter.CENTER)
    table2.column("Date", width=130, minwidth=130, anchor=tkinter.CENTER)
    table2.column("TimeIn", width=100, minwidth=100, anchor=tkinter.CENTER)
    table2.column("TimeOut", width=100, minwidth=100, anchor=tkinter.CENTER)

    table2.heading("LogNumber", text="Log Number", anchor=tkinter.CENTER)
    table2.heading("UserName", text="Username", anchor=tkinter.CENTER)
    table2.heading("Password", text="Password", anchor=tkinter.CENTER)
    table2.heading("Date", text="Date", anchor=tkinter.CENTER)
    table2.heading("TimeIn", text="Time In", anchor=tkinter.CENTER)
    table2.heading("TimeOut", text="Time Out", anchor=tkinter.CENTER)

    z = 0
    for row2 in my_cursor:
        table2.insert("", z, text="", values=(row2[0], row2[1], row2[2], row2[3], row2[4], row2[5]))
        z = z + 1

    scrolls = ttk.Scrollbar(root, orient="horizontal")
    scrolls.configure(command=table2.xview)
    table2.configure(xscrollcommand=scrolls.set)
    scrolls.pack(fill=X, side=BOTTOM)

    scrollu = ttk.Scrollbar(root, orient="vertical")
    scrollu.configure(command=table2.yview)
    table2.configure(yscrollcommand=scrollu.set)
    scrollu.pack(fill=Y, side=RIGHT)

    table2.pack(side=BOTTOM)

    # display signed in
    log_frame = LabelFrame(root, width=400, height=230, bg="#89db33")
    log_frame.place(x=160, y=100)

    font = ("Sans Serif", 15, "bold")
    Label(log_frame, text="User's Signed In:", bg="#FFFFFF", width=15, foreground="#0F0F0F", font=font).place(x=100, y=20)
    Label(log_frame, text="User's Signed Out:", bg="#FFFFFF", width=15, foreground="#0F0F0F", font=font).place(x=100, y=140)

    people_in = StringVar()
    my_cursor.execute("select Count(TimeIn) from Log")

    count_in = Label(log_frame, textvariable=people_in, bg="#89db33", foreground="#0F0F0F", font=font)
    count_in.place(x=200, y=60)
    for i in my_cursor:
        people_in.set(i)

    # sign out
    people_out = StringVar()
    my_cursor.execute("select Count(TimeOut) from Log")

    count_out = Label(log_frame, textvariable=people_out, bg="#89db33", foreground="#0F0F0F", font=font)
    count_out.place(x=200, y=180)
    for o in my_cursor:
        people_out.set(o)
        if len(o) > 0:
            print("there are still users inside")

    def close():
        log_btn.config(state=NORMAL)
        add_btn.config(state=NORMAL)
        rt_btn.config(state=NORMAL)
        admin_btn.config(state=NORMAL)
        search_btn.config(state=NORMAL)
        scrollu.destroy()
        scrolls.destroy()
        table2.destroy()
        log_frame.destroy()
        close_btn.destroy()

    close_btn = Button(root, text="Close", command=close, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
    close_btn.place(x=570, y=370)


log_btn = Button(root, text="Logged Users", command=table_log, width=14, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
log_btn.place(x=10, y=150)


def new_admin():
    log_btn.config(state=DISABLED)
    add_btn.config(state=DISABLED)
    rt_btn.config(state=DISABLED)
    admin_btn.config(state=DISABLED)
    search_btn.config(state=DISABLED)
    admin_frame = LabelFrame(root, width=450, height=280, bg="#89db33")
    admin_frame.place(x=160, y=100)

    Label(admin_frame, text="Username", bg="#89db33", foreground="#0F0F0F").place(x=130, y=60)
    Label(admin_frame, text="Password", bg="#89db33", foreground="#0F0F0F").place(x=130, y=110)

    username_ent = Entry(admin_frame, width=24)
    username_ent.place(x=130, y=80)
    password_ent = Entry(admin_frame, width=24)
    password_ent.place(x=130, y=130)

    def reg_admin():
        if username_ent.get() == "" or password_ent.get() == "":
            messagebox.showerror("No Entries", "Please fill all fields")
        else:
            my_db = mysql.connector.connect(user="abdul-malik", password="@8-2fermENt2020", host="127.0.0.1", database="LCA_Online", auth_plugin="mysql_native_password")
            my_cursor = my_db.cursor()
            insert = "INSERT INTO Admin (Name, Password) VALUES (%s, %s)"
            entries = (username_ent.get(), password_ent.get())
            my_cursor.execute(insert, entries)
            my_db.commit()
            messagebox.showinfo("Register Successful", "You have registered a new Admin")
            admin_frame.destroy()

    reg_btn = Button(admin_frame, text="Register", command=reg_admin, foreground="#89db33", bg="#0F0F0F", width=10)
    reg_btn.place(x=220, y=170)

    def close():
        log_btn.config(state=NORMAL)
        add_btn.config(state=NORMAL)
        rt_btn.config(state=NORMAL)
        admin_btn.config(state=NORMAL)
        search_btn.config(state=NORMAL)
        admin_frame.destroy()

    close_btn = Button(admin_frame, text="Quit", command=close, foreground="#89db33", bg="#0F0F0F", width=7)
    close_btn.place(x=245, y=220)


admin_btn = Button(root, text="New Admin", command=new_admin, width=14, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
admin_btn.place(x=10, y=300)


def quite():
    root.destroy()
    import main


q_btn = Button(root, text="Quit", command=quite, width=14, foreground="#89db33", bg="#0F0F0F", highlightbackground="#89db33")
q_btn.place(x=10, y=350)

root.mainloop()


# Label(search_frame, text="ID Number", bg="#0F0F0F", foreground="#89db33").place(x=10, y=50)
# Label(search_frame, text="Name", bg="#0F0F0F", foreground="#89db33").place(x=10, y=100)
# Label(search_frame, text="Surname", bg="#0F0F0F", foreground="#89db33").place(x=10, y=150)
# Label(search_frame, text="Username", bg="#0F0F0F", foreground="#89db33").place(x=10, y=200)
# Label(search_frame, text="Role", bg="#0F0F0F", foreground="#89db33").place(x=200, y=50)
# Label(search_frame, text="Password", bg="#0F0F0F", foreground="#89db33").place(x=10, y=250)
# Label(search_frame, text="Cell Number", bg="#0F0F0F", foreground="#89db33").place(x=200, y=100)
# Label(search_frame, text="Next of kin", bg="#0F0F0F", foreground="#89db33").place(x=200, y=150)
# Label(search_frame, text="Next of Kin Cell Number", bg="#0F0F0F", foreground="#89db33").place(x=200, y=200)
