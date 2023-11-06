import tkinter as tk
import random

available_fonts = ["Arial", "Helvetica", "Times", "Courier", "Verdana", "Comic Sans MS"]

def change_color():
    color = "#{:02x}{:02x}{:02x}".format(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    label.config(fg=color)

def change_font():
    new_font = random.choice(available_fonts)
    current_size = label.cget("font").split(" ")[1]
    label.config(font=(new_font, current_size))

root = tk.Tk()
root.title("Colour and Font Changer")
root.geometry("400x300")

label = tk.Label(root, text="Hello, World!", font=("Arial", 30))
label.pack(pady=20)

color_button = tk.Button(root, text="Change Color", command=change_color)
color_button.pack(side=tk.LEFT, padx=10)

font_button = tk.Button(root, text="Change Font", command=change_font)
font_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
