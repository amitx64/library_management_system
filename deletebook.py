from tkinter import *
from tkinter import messagebox
import main


# Class for Add New Book Page
class DeleteBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('Delete Book')
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
        label_1 = Label(frame_1, text='Delete Book', bg="gray72", height=3, font=("Courier", 20, 'bold'))
        label_1.pack(side=TOP, fill="x")
        # screen resize enable/disable
        self.resizable(False, False)
        self.delete_book_frame = LabelFrame(self, bd=3, height=100, borderwidth=2)
        self.delete_book_frame.pack(fill="x", padx=5, pady=5)
        # Create Label , Entry Box and Save Button
        self.label_delete_book_ID = Label(self.delete_book_frame, text='Enter Book ID : ')
        self.label_delete_book_ID.grid(row=0, column=0, padx=10)
        self.entry_delete_book_ID = Entry(self.delete_book_frame, width=30, bd=3)
        self.entry_delete_book_ID.grid(row=0, column=1, padx=10, pady=10)

        self.frame_2 = Frame(self)
        self.frame_2.pack(fill="x")
        self.cancel_button = Button(self.frame_2, text='Cancel', font='bold', command=self.destroy)
        self.cancel_button.pack(side=LEFT, fill="x", padx=100, pady=10)
        self.delete_button = Button(self.frame_2, text='delete', font='bold', command=self.delete_book)
        self.delete_button.pack(side=LEFT, fill="x", pady=10)

    def delete_book(self):
        cur = main.db.conn.cursor()
        check_book_library = None
        check_book_issued = None
        var_deleteBookID = self.entry_delete_book_ID.get()
        print(var_deleteBookID)
        try:
            check_book_library = cur.execute("SELECT count(*) FROM books WHERE book_id=?",
                                             (var_deleteBookID,)).fetchall()
            check_book_issued = cur.execute("SELECT count(*) FROM issued WHERE book_id=?",
                                            (var_deleteBookID,)).fetchall()
        except Exception as e:
            print(e)
        finally:
            # print(check_book_library[0][0])
            if (check_book_library and check_book_issued) != None:
                if var_deleteBookID != "" and check_book_library[0][0] != 0 and check_book_issued[0][0] == 0:
                    cur.execute("DELETE FROM books WHERE book_id=?", (var_deleteBookID,))
                    main.db.conn.commit()
                    messagebox.showinfo("Success", 'Book has been delete successfully', icon='info')
                    DeleteBook.destroy(self)
                elif var_deleteBookID != "" and (check_book_library[0][0] and check_book_issued[0][0]) != 0:
                    messagebox.showerror("UnSuccess", 'Book has been issued to someone', icon='info')
                    DeleteBook.destroy(self)
                elif var_deleteBookID != "" and (check_book_library[0][0] and  check_book_issued[0][0]) == 0:
                    messagebox.showerror("UnSuccess", "Book not present", icon='warning')
                    DeleteBook.destroy(self)
                else:
                    messagebox.showerror("Error", 'All fields are mandatory', icon='warning')
                    DeleteBook.destroy(self)
            else:
                print('Error : check_book_library = None')
                DeleteBook.destroy(self)
