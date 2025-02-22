import tkinter as tk
from tkinter import simpledialog

def calculate_area():
    radius = simpledialog.askfloat("Input", "Enter the radius of the circle:")
    if radius is not None:
        area = 3.14159 * radius ** 2
        result_label.config(text=f"Area: {area:.2f}")

root = tk.Tk()
root.title("Circle Area Calculator")

calc_button = tk.Button(root, text="Calculate Area", command=calculate_area)
calc_button.pack(pady=10)

result_label = tk.Label(root, text="Area: ")
result_label.pack(pady=10)

root.mainloop()