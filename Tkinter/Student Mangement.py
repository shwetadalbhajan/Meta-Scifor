import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self,id,name,age,course):
        self.id=id
        self.name=name
        self.age=age
        self.course=course

class management:
    def __init__(self,root):
        self.students={}
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("500x500")

        self.title=tk.Label(root,text="Student Management System",font=("Helvetica",18,"bold"),bg="#4CAF50",fg="white")
        self.title.pack(pady=10,fill=tk.X)

        self.form=tk.Frame(root)
        self.form.pack(pady=20)

        tk.Label(self.form,text="Student ID: ",font=("Serif",12)).grid(row=0,column=0,padx=10,pady=5,sticky=tk.W)
        self.input_id=tk.Entry(self.form,font=("Serif",12),width=25)
        self.input_id.grid(row=0,column=1,padx=10,pady=5)

        tk.Label(self.form, text="Name: ", font=("Serif", 12)).grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.input_name = tk.Entry(self.form, font=("Serif", 12), width=25)
        self.input_name.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.form, text="Age: ", font=("Serif", 12)).grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.input_age = tk.Entry(self.form, font=("Serif", 12), width=25)
        self.input_age.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.form, text="Course: ", font=("Serif", 12)).grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.input_course = tk.Entry(self.form, font=("Serif", 12), width=25)
        self.input_course.grid(row=3, column=1, padx=10, pady=5)

        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        # Buttons with styling
        button_style = {"font": ("Helvetica", 12, "bold"), "bg": "#2196F3", "fg": "white", "width": 15, "height": 2}

        self.button_add = tk.Button(self.button_frame, text="Add Student", **button_style, command=self.add)
        self.button_add.grid(row=0, column=0, padx=10, pady=5)

        self.button_display = tk.Button(self.button_frame, text="Display Students", **button_style,command=self.display)
        self.button_display.grid(row=0, column=1, padx=10, pady=5)

        self.button_search = tk.Button(self.button_frame, text="Search Student", **button_style,command=self.search)
        self.button_search.grid(row=1, column=0, padx=10, pady=5)

        self.button_update = tk.Button(self.button_frame, text="Update Student", **button_style,command=self.update)
        self.button_update.grid(row=1, column=1, padx=10, pady=5)

        self.button_delete = tk.Button(self.button_frame, text="Delete Student", **button_style,command=self.delete)
        self.button_delete.grid(row=2, column=0, padx=10, pady=5)

        self.button_exit = tk.Button(self.button_frame, text="Exit", font=("Helvetica", 12, "bold"), bg="#F44336",fg="white", width=15, height=2, command=root.quit)
        self.button_exit.grid(row=2, column=1, padx=10, pady=5)

    def add(self):
        id=self.input_id.get()
        name=self.input_name.get()
        age=self.input_age.get()
        course=self.input_course.get()
        if id and name and age and course:
            if id not in self.students:
                self.students[id]=Student(id,name,age,course)
                messagebox.showinfo("Success","Student added successfully!")
            else:
                messagebox.showinfo("Error","ID already exists!")
        else:
            messagebox.showinfo("Error","All fields are required!")
        self.clear_entries()

    def display(self):
        if self.students:
            details = ""
            for student in self.students.values():
                details += f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Course: {student.course}\n"
            messagebox.showinfo("Student Details", details)
        else:
            messagebox.showinfo("No Data", "No students available!")

    def search(self):
        student_id = self.input_id.get()
        if student_id in self.students:
            student = self.students[student_id]
            messagebox.showinfo("Student Found",f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Course: {student.course}")
        else:
            messagebox.showwarning("Not Found", "Student not found!")

    def update(self):
        student_id = self.input_id.get()
        if student_id in self.students:
            name = self.input_name.get()
            age = self.input_age.get()
            course = self.input_course.get()
            if name:
                self.students[student_id].name = name
            if age:
                self.students[student_id].age = age
            if course:
                self.students[student_id].course = course
            messagebox.showinfo("Success", "Student details updated!")
        else:
            messagebox.showwarning("Error", "Student not found!")
        self.clear_entries()


    def delete(self):
        student_id = self.input_id.get()
        if student_id in self.students:
            del self.students[student_id]
            messagebox.showinfo("Success", "Student deleted successfully!")
        else:
            messagebox.showwarning("Error", "Student not found!")
        self.clear_entries()

    def clear_entries(self):
        self.input_id.delete(0, tk.END)
        self.input_name.delete(0, tk.END)
        self.input_age.delete(0, tk.END)
        self.input_course.delete(0, tk.END)


root=tk.Tk()
app=management(root)
root.mainloop()