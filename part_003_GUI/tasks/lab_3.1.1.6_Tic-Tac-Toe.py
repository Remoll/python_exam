import tkinter as tk
from tkinter import messagebox
from random import randrange

PLAYER_SYMBOL = "O"
COMPUTER_SYMBOL = "X"

board = (
    {"x":0, "y":0, "symbol":"", "button": None},
    {"x":1, "y":0, "symbol":"", "button": None},
    {"x":2, "y":0, "symbol":"", "button": None},
    {"x":0, "y":1, "symbol":"", "button": None},
    {"x":1, "y":1, "symbol":"", "button": None},
    {"x":2, "y":1, "symbol":"", "button": None},
    {"x":0, "y":2, "symbol":"", "button": None},
    {"x":1, "y":2, "symbol":"", "button": None},
    {"x":2, "y":2, "symbol":"", "button": None},
)


def check_win_result(side: str) -> bool:
    diagonal_wins_cords = (
        ({"x":0, "y":0}, {"x":1, "y":1}, {"x":2,"y":2}),
        ({"x":0, "y":2}, {"x":1, "y":1}, {"x":2,"y":0})
    )

    # fix it
    for i in diagonal_wins_cords:
        tiles = []
        for cord in i:
            tile = list(filter(lambda tile : tile["x"] == cord["x"] and tile["y"] == cord["y"] and tile["symbol"] == side, board))
            print(tile)
            if len(tile) == 1:
                tiles.append(tile[0])
        if len(tiles) == 3:
            return True

    for i in range(3):
        row = list(filter(lambda tile : tile["x"] == i and tile["symbol"] == side, board))
        if len(row) == 3:
            return True
        column = list(filter(lambda tile : tile["y"] == i and tile["symbol"] == side, board))
        if len(column) == 3:
            return True
        
    return False


def player_move(x, y):
    selected_tile = next(
        tile for tile in board
        if tile["x"] == x and tile["y"] == y
    )

    if selected_tile["symbol"] != "":
        return
    
    selected_tile["symbol"] = PLAYER_SYMBOL
    selected_tile["button"].config(fg="green")
    selected_tile["button"].config(text=PLAYER_SYMBOL)


def enemy_move():
    aviable_tiles = list(filter(lambda tile : tile["symbol"] == "", board))

    random_index = randrange(0, len(aviable_tiles) - 1, 1)

    selected_tile = aviable_tiles[random_index]

    board_tile_to_mark = next(
        tile for tile in board
        if tile["x"] == selected_tile["x"] and tile["y"] == selected_tile["y"]
    )

    board_tile_to_mark["symbol"] = COMPUTER_SYMBOL
    board_tile_to_mark["button"].config(fg="red")
    board_tile_to_mark["button"].config(text=COMPUTER_SYMBOL)
    

def on_btn_click(x, y):
    player_move(x, y)
    have_player_win = check_win_result(PLAYER_SYMBOL)
    if have_player_win:
        messagebox.showwarning(title="GAME OVER", message="PLAYER HAVE WIN")
        return
    
    enemy_move()
    have_enemy_win = check_win_result(COMPUTER_SYMBOL)
    if have_enemy_win:
        messagebox.showwarning(title="GAME OVER", message="ENEMY HAVE WIN")
        return



wnd = tk.Tk()
wnd.title("TicTacToe")

for cord in board:
    button = tk.Button(wnd, text="", width=4, height=2, font=("Times", "25", "bold"))
    cord["button"] = button
    button.bind("<Button-1>", lambda *args, x=cord["x"], y=cord["y"]: on_btn_click(x,y))
    button.grid(row=cord["x"], column=cord["y"])

wnd.mainloop()