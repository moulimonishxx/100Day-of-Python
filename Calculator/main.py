import tkinter as tk
from tkinter import messagebox, ttk
import math
def button_click(value, entry):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)
def calculate(entry):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Function to clear the text entry
def clear(entry):
    entry.delete(0, tk.END)
def erase(entry):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])

# Function to handle trigonometric and log operations
def scientific_operation(op, entry):
    try:
        current_value = float(entry.get())
        if op == "sin":
            result = math.sin(math.radians(current_value))
        elif op == "cos":
            result = math.cos(math.radians(current_value))
        elif op == "tan":
            result = math.tan(math.radians(current_value))
        elif op == "log":
            result = math.log10(current_value)
        elif op == "pi":
            result = round(math.pi, 3)
        elif op == "sqrt":
            result = math.sqrt(current_value)
        else:
            raise ValueError("Unknown Operation")
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Create the main window
app = tk.Tk()
app.title("Calculator")
app.geometry("300x400")

app.iconbitmap('calculator-solid.ico')
# Create a notebook (tabs)
notebook = ttk.Notebook(app)
notebook.pack(fill="both", expand=True)

# Tab for standard calculator
standard_tab = ttk.Frame(notebook)
notebook.add(standard_tab, text="\u2665 Standard")

# Tab for scientific calculator
scientific_tab = ttk.Frame(notebook)
notebook.add(scientific_tab, text="\u2665 Scientific")

# Standard calculator layout
entry_standard = tk.Entry(standard_tab, font=("Bungee", 18, "bold"), borderwidth=2, relief=tk.RIDGE, justify="right")
entry_standard.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0, "lightgray"), ('8', 1, 1, "lightgray"), ('9', 1, 2, "lightgray"), ('/', 1, 3, "lightpink"),
    ('4', 2, 0, "lightgray"), ('5', 2, 1, "lightgray"), ('6', 2, 2, "lightgray"), ('*', 2, 3, "lightpink"),
    ('1', 3, 0, "lightgray"), ('2', 3, 1, "lightgray"), ('3', 3, 2, "lightgray"), ('-', 3, 3, "lightpink"),
    ('0', 4, 0, "lightgray"), ('.', 4, 1, "lightgray"), ('+', 4, 2, "lightpink"), ('=', 4, 3, "lightblue"),
    ('C', 5, 0, "lightcoral"), ('Erase', 5, 1, "lightyellow")
]

for (text, row, col, color) in buttons:
    if text == '=':
        button = tk.Button(standard_tab, text=text, font=("Bungee", 14, "bold"), bg=color, command=lambda: calculate(entry_standard))
    elif text == 'C':
        button = tk.Button(standard_tab, text=text, font=("Bungee", 14, "bold"), bg=color, command=lambda: clear(entry_standard))
    elif text == 'Erase':
        button = tk.Button(standard_tab, text=text, font=("Bungee", 14, "bold"), bg=color, command=lambda: erase(entry_standard))
    else:
        button = tk.Button(standard_tab, text=text, font=("Bungee", 14, "bold"), bg=color, command=lambda t=text: button_click(t, entry_standard))

    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

for i in range(6):
    standard_tab.grid_rowconfigure(i, weight=1)
for j in range(4):
    standard_tab.grid_columnconfigure(j, weight=1)

# Scientific calculator layout
entry_sci = tk.Entry(scientific_tab, font=("Bungee", 18, "bold"), borderwidth=2, relief=tk.RIDGE, justify="right")
entry_sci.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

sci_buttons = [
    ('7', 1, 0, "lightgray"), ('8', 1, 1, "lightgray"), ('9', 1, 2, "lightgray"), ('/', 1, 3, "lightpink"),
    ('4', 2, 0, "lightgray"), ('5', 2, 1, "lightgray"), ('6', 2, 2, "lightgray"), ('*', 2, 3, "lightpink"),
    ('1', 3, 0, "lightgray"), ('2', 3, 1, "lightgray"), ('3', 3, 2, "lightgray"), ('-', 3, 3, "lightpink"),
    ('0', 4, 0, "lightgray"), ('.', 4, 1, "lightgray"), ('+', 4, 2, "lightpink"), ('=', 4, 3, "lightblue"),
    ('sin', 5, 0, "lightgreen"), ('cos', 5, 1, "lightgreen"), ('tan', 5, 2, "lightgreen"), ('log', 5, 3, "lightblue"),
    ('pi', 6, 0, "lightgreen"), ('sqrt', 6, 1, "lightgreen"), ('C', 6, 2, "lightcoral"), ('Erase', 6, 3, "lightyellow")
]

for (text, row, col, color) in sci_buttons:
    if text == '=':
        button = tk.Button(scientific_tab, text=text, font=("Bungee", 14, "bold"), bg=color, command=lambda: calculate(entry_sci))
    elif text == 'C':
        button = tk.Button(scientific_tab, text=text, font=("Bungee", 14, "bold"), bg=color, command=lambda: clear(entry_sci))
    elif text == 'Erase':
        button = tk.Button(scientific_tab, text=text, font=("Bungee", 14, "bold"), bg=color, command=lambda: erase(entry_sci))

    elif text in ['sin', 'cos', 'tan', 'log', 'pi', 'sqrt']:
        button = tk.Button(scientific_tab, text=text, font=("Bungee", 14, "bold"), bg=color, command=lambda t=text: scientific_operation(t, entry_sci))
    else:
        button = tk.Button(scientific_tab, text=text, font=("Bungee", 14, "bold"), bg=color, command=lambda t=text: button_click(t, entry_sci))

    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

for i in range(7):
    scientific_tab.grid_rowconfigure(i, weight=1)
for j in range(4):
    scientific_tab.grid_columnconfigure(j, weight=1)

# Run the application
app.mainloop()
