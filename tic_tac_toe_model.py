# Core game model here. Define your namedtuple to represent your game state.
# All functions should be pure i.e. no i/o, no global vars etc.

import random

class Board():
    def __init__(self):
        # how are we going to store the data --> box
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self): 
        #display current state of the board
        print(f'{self.cells[1]} | {self.cells[2]} | {self.cells[3]}')
        print("--+---+--")
        print(f'{self.cells[4]} | {self.cells[5]} | {self.cells[6]}')
        print("--+---+--")
        print(f'{self.cells[7]} | {self.cells[8]} | {self.cells[9]}')        

    #def start_game
    
    def check_cell(self, i: int):
        if  self.cells[i] == " ":
            return True            
        else:
            return False

    def mark(self, i: int, token: str):
        if self.check_cell(i):
            self.cells[i] = token
        else:
            print ("sorry, that cell is taken") # throw an exception

    def update_board(self, i: int):
        if not self.check_cell(i): # if that's not true
            self.display() 

    def is_board_filled(self):
        # conditions that game is not over: 1. board is not yet filled 
        for i in range(1, len(self.cells)):
            if self.check_cell(i): 
                return False
        return True
    
    def game_is_ongoing(self):
        return not self.is_board_filled()

    def status_winner(self, token) -> bool:
        # conditions that game is not over: 2. no player connects 3 in a row yet
        if self.cells[1] == token and self.cells[2] == token and self.cells[3] == token: #2.1.1 top row
            print("test 1")
            return True
        elif self.cells[4] == token and self.cells[5] == token and self.cells[6] == token: #2.1.2 middle row
            print("test 2")
            return True
        elif self.cells[7] == token and self.cells[8] == token and self.cells[9] == token: #2.1.3 bottom row
            return True
        elif self.cells[1] == token and self.cells[4] == token and self.cells[7] == token: #2.2.1 left column
            return True
        elif self.cells[2] == token and self.cells[5] == token and self.cells[8] == token: #2.2.2 mid column
            return True
        elif self.cells[3] == token and self.cells[6] == token and self.cells[9] == token: #2.2.3 right column
            return True
        elif self.cells[1] == token and self.cells[5] == token and self.cells[9] == token: #2.3.1 top left diagonal
            return True
        elif self.cells[3] == token and self.cells[5] == token and self.cells[7] == token: #2.3.2 top right diagonal
            return True
        else:
            return False            
            
# Exception, Raise, Try, Except

class Player():
    def __init__(self, name, token):
        self.name = name
        self.token = token







        
