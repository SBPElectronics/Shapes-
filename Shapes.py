import tkinter as tk
from tkinter import simpledialog

import circle  
import Saleem



class ButtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Button App")
        
        # Create three buttons
        self.button1 = tk.Button(self.root, text="Button 1", command=self.button1_action)
        self.button1.pack(pady=10)
        
        self.button2 = tk.Button(self.root, text="Button 2", command=self.button2_action)
        self.button2.pack(pady=10)
        
        self.button3 = tk.Button(self.root, text="Button 3", command=self.button3_action)
        self.button3.pack(pady=10)
        
    def button1_action(self):

        print("hello froam SUPER MAN")
        Saleem.ask_side_length() 
        
    def button2_action(self):

        print('working')

        circle.print_message()

        
    def button3_action(self):

        print("ello from mahd")

        print("Hello World From MahPooda")   

        print("Hello World From MahLooda")


# Create the main window
root = tk.Tk()

# Create an instance of the ButtonApp class
app = ButtonApp(root)

# Start the Tkinter event loop
root.mainloop()
