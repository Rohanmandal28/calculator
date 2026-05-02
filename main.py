import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
        entry.delete(0, tk.END)
    except Exception:
        messagebox.showerror("Error", "Invalid input.")
        entry.delete(0, tk.END)

# Function to append text to the entry field
def append_text(text):
    entry.insert(tk.END, text)

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry field
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=evaluate_expression)
    elif text == "C":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=clear_entry)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda t=text: append_text(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
