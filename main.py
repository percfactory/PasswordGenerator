import tkinter as tkinter
    from tkinter import ttk
    import random
    import string

# Main function with choices of length,numbers and symbols
def generate_password():
    length = password_length_slider.get()
    include_symbols = var_symbols.get()
    include_numbers = var_numbers.get()
    
# Defining the pool of characters to be included in the password     
    characters = string.ascii_letters
    if include_symbols:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits
 
 # Generating a random password with characters taken from the predefined pool including length
 password = ''.join(random.choice(characters) for _ in range(length)) 
 
 # Clears previous password and updates the entry field with a newly gtenerated one
 entry_password.delete(0, tk.END)
 entry_password.insert(0, password)
 
 # Setting up main window
 window = tk.Tk()
 window.title("Password Generator")
 window.geometry("400x450") # Window size
 window.config(bg="#f0f0f0") # Bg colour
 
# Adding a title label with styling
 title_label = tk.Label(window, text="Password Generator", font=("Helvetica"), 18, "bold", bg="#f0f0f0") 
 title_label.pack(pady=20)
 
 # Label and slider for the length of the password
 label_length = tk.Label(window, text="Password Length:", font=("Helvetica"), 12, bbg="#f0f0f0") 
 label_length.pack(pady=5)
 
   # Range slider for the length of the password
 password_length_slider = tk.Scale(window, from_=8, to=20, orient="horizontal", length=300, font=("Helvetica", 12), sliderlength=20, showvalue=1, bg="#f0f0f0", troughcolor="#4CAF50", highlightthickness=0)

 password_length_slider.set(12)
 password_length_slider.pack(pady=10)

# Define boolean variables for states of the checkboxes
 var_numbers = tk.BooleanVar()
 var_symbols = tk.BooleanVar()

# Adding check buttons using ttk
 check_symbols = ttk.Checkbutton(window, text="Include Symbols", variable=var_symbols, style="TCheckbutton")
 check_symbols.pack(pady=5)

 check_numbers = ttk.Checkbutton(window, text="Include Numbers", variable=var_symbols, style="TCheckbutton")
 check_numbers.pack(pady=5)
 
 # Function to create rounded button with tk.Button
 def create_rounded_button

 

