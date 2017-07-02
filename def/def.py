


def play_game():
    reset_board()
    global announce
    
    # Set marks
    X='X'
    O='O'
    while True:
        # Show board
        clear_output()
        display_board()
        
        # Player X turn
        game_state,announce = player_choice(X)
        print announce
        if game_state == False:
            break
            
        
    
    
