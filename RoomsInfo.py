import sqlite3
from tkinter import *
import main





class GetInfo:

    # -Get info

    def get_info(self):
        room_number = int(self.room_no_entry.get())
        conn = sqlite3.connect('Hotel.db')
        cursor = conn.cursor()

        cursor.execute("SELECT room_number FROM Hotel")
        returned_data = cursor.fetchall()
        room = []
        for i in returned_data:
            room.append(i[0])
        if room_number in room:
            cursor.execute("SELECT * FROM Hotel")
            data = cursor.fetchall()
            for i in data:
                if room_number == int(i[4]):
                    self.get_info_entry.insert(INSERT,
                                               'NAME: ' + str(i[0]) + '\nADDRESS: ' + str(
                                                   i[1]) + '\nMOBILE NUMBER:  ' + str(
                                                   i[2]) + '\nNUMBER OF DAYS: ' + str(
                                                   i[3]) + '\nROOM NUMBER: ' + str(i[4]) + '\n')
        else:
            self.get_info_entry.insert(INSERT, "\nPLEASE ENTER VALID ROOM NUMBER")


    # -Constructor
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("GET INFO")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # create mainframe to Control Design
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        info_frame = Frame(self.root, width=454, height=20)
        info_frame.pack(side="top")

        button_frame = Frame(self.root)
        button_frame.pack(side="top")

        # Welcome Message
        self.label = Label(top, font=('arial', 50, 'bold'), text="Information Of Customers", fg="#FF6666",
                           anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)

        # -Room number label
        self.room_no_label = Label(bottom, font=('arial', 20, 'bold'), text="Enter The Room Number :", fg="#FF6666",
                                   anchor="center")
        self.room_no_label.grid(row=2, column=2, padx=10, pady=30)

        # -Enter number
        self.room_number = IntVar()
        self.room_no_entry = Entry(bottom, width=5, text=self.room_number)
        self.room_no_entry.grid(row=2, column=3, padx=10, pady=10)

        # -Enter to show data
        self.get_info_entry = Text(info_frame, height=15, width=90)
        self.get_info_entry.grid(row=1, column=1, padx=10, pady=10)

        # -Submit button
        self.submit_button = Button(button_frame, text="Submit", font=('', 15), bg="#FFF", relief=RIDGE, height=2,
                                    width=15, fg="#000", anchor="center", command=self.get_info)

        self.submit_button.grid(row=8, column=2, padx=10, pady=20)





def roomInfoUi():
    root = Tk()
    application = GetInfo(root)
    root.mainloop()