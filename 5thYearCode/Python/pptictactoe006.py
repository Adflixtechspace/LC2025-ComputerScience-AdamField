game = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
def game_board():
    print("    A  B  C")
    for count, row in enumerate(game):       #this will cause each row to print out for x and o's
        print(count, row)
game_board()
game[0][1]=1
game_board()
game[2][2]=2
game_board()