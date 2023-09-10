import tkinter as tk

# Function to perform addition
def add():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 + num2
    result_label.config(text=f"Result: {result}")

# Function to perform subtraction
def subtract():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 - num2
    result_label.config(text=f"Result: {result}")

# Function to perform multiplication
def multiply():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 * num2
    result_label.config(text=f"Result: {result}")

# Function to perform division
def divide():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 == 0:
        result_label.config(text="Cannot divide by zero")
    else:
        result = num1 / num2
        result_label.config(text=f"Result: {result}")

# Function to clear input fields and result label
def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields for numbers
entry_num1 = tk.Entry(root)
entry_num1.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

# Create buttons for each operation
add_button = tk.Button(root, text="Add", command=add)
add_button.pack()

subtract_button = tk.Button(root, text="Subtract", command=subtract)
subtract_button.pack()

multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.pack()

divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.pack()

# Create a button to clear input fields and result
clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
