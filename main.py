import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook
import splashscreen
import addstudent
import addbook
import returnbook
import deletebook
import issuebook
import deletestudent
import database

db = database.DBconnection()


# Startup Screen
class MainWindow(object):
    def __init__(self, master):
        self.master = master

        # TOP Frame for LABEL
        frame_1 = LabelFrame(self.master, bd=1, height=80, borderwidth=2)
        frame_1.pack(side=TOP, fill="x", padx=1)
        # create a label in first frame_1
        label_1 = Label(frame_1, text='Library Management System', bg="gray72", height=3, font=("Courier", 25, 'bold'))
        label_1.pack(side=TOP, fill="x")

        # Frame 2 for management
        frame_2 = LabelFrame(self.master, bd=1, borderwidth=2)
        frame_2.pack(fill="x", padx=1, pady=1)
        # Create TABS for frame_4
        self.tabs = Notebook(frame_2, width=800, height=500)
        self.tabs.pack(fill="x")
        self.tab1 = Frame(self.tabs)
        self.tab2 = Frame(self.tabs)
        self.tabs.add(self.tab1, text="Book Management")
        self.tabs.add(self.tab2, text="Student Management")

        # Book Management in Tab1
        # Book Management Frame_1
        book_management_frame_1 = LabelFrame(self.tab1, bd=1, height=50, borderwidth=2)
        book_management_frame_1.pack(fill="x", padx=1, pady=1)
        # Add buttons in book_management_frame_1
        btName = ["Add Book", "Return Book", "Delete Book"]
        # Dynamically adjust buttons configuration
        Grid.rowconfigure(book_management_frame_1, 0, weight=1)
        Grid.columnconfigure(book_management_frame_1, 0, weight=1)
        Grid.columnconfigure(book_management_frame_1, 1, weight=1)
        Grid.columnconfigure(book_management_frame_1, 2, weight=1)
        self.addBook = Button(book_management_frame_1, text=btName[0], font='bold', command=self.new_book)
        self.addBook.grid(row=0, column=0, sticky="EW", ipadx=60)
        self.returnBook = Button(book_management_frame_1, text=btName[1], font='bold', command=self.return_book)
        self.returnBook.grid(row=0, column=1, sticky="EW")
        self.delBook = Button(book_management_frame_1, text=btName[2], font='bold', command=self.delete_book)
        self.delBook.grid(row=0, column=2, sticky="EW")
        # Book Management Frame_2
        book_management_frame_2 = LabelFrame(self.tab1, bd=1, height=80, borderwidth=2)
        book_management_frame_2.pack(fill="x", padx=1, pady=1)
        # Create Combobox for Choice
        self.book_search_choice = StringVar()
        self.combo_book_search_choice = ttk.Combobox(book_management_frame_2, font=("", 10),
                                                     textvariable=self.book_search_choice, postcommand=self.show_books)
        self.combo_book_search_choice.pack(side=LEFT, padx=10)
        # fill comboBox
        self.bookSearchChoice = ['All books', 'Issued book', "Not issued books"]
        self.combo_book_search_choice['values'] = self.bookSearchChoice
        # select default
        self.combo_book_search_choice.current(0)
        self.entry_search_book = Entry(book_management_frame_2, width=40, bd=3, font=("", 15))
        self.entry_search_book.pack(side=LEFT, fill="x", padx=10, pady=10)
        self.bookSearchBtn = Button(book_management_frame_2, text='Search', padx=12, font="bold",
                                    command=self.book_search)
        self.bookSearchBtn.pack(side=LEFT, fill="x", padx=10, ipadx=20)
        # Book Management Frame_3
        book_management_frame_3 = LabelFrame(self.tab1, text="", bd=3, height=400, borderwidth=2, relief=SUNKEN)
        book_management_frame_3.pack(fill="x", padx=5, pady=5)
        # Create Tab1: Management
        self.book_managementBox = Listbox(book_management_frame_3, width=50, height=25)
        self.book_managementBox_sb = Scrollbar(book_management_frame_3, orient=VERTICAL)
        self.book_managementBox.grid(row=0, column=0, padx=(3, 0), sticky=N)
        self.book_managementBox_sb.config(command=self.book_managementBox.yview)
        self.book_managementBox.config(yscrollcommand=self.book_managementBox_sb.set)
        self.book_managementBox_sb.grid(row=0, column=0, sticky=N + S + E)
        # Details of books
        self.book_managementBox_detail = Listbox(book_management_frame_3, width=80, height=25)
        self.book_managementBox_detail.grid(row=0, column=1, padx=(10, 0), sticky=N)

        # Student Management in Tab2
        # Student Management Frame_1
        student_management_frame_1 = LabelFrame(self.tab2, bd=1, height=50, borderwidth=2)
        student_management_frame_1.pack(fill="x", padx=1, pady=1)
        # Add buttons in student_management_frame_1
        student_btName = ["Add Student", "Issue Book", "Delete Student"]
        # Dynamically adjust buttons configuration
        Grid.rowconfigure(student_management_frame_1, 0, weight=1)
        Grid.columnconfigure(student_management_frame_1, 0, weight=1)
        Grid.columnconfigure(student_management_frame_1, 1, weight=1)
        Grid.columnconfigure(student_management_frame_1, 2, weight=1)
        self.addStudent = Button(student_management_frame_1, text=student_btName[0], font='bold',
                                 command=self.new_student)
        self.addStudent.grid(row=0, column=0, sticky="EW", ipadx=60)
        self.iBook = Button(student_management_frame_1, text=student_btName[1], font='bold', command=self.issue_book)
        self.iBook.grid(row=0, column=1, sticky="EW")
        self.delStudent = Button(student_management_frame_1, text=student_btName[2], font='bold',
                                 command=self.delete_student)
        self.delStudent.grid(row=0, column=2, sticky="EW")

        # Student Management Frame_2
        student_management_frame_2 = LabelFrame(self.tab2, bd=1, height=80, borderwidth=2)
        student_management_frame_2.pack(fill="x", padx=1, pady=1)
        # Create Combobox for Choice
        self.student_search_choice = StringVar()
        self.combo_student_search_choice = ttk.Combobox(student_management_frame_2, font=("", 10),
                                                        textvariable=self.student_search_choice,
                                                        postcommand=self.show_students)
        self.combo_student_search_choice.pack(side=LEFT, padx=10)
        # fill comboBox
        self.studentSearchChoice = ['All Students', 'Students who issued book', "Students who didn't issued"]
        self.combo_student_search_choice['values'] = self.studentSearchChoice
        # select default
        self.combo_student_search_choice.current(0)
        self.entry_search_student = Entry(student_management_frame_2, width=40, bd=3, font=("", 15))
        self.entry_search_student.pack(side=LEFT, fill="x", padx=10, pady=10)
        self.studentSearchBtn = Button(student_management_frame_2, text='Search', padx=12, font="bold",
                                       command=self.student_search)
        self.studentSearchBtn.pack(side=LEFT, fill="x", padx=10, ipadx=20)

        # student Management Frame_3
        student_management_frame_3 = LabelFrame(self.tab2, text="", bd=3, height=400, borderwidth=2, relief=SUNKEN)
        student_management_frame_3.pack(fill="x", padx=5, pady=5)
        # Create Tab1: Management
        self.student_managementBox = Listbox(student_management_frame_3, width=50, height=25)
        self.student_managementBox_sb = Scrollbar(student_management_frame_3, orient=VERTICAL)
        self.student_managementBox.grid(row=0, column=0, padx=(3, 0), sticky=N)
        self.student_managementBox_sb.config(command=self.student_managementBox.yview)
        self.student_managementBox.config(yscrollcommand=self.student_managementBox_sb.set)
        self.student_managementBox_sb.grid(row=0, column=0, sticky=N + S + E)
        # Details of students
        self.student_managementBox_detail = Listbox(student_management_frame_3, width=80, height=25)
        self.student_managementBox_detail.grid(row=0, column=1, padx=(10, 0), sticky=N)
        self.show_students()
        self.show_books()

    # show student list in message box
    def show_students(self):
        cur = db.conn.cursor()
        if self.studentSearchChoice[0] == self.combo_student_search_choice.get():
            self.student_managementBox.delete(0, END)
            self.student_managementBox_detail.delete(0, END)
            print("ALL student")
            students = cur.execute("SELECT * FROM students").fetchall()
            counter = 0
            for student in students:
                self.student_managementBox.insert(counter,
                                                  str(counter + 1) + ") " + student[0] + "  ( ID: " + student[
                                                      3] + " )")
                counter += 1
        elif self.studentSearchChoice[1] == self.combo_student_search_choice.get():
            self.student_managementBox.delete(0, END)
            self.student_managementBox_detail.delete(0, END)
            print("Issued student")
            students = cur.execute("SELECT * FROM issued").fetchall()
            counter = 0
            for student in students:
                value1 = student[1]
                # print(value)
                studentDetail = cur.execute("SELECT * FROM students WHERE student_id LIKE ?",
                                            ('%' + value1 + '%',)).fetchall()
                # print(studentDetail)
                self.student_managementBox.insert(counter,
                                                  str(counter + 1) + ") " + studentDetail[0][0] + "( ID : " +
                                                  studentDetail[0][3] + " )")
                counter += 1
        else:
            self.student_managementBox.delete(0, END)
            self.student_managementBox_detail.delete(0, END)
            print("not issued student")
            students = cur.execute(
                "SELECT * FROM students WHERE student_id NOT IN (SELECT student_id FROM issued)").fetchall()
            # print(students)
            counter = 0
            for student in students:
                self.student_managementBox.insert(counter,
                                                  str(counter + 1) + ") " + student[0] + " ( ID : " + student[3] + " )")

        # show student info
        def showStudentInfo(evt):
            if self.studentSearchChoice[0] == self.combo_student_search_choice.get():
                value2 = None
                try:
                    value2 = str(self.student_managementBox.get(self.student_managementBox.curselection()))
                except Exception as e:
                    print(e)
                finally:
                    if value2 != None:
                        ID1 = value2.split(')')[1].split(': ')[1][0:3]
                        # print(ID1)
                        self.student_managementBox_detail.delete(0, END)
                        student1 = cur.execute("SELECT * FROM students WHERE student_id=?", (ID1,))
                        student_info = student1.fetchall()
                        # print(student_info)
                        self.student_managementBox_detail.insert(0, "Student Name : " + student_info[0][0])
                        self.student_managementBox_detail.insert(1, "Father Name : " + student_info[0][2])
                        self.student_managementBox_detail.insert(2, "Phone Number : " + student_info[0][1])
                    else:
                        print('Value2 : None')
            elif self.studentSearchChoice[1] == self.combo_student_search_choice.get():
                value3 = None
                try:
                    value3 = str(self.student_managementBox.get(self.student_managementBox.curselection()))
                except Exception as e:
                    print(e)
                finally:
                    if value3 != None:
                        ID2 = value3.split(') ')[1].split(': ')[1][0:3]
                        self.student_managementBox_detail.delete(0, END)
                        print(ID2)
                        student2 = cur.execute("SELECT * FROM students WHERE student_id=?", (ID2,)).fetchall()
                        print(student2)
                        self.student_managementBox_detail.insert(0, "Student Name : " + student2[0][0])
                        self.student_managementBox_detail.insert(1, "Father Name : " + student2[0][2])
                        self.student_managementBox_detail.insert(2, "Phone Number : " + student2[0][1])
                    else:
                        print('Value3 : None')
            else:
                value4 = None
                try:
                    value4 = str(self.student_managementBox.get(self.student_managementBox.curselection()))
                    print(value4)
                except Exception as e:
                    if value4 != None:
                        ID3 = value4.split(') ')[1].split(': ')[1][0:3]
                        print(ID3)
                        self.student_managementBox_detail.delete(0, END)
                        student3 = cur.execute("SELECT * FROM students WHERE student_id=?", (ID3,)).fetchall()
                        print(student3)
                        self.student_managementBox_detail.insert(0, "Student Name : " + student3[0][0])
                        self.student_managementBox_detail.insert(1, "Father Name : " + student3[0][2])
                        self.student_managementBox_detail.insert(2, "Phone Number : " + student3[0][1])
                    else:
                        print('Value4 : None')

        # student_managementBox bind with student_managementBox_detail
        self.student_managementBox.bind('<<ListboxSelect>>', showStudentInfo)

    def student_search(self):
        cur = db.conn.cursor()
        comboBoxEntry = self.combo_student_search_choice.get()
        studentSearchEntry = self.entry_search_student.get()
        # print(comboBoxEntry)
        # print(studentSearchEntry)
        if comboBoxEntry == self.studentSearchChoice[0]:
            searchQuery = cur.execute("SELECT * FROM students where sname LIKE ?",
                                      ('%' + studentSearchEntry + '%',)).fetchall()
            self.student_managementBox.delete(0, END)
            self.student_managementBox_detail.delete(0, END)
            counter = 0
            for student in searchQuery:
                self.student_managementBox.insert(counter,
                                                  str(counter + 1) + ") " + student[0] + "  ( ID: " + student[3] + " )")
                counter += 1
        elif comboBoxEntry == self.studentSearchChoice[1]:
            searchQuery = cur.execute("SELECT * FROM students WHERE sname LIKE ?",
                                      ('%' + studentSearchEntry + '%',)).fetchall()
            # print(searchQuery)
            self.student_managementBox.delete(0, END)
            self.student_managementBox_detail.delete(0, END)
            counter = 0
            for student in searchQuery:
                cur = db.conn.cursor()
                value = student[3]
                # print(value)
                studentDetail = cur.execute("SELECT count(*) FROM issued WHERE student_id=?", (value,)).fetchall()
                print(studentDetail[0][0])
                print(student)
                if studentDetail[0][0] != 0:
                    counter += 1
                    self.student_managementBox.insert(counter,
                                                      str(counter) + ") " + student[0] + " ( ID : " + student[3] + " )")

        else:
            searchQuery = cur.execute(
                "SELECT * FROM students WHERE student_id NOT IN (SELECT student_id FROM issued) AND (sname LIKE ?)",
                ('%' + studentSearchEntry + '%',)).fetchall()
            print(searchQuery)
            self.student_managementBox.delete(0, END)
            self.student_managementBox_detail.delete(0, END)
            counter = 0
            for student in searchQuery:
                cur = db.conn.cursor()
                # print(student)
                counter += 1
                self.student_managementBox.insert(counter,
                                                  str(counter) + ") " + student[0] + " ( ID : " + student[3] + " )")

    # show student list in message box
    def show_books(self):
        cur = db.conn.cursor()
        if self.bookSearchChoice[0] == self.combo_book_search_choice.get():
            self.book_managementBox.delete(0, END)
            self.book_managementBox_detail.delete(0, END)
            print("All Books")
            books = cur.execute("SELECT * FROM books").fetchall()
            # print(books)
            counter = 0
            for book in books:
                self.book_managementBox.insert(counter,
                                               str(counter + 1) + ") " + book[0] + "  ( ID: " + book[
                                                   3] + " )")
                counter += 1
        elif self.bookSearchChoice[1] == self.combo_book_search_choice.get():
            self.book_managementBox.delete(0, END)
            self.book_managementBox_detail.delete(0, END)
            print("Issued books")
            books = cur.execute("SELECT * FROM issued").fetchall()
            counter = 0
            for book in books:
                value1 = book[0]
                # print(value1)
                bookDetail = cur.execute("SELECT * FROM books WHERE book_id LIKE ?",
                                         ('%' + value1 + '%',)).fetchall()
                print(bookDetail)
                self.book_managementBox.insert(counter,
                                               str(counter + 1) + ") " + bookDetail[0][0] + "( ID : " +
                                               bookDetail[0][3] + " )")
                counter += 1
        else:
            self.book_managementBox.delete(0, END)
            self.book_managementBox_detail.delete(0, END)
            print("not issued books")
            books = cur.execute(
                "SELECT * FROM books WHERE book_id NOT IN (SELECT book_id FROM issued)").fetchall()
            # print(books)
            counter = 0
            for book in books:
                self.book_managementBox.insert(counter,
                                               str(counter + 1) + ") " + book[0] + " ( ID : " + book[
                                                   3] + " )")
                counter += 1

        # show student info
        def showBookInfo(evt):
            if self.bookSearchChoice[0] == self.combo_book_search_choice.get():
                value2 = None
                try:
                    value2 = str(self.book_managementBox.get(self.book_managementBox.curselection()))
                except Exception as e:
                    print(e)
                finally:
                    if value2 != None:
                        ID1 = value2.split(')')[1].split(': ')[1][0:3]
                        print(ID1)
                        self.book_managementBox_detail.delete(0, END)
                        book1 = cur.execute("SELECT * FROM books WHERE book_id=?", (ID1,))
                        book_info = book1.fetchall()
                        print(book_info)
                        self.book_managementBox_detail.insert(0, "Book Name   : " + book_info[0][0])
                        self.book_managementBox_detail.insert(1, "Author Name : " + book_info[0][1])
                        self.book_managementBox_detail.insert(2, "Category    : " + book_info[0][2])
                    else:
                        print('Value2 : None')
            elif self.bookSearchChoice[1] == self.combo_book_search_choice.get():
                value3 = None
                try:
                    value3 = str(self.book_managementBox.get(self.book_managementBox.curselection()))
                except Exception as e:
                    print(e)
                finally:
                    if value3 != None:
                        ID2 = value3.split(') ')[1].split(': ')[1][0:3]
                        self.book_managementBox_detail.delete(0, END)
                        print(ID2)
                        book2 = cur.execute("SELECT * FROM books WHERE book_id=?", (ID2,)).fetchall()
                        print(book2)
                        self.book_managementBox_detail.insert(0, "Book Name   : " + book2[0][0])
                        self.book_managementBox_detail.insert(1, "Author Name : " + book2[0][1])
                        self.book_managementBox_detail.insert(2, "Category    : " + book2[0][2])
                    else:
                        print('Value3 : None')
            else:
                value4 = None
                try:
                    value4 = str(self.book_managementBox.get(self.book_managementBox.curselection()))
                except Exception as e:
                    print(e)
                finally:
                    if value4 != None:
                        print(value4)
                        ID3 = value4.split(') ')[1].split(': ')[1][0:3]
                        print(ID3)
                        self.book_managementBox_detail.delete(0, END)
                        book3 = cur.execute("SELECT * FROM books WHERE book_id=?", (ID3,)).fetchall()
                        print(book3)
                        self.book_managementBox_detail.insert(0, "Book Name    : " + book3[0][0])
                        self.book_managementBox_detail.insert(1, "Author Name  : " + book3[0][1])
                        self.book_managementBox_detail.insert(2, "Category     : " + book3[0][2])
                    else:
                        print('Value4 : None')

        # student_managementBox bind with student_managementBox_detail
        self.book_managementBox.bind('<<ListboxSelect>>', showBookInfo)

    def book_search(self):
        cur = db.conn.cursor()
        comboBoxEntry = self.combo_book_search_choice.get()
        bookSearchEntry = self.entry_search_book.get()
        # print(comboBoxEntry)
        # print(bookSearchEntry)
        if comboBoxEntry == self.bookSearchChoice[0]:
            searchQuery = cur.execute("SELECT * FROM books where bname LIKE ?",
                                      ('%' + bookSearchEntry + '%',)).fetchall()
            self.book_managementBox.delete(0, END)
            self.book_managementBox_detail.delete(0, END)
            counter = 0
            for book in searchQuery:
                self.book_managementBox.insert(counter,
                                               str(counter + 1) + ") " + book[0] + "  ( ID: " + book[3] + " )")
                counter += 1
        elif comboBoxEntry == self.bookSearchChoice[1]:
            searchQuery = cur.execute("SELECT * FROM books WHERE bname LIKE ?",
                                      ('%' + bookSearchEntry + '%',)).fetchall()
            # print(searchQuery)
            self.book_managementBox.delete(0, END)
            self.book_managementBox_detail.delete(0, END)
            counter = 0
            for book in searchQuery:
                cur = db.conn.cursor()
                value = book[3]
                print(value)
                bookDetail = cur.execute("SELECT count(*) FROM issued WHERE book_id=?", (value,)).fetchall()
                # print(bookDetail)
                # print(book)
                if bookDetail[0][0] != 0:
                    counter += 1
                    self.book_managementBox.insert(counter, str(counter) + ") " + book[0] + " ( ID : " + book[3] + " )")

        else:
            searchQuery = cur.execute(
                "SELECT * FROM books WHERE book_id NOT IN (SELECT book_id FROM issued) AND (bname LIKE ?)",
                ('%' + bookSearchEntry + '%',)).fetchall()
            print(searchQuery)
            self.book_managementBox.delete(0, END)
            self.book_managementBox_detail.delete(0, END)
            counter = 0
            for book in searchQuery:
                cur = db.conn.cursor()
                # print(book)
                counter += 1
                self.book_managementBox.insert(counter, str(counter) + ") " + book[0] + " ( ID : " + book[3] + " )")

    @staticmethod
    def new_student():
        newStudent = addstudent.AddStudent()

    @staticmethod
    def new_book():
        newBook = addbook.AddBook()

    @staticmethod
    def return_book():
        ret_book_obj = returnbook.ReturnBook()

    @staticmethod
    def delete_book():
        del_book_obj = deletebook.DeleteBook()

    @staticmethod
    def issue_book():
        issue_book_obj = issuebook.IssueBook()

    @staticmethod
    def delete_student():
        delete_student_obj = deletestudent.DeleteStudent()


def splash():
    # Initialize TK() class for main window
    splashWin = tkinter.Tk()
    start_screen = splashscreen.SplashScreen(splashWin)
    splashWin.title('SPLASH!')
    # Size of Screen
    splash_app_width = 800
    splash_app_height = 600
    splash_screen_width = (splashWin.winfo_screenwidth() / 2) - (splash_app_width / 2)
    splash_screen_height = (splashWin.winfo_screenheight() / 2) - (splash_app_height / 2)
    splash_x = int(splash_screen_width)
    splash_y = int(splash_screen_height)
    splashWin.geometry(f"{splash_app_width}x{splash_app_height}+{splash_x}+{splash_y}")
    splashWin.overrideredirect(1)

    def main():
        splashWin.destroy()
        # Initialize TK() class for main window
        win = tkinter.Tk()
        app = MainWindow(win)
        # to refresh app
        # win.update()
        win.update_idletasks()
        # Title
        win.title('Library Management System')
        # Size of Screen
        app_width = 800
        app_height = 600
        screen_width = (win.winfo_screenwidth() / 2) - (app_width / 2)
        screen_height = (win.winfo_screenheight() / 2) - (app_height / 2)
        x = int(screen_width)
        y = int(screen_height)

        win.geometry(f"{app_width}x{app_height}+{x}+{y}")
        # Resizable ability of screen : DISABLE
        # win.resizable(False, False)
        win.mainloop()

    splashWin.after(3000, main)
    splashWin.mainloop()


# Control of app
if __name__ == "__main__":
    splash()
