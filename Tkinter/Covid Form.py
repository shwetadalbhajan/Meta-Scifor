import tkinter as tk
from idlelib.help import show_idlehelp
from tkinter import messagebox

class covid:
    def __init__(self,root):
        self.root=root
        self.root.title("Covid Registration Form")
        self.root.geometry("500x700")

        self.name=tk.StringVar()
        self.age=tk.StringVar()
        self.gender=tk.StringVar(value="Male")
        self.contact=tk.StringVar()
        self.email=tk.StringVar()
        self.vaccine=tk.StringVar(value="Not Vaccinated")
        self.infected=tk.StringVar(value="No")
        self.symptoms=tk.StringVar()

        self.form()

    def form(self):
        tk.Label(self.root, text='Covid Registration Form', font=('Arial', 16, 'bold'),
                 bg='#4682B4',fg='white',padx=10,pady=10).pack(fill='x')
        frame=tk.Frame(self.root,bg='#f2f2f2')
        frame.pack(pady=20)

        def labels(text,variable,frame1):
            tk.Label(frame1,text=text,font=('Arial',12,'bold'),bg='#f2f2f2').pack(anchor='w',padx=20,pady=(10,0))
            tk.Entry(frame1,textvariable=variable,width=40,font=('Arial',12),bd=2,relief='solid').pack(pady=5,padx=20)
        labels("Name: ",self.name,frame)
        labels("Age: ",self.age,frame)
        labels("Contact No: ", self.contact, frame)
        labels("Email: ", self.email, frame)

        tk.Label(frame,text="Gender: ",font=('Arial',12,'bold'),bg='#f2f2f2').pack(anchor='w',padx=20,pady=(10,0))
        tk.Radiobutton(frame,text="Male",variable=self.gender,value="Male",font=('Arial',11),bg='#f2f2f2').pack(padx=10)
        tk.Radiobutton(frame,text="Female",variable=self.gender,value="Female",font=('Arial',11),bg='#f2f2f2').pack(padx=10)

        tk.Label(frame, text="Infection Status: ", font=('Arial', 12, 'bold'), bg='#f2f2f2').pack(anchor='w', padx=20,pady=(10, 0))
        tk.Radiobutton(frame, text="Infected", variable=self.gender, value="Yes", font=('Arial', 11),bg='#f2f2f2').pack(padx=10)
        tk.Radiobutton(frame, text="Not Infected", variable=self.gender, value="No", font=('Arial', 11),bg='#f2f2f2').pack(padx=10)

        labels("Symptoms if infected: ",self.symptoms,frame)

        submit=tk.Button(self.root,text="Submit",font=('Arial',14,'bold'),
                         command=self.submit,bg='#4682B4',fg='white',bd=0,padx=10,pady=10)
        submit.pack(pady=20)

    def submit(self):
        messagebox.showinfo("message","Thanks you for the survey!\nYour participation is appreciated")

root=tk.Tk()
app=covid(root)
root.mainloop()