from tkinter import Tk, Button, Canvas

CANVAS_WIDTH = 100
CANVAS_HEIGTH = 300

phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))

active_combination_index = 0

def draw_ligths():
    ovals_cords = (
        {"x0":20, "y0":20, "x1":80, "y1":80, "color":"red"},
        {"x0":20, "y0":120, "x1":80, "y1":180, "color":"yellow"},
        {"x0":20, "y0":220, "x1":80, "y1":280, "color":"green"},
    )

    for index, cord in enumerate(ovals_cords):
        color="#666666"

        if (phases[active_combination_index][index]):
            color=cord["color"]
        
        canvas.create_oval(cord["x0"], cord["y0"], cord["x1"], cord["y1"], fill=color)

def next_combination():
    global active_combination_index
    if active_combination_index == len(phases) - 1:
        active_combination_index = 0
    else:
        active_combination_index += 1
    draw_ligths()

def exit_app():
    window.destroy()

window = Tk()

canvas = Canvas(window, bg="gray", height=CANVAS_HEIGTH, width=CANVAS_WIDTH)
canvas.pack()
draw_ligths()

btn_next = Button(window, text="Next", command=next_combination)
btn_next.pack()

btn_exit = Button(window, text="Exit", command=exit_app)
btn_exit.pack()

window.mainloop()