import tkinter as tk
from tkinter import messagebox

def calculate_area():
    try:
        base = float(base_entry.get())
        height = float(height_entry.get())
        
        if base <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Base and height must be positive numbers.")
            return
        
        area = 0.5 * base * height
        result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Create the main window
root = tk.Tk()
root.title("Triangle Area Calculator")
root.geometry("300x200")

# Create and place widgets
base_label = tk.Label(root, text="Enter base:")
base_label.pack()
base_entry = tk.Entry(root)
base_entry.pack()

height_label = tk.Label(root, text="Enter height:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate Area", command=calculate_area)
calculate_button.pack()

result_label = tk.Label(root, text="Area: ")
result_label.pack()

# Run the application
root.mainloop()
