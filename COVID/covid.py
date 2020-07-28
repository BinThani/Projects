import tkinter as tk
from PIL import Image, ImageTk
import requests

# Variables
HEIGHT = 700
WIDTH = 800

# API
def covid(country):
    url = "https://api.covid19api.com/countries"
    response = requests.get(url)
    response.json()

root = tk.Tk()

root.resizable(False, False) # X and Y Direction False for no resize

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#Background
background_image = tk.PhotoImage(file="covid.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0, relwidth=1, relheight=1)

# Above frame VVV

frame = tk.Frame(root, bg="#C1F2BD", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=40) # EntryWidget: Gets userInput.
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Info", font=40, command=lambda: covid(entry.get()))
button.place(relx=0.75, relheight=1, relwidth=0.25)

# Lower frame

lower_frame = tk.Frame(root, bg="#C1F2BD", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()

# TODO Get COVIDAPI
# TODO Commands for working buttons.
