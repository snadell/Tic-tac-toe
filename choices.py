


def ask_player(mark):
    ''' Asks player where to place X or O mark, checks validity '''
    global board
    req = 'Choose where to place your: ' + mark
    while True:
        try:
            choice = int(raw_input(req))
        except ValueError:
            print("Sorry, please input a number between 1-9.")
            continue

        if choice not in range(1,10):
            print("Sorry, please input a number between 1-9.")
            continue

        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print "That space isn't empty!"
            continue
def player_choice(mark):
    global board,game_state,announce
    #Set game blank game announcement
    announce = ''
    #Get Player Input
    mark = str(mark)
    # Validate input
    ask_player(mark)

    #Check for player win
    if win_check(board,mark):
        clear_output()
        display_board()
        announce = mark +" wins! Congratulations"
        game_state = False
        
    
    #Show board
    clear_output()
    display_board()

    #Check for a tie 
    if full_board_check(board):
        announce = "Tie!"
        game_state = False
        
    return game_state,announce




