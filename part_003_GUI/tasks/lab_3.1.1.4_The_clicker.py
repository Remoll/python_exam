import tkinter as tk
from random import randint

window = tk.Tk()

exist_numbers = set()

def is_number_smallest(number: int):
    for i in exist_numbers:
        if i < number:
            return False
    return True
    
is_couter_on = False

def count():
    timer.set(timer.get() + 1)
    global timeout_id
    timeout_id = timer_widget.after(1000, count)


def on_button_click(event):
    if event.widget.cget("state") == "disabled":
        return
    global is_couter_on
    global timeout_id
    if not is_couter_on:
        is_couter_on = True
        timeout_id = timer_widget.after(1000, count)
    number = event.widget.cget("text")
    if is_number_smallest(int(number)):
        event.widget.config(state="disabled")
        exist_numbers.remove(int(number))
        if len(exist_numbers) == 0:
            timer_widget.after_cancel(timeout_id)
    
def create_new_number_button(x,y):
    while True:
        random_number = randint(0, 1000)
        if random_number not in exist_numbers:
            exist_numbers.add(random_number)
            button = tk.Button(window, text=random_number)
            button.grid(row=x, column=y)
            button.bind("<Button-1>", on_button_click)
            break

for i in range(5):
    for j in range(5):
        create_new_number_button(i,j)

timer = tk.IntVar(window)
timer.set(0)

timer_widget = tk.Label(window, textvariable=timer)
timer_widget.grid(row=5, column=2)
    

window.mainloop()