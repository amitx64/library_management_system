from tkinter import *
from tkinter import messagebox
import main


# Class for Add New Book Page
class DeleteStudent(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('Delete Student')
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
        label_1 = Label(frame_1, text='Delete Student', bg="gray72", height=3, font=("Courier", 20, 'bold'))
        label_1.pack(side=TOP, fill="x")
        # screen resize enable/disable
        self.resizable(False, False)
        self.delete_student_frame = LabelFrame(self, bd=3, height=100, borderwidth=2)
        self.delete_student_frame.pack(fill="x", padx=5, pady=5)
        # Create Label , Entry Box and Save Button
        self.label_delete_student_ID = Label(self.delete_student_frame, text='Enter student ID : ')
        self.label_delete_student_ID.grid(row=0, column=0, padx=10)
        self.entry_delete_student_ID = Entry(self.delete_student_frame, width=30, bd=3)
        self.entry_delete_student_ID.grid(row=0, column=1, padx=10, pady=10)

        self.frame_2 = Frame(self)
        self.frame_2.pack(fill="x")
        self.cancel_button = Button(self.frame_2, text='Cancel', font='bold', command=self.destroy)
        self.cancel_button.pack(side=LEFT, fill="x", padx=100, pady=10)
        self.delete_button = Button(self.frame_2, text='delete', font='bold', command=self.delete_student)
        self.delete_button.pack(side=LEFT, fill="x", pady=10)

    def delete_student(self):
        cur = main.db.conn.cursor()
        check_student_list = None
        check_student_issued = None
        var_deleteStudentID = self.entry_delete_student_ID.get()
        print(var_deleteStudentID)
        try:
            check_student_list = cur.execute("SELECT count(*) FROM students WHERE student_id=?",
                                             (var_deleteStudentID,)).fetchall()
            check_student_issued = cur.execute("SELECT count(*) FROM issued WHERE student_id=?",
                                               (var_deleteStudentID,)).fetchall()
        except Exception as e:
            print(e)
        finally:
            # print(check_student_list[0][0])
            if check_student_list and check_student_issued != None:
                if var_deleteStudentID != "" and check_student_list[0][0] != 0 and check_student_issued[0][0] == 0:
                    cur.execute("DELETE FROM students WHERE student_id=?", (var_deleteStudentID,))
                    main.db.conn.commit()
                    messagebox.showinfo("Success", 'Student has been delete successfully', icon='info')
                elif var_deleteStudentID != "" and (check_student_list[0][0] and check_student_issued[0][0]) != 0:
                    messagebox.showerror("UnSuccess", "Student have some books", icon='warning')
                elif (check_student_list[0][0] and check_student_issued[0][0]) == 0 and var_deleteStudentID != "":
                    messagebox.showerror("UnSuccess", "Student not present", icon='warning')
                else:
                    messagebox.showerror("Error", 'All fields are mandatory', icon='warning')
            else:
                print('Error : check_student_list = None')
