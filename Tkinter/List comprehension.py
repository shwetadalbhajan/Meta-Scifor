import tkinter as tk
from tkinter import ttk


def double(numbers):
    return list(map(lambda x: x * 2, numbers))


def even(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


def sums(numbers):
    return sum(x for x in numbers)


def squares(numbers):
    return [x ** 2 for x in numbers]


def process():
    num_str = num.get()
    numbers = list(map(int, num_str.split()))
    selected = operation_var.get()

    if selected == "Double Numbers":
        result = double(numbers)
    elif selected == "Filter Even Numbers":
        result = even(numbers)
    elif selected == "Sum Numbers":
        result = sums(numbers)
    elif selected == "Squares":
        result = squares(numbers)
    else:
        result = "Select a valid operation"

    result_label.config(text=f"Result: {result}")


def reset():
    num.delete(0, 'end')
    result_label.config(text="Result:")


# Main application window
root = tk.Tk()
root.title("Number Operations")
root.geometry("500x500")
root.configure(bg="#2E8B57")  # Sea Green background for better aesthetics

# Define style
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12), padding=10)
style.configure("TButton", font=("Helvetica", 12), padding=5)
style.configure("TFrame", background="#F0F8FF")  # Light cyan background for frames

# Frame for title
title_frame = ttk.Frame(root, padding=10)
title_frame.pack(pady=10)

ttk.Label(title_frame, text="Number Operations App", font=("Helvetica", 18, "bold"), background="#F0F8FF").pack()

# Frame for input and options
input_frame = ttk.Frame(root, padding=20)
input_frame.pack(pady=10)

ttk.Label(input_frame, text="Enter numbers separated by spaces: ", background="#F0F8FF").grid(row=0, column=0, pady=5)
num = ttk.Entry(input_frame, width=40, font=("Helvetica", 12))
num.grid(row=1, column=0, pady=5)

# Dropdown menu for selecting operation
operation_var = tk.StringVar()
operations = ["Double Numbers", "Filter Even Numbers", "Sum Numbers", "Squares"]
menu = ttk.OptionMenu(input_frame, operation_var, "Select Operation", *operations)
menu.grid(row=2, column=0, pady=10)

# Buttons for process and reset
button_frame = ttk.Frame(root, padding=20)
button_frame.pack()

process_button = ttk.Button(button_frame, text="Process", command=process)
process_button.grid(row=0, column=0, padx=10, pady=5)

reset_button = ttk.Button(button_frame, text="Reset", command=reset)
reset_button.grid(row=0, column=1, padx=10, pady=5)

# Frame for result display
result_frame = ttk.Frame(root, padding=20)
result_frame.pack(pady=20)

result_label = ttk.Label(result_frame, text="Result: ", font=("Helvetica", 12), background="#F0F8FF")
result_label.pack()

root.mainloop()
