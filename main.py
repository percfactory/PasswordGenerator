import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string

def generate_password():
    length = password_length_slider.get()
    include_symbols = var_symbols.get()
    include_numbers = var_numbers.get()
    
    password = []
    
    # Guarantee at least one letter
    password.append(secrets.choice(string.ascii_letters))
    
    # Guarantee at least one of each selected type
    if include_numbers:
        password.append(secrets.choice(string.digits))
    if include_symbols:
        password.append(secrets.choice(string.punctuation))
    
    # Build character pool for remaining slots
    characters = string.ascii_letters
    if include_symbols:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits
    
    # Fill remaining slots to reach desired length
    remaining_length = length - len(password)
    password.extend(secrets.choice(characters) for _ in range(remaining_length))
    
    # Shuffle to mix up the guaranteed characters
    password_list = list(password)
    for i in range(len(password_list) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_list[i], password_list[j] = password_list[j], password_list[i]
    
    password = ''.join(password_list)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
    update_strength()

def copy_to_clipboard():
    password = entry_password.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "Generate a password first!")

def update_strength():
    password = entry_password.get()
    if not password:
        strength_label.config(text="", fg="")
        return
    
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    strength_score = sum([has_upper, has_lower, has_digits, has_special])
    
    if length < 10:
        strength_text, color = "Weak", "#e74c3c"
    elif strength_score < 3:
        strength_text, color = "Fair", "#f39c12"
    elif strength_score < 4:
        strength_text, color = "Good", "#3498db"
    else:
        strength_text, color = "Strong", "#27ae60"
    
    strength_label.config(text=f"Strength: {strength_text}", fg=color)
 
# Setting up main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("450x650")
window.config(bg="#1e1e2e")
window.resizable(False, False)

# Main container frame
main_frame = tk.Frame(window, bg="#1e1e2e")
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Adding a title label with styling
title_label = tk.Label(main_frame, text="🔐 Password Generator", font=("Helvetica", 20, "bold"), bg="#1e1e2e", fg="#00d4ff")
title_label.pack(pady=(0, 25))

# Label and slider for the length of the password
label_length = tk.Label(main_frame, text="Password Length:", font=("Helvetica", 11, "bold"), bg="#1e1e2e", fg="#e0e0e0")
label_length.pack(pady=(15, 5), anchor="w")

length_display_frame = tk.Frame(main_frame, bg="#1e1e2e")
length_display_frame.pack(anchor="w", pady=(0, 10))

length_value_label = tk.Label(length_display_frame, text="12", font=("Helvetica", 16, "bold"), bg="#1e1e2e", fg="#00d4ff", width=3)
length_value_label.pack(side=tk.LEFT, padx=(0, 10))

# Range slider for the length of the password
def update_length_display(value):
    length_value_label.config(text=str(int(float(value))))

password_length_slider = tk.Scale(main_frame, from_=8, to=32, orient="horizontal", length=280, font=("Helvetica", 11), 
                                   sliderlength=20, showvalue=0, bg="#2a2a3e", troughcolor="#00d4ff", 
                                   fg="#00d4ff", highlightthickness=0, command=update_length_display)
password_length_slider.set(12)
password_length_slider.pack(pady=10, fill=tk.X)

# Divider
divider = tk.Frame(main_frame, height=1, bg="#3a3a4e")
divider.pack(fill=tk.X, pady=15)

# Define boolean variables for states of the checkboxes
var_numbers = tk.BooleanVar()
var_symbols = tk.BooleanVar()

# Options frame
options_label = tk.Label(main_frame, text="Include in Password:", font=("Helvetica", 11, "bold"), bg="#1e1e2e", fg="#e0e0e0")
options_label.pack(pady=(10, 10), anchor="w")

# Adding check buttons using ttk
check_numbers = ttk.Checkbutton(main_frame, text="Include Numbers", variable=var_numbers, style="TCheckbutton")
check_numbers.pack(pady=5, anchor="w")

check_symbols = ttk.Checkbutton(main_frame, text="Include Symbols", variable=var_symbols, style="TCheckbutton")
check_symbols.pack(pady=5, anchor="w")

# Divider
divider2 = tk.Frame(main_frame, height=1, bg="#3a3a4e")
divider2.pack(fill=tk.X, pady=15)

# Button frame for generate and refresh buttons
button_frame = tk.Frame(main_frame, bg="#1e1e2e")
button_frame.pack(pady=15, fill=tk.X)

# Generate button
generate_btn = tk.Button(button_frame, text="Generate Password", command=generate_password, 
                        font=("Helvetica", 11, "bold"), bg="#00d4ff", fg="#1e1e2e", 
                        relief="flat", height=2, bd=0, cursor="hand2")
generate_btn.pack(side=tk.LEFT, padx=(0, 10), fill=tk.BOTH, expand=True)

# Refresh button
refresh_btn = tk.Button(button_frame, text="🔄 Refresh", command=generate_password, 
                       font=("Helvetica", 11, "bold"), bg="#2a9d8f", fg="white", 
                       relief="flat", height=2, bd=0, cursor="hand2", width=8)
refresh_btn.pack(side=tk.LEFT, fill=tk.BOTH)

# Entry field to display the generated password
label_password = tk.Label(main_frame, text="Generated Password", font=("Helvetica", 11, "bold"), bg="#1e1e2e", fg="#e0e0e0")
label_password.pack(pady=(15, 8), anchor="w")

# Entry field for the password so that the user can copy it
entry_password = tk.Entry(main_frame, font=("Courier New", 12), width=35, bd=2, 
                         relief="solid", fg="#00d4ff", bg="#2a2a3e", insertbackground="#00d4ff")
entry_password.pack(pady=(0, 10), ipady=8)

# Copy button
copy_btn = tk.Button(main_frame, text="📋 Copy to Clipboard", command=copy_to_clipboard, 
                    font=("Helvetica", 10, "bold"), bg="#e74c3c", fg="white", 
                    relief="flat", height=1, bd=0, cursor="hand2")
copy_btn.pack(fill=tk.X, pady=10)

# Strength indicator
strength_label = tk.Label(main_frame, text="", font=("Helvetica", 10, "bold"), bg="#1e1e2e")
strength_label.pack(pady=5)
 
# Styling the check buttons using ttk theme
style = ttk.Style()
style.theme_use('clam')
style.configure("TCheckbutton", font=("Helvetica", 11), background="#1e1e2e", foreground="#e0e0e0", 
               padding=5, focuscolor="none", borderwidth=0)
style.map("TCheckbutton", 
         background=[("active", "#2a2a3e")],
         foreground=[("active", "#00d4ff")])

# Making an event loop so that the application keeps running
window.mainloop()
 