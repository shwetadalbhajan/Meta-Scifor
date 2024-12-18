import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def bmi():
    h = float(height.get())
    w = float(weight.get())
    bmi = w / (h ** 2)
    result.config(text=f"BMI: {bmi:.2f}")
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    messagebox.showinfo("BMI category", f"You are {category}")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")
root.configure(bg="yellow")

tk.Label(root, text="BMI Calculator", font=("Arial", 20, "bold"), fg="blue", bg="yellow").pack(pady=10)

tk.Label(root, text="Enter your height (meters): ", bg="yellow").pack()
height = tk.Entry(root)
height.pack()

tk.Label(root, text="Enter your Weight (kg): ", bg="yellow").pack()
weight = tk.Entry(root)
weight.pack()

tk.Button(root, text="Calculate", command=bmi).pack(pady=10)

result = tk.Label(root, text="", bg="yellow")
result.pack()

root.mainloop()