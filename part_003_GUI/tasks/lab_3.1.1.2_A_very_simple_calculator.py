from tkinter import *

from tkinter import *
from tkinter import messagebox

window = Tk()

def evaluate():
    try:
        number_1 = float(input_1_value.get())
    except ValueError as e:
        messagebox.showerror(title="ValueError", message="Wrong input value - provide valid int or float for both inputs: {}".format(e), )
        input_1.focus_set()
        return
    
    try:
        number_2 = float(input_2_value.get())
    except ValueError as e:
        messagebox.showerror(title="ValueError", message="Wrong input value - provide valid int or float for both inputs: {}".format(e))
        input_2.focus_set()
        return
        
    operation_value = operation.get()

    result = 0
    
    match operation_value:
        case "+":
            result = number_1 + number_2
        case "-":
            result = number_1 - number_2
        case "*":
            result = number_1 * number_2
        case "/":
            try:
                result = number_1 / number_2
            except ZeroDivisionError as e:
                messagebox.showerror(title="ZeroDivisionError", message=e)
                input_2.focus_set()
                return
    
    messagebox.showinfo("result", "{} {} {} = {}".format(input_1_value.get(), operation_value, input_2_value.get(), str(result)))


input_1_value = StringVar(window)
input_1 = Entry(window, textvariable=input_1_value)
input_1.grid(column=0, row=1, rowspan=2)

operation = StringVar(window)
operation.set("+")

plus = Radiobutton(window, text="+", variable=operation, value="+")
plus.grid(column=1, row=0)

minus = Radiobutton(window, text="-", variable=operation, value="-")
minus.grid(column=1, row=1)

razy = Radiobutton(window, text="*", variable=operation, value="*")
razy.grid(column=1, row=2)

podzielic = Radiobutton(window, text="/", variable=operation, value="/")
podzielic.grid(column=1, row=3)

input_2_value = StringVar(window)
input_2 = Entry(window, textvariable=input_2_value)
input_2.grid(column=2, row=1, rowspan=2)

calculate_btn = Button(window, text="Evaluate", command=evaluate)
calculate_btn.grid(column=1, row=4)

window.mainloop()
