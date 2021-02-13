from tkinter import *
from tkinter import messagebox
from main import db


# Class for Add New Student Page
class AddStudent(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('Add Student')
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
        label_1 = Label(frame_1, text='Add Student', bg="gray72", height=3, font=("Courier", 20, 'bold'))
        label_1.pack(side=TOP, fill="x")
        # screen resize enable/disable
        self.resizable(False, False)
        self.add_student_frame = LabelFrame(self, bd=3, height=100, borderwidth=2)
        self.add_student_frame.pack(fill="x", padx=5, pady=5)
        # Create Label , Entry Box and Save Button
        self.label_name = Label(self.add_student_frame, text='Enter Student Name : ')
        self.label_name.grid(row=0, column=0, padx=10)
        self.entry_name = Entry(self.add_student_frame, width=30, bd=3)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)
        self.label_phone_number = Label(self.add_student_frame, text='Enter Student Phone Number : ')
        self.label_phone_number.grid(row=1, column=0, padx=10)
        self.entry_phone_number = Entry(self.add_student_frame, width=30, bd=3)
        self.entry_phone_number.grid(row=1, column=1, padx=10, pady=10)

        self.frame_2 = Frame(self)
        self.frame_2.pack(fill="x")

        self.label_guardian_name = Label(self.add_student_frame, text='Enter Guardian Name : ')
        self.label_guardian_name.grid(row=2, column=0, padx=10)
        self.entry_guardian_name = Entry(self.add_student_frame, width=30, bd=3)
        self.entry_guardian_name.grid(row=2, column=1, padx=10, pady=10)
        self.label_student_id = Label(self.add_student_frame, text='Enter Student ID : ')
        self.label_student_id.grid(row=3, column=0, padx=10)
        self.entry_student_id = Entry(self.add_student_frame, width=30, bd=3)
        self.entry_student_id.grid(row=3, column=1, padx=10, pady=10)
        self.cancel_newStudent_button = Button(self.frame_2, text='Cancel', font='bold', command=self.destroy)
        self.cancel_newStudent_button.pack(side=LEFT, padx=100, pady=10)
        self.save_button = Button(self.frame_2, text='Save', font='bold', command=self.save_student)
        self.save_button.pack(side=LEFT, pady=10, ipadx=10)

    def save_student(self):
        stName = self.entry_name.get()
        stPhone = self.entry_phone_number.get()
        stGuardianName = self.entry_guardian_name.get()
        stID = self.entry_student_id.get()
        # print(stName)
        # print(stPhone)
        # print(stGuardianName)
        # print(stID)
        if stName and stPhone and stGuardianName and stID != "":
            try:
                query = "INSERT INTO 'students'(sname, phone, fname, student_id)VALUES(?,?,?,?)"
                cur = db.conn.cursor()
                cur.execute(query, (stName, stPhone, stGuardianName, stID))
                db.conn.commit()
                messagebox.showinfo("success", "student has been add successfully", icon='info')
                AddStudent.destroy(self)
            except:
                messagebox.showerror("Error", "Transaction not commit", icon='warning')
                AddStudent.destroy(self)
        else:
            messagebox.showerror("Error", "All fields are mandatory", icon='warning')
            AddStudent.destroy(self)