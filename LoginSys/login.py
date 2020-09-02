import tkinter as tk
import time
"""
Main login system.
#355C7D
User&pass System + Login.
#ADD8E6

Things gained from this project.

Files.
Line.strip to read lines.

Strings:
If not varname <-- Check's if string is empty.

Lambda functions learn them.
can transfer variables from one to another(actually use.)
"""

"""
Work on registerUser.
"""
# Globals

# Backend.
def loginstatebutton():
    login.config(state='normal')
    register.config(state='normal')

def Invalid_window():
    window = tk.Toplevel(root)
    window.geometry("300x100")
    window.config(bg='#355C7D')

    # GUI's
    label = tk.Label(window, text="Invalid Credentials.", bg='#ADD8E6', fg="red")
    button = tk.Button(window, text='OK', height=1, width=10, bg='#ADD8E6', font=40, command=lambda: [window.destroy(), loginstatebutton()])
    button.place(relx=0.6, rely=0.5)
    label.place(relx=0.2, rely=0.2)
    window.mainloop()

def Login():
    login.config(state='disabled')
    register.config(state='disabled')
    line = 0
    entryUser = username.get()
    entryPass = password.get()
    # Checks if it's Empty.
    if not entryUser or not entryPass:
        return Invalid_window()
    with open(r'C:\Users#path', 'r') as users:
        with open(r'C:\Users#path', 'r') as pswr:
            for line1 in users:
                for line2 in pswr:
                    print("Line1: ", line1.strip())
                    print("Line2: ", line2)
                    if entryUser == line1.strip():
                        return after_registered()
    return Invalid_window()

def after_registered():
    """
    Would say somthing like:
    Succesfully registered in Green.
    then sleep for 1-2 sec then auto close.(use time module)
    """
    after = tk.Toplevel(root)
    after.resizable(False, False)
    after.config(bg="#355C7D")
    after.geometry("300x175")

    success = tk.Label(after, text="Successfully Registered", fg="#00ff00", font=20, bg="#355C7D")
    success.place(relx=0.20, rely=0.40)


def registeruser(register_user, register_password):
    """
    Bugs:
    Doesn't check if user is registered for example:
    sango is in users
    but a person using this program can use sango and then
    we would have 2 sangos in the users.txt.
    """
    username_registering = register_user.get() + "\n"
    password_registering = register_password.get() + "\n"
    print(username_registering)
    print(password_registering)
    with open(r'C:\Users#path', 'a') as users:
        with open(r'C:\Users#path', 'a') as pswr:
            users.write(username_registering)
            pswr.write(password_registering)

def registerstate():
    register.config(state='disabled')
    login.config(state='disabled')

def registerbackbutton():
    register.config(state='normal')
    login.config(state='normal')

def registerempty(register_users, register_passs):
    """
    Bug:
    Need to delete the empty lines when
    user is not inputting for register.
    """
    reg_user = register_users.get()
    reg_pass = register_passs.get()
    if not reg_user or not reg_pass:
        with open(r'C:\Users#path', 'w') as users:
            with open(r'C:\Users#path', 'w') as pswr:
                return Invalid_window()


def registerwindow():
    """
    When this window is opened.
    Login buttons must be disabled to be fully functional.
    """
    register = tk.Toplevel(root)
    register.geometry('275x200')
    register.config(bg="#355C7D")

    # GUI's
    register_button = tk.Button(register, text="REGISTER", bg="#ADD8E6", height=1, width=10, command=lambda: [registeruser(register_user, register_password), registerempty(register_user, register_password), after_registered()])
    register_user = tk.Entry(register, bg="#ADD8E6")
    register_password = tk.Entry(register, bg="#ADD8E6")
    register_user_label = tk.Label(register, bg="#ADD8E6", text="Username")
    register_pass_label = tk.Label(register, bg="#ADD8E6", text="Password")
    register_back_button = tk.Button(register, bg="#ADD8E6", text="Back", command=lambda: [registerbackbutton(), register.destroy()])

    # GUI's Config.
    register_button.place(relx=0.35, rely=0.7)
    register_user.place(relx=0.30, rely=0.2)
    register_password.place(relx=0.30, rely=0.4)
    register_user_label.place(relx=0.05, rely=0.2)
    register_pass_label.place(relx=0.05, rely=0.4)
    register_back_button.place(relx=0.05, rely=0.7)
    register.mainloop()


# Configuration.
root = tk.Tk()
root.title("Login system")
root.geometry("275x300")
root.resizable(False, False)
root.configure(bg='#355C7D')

# GUI's.
username = tk.Entry(root, bg='#ADD8E6')
password = tk.Entry(root, bg='#ADD8E6')
login = tk.Button(root, bg='#ADD8E6', height=1, width=13, text="Login", command=Login)
userlabel = tk.Label(root, text='username', bg='#355C7D')
passlabel = tk.Label(root, text='password', bg='#355C7D')
register = tk.Button(root, bg='#ADD8E6', height=1, width=13, text="Click me to register.", command=lambda: [registerwindow(), registerstate()])

# GUI Config.
username.place(relx=0.33, rely=0.25)
password.place(relx=0.33, rely=0.45)
login.place(relx=0.33, rely=0.65)
userlabel.place(relx=0.08, rely=0.25)
passlabel.place(relx=0.08, rely=0.45)
register.place(relx=0.33, rely=0.80)
root.mainloop()
