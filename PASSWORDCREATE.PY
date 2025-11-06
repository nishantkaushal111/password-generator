import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be greater than 0")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length")
        return

    characters = ""
    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_output.delete(0, tk.END)
    password_output.insert(0, password)

def copy_password():
    window.clipboard_clear()
    window.clipboard_append(password_output.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# --- GUI Window Setup ---
window = tk.Tk()
window.title("🔐 Password Generator")
window.geometry("400x400")
window.config(bg="#f0f0f0")

# Title
tk.Label(window, text="Python Password Generator", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Length
tk.Label(window, text="Enter Password Length:", bg="#f0f0f0", font=("Arial", 12)).pack()
length_entry = tk.Entry(window, font=("Arial", 12), width=10, justify='center')
length_entry.pack(pady=5)
length_entry.insert(0, "12")

# Options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(window, text="Include Uppercase (A-Z)", variable=var_upper, bg="#f0f0f0", font=("Arial", 11)).pack(anchor='w', padx=60)
tk.Checkbutton(window, text="Include Lowercase (a-z)", variable=var_lower, bg="#f0f0f0", font=("Arial", 11)).pack(anchor='w', padx=60)
tk.Checkbutton(window, text="Include Numbers (0-9)", variable=var_digits, bg="#f0f0f0", font=("Arial", 11)).pack(anchor='w', padx=60)
tk.Checkbutton(window, text="Include Symbols (!@#$)", variable=var_symbols, bg="#f0f0f0", font=("Arial", 11)).pack(anchor='w', padx=60)

# Generate Button
tk.Button(window, text="Generate Password", command=generate_password, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=15)

# Output
password_output = tk.Entry(window, font=("Arial", 13), justify='center', width=30)
password_output.pack(pady=10)

# Copy Button
tk.Button(window, text="Copy Password", command=copy_password, font=("Arial", 11, "bold"), bg="#2196F3", fg="white", padx=10, pady=5).pack(pady=5)

# Run the app
window.mainloop()
