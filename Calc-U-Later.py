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
root.title("Calc U Later")
root.geometry("340x440")
root.resizable(False, False)  # Disable resizing

# Create a style for the buttons
style = ttk.Style()
style.configure('TButton', font=('Arial', 12), padding=10)
style.map('TButton', foreground=[('pressed', 'black'), ('active', 'blue')], background=[('pressed', '!disabled', 'gray'), ('active', 'lightgray')])

# Create a frame for the calculator buttons
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

# Create buttons for numbers and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '='
]

# Layout the buttons in a grid
row = 0
col = 0
for button in buttons:
    if button == '=':
        btn = ttk.Button(button_frame, text=button, style='TButton', width=5, command=calculate_expression)
    else:
        btn = ttk.Button(button_frame, text=button, style='TButton', width=5, command=lambda btn=button: add_to_expression(btn))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    # Bind keyboard events to the buttons
    root.bind(button, lambda event, btn=btn: btn.invoke())
    col += 1
    if col > 3:
        col = 0
        row += 1

# Bind Enter key to "=" button's command
root.bind('<Return>', lambda event: calculate_expression())

# Label to display the result
result_label = tk.Label(root, text="Result: ", font=('Arial', 14))
result_label.pack(pady=(0, 2))  # Reduced bottom padding

# Label to display the current expression
expression_label = tk.Label(root, text="Expression: ", font=('Arial', 12))
expression_label.pack(pady=(0, 2))  # Reduced bottom padding

# Run the GUI
root.mainloop()
