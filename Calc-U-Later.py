import tkinter as tk
from tkinter import ttk
import random

# Global variable to store the current calculation expression
current_expression = ""

def calculate_wrong_result():
    # Get the correct result from the expression
    try:
        result = eval(current_expression)
    except ZeroDivisionError:
        result = "Error: Division by zero"
    
    # Add or subtract a random small value to introduce randomness
    random_offset = random.uniform(-0.1, 0.1) * abs(result)
    
    # Calculate the wrong result
    wrong_result = round(float(result) + random_offset, 2)
    
    # Update the result label
    result_label.config(text="Result: " + str(wrong_result))

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
        ttk.Button(button_frame, text=button, style='TButton', width=5, command=calculate_expression).grid(row=row, column=col, padx=3, pady=3)
    else:
        ttk.Button(button_frame, text=button, style='TButton', width=5, command=lambda btn=button: add_to_expression(btn)).grid(row=row, column=col, padx=3, pady=3)
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
