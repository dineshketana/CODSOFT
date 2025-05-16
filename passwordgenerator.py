import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showwarning("Warning", "Password length must be greater than zero.")
            return

        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()

        characters = ''
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("Warning", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for i in range(length))
        result_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showwarning("Warning", "Invalid input! Please enter a valid password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create input fields and labels
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)

entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=5)

upper_var = tk.BooleanVar()
upper_checkbox = tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var)
upper_checkbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

lower_var = tk.BooleanVar()
lower_checkbox = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var)
lower_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_checkbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

special_var = tk.BooleanVar()
special_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_checkbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Run the application
root.mainloop()