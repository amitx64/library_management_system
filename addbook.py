from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import main


# Class for Add New Book Page
class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('Add Book')
        # Size of Screen
        app_width = 450
        app_height = 340
        screen_width = (self.winfo_screenwidth() / 2) - (app_width / 2)
        screen_height = (self.winfo_screenheight() / 2) - (app_height / 2)
        x = int(screen_width)
        y = int(screen_height)
        self.geometry(f"{app_width}x{app_height}+{x}+{y}")
        # TOP Frame for LABEL
        frame_1 = LabelFrame(self, bd=1, height=80, borderwidth=2)
        frame_1.pack(side=TOP, fill="x", padx=1)
        # create a label in first frame_1
        label_1 = Label(frame_1, text='Add Book', bg="gray72", height=3, font=("Courier", 20, 'bold'))
        label_1.pack(side=TOP, fill="x")
        # screen resize enable/disable
        self.resizable(False, False)
        self.add_book_frame = LabelFrame(self, bd=3, height=100, borderwidth=2)
        self.add_book_frame.pack(fill="x", padx=5, pady=5)
        # Create Label , Entry Box and Save Button
        self.label_book_name = Label(self.add_book_frame, text='Enter Book Name : ')
        self.label_book_name.grid(row=0, column=0, padx=10)
        self.entry_book_name = Entry(self.add_book_frame, width=30, bd=3)
        self.entry_book_name.grid(row=0, column=1, padx=10, pady=10)
        self.label_author_name = Label(self.add_book_frame, text='Enter Book Author Name : ')
        self.label_author_name.grid(row=1, column=0, padx=10)
        self.entry_author_name = Entry(self.add_book_frame, width=30, bd=3)
        self.entry_author_name.grid(row=1, column=1, padx=10, pady=10)

        self.frame_2 = Frame(self)
        self.frame_2.pack(fill="x")

        self.label_category = Label(self.add_book_frame, text='Select Category : ')
        self.label_category.grid(row=2, column=0, padx=10)
        # Create Combobox for Choice
        self.book_category_select = StringVar()
        self.combo_book_category_select = ttk.Combobox(self.add_book_frame, font=("", 10),
                                                       textvariable=self.book_category_select)
        self.combo_book_category_select.grid(row=2, column=1, padx=10, pady=10, ipadx=12)
        # fill comboBox
        self.combo_book_category_select['values'] = ['Core subject', 'Programming', 'Others']
        self.label_book_id = Label(self.add_book_frame, text='Enter Book ID : ')
        self.label_book_id.grid(row=3, column=0, padx=10)
        self.entry_book_id = Entry(self.add_book_frame, width=30, bd=3)
        self.entry_book_id.grid(row=3, column=1, padx=10, pady=10)
        self.cancelBook_button = Button(self.frame_2, text='Cancel', font='bold', command=self.destroy)
        self.cancelBook_button.pack(side=LEFT, fill="x", padx=100, pady=10)
        self.saveBook_button = Button(self.frame_2, text='Save', font='bold', command=self.save_book)
        self.saveBook_button.pack(side=LEFT, fill="x", pady=10, ipadx=10)

    def save_book(self):
        bkName = self.entry_book_name.get()
        bkAuthor = self.entry_author_name.get()
        bkCategory = self.combo_book_category_select.get()
        bkID = self.entry_book_id.get()
        # print(bkName)
        # print(bkAuthor)
        # print(bkCategory)
        # print(bkID)
        if bkName and bkAuthor and bkCategory and bkID != "":
            try:
                query = "INSERT INTO 'books'(bname, aname, category, book_id)VALUES(?,?,?,?)"
                cur = main.db.conn.cursor()
                cur.execute(query, (bkName, bkAuthor, bkCategory, bkID))
                main.db.conn.commit()
                messagebox.showinfo("success", "Book has been add successfully", icon='info')
                AddBook.destroy(self)
            except:
                messagebox.showerror("Error", "Transaction not commit", icon='warning')
                AddBook.destroy(self)
        else:
            messagebox.showerror("Error", "All fields are mandatory", icon='warning')
            AddBook.destroy(self)
