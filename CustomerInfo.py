import sqlite3
from tkinter import *
import main



class CustomerInfo:

    # -Get all users data
    def display_info(self):

        conn = sqlite3.connect('Hotel.db')
        cursor = conn.cursor()

        # -Get Guests name from table
        cursor.execute("SELECT Fullname FROM Hotel")
        ans = cursor.fetchall()
        for i in ans:
            self.name_customer_entry.insert(INSERT, i[0] + '\n')

        # -Get Guests Room number from table
        cursor.execute("SELECT room_number FROM Hotel")
        ans = cursor.fetchall()
        for i in ans:
            self.room_no_customer_entry.insert(INSERT, str(i[0]) + '\n')
        # create display button

    def __init__(self,root):

        self.root = root
        self.root.title("CUSTOMER INFO")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - 3, self.root.winfo_screenheight() - 3))

        # Mainframes
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        left = Frame(self.root, relief="solid")
        left.pack(side="left")

        right = Frame(self.root, relief="solid")
        right.pack(side="left")

        # -Message
        self.label = Label(top, font=('arial', 50, 'bold'), text="List Of Customer", fg="#FF6666", anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)
        self.name_label = Label(left, font=('arial', 20, 'bold'), text="Name", fg="#000", anchor="center")
        self.name_label.grid(row=0, column=1, padx=10, pady=10)

        self.name_customer_entry = Text(left, height=30, width=70)
        self.name_customer_entry.grid(row=1, column=1, padx=100, pady=10)

        self.room_no_label = Label(right, font=('arial', 20, 'bold'), text="Room No", fg="#000", anchor="center")
        self.room_no_label.grid(row=0, column=1, padx=10, pady=10)

        self.room_no_customer_entry = Text(right, height=30, width=70)
        self.room_no_customer_entry.grid(row=1, column=1, padx=100, pady=10)
        self.display_info()


def customerInfoUi():
    root = Tk()
    home =CustomerInfo(root)
    root.mainloop()
