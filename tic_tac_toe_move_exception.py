# Your exception here

class GameException(Exception):
    "Raised when user try to penetrate the game in different ways"
    pass

number = 1

try:
    choice = int(input(f'select the cell number to put your mark on: '))
    if choice < number or choice > 9:
        raise IndexError

except IndexError:
    print("Invalid cell number, please choose only from 1 to 9")




