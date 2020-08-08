import tkinter as tk
#TODO Time in GUI
#TODO Delete Text
#TODO Copy to clipboard
#TODO Fix issues

#Pomodoros : 5

# Variables
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x100")
root.resizable(False, False)

# Functions
def passwordGenerator():
    import random
    global passwordLabel
    words = "abcdefghijklmnopqrstuvxwyz1234567890!@#$%^&*"
    result = ""
    while len(result) < 20:
        result += random.choice(words)
    answer = result
    passwordLabel = tk.Label(root, text=answer)
    passwordLabel.pack()

def Delete_Label():
    passwordLabel.pack_forget()

# GUI

ButtonGenerate = tk.Button(root, padx=20, height=1, text="Generate", font=40, command=passwordGenerator)
ButtonGenerate.place(relx=0.20, rely=0.60)

DeleteButton = tk.Button(root, text="Delete", padx=20, font=40, height=1, command=Delete_Label)
DeleteButton.place(relx=0.5, rely=0.60)

PasswordLabel = tk.Label(root, text="Press Generate").place(relx=0.35, rely=0)


# PasswordEntry = tk.Entry(root, width=25)
# PasswordEntry.place(relx=0.25, rely=0.25)

root.mainloop()
