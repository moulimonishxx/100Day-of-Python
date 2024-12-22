import tkinter as tk
from tkinter import ttk, messagebox
import calendar
from datetime import datetime

notes = {}
date_buttons = {}

current_selected_button = None

#update the calendar
def update_calendar():
    month = int(month_var.get())
    year = int(year_var.get())
    update_calendar_grid(year, month)

# display the calendar grid
def update_calendar_grid(year, month):
    global current_selected_button

    # Clear the old calendar grid
    for widget in calendar_frame.winfo_children():
        widget.destroy()

    cal = calendar.Calendar()
    days = cal.itermonthdays(year, month)

    # Add headers with background colors
    headers = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    colors = ["#f8c291", "#78e08f", "#60a3bc", "#e58e26", "#6a89cc", "#e55039", "#f6b93b"]
    for i, header in enumerate(headers):
        lbl = tk.Label(calendar_frame, text=header, font=("Arial", 10, "bold"), bg=colors[i], width=5, height=2)
        lbl.grid(row=0, column=i)

    # Add day buttons
    row = 1
    col = 0
    for day in days:
        if day == 0:  # Skip empty cells
            lbl = tk.Label(calendar_frame, text="", width=5, height=2)
            lbl.grid(row=row, column=col)
        else:
            btn = tk.Button(
                calendar_frame,
                text=str(day),
                width=5,
                height=2,
                command=lambda d=day: select_date(d),
                relief=tk.GROOVE
            )
            btn.grid(row=row, column=col)
            date_buttons[(day, month, year)] = btn

        col += 1
        if col > 6:  # Start a new row after Sunday
            col = 0
            row += 1

    # Reset current selection
    current_selected_button = None

# Function to handle date selection and highlight
def select_date(day):
    global current_selected_button

    month = int(month_var.get())
    year = int(year_var.get())
    selected_date = f"{day:02d}/{month:02d}/{year}"

    # Reset the previously selected button
    if current_selected_button:
        current_selected_button.config(bg="SystemButtonFace")

    # Highlight the new selected button
    current_button = date_buttons.get((day, month, year))
    if current_button:
        current_button.config(bg="#ffcccc")  # Highlight color
        current_selected_button = current_button

    # Update the label and display notes
    date_label.config(text=f"Selected Date: {selected_date}")
    display_notes(selected_date)

# Function to add a note to the selected date
def add_note():
    selected_date = date_label.cget("text").replace("Selected Date: ", "")
    note_text = note_entry.get("1.0", tk.END).strip()

    if not note_text:
        messagebox.showerror("Error", "Please enter a note.")
        return

    if selected_date in notes:
        notes[selected_date].append(note_text)
    else:
        notes[selected_date] = [note_text]

    messagebox.showinfo("Success", f"Note added for {selected_date}!")
    note_entry.delete("1.0", tk.END)

# Function to display notes for the selected date
def display_notes(selected_date):
    if selected_date in notes:
        note_list = "\n".join(f"- {note}" for note in notes[selected_date])
        notes_display.config(state='normal')
        notes_display.delete("1.0", tk.END)
        notes_display.insert(tk.END, note_list)
        notes_display.config(state='disabled')
    else:
        notes_display.config(state='normal')
        notes_display.delete("1.0", tk.END)
        notes_display.insert(tk.END, "No notes for this date.")
        notes_display.config(state='disabled')

# Initialize the main window
root = tk.Tk()
root.title("Interactive Calendar with Notes")
root.geometry("550x600")

# Current month and year
current_month = datetime.now().month
current_year = datetime.now().year

# Dropdown for selecting month
month_var = tk.StringVar(value=current_month)
month_label = tk.Label(root, text="Month:")
month_label.pack()
month_dropdown = ttk.Combobox(root, textvariable=month_var, values=list(range(1, 13)))
month_dropdown.pack()

# Dropdown for selecting year
year_var = tk.StringVar(value=current_year)
year_label = tk.Label(root, text="Year:")
year_label.pack()
year_dropdown = ttk.Combobox(root, textvariable=year_var, values=list(range(1900, 2101)))
year_dropdown.pack()

# Update button
update_button = tk.Button(root, text="Update Calendar", command=update_calendar)
update_button.pack(pady=5)

# Calendar frame
calendar_frame = tk.Frame(root)
calendar_frame.pack(pady=10)

# Display the initial calendar
update_calendar_grid(current_year, current_month)

# Selected date label
date_label = tk.Label(root, text="Selected Date: None", font=("Arial", 12, "bold"))
date_label.pack(pady=5)

# Text box for adding notes
note_label = tk.Label(root, text="Add Note:")
note_label.pack()
note_entry = tk.Text(root, height=5, width=40)
note_entry.pack()

# Button to add notes
add_note_button = tk.Button(root, text="Add Note", command=add_note)
add_note_button.pack(pady=5)

# Notes display
notes_label = tk.Label(root, text="Notes for Selected Date:")
notes_label.pack()
notes_display = tk.Text(root, height=8, width=40, state='disabled')
notes_display.pack()

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=10)

# Run the application
root.mainloop()
