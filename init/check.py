
# coding: utf-8

# In[1]:

def win_check(board, player):
    ''' Check Horizontals,Verticals, and Diagonals for a win '''
    if (board[7]  ==  board[8] ==  board[9] == player) or         (board[4] ==  board[5] ==  board[6] == player) or         (board[1] ==  board[2] ==  board[3] == player) or         (board[7] ==  board[4] ==  board[1] == player) or         (board[8] ==  board[5] ==  board[2] == player) or         (board[9] ==  board[6] ==  board[3] == player) or         (board[1] ==  board[5] ==  board[9] == player) or         (board[3] ==  board[5] ==  board[7] == player):
        return True
    else:
        return False
def full_board_check(board):
    ''' Function to check if any remaining blanks are in the board '''
    if " " in board[1:]:
        return False
    else:
        return True


# In[ ]:




# In[ ]:



