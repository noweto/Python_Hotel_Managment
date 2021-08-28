import sqlite3
from tkinter import *
from tkinter import messagebox
import random

import main


class CheckIn:

    # -add Data
    def submit_info(self):

        sub1 = FALSE
        sub2 = FALSE

        # - Validation
        name = self.name_entry.get()
        address = self.address_entry.get()
        room_num = self.room_number_var

        var1 = str(self.mobile_entry.get())

        if var1.isdigit() == True and len(var1) != 0 and len(var1) == 11:
            mobile = var1
            sub1 = TRUE

        else:
            messagebox.showerror("ERROR", "PLEASE ENTER 10 DIGIT MOBILE NUMBER")

        var2 = str(self.days_entry.get())
        if var2.isdigit():
            days = var2
            sub2 = TRUE

        else:
            messagebox.showerror("ERROR", "NUMBER OF DAYS CANNOT BE VARIABLE")

        """ Primary key -auto increment """
        # -Add to DB
        if sub1 == TRUE and sub2 == True:
            # -Connect Db File
            conn = sqlite3.connect('Hotel.db')
            cursor = conn.cursor()
            # -Create Db table
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Hotel (Fullname TEXT,Address TEXT,mobile_number NUMBER,number_days '
                'NUMBER,room_number NUMBER)'
            )

            # -Insert record into Db
            cursor.execute('INSERT INTO Hotel (FullName,Address,mobile_number,number_days,room_number) '
                           'VALUES(?,?,?,?,?)', (name, address, mobile, days, room_num))
            conn.commit()


            messagebox.showinfo("Signed in", "User stored successfully")

        self.name_var.set('')
        self.address_var.set('')
        self.days_var.set('')
        self.mobile_var.set('')

    def __init__(self,root):

        self.root = root
        self.root.title("CHECK IN")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - 3, self.root.winfo_screenheight() - 3))

        self.top = Frame(self.root)
        self.top.pack(side="top")

        self.bottom = Frame(self.root)
        self.bottom.pack(side="top")

        self.checkbox = Frame(self.root)
        self.checkbox.pack(side="top")


        # -message
        self.label = Label(self.top, font=('arial', 50, 'bold'), text="CHECK IN", fg="#FF6666", anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=50)

        # name label
        self.name_label = Label(self.bottom, font=('arial', 20, 'bold'), text="Enter Your Name :", fg="#000",
                                anchor="w")
        self.name_label.grid(row=0, column=2, padx=10, pady=10)

        self.name_var = StringVar()

        # text enter field
        self.name_entry = Entry(self.bottom, width=50, textvar=self.name_var)
        self.name_entry.grid(row=0, column=3, padx=10, pady=10)

        # address label
        self.address_label = Label(self.bottom, font=('arial', 20, 'bold'), text="Enter Your Address :", fg="#000",
                                   anchor="w")
        self.address_label.grid(row=1, column=2, padx=10, pady=10)

        # -Enter address
        self.address_var = StringVar()

        self.address_entry = Entry(self.bottom, width=50, textvar=self.address_var)
        self.address_entry.grid(row=1, column=3, padx=10, pady=10)

        # mobile label

        self.mobile_label = Label(self.bottom, font=('arial', 20, 'bold'), text="Enter Your Mobile Number :",
                                  fg="#000",
                                  anchor="w")
        self.mobile_label.grid(row=2, column=2, padx=10, pady=10)

        # text enter field
        self.mobile_var = IntVar()

        self.mobile_entry = Entry(self.bottom, width=50, text=self.mobile_var)
        self.mobile_entry.grid(row=2, column=3, padx=10, pady=10)

        # number of days label
        self.days_label = Label(self.bottom, font=('arial', 20, 'bold'), text="Enter Number Of Days To Stay :",
                                fg="#000",
                                anchor="w")
        self.days_label.grid(row=3, column=2, padx=10, pady=10)

        # text enter field
        self.days_var = IntVar()
        self.days_entry = Entry(self.bottom, width=50, text=self.days_var)
        self.days_entry.grid(row=3, column=3, padx=10, pady=10)

        # room number label
        self.room_number_label = Label(self.bottom, font=('arial', 20, 'bold'), text="Room Number: ",
                                       fg="#000",
                                       anchor="w")
        self.room_number_label.grid(row=4, column=2, padx=10, pady=10)


        # -Empty Room List .. (Sample List)
        room_list = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110 ,111 ,112 ,113 ,114 ,115 ,116,117,118,119,120]

        chosen_value = random.choice(room_list)
        self.room_number_var = chosen_value
        room_list.remove(chosen_value)

        self.room_entry = Entry(self.bottom, width=50)

        # -Set Random value to Entry text
        self.room_entry.insert(INSERT, self.room_number_var)

        self.room_entry.grid(row=4, column=3, padx=10, pady=10)

        # -submit button
        self.submit_button = Button(self.checkbox, text="Submit", font=('', 15), bg="#FFF", relief=RIDGE,
                                    height=2,
                                    width=15,
                                    fg="black", anchor="center", command=self.submit_info)
        self.submit_button.grid(row=5, column=1, padx=10, pady=50)

def checkInUi():
    root=Tk()
    home = CheckIn(root)
    root.mainloop()