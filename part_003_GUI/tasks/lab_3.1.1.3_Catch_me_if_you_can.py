from tkinter import *
import random

def placed_btn_randomly(*arg):
    global button
    BUTTON_WIDTH = 70
    BUTTON_HEIGTH = 30

    x = random.randint(0, 500 - BUTTON_WIDTH)
    y = random.randint(0, 500 - BUTTON_HEIGTH)
    
    button.place(x=x, y=y, width=BUTTON_WIDTH, height=BUTTON_HEIGTH)

window = Tk()

window.geometry("500x500")
window.resizable(width=False, height=False)

button = Button(window, text="Catch me!")
button.bind("<Enter>", placed_btn_randomly)
placed_btn_randomly()

window.mainloop()
