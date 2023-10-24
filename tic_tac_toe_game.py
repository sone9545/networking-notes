from tic_tac_toe_model import Board, Player
import random
# Your game here
board = Board()
player1 = Player("user", "O")
player2 = Player("computer", "X")

who_first = [player1, player2]
current_player = random.choice(who_first)

def print_header():
        print('Tic-Tac-Toe game!')

def interface():
    #interface of the game
    print_header()
    board.display()
    print(f"the current player is {current_player.name} with mark {current_player.token}")

while board.game_is_ongoing():
    interface()
    
    choice = int(input(f'select the cell number to put your mark on: '))
    
    board.mark(choice, current_player.token)

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1
          
    winner =  board.status_winner(current_player.token) 

    if winner:
        board.display()
        print(f"congratulations {current_player}, you are the winner!")
        break
    
    if board.is_board_filled():
        board.display()
        print("tie game!")
        break


# how the game is played e.g. random who goes first, computer random choice