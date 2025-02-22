import tkinter as tk
from tkinter import simpledialog

def ask_side_length():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask for the side length in mm
    side_length_mm = simpledialog.askfloat("Inpust", "Enter the side length of the square (in mm):")

    if side_length_mm is not None:
        draw_square(side_length_mm)  # Call function to draw square

    root.destroy()

def draw_square(side_length_mm):
    # Convert mm to pixels (1 mm ≈ 3.78 pixels)
    scale_factor = 3.78
    side_length_px = side_length_mm * scale_factor

    # Create a new window for drawing
    square_window = tk.Tk()
    square_window.title(f"Square ({side_length_mm} mm)")

    # Create a Canvas
    canvas_size = max(200, side_length_px + 20)  # Ensure canvas is large enough
    canvas = tk.Canvas(square_window, width=canvas_size, height=canvas_size, bg="white")
    canvas.pack()

    # Draw the square
    padding = 10  # Margin from the edges
    canvas.create_rectangle(padding, padding, padding + side_length_px, padding + side_length_px, outline="black", width=2)

    square_window.mainloop()
