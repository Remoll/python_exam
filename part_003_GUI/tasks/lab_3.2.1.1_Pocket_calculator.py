import tkinter as tk

def print_error():
    change_value("    Error!")

def change_value(new_value):
    if len(new_value) > 10:
        print_error()
        return

    global confirmed_entry_value
    confirmed_entry_value = new_value
    entry_value.set(confirmed_entry_value)


def add_char_to_value(new_char: str):
    change_value(confirmed_entry_value + new_char)


def clear_value():
    change_value("")


def remove_last_char():
    change_value(confirmed_entry_value[:-1])


def toggle_sign():
    if len(confirmed_entry_value) > 0 and confirmed_entry_value[0] == "-":
        change_value(confirmed_entry_value[1:])
    else:
        change_value("-" + confirmed_entry_value)


def add_decimal_sign():
    if len(confirmed_entry_value) < 1 or "." in confirmed_entry_value:
        return
    change_value(confirmed_entry_value + ".")



def init_operation(operation_sign: str):
    if len(label_value.get()) > 0:
        if len(confirmed_entry_value) == 0 or confirmed_entry_value == "-":
            label_value.set(label_value.get()[:-1] + operation_sign)
            return
        if len(confirmed_entry_value) > 0 and confirmed_entry_value != "-":
            sum_values()

    label_value.set(confirmed_entry_value + operation_sign)
    change_value("")


def sum_values():
    if confirmed_entry_value == "-" or len(confirmed_entry_value) < 1 or len(label_value.get()) < 1:
        return
    
    first_value = label_value.get()

    first_number = float(first_value[:-1])
    sign = first_value[-1]
    second_number = float(confirmed_entry_value)

    sum = 0

    match sign:
        case "+":
            sum = first_number + second_number
        case "-":
            sum = first_number - second_number
        case "*":
            sum = first_number * second_number
        case "/":
            if (second_number == 0):
                print_error()
                return
            sum = first_number / second_number

    sum_decimal_part = str(sum).split(".")[1]
    sum_integer_part = str(sum).split(".")[0]

    sum_decimal_part_int = int(sum_decimal_part)

    if sum_decimal_part_int == 0:
        change_value(sum_integer_part)
        label_value.set("")
        return
    
    if len(str(sum)) > 10:
        if len(sum_integer_part) + 2 <= 10:
            visible_decimal_chars_number = 10 - 1 - len(sum_integer_part)
            visible_decimal_part = sum_decimal_part[:visible_decimal_chars_number]
            change_value(sum_integer_part + "." + visible_decimal_part)
            label_value.set("")
            return
        if len(sum_integer_part) <= 10:
            change_value(sum_integer_part)
            label_value.set("")
            return
    
    change_value(str(sum))
    label_value.set("")


buttons = (
    {"x":2, "y":0, "text":"7", "action":(lambda : add_char_to_value("7"))},
    {"x":2, "y":1, "text":"8", "action":(lambda : add_char_to_value("8"))},
    {"x":2, "y":2, "text":"9", "action":(lambda : add_char_to_value("9"))},
    {"x":2, "y":3, "text":"+", "action":(lambda : init_operation("+"))},
    {"x":2, "y":4, "text":"C", "action":clear_value},
    {"x":3, "y":0, "text":"4", "action":(lambda : add_char_to_value("4"))},
    {"x":3, "y":1, "text":"5", "action":(lambda : add_char_to_value("5"))},
    {"x":3, "y":2, "text":"6", "action":(lambda : add_char_to_value("6"))},
    {"x":3, "y":3, "text":"-", "action":(lambda : init_operation("-"))},
    {"x":3, "y":4, "text":"<[X]", "action":remove_last_char},
    {"x":4, "y":0, "text":"1", "action":(lambda : add_char_to_value("1"))},
    {"x":4, "y":1, "text":"2", "action":(lambda : add_char_to_value("2"))},
    {"x":4, "y":2, "text":"3", "action":(lambda : add_char_to_value("3"))},
    {"x":4, "y":3, "text":"*", "action":(lambda : init_operation("*"))},
    {"x":5, "y":0, "text":"+/-", "action":toggle_sign},
    {"x":5, "y":1, "text":"0", "action":(lambda : add_char_to_value("0"))},
    {"x":5, "y":2, "text":".", "action":add_decimal_sign},
    {"x":5, "y":3, "text":"/", "action":(lambda : init_operation("/"))},
    {"x":5, "y":4, "text":"=", "action":sum_values},
)

confirmed_entry_value = ""

def prevent_keyboard(*args):
    entry_value.set(confirmed_entry_value)

window = tk.Tk()

label_value = tk.StringVar(window)
label = tk.Label(textvariable=label_value)
label.grid(row=0, column=0, columnspan=5)

entry_value = tk.StringVar(window)
entry_value.trace("w", prevent_keyboard)

entry = tk.Entry(window, textvariable=entry_value)
entry.grid(row=1, column=0, columnspan=5)

for button in buttons:
    buttonElement = tk.Button(window, text=button["text"], command=button["action"])
    buttonElement.grid(row=button["x"], column=button["y"])

window.mainloop()