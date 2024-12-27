import tkinter as tk
from tkinter import messagebox
import secrets
import string
import pyperclip
from tkinter import font
import os


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("600x500")
        self.root.config(bg="#f4f4f4")  # Updated background color

        self.root.iconbitmap("lock-solid.ico")
        # Load the Josefin Sans font manually if not in system fonts
        self.font_family = self.load_font()

        # Create a frame for the single box
        self.frame = tk.Frame(self.root, bg="#ffffff", relief="solid", bd=1, padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title Label
        self.title_label = tk.Label(self.frame, text="Password Generator", font=(self.font_family, 24, "bold"),
                                    bg="#ffffff", fg="#333333")
        self.title_label.pack(pady=20)

        # Password Length Section
        self.length_frame = tk.Frame(self.frame, bg="#ffffff")
        self.length_frame.pack(pady=10)

        self.length_label = tk.Label(self.length_frame, text="Password Length:", font=(self.font_family, 14, "bold"),
                                     bg="#ffffff", fg="#333333")
        self.length_label.pack(side=tk.LEFT, padx=10)

        self.length_entry = self.create_textbox(self.length_frame, "12")  # Default length
        self.length_entry.pack(side=tk.LEFT)

        # Character Types Section
        self.character_types_frame = tk.Frame(self.frame, bg="#ffffff")
        self.character_types_frame.pack(pady=10, anchor="w", padx=30)

        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)

        self.uppercase_checkbox = tk.Checkbutton(self.character_types_frame, text="Uppercase",
                                                 variable=self.include_uppercase, font=(self.font_family, 12, "bold"),
                                                 bg="#ffffff", fg="#333333")
        self.uppercase_checkbox.grid(row=0, column=0, sticky="w", pady=5)

        self.lowercase_checkbox = tk.Checkbutton(self.character_types_frame, text="Lowercase",
                                                 variable=self.include_lowercase, font=(self.font_family, 12, "bold"),
                                                 bg="#ffffff", fg="#333333")
        self.lowercase_checkbox.grid(row=1, column=0, sticky="w", pady=5)

        self.digits_checkbox = tk.Checkbutton(self.character_types_frame, text="Digits", variable=self.include_digits,
                                              font=(self.font_family, 12, "bold"), bg="#ffffff", fg="#333333")
        self.digits_checkbox.grid(row=2, column=0, sticky="w", pady=5)

        self.symbols_checkbox = tk.Checkbutton(self.character_types_frame, text="Symbols",
                                               variable=self.include_symbols, font=(self.font_family, 12, "bold"), bg="#ffffff",
                                               fg="#333333")
        self.symbols_checkbox.grid(row=3, column=0, sticky="w", pady=5)

        # Custom Characters Section
        self.custom_char_frame = tk.Frame(self.frame, bg="#ffffff")
        self.custom_char_frame.pack(pady=10, anchor="w", padx=30)

        self.custom_char_label = tk.Label(self.custom_char_frame, text="Custom Characters:",
                                          font=(self.font_family, 12, "bold"), bg="#ffffff", fg="#333333")
        self.custom_char_label.pack(side=tk.LEFT, padx=10)

        self.custom_char_entry = self.create_textbox(self.custom_char_frame)
        self.custom_char_entry.pack(side=tk.LEFT)

        # Generate Password Button
        self.generate_button = tk.Button(self.frame, text="Generate", font=(self.font_family, 14, "bold"),
                                         command=self.generate_password, bg="#4CAF50", fg="white", relief="flat",
                                         height=1, width=12)
        self.generate_button.pack(pady=10)

        # Password Display Section
        self.password_label = tk.Label(self.frame, text="Generated Password:", font=(self.font_family, 14, "bold"),
                                       bg="#ffffff", fg="#333333")
        self.password_label.pack(pady=5)

        self.password_display = tk.Label(self.frame, text="", font=(self.font_family, 16, "bold"), bg="#f1f1f1",
                                         width=25, height=2, relief="sunken", anchor="center", fg="#333333")
        self.password_display.pack(pady=10)

        # Buttons Frame (for Clear and Copy buttons)
        self.buttons_frame = tk.Frame(self.frame, bg="#ffffff")
        self.buttons_frame.pack(pady=10)

        # Clear Button
        self.clear_button = tk.Button(self.buttons_frame, text="Clear", font=(self.font_family, 12, "bold"),
                                      command=self.clear_input, bg="#f44336", fg="white", relief="flat", height=1,
                                      width=8)
        self.clear_button.pack(side=tk.LEFT, padx=10)

        # Copy Button (placed to the right of the password display)
        self.copy_button = tk.Button(self.buttons_frame, text="Copy", font=(self.font_family, 12, "bold"),
                                     command=self.copy_password, bg="#008CBA", fg="white", relief="flat", height=1,
                                     width=8)
        self.copy_button.pack(side=tk.LEFT, padx=10)

        # Hover effect for buttons with smooth transitions
        self.generate_button.bind("<Enter>", lambda e: self.on_hover(self.generate_button, "#45a049"))
        self.generate_button.bind("<Leave>", lambda e: self.on_leave(self.generate_button, "#4CAF50"))

        self.clear_button.bind("<Enter>", lambda e: self.on_hover(self.clear_button, "#d32f2f"))
        self.clear_button.bind("<Leave>", lambda e: self.on_leave(self.clear_button, "#f44336"))

        self.copy_button.bind("<Enter>", lambda e: self.on_hover(self.copy_button, "#007bb5"))
        self.copy_button.bind("<Leave>", lambda e: self.on_leave(self.copy_button, "#008CBA"))

    def load_font(self):
        # Check if the Josefin Sans font is available
        font_path = "E:/program_unit/pythonProject5/font/Josefin_Sans"  # Path to your font file
        if os.path.exists(font_path):
            self.root.tk.call("font", "create", "JosefinSans", "-family", "Josefin Sans", "-size", "12", "-weight",
                              "normal")
            return "JosefinSans"
        else:
            return "Arial"  # Fallback to Arial if not found

    def create_textbox(self, parent, default_value=""):
        """Create a styled text box."""
        entry = tk.Entry(parent, font=(self.font_family, 12), width=25, bd=2, relief="sunken", highlightthickness=1,
                         highlightcolor="#4CAF50", highlightbackground="#ddd")
        entry.insert(0, default_value)
        entry.config(insertbackground='black')  # Cursor color
        entry.bind("<FocusIn>", self.on_focus_in)
        entry.bind("<FocusOut>", self.on_focus_out)
        return entry

    def on_focus_in(self, event):
        event.widget.config(bg="#e8f5e9")  # Light green background on focus

    def on_focus_out(self, event):
        event.widget.config(bg="white")  # White background when focus is lost

    def on_hover(self, button, hover_color):
        button.config(bg=hover_color)  # Change background on hover

    def on_leave(self, button, default_color):
        button.config(bg=default_color)  # Revert to default color on mouse leave

    def generate_password(self):
        try:
            length = int(self.length_entry.get())

            if length < 4:
                raise ValueError("Password length should be at least 4 characters.")

            # Define character sets
            available_characters = ""
            if self.include_uppercase.get():
                available_characters += string.ascii_uppercase
            if self.include_lowercase.get():
                available_characters += string.ascii_lowercase
            if self.include_digits.get():
                available_characters += string.digits
            if self.include_symbols.get():
                available_characters += string.punctuation

            # Add custom characters to the pool if any
            custom_chars = self.custom_char_entry.get()
            available_characters += custom_chars

            if not available_characters:
                messagebox.showerror("Error", "At least one character type must be selected.")
                return

            # Generate password using secrets for cryptographic security
            password = ''.join(secrets.choice(available_characters) for _ in range(length))

            # Display the password
            self.password_display.config(text=password)

        except ValueError as e:
            messagebox.showerror("Invalid Input", f"Please enter a valid number for password length. {str(e)}")

    def copy_password(self):
        password = self.password_display.cget("text")

        if password:
            pyperclip.copy(password)  # Copy the password to the clipboard
            messagebox.showinfo("Password Copied", "Your password has been copied to the clipboard.")
        else:
            messagebox.showwarning("No Password", "Please generate a password first.")

    def clear_input(self):
        self.length_entry.delete(0, tk.END)
        self.length_entry.insert(0, "12")
        self.include_uppercase.set(True)
        self.include_lowercase.set(True)
        self.include_digits.set(True)
        self.include_symbols.set(True)
        self.custom_char_entry.delete(0, tk.END)
        self.password_display.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
