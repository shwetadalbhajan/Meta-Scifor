import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("500x500")
        self.root.config(bg="#F6C90E")

        self.tasks = []

        self.title_label = tk.Label(root, text="My To-Do List", font=("Georgia", 24, "bold"), bg="#F6C90E",
                                    fg="#002147")
        self.title_label.pack(pady=20)

        self.task_frame = tk.Frame(root, bg="#F6C90E")
        self.task_frame.pack(pady=10)

        self.task_label = tk.Label(self.task_frame, text="Task:", font=("Georgia", 14), bg="#F6C90E", fg="#002147")
        self.task_label.grid(row=0, column=0, padx=10, pady=10)

        self.task_entry = tk.Entry(self.task_frame, width=30, font=("Georgia", 14), bg="#FFE79E", fg="#002147",
                                   relief="flat")
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.task_frame, text="Add Task", width=15, font=("Georgia", 12), bg="#003DA5",
                                    fg="white", command=self.add_task, relief="flat")
        self.add_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.task_listbox = tk.Listbox(root, height=10, width=45, font=("Georgia", 14), bg="#FFE79E", fg="#002147",
                                       selectbackground="#003DA5", relief="flat")
        self.task_listbox.pack(pady=20)

        self.button_frame = tk.Frame(root, bg="#F6C90E")
        self.button_frame.pack(pady=10)

        self.update_button = tk.Button(self.button_frame, text="Update Task", width=15, font=("Georgia", 12),
                                       bg="#003DA5", fg="white", command=self.update_task, relief="flat")
        self.update_button.grid(row=0, column=0, padx=5)

        self.remove_button = tk.Button(self.button_frame, text="Remove Task", width=15, font=("Georgia", 12),
                                       bg="#003DA5", fg="white", command=self.remove_task, relief="flat")
        self.remove_button.grid(row=0, column=1, padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear All Tasks", width=15, font=("Georgia", 12),
                                      bg="#003DA5", fg="white", command=self.clear_tasks, relief="flat")
        self.clear_button.grid(row=0, column=2, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove")

    def clear_tasks(self):
        self.tasks.clear()
        self.update_task_listbox()

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Task cannot be empty")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
