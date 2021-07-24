#!/usr/bin/env python3
from tkinter import Tk, Button, PhotoImage, Label, LabelFrame, W, E, N, S, Entry, END, StringVar, Scrollbar, Toplevel
from tkinter import ttk
import sqlite3


class Contacts:
    db_filename = "contacts.db"

    def __init__(self, root):
        self.root = root
        self.create_gui()
        ttk.style = ttk.Style()
        ttk.style.configure("Treeview", font=("helvetica", 10))
        ttk.style.configure("Treeview.Heading", font=("helvetica", 12, "bold"))

    def execute_db_query(self, query, parameters=()):
        with sqlite3.connect(self.db_filename) as conn:
            print(conn)
            print("You have successfully connected to the database.")
            cursor = conn.curor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result

    def create_gui(self):
        self.create_left_icon()
        self.create_label_frame()
        self.create_message_area()
        self.create_tree_view()
        self.create_scrollbar()
        self.create_bottom_buttons()

    def Oiva(self):
        """
        Fun, hidden function
        named after my beloved cat
        """
        print("Meowwwww!")

    def create_left_icon(self):
        """
        adding logo to top left
        """
        photo = PhotoImage(file='contactslogo.gif')
        label = Label(image=photo)
        label.image = photo
        label.grid(row=0, column=0)

    def create_label_frame(self):
        labelframe = LabelFrame(
            self.root, text="Create New Contact", bg="sky blue", font="helvetica 10")
        labelframe.grid(row=0, column=1, padx=8, pady=8, sticky="ew")
        Label(labelframe, text="Name:").grid(
            row=1, column=1, sticky=W, padx=34, pady=2)
        self.namefield = Entry(labelframe)
        self.namefield.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        Label(labelframe, text="Email:").grid(
            row=2, column=1, sticky=W, padx=36, pady=2)
        self.emailfield = Entry(labelframe)
        self.emailfield.grid(row=2, column=2, sticky=W, padx=5, pady=2)
        Label(labelframe, text="Number:", padx=5, pady=2).grid(
            row=3, column=1, sticky=W, pady=2, padx=14)
        self.numfield = Entry(labelframe)
        self.numfield.grid(row=3, column=2, sticky=W, padx=5, pady=2)
        Button(labelframe, text="Add Contact", command="", bg="blue",
               fg="white").grid(row=4, column=2, sticky=E, padx=5, pady=5)

    def create_message_area(self):
        self.message = Label(text="", fg="red")
        self.message.grid(row=3, column=1, sticky=W)

    def create_tree_view(self):
        self.tree = ttk.Treeview(height=10, columns=("Email", "Number"))
        self.tree.grid(row=6, column=0, columnspan=2)
        self.tree.heading("#0", text="Name", anchor=W)
        self.tree.heading("Email", text="Email Address", anchor=W)
        self.tree.heading("Number", text="Contact Number", anchor=W)

    def create_scrollbar(self):
        self.scrollbar = Scrollbar(orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=6, column=3, rowspan=10, sticky="sn")

    def create_bottom_buttons(self):
        Button(text="Delete Selected", command="").grid(
            row=8, column=0, sticky=W, padx=20, pady=10)
        Button(text="Modify Selected", command="").grid(
            row=8, column=1, sticky=W)


if __name__ == '__main__':
    root = Tk()
    root.title("My Contacts")
    application = Contacts(root)
    root.mainloop()
