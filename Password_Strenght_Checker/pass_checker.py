import tkinter as tk
from tkinter import ttk
import string

try:
    with open("rockyou.txt", "r", encoding="latin-1") as f:
        rockyou = set(f.read().splitlines())
except FileNotFoundError:
    rockyou = set()

def check_password():
    pwd = myEntry.get()
    score = 0

    if pwd in rockyou:
        result_label.config(text="Password is too common!", fg="red")
        progress['value'] = 0
    else:
        if any(c.islower() for c in pwd):
            score += 1
            has_lower.set(True)
        else:
            has_lower.set(False)

        if any(c.isupper() for c in pwd):
            score += 1
            has_upper.set(True)
        else:
            has_upper.set(False)

        if any(c.isdigit() for c in pwd):
            score += 1
            has_digit.set(True)
        else:
            has_digit.set(False)

        if any(c in string.punctuation for c in pwd):
            score += 1
            has_symbol.set(True)
        else:
            has_symbol.set(False)

        if len(pwd) >= 8:
            score += 1
            has_length.set(True)
        else:
            has_length.set(False)

        if len(pwd) <= 4:
            score -= 2

        progress['value'] = score * 20

        if score <= 2:
            result_label.config(text="Weak", fg="red")
        elif score in (3, 4):
            result_label.config(text="Medium", fg="orange")
        else:
            result_label.config(text="Strong", fg="green")

#GUI
root = tk.Tk()
root.geometry("600x400")
root.title("Password Strength Checker")

label = tk.Label(root, text="Enter your password:", font=('Arial', 14))
label.pack(anchor="w", padx=20, pady=(20, 5))

frame = tk.Frame(root)
frame.pack(anchor="w", padx=20, pady=10)

myEntry = tk.Entry(frame, width=40, font=('Arial', 12), show="*")
myEntry.pack(side=tk.LEFT, padx=5)

button = tk.Button(frame, text="Check", font=('Arial', 12), width=10, command=check_password)
button.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.pack(anchor="w", padx=20, pady=10)

progress = ttk.Progressbar(root, length=300, mode='determinate')
progress.pack(anchor="w", padx=20, pady=10)

#checkbox-uri
has_lower = tk.BooleanVar()
has_upper = tk.BooleanVar()
has_digit = tk.BooleanVar()
has_symbol = tk.BooleanVar()
has_length = tk.BooleanVar()

criteria_frame = tk.Frame(root)
criteria_frame.pack(anchor="w", padx=40, pady=15)

tk.Checkbutton(criteria_frame, text="Contains lowercase letter",
               variable=has_lower, state="disabled").pack(anchor="w")
tk.Checkbutton(criteria_frame, text="Contains uppercase letter",
               variable=has_upper, state="disabled").pack(anchor="w")
tk.Checkbutton(criteria_frame, text="Contains digit",
               variable=has_digit, state="disabled").pack(anchor="w")
tk.Checkbutton(criteria_frame, text="Contains symbol",
               variable=has_symbol, state="disabled").pack(anchor="w")
tk.Checkbutton(criteria_frame, text="At least 8 characters",
               variable=has_length, state="disabled").pack(anchor="w")

root.mainloop()
