import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
from playsound import playsound
from gtts import gTTS


TEMP_AUDIO_FILE = "preview_audio.mp3"

# Supported languages
LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta",
    "French": "fr",
    "Spanish": "es"
}


engine = pyttsx3.init()

# Function to convert text to speech and preview using pyttsx3 (for detailed speed control)
def preview_speech():
    text = text_input.get("1.0", "end").strip()  # Get text from the text box
    selected_language = LANGUAGES[language_choice.get()]  # Get selected language
    speed = speed_slider.get()  # Get the speed from the slider

    if not text:
        messagebox.showwarning("Input Error", "Please enter some text to preview.")
        return

    try:
        # Set the speech rate based on the slider value (range: 100 to 500)
        engine.setProperty('rate', speed)

        # Speak the text (preview speech)
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during preview: {e}")


# Function to play the audio file (only used for gTTS preview here)
def play_audio_file(file_path):
    try:
        # Ensure the file path is quoted properly to avoid issues with spaces or special characters
        subprocess.run(["start", "", file_path], shell=True, check=True)
    except Exception as e:
        print(f"Error playing the audio: {e}")


# Function to save the audio file using gTTS (still works with gTTS for saving files)
def save_speech():
    text = text_input.get("1.0", "end").strip()  # Get text from the text box
    selected_language = LANGUAGES[language_choice.get()]  # Get selected language
    speed = speed_slider.get()  # Get the speed from the slider

    if not text:
        messagebox.showwarning("Input Error", "Please enter some text to save.")
        return

    try:
        # File save dialog
        output_file = filedialog.asksaveasfilename(
            defaultextension=".mp3",
            filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")],
            title="Save as"
        )
        if not output_file:
            return  # User canceled saving

        # Generate and save the audio file using gTTS
        tts = gTTS(text=text, lang=selected_language, slow=False)  # Use normal speed for file save
        tts.save(output_file)

        messagebox.showinfo("Success", f"Speech saved as '{output_file}'")

        # Optionally, play the saved file
        play_audio_file(output_file)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during saving: {e}")


# Create the main application window
app = tk.Tk()
app.title("Text-to-Speech Converter with Language Selection and Speed Control")
app.geometry("500x600")
app.config(bg="#F0F0F0")  # Set background color

# Add a header label with a modern look
header_label = tk.Label(app, text="Text-to-Speech Converter", font=("Arial", 18, "bold"), bg="#F0F0F0", fg="#3E8E41")
header_label.pack(pady=20)

# Add a label for input text
label = tk.Label(app, text="Enter Text Below:", font=("Arial", 14), bg="#F0F0F0")
label.pack(pady=10)

# Add a text box for user input
text_input = tk.Text(app, height=10, width=50, wrap="word", font=("Arial", 12), bd=2, relief="solid")
text_input.pack(pady=10)

# Add a dropdown menu for language selection
language_label = tk.Label(app, text="Select Language:", font=("Arial", 12), bg="#F0F0F0")
language_label.pack(pady=5)

language_choice = tk.StringVar(app)
language_choice.set("English")  # Default language

language_menu = tk.OptionMenu(app, language_choice, *LANGUAGES.keys())
language_menu.config(width=20, font=("Arial", 12), bd=2, relief="solid")
language_menu.pack(pady=10)

# Add a slider for speed control
speed_label = tk.Label(app, text="Select Speed:", font=("Arial", 12), bg="#F0F0F0")
speed_label.pack(pady=5)

speed_slider = tk.Scale(app, from_=100, to=500, orient="horizontal", length=300, label="Speed (Rate)", tickinterval=50)
speed_slider.set(200)  # Set default speed
speed_slider.pack(pady=10)

# Add a preview button with a rounded look
preview_button = tk.Button(app, text="Preview Speech", font=("Arial", 12), command=preview_speech, width=20, height=2, bg="#4CAF50", fg="white", bd=0, relief="ridge")
preview_button.pack(pady=10)

# Add a save button with a modern look
save_button = tk.Button(app, text="Save Speech", font=("Arial", 12), command=save_speech, width=20, height=2, bg="#2196F3", fg="white", bd=0, relief="ridge")
save_button.pack(pady=10)

# Footer with extra space
footer_label = tk.Label(app, text="© 2024 Text-to-Speech Converter By Mouli", font=("Arial", 10), bg="#F0F0F0", fg="#888")
footer_label.pack(side="bottom", pady=20)

# Cleanup: Delete the temporary audio file on application exit
def on_close():
    if os.path.exists(TEMP_AUDIO_FILE):
        os.remove(TEMP_AUDIO_FILE)
    app.destroy()


app.protocol("WM_DELETE_WINDOW", on_close)

# Run the application
app.mainloop()
