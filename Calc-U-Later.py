import tkinter as tk
from tkinter import ttk
import random

# Global variable to store the current calculation expression
current_expression = ""

def calculate_wrong_result():
    global current_expression
    # Generate a random wrong result
    result = random.randint(1, 1000)  # Adjust the range as needed
    result_label.config(text="Result: " + str(result))

def add_to_expression(value):
    global current_expression
    current_expression += value
    expression_label.config(text="Expression: " + current_expression)

def calculate_expression():
    global current_expression
    # You can add your own logic to evaluate the expression here
    calculate_wrong_result()
    current_expression = ""
    expression_label.config(text="Expression: ")

# Create the main window
root = tk.Tk()
root.title("Awesome Wrong Calculator")

# Create a style for the buttons
style = ttk.Style()
style.configure('TButton', font=('Arial', 10), padding=5)

# Create a frame for the calculator buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create buttons for numbers and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '='
]

# Layout the buttons in a grid
row = 1
col = 0
for button in buttons:
    if button == '=':
        btn = ttk.Button(button_frame, text=button, style='TButton', width=5, command=calculate_expression)
    else:
        btn = ttk.Button(button_frame, text=button, style='TButton', width=5, command=lambda btn=button: add_to_expression(btn))
    btn.grid(row=row, column=col, padx=3, pady=3)
    # Bind keyboard events to the buttons
    root.bind(button, lambda event, btn=btn: btn.invoke())
    col += 1
    if col > 3:
        col = 0
        row += 1

# Label to display the result
result_label = tk.Label(root, text="Result: ", font=('Arial', 12))
result_label.pack()

# Label to display the current expression
expression_label = tk.Label(root, text="Expression: ", font=('Arial', 10))
expression_label.pack()

# Run the GUI
root.mainloop()
