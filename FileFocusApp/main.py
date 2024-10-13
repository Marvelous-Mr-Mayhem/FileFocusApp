import tkinter as tk
from tkinter import filedialog, messagebox
from file_organizer import organizer

# Function to select the source directory
def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        return directory
    else:
        messagebox.showerror("Error", "Please select a valid directory.")
        return None

# Function to start organizing files
def start_organizing():
    directory = select_directory()
    if directory:
        try:
            organizer.organize_files(directory)
            messagebox.showinfo("Success", "File organization complete!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create the GUI window
app = tk.Tk()
app.title("FileFocusApp - File Organizer")

# Set window size and color theme
app.geometry("500x300")
app.configure(bg="#4B0082")  # Indigo purple background

# Add a label for the title
label = tk.Label(app, text="Welcome to FileFocusApp Organize your files easily.",
                 font=("Helvetica", 14), bg="#4B0082", fg="white")
label.pack(pady=20)

# Button to start organizing files
organize_btn = tk.Button(app, text="Select Directory and Organize", command=start_organizing,
                         font=("Helvetica", 12), bg="#9370DB", fg="white")
organize_btn.pack(pady=10)

# Add "By Marvelous Mr Mayhem" tag at the bottom left corner
footer_label = tk.Label(app, text="By Marvelous Mr Mayhem",
                        font=("Helvetica", 10), bg="#4B0082", fg="white", anchor="w")
footer_label.pack(side="left", padx=10, pady=20)

# Start the GUI loop
app.mainloop()
