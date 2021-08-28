import sqlite3
from tkinter import *
import main

class CheckOut:

    # -Check out user method
    def check_out(self):
        room_number = int(self.room_no_entry.get())
        conn = sqlite3.connect('Hotel.db')
        cursor = conn.cursor()
        # -Select all rooms number column .. Select all column ..But first element is room_number
        cursor.execute("SELECT room_number FROM Hotel")
        returned_data = cursor.fetchall()
        room = []

        for i in returned_data:
            room.append(i[0])

        # -Check if number which inserted already exist in room list
        if room_number in room:
            cursor.execute("SELECT Fullname,room_number FROM Hotel")
            data = cursor.fetchall()
            for i in data:
                if room_number == int(i[1]):
                    self.get_info_entry.insert(INSERT,
                                               '\n' + str(i[0]) + ' have check out from ' + str(i[1]) + '\n')
                    cursor.execute("""DELETE FROM Hotel where room_number = ?""", [room_number])
                    conn.commit()
        else:
            self.get_info_entry.insert(INSERT, "Please Enter Valid Room Number")



    # -Constructor
    def __init__(self,root):
        self.root = root
        pad = 3
        self.root.title("Check Out")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # create mainframe to control design
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        info_frame = Frame(self.root)
        info_frame.pack(side="top")

        # -Welcome message
        self.label = Label(top, font=('arial', 50, 'bold'), text="Check Out", fg="#FF6666", anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=50)

        # -Room number label
        self.room_no_label = Label(bottom, font=('arial', 20, 'bold'), text="Enter The Room Number :", fg="#FF6666",
                                   anchor="center")
        self.room_no_label.grid(row=2, column=2, padx=10, pady=30)

        # -Enter room number
        self.room_var = IntVar()
        self.room_no_entry = Entry(bottom, width=10, text=self.room_var)
        self.room_no_entry.grid(row=2, column=3, padx=10, pady=30)

        # -Enter text to show data
        self.get_info_entry = Text(info_frame, height=15, width=90)
        self.get_info_entry.grid(row=1, column=1, padx=10, pady=10)

        # Display Info button
        self.check_out_button = Button(info_frame, text="Check Out", font=('', 15), bg="#FFF", relief=RIDGE, height=2,
                                       width=15,
                                       fg="#000", anchor="center",
                                       command=self.check_out)

        self.check_out_button.grid(row=2, column=1, padx=10, pady=20)



def checkOutUi():
    root = Tk()
    application =CheckOut(root)
    root.mainloop()


