import tkinter

def print_winner():
    global win
    global label
    if win is False:
        win = True
        label.config(text="Player "+current_player+" is the winner")

def switch_player():
    global current_player
    global label

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    label.config(text="Player : "+current_player)

def check_win(clicked_row, clicked_col):
    # check for row win
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]

        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # check for column win
    count = 0
    for i in range(3):
        current_button = buttons[clicked_col][i]

        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # check for diagonal win
    count = 0
    for i in range(3):
        current_button = buttons[i][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # check for reversed diagonal win
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    if win is False:
        # check for no winner
        count = 0
        for col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button['text'] == "X" or current_button['text'] == "O":
                    count += 1
        if count == 9:
            label.config(text="Neither team can win")

def place_symbol(row, column):
    if win is False:
        clicked_button = buttons[column][row]
        if clicked_button['text'] == "":
            clicked_button.config(text=current_player)

            check_win(row, column)

            if win is False:
                switch_player()

def draw_grid():
    global label
    label = tkinter.Label(root, font=("Arial", 20), text="Player : "+current_player)
    label.grid(row=0)

    frame = tkinter.Frame(root)
    frame.grid(row=1, column=0, padx=10, pady=10)
    
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                frame, font=("Arial", 50),
                width=4, height=1,
                command=lambda r=row, c=column: place_symbol(r, c)
                )
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

# vars

buttons = []
current_player = "X"
win = False
label = 0

# create root window
root = tkinter.Tk()

root.title("TicTacToe")
root.minsize(500, 500)

draw_grid()

root.mainloop()
