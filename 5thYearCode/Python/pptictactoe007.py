game = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
def game_board(player=0, row=0, column=0, just_display=False):
    print("    A  B  C")
    if not just_display:
           game[row][column] = player
    for count, row in enumerate(game):       #this will cause each row to print out for x and o's
        print(count, row)
game_board(just_display=True)
game_board(1,1,1)
game_board(7,2,1)
game_board(2, 0, 0)
game_board(just_display=True)