from tkinter import *
from tkinter import messagebox
import main


# Class for Add New Book Page
class IssueBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('Issue Book')
        # Size of Screen
        app_width = 450
        app_height = 260
        screen_width = (self.winfo_screenwidth() / 2) - (app_width / 2)
        screen_height = (self.winfo_screenheight() / 2) - (app_height / 2)
        x = int(screen_width)
        y = int(screen_height)
        self.geometry(f"{app_width}x{app_height}+{x}+{y}")
        # TOP Frame for LABEL
        frame_1 = LabelFrame(self, bd=1, height=80, borderwidth=2)
        frame_1.pack(side=TOP, fill="x", padx=1)
        # create a label in first frame_1
        label_1 = Label(frame_1, text='Issue Book', bg="gray72", height=3, font=("Courier", 20, 'bold'))
        label_1.pack(side=TOP, fill="x")
        # screen resize enable/disable
        self.resizable(False, False)
        self.issue_book_frame = LabelFrame(self, bd=3, height=100, borderwidth=2)
        self.issue_book_frame.pack(fill="x", padx=5, pady=5)
        # Create Label , Entry Box and Save Button
        self.label_book_ID = Label(self.issue_book_frame, text='Enter Book ID : ')
        self.label_book_ID.grid(row=0, column=0, padx=10)
        self.entry_book_ID = Entry(self.issue_book_frame, width=30, bd=3)
        self.entry_book_ID.grid(row=0, column=1, padx=10, pady=10)
        self.label_student_ID = Label(self.issue_book_frame, text='Enter Student ID : ')
        self.label_student_ID.grid(row=1, column=0, padx=10)
        self.entry_student_ID = Entry(self.issue_book_frame, width=30, bd=3)
        self.entry_student_ID.grid(row=1, column=1, padx=10, pady=10)

        self.frame_2 = Frame(self)
        self.frame_2.pack(fill="x")
        self.cancel_button = Button(self.frame_2, text='Cancel', font='bold', command=self.destroy)
        self.cancel_button.pack(side=LEFT, fill="x", padx=100, pady=10)
        self.ret_button = Button(self.frame_2, text='issue', font='bold', command=self.issue_book)
        self.ret_button.pack(side=LEFT, fill="x", pady=10)

    def issue_book(self):
        bkID = self.entry_book_ID.get()
        stID = self.entry_student_ID.get()
        print(bkID)
        print(stID)
        check_issued = None
        check_books = None
        cur = main.db.conn.cursor()
        try:
            check_issued = cur.execute("SELECT count(*) FROM issued WHERE book_id=?", (bkID,)).fetchall()
            check_books = cur.execute("SELECT count(*) FROM books WHERE book_id=?", (bkID,)).fetchall()
        except Exception as e:
            print(e)
        finally:
            if check_issued and check_books != None:
                if bkID and stID != "" and check_issued[0][0] == 0 and check_books[0][0] != 0:
                    query = "INSERT INTO issued(book_id,student_id)VALUES(?,?)"
                    cur.execute(query, (bkID, stID))
                    main.db.conn.commit()
                    messagebox.showinfo("Success", 'Book has been issued successfully', icon='info')
                elif bkID and stID != "" and check_issued[0][0] and check_books[0][0] != 0:
                    messagebox.showerror("Error", 'Book has already been issued', icon='warning')
                elif bkID and stID != "" and check_issued[0][0] == 0 and check_books[0][0] == 0:
                    messagebox.showerror("Error", 'Entered book id not present', icon='warning')
                else:
                    messagebox.showerror("Error", "All fields are mandatory", icon='warning')
            else:
                print('Check_issued : None , Check_books : None')