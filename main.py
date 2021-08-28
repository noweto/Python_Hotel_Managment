import sqlite3
from tkinter import *
from tkinter.ttk import Style

import CheckIn
import CheckOut
import CustomerInfo
import RoomsInfo


class Hotel:

    # -Constructor
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - 3, self.root.winfo_screenheight() - 3))


        # -mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")
        # -frame to add buttons
        bottom = Frame(self.root)
        bottom.pack(side="top")



        # -Welcome message
        self.label = Label(top, font=('arial', 50, 'bold'), text="Welcome", fg="#FF6666", anchor="center")
        self.label.grid(row=0, column=3,padx=10,pady=50)

        # -Buttons

        # check in button -Feature 1
        self.check_in_button = Button(bottom,
                                      text="Check In",
                                      font=('', 20), bg="#FFF",
                                      relief=RIDGE, height=2,
                                      width=50,
                                      fg="black", anchor="center",
                                      command =CheckIn.checkInUi
                                      )


        self.check_in_button.grid(row=0, column=2, padx=10, pady=10)

        # check out button -Feature 2
        self.check_out_button = Button(bottom, text="Check Out",
                                       font=('', 20), bg="#FFF",
                                       relief=RIDGE, height=2,
                                       width=50, fg="black", anchor="center",
                                       command=CheckOut.checkOutUi
                                       )
        self.check_out_button.grid(row=1, column=2, padx=10, pady=10)

        # Room Info button -Feature 3
        self.room_info_button = Button(bottom, text="Information Of Rooms",
                                       font=('', 20), bg="#FFF",
                                       relief=RIDGE,height=2,
                                       width=50, fg="black", anchor="center",
                                       command=RoomsInfo.roomInfoUi
                                       )
        self.room_info_button.grid(row=2, column=2, padx=10, pady=10)


        # Get Customer Info -Feature 4
        self.get_info_button = Button(bottom, text="Information Of All Guests",
                                      font=('', 20), bg="#FFF",
                                      relief=RIDGE,height=2,
                                      width=50, fg="black", anchor="center",
                                      command = CustomerInfo.customerInfoUi
                                      )

        self.get_info_button.grid(row=3, column=2, padx=10, pady=10)


        self.exit_button = Button(bottom, text="EXIT",
                                  font=('', 20), bg="#FFF",
                                  relief=RIDGE, height=2, width=50,
                                  fg="black",
                                  anchor="center", command=quit) # -Exit the app
        # Exit Button

        self.exit_button.grid(row=4, column=2, padx=10, pady=10)


def homeUi():
    root = Tk()
    home = Hotel(root)
    # -Execute tkinter
    root.mainloop()

# -Delete all Db table
def deleteHotelDb():
    conn = sqlite3.connect('Hotel.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Hotel ")
    conn.commit()


if __name__ == '__main__':
    homeUi()




