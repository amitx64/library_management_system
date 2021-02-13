from tkinter import *
from tkinter import messagebox
import main


# Class for Add New Book Page
class ReturnBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('Return Book')
        # Size of Screen
        app_width = 450
        app_height = 210
        screen_width = (self.winfo_screenwidth() / 2) - (app_width / 2)
        screen_height = (self.winfo_screenheight() / 2) - (app_height / 2)
        x = int(screen_width)
        y = int(screen_height)
        self.geometry(f"{app_width}x{app_height}+{x}+{y}")
        # TOP Frame for LABEL
        frame_1 = LabelFrame(self, bd=1, height=80, borderwidth=2)
        frame_1.pack(side=TOP, fill="x", padx=1)
        # create a label in first frame_1
        label_1 = Label(frame_1, text='Return Book', bg="gray72", height=3, font=("Courier", 20, 'bold'))
        label_1.pack(side=TOP, fill="x")
        # screen resize enable/disable
        self.resizable(False, False)
        self.ret_book_frame = LabelFrame(self, bd=3, height=100, borderwidth=2)
        self.ret_book_frame.pack(fill="x", padx=5, pady=5)
        # Create Label , Entry Box and Save Button
        self.label_ret_book_ID = Label(self.ret_book_frame, text='Enter Book ID : ')
        self.label_ret_book_ID.grid(row=0, column=0, padx=10)
        self.entry_ret_book_ID = Entry(self.ret_book_frame, width=30, bd=3)
        self.entry_ret_book_ID.grid(row=0, column=1, padx=10, pady=10)

        self.frame_2 = Frame(self)
        self.frame_2.pack(fill="x")
        self.cancel_button = Button(self.frame_2, text='Cancel', font='bold', command=self.destroy)
        self.cancel_button.pack(side=LEFT, fill="x", padx=100, pady=10)
        self.ret_button = Button(self.frame_2, text='return', font='bold', command=self.ret_book)
        self.ret_button.pack(side=LEFT, fill="x", pady=10)

    def ret_book(self):
        cur = main.db.conn.cursor()
        ret_query = None
        ret_book_ID = self.entry_ret_book_ID.get()
        # print(ret_book_ID)
        try:
            ret_query = cur.execute("SELECT count(*) FROM issued WHERE book_id=?", (ret_book_ID,)).fetchall()
            print(ret_query[0][0])
        except Exception as e:
            print(e)
        finally:
            if ret_query != None:
                if ret_query[0][0] and ret_book_ID != "":
                    cur.execute("DELETE FROM issued WHERE book_id=?", (ret_book_ID,))
                    main.db.conn.commit()
                    messagebox.showinfo("Success", 'Book has been returned successfully', icon='info')
                    ReturnBook.destroy(self)
                elif ret_query[0][0] == 0 and ret_book_ID != "":
                    messagebox.showinfo("UnSuccess", 'Entered Book ID is not present', icon='info')
                    ReturnBook.destroy(self)
                else:
                    messagebox.showerror("Error", 'All fields are mandatory', icon='warning')
                    ReturnBook.destroy(self)
            else:
                print('return query : None')
                ReturnBook.destroy(self)