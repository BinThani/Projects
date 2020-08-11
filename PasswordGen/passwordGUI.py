import tkinter as tk
import pyperclip
# TODO FIX THE COPY BUTTON

# Pomodoros : 8

# Variables
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x100")
root.resizable(False, False)
root.configure(background="gray")

# Functions

def passwordGenerator():
    import random
    global passwordLabel
    global copiedLabel
    words = "abcdefghijklmnopqrstuvxwyz1234567890!@#$%^&*"
    result = ""

    while len(result) < 20:
        result += random.choice(words)

    answer = result
    pyperclip.copy(answer)
    passwordLabel = tk.Label(root, text=answer)
    passwordLabel.pack()
    #copiedLabel = tk.Label(root, text="Copied to Clipboard")
    #copiedLabel.pack()
    ButtonGenerate['state'] = 'disabled'  # When this is clicked it sets the button to disabled which means you can't press it
    return answer

def Delete_Label():
    passwordLabel.pack_forget()
    ButtonGenerate['state'] = 'normal'  # When Delete is clicked it would return buttonGenerate to normal.

def copy_to_clipboard():
    return

# GUI

ButtonGenerate = tk.Button(root, padx=20, height=1, text="Generate", font=40, command=passwordGenerator)
ButtonGenerate.place(relx=0.10, rely=0.60)

DeleteButton = tk.Button(root, text="Delete", padx=20, font=40, height=1, command=Delete_Label)
DeleteButton.place(relx=0.4, rely=0.60)

PasswordLabel = tk.Label(root, text="Press Generate").place(relx=0.35, rely=0)

copyButton = tk.Button(root, text="CopyToClipboard", font=40, command=copy_to_clipboard())
copyButton.place(relx=0.65, rely=0.60)


# PasswordEntry = tk.Entry(root, width=25)
# PasswordEntry.place(relx=0.25, rely=0.25)

root.mainloop()
