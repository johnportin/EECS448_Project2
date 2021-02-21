from pygameInputHandler import *


# A board is a list of rows, and each row is a list of cells with either an 'X' (a battleship)
# or a blank ' '
board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

# We want to refer to columns by letter, but Python accesses lists by number. So we define
# a dictionary to translate letters to the corresponding number.
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
}

#Asking the user the total number of ships.
def ask_user_for_ship_number():
    ships = input("Input number of ships to place:")
    while ships not in "123456":
        print("Wrong number! It should be 1, 2, 3, 4, 5, or 6")
        ships = input("Input number of ships to place:")
    return ships

# By writing this as a function, we don't have to repeat it later. It's less code, it makes
# the rest easier to read, and if we improve this, we have to do it only once!
def ask_user_for_board_position():
    column = input("column (A to J):")
    while column not in "ABCDEFGHIJ":
        print("That column is wrong! It should be A, B, C, D, E, F, G, H, I, or J")
        column = input("column (A to J):")

    row = input("row (1 to 10):")
    while row not in "12345678910":
        print("That row is wrong! it should be 1, 2, 3, 4, 5, 6, 7, 8, 9, or 10")
        row = input("row (1 to 10):")

    # The code calling this function will receive the values listed in the return statement below
    # and it can assign it to variables
    return int(row) - 1, letters_to_numbers[column]

def ask_user_for_ship_orientation():
    orientation = input("Place ship left, right, up, down (L,R,U,D):")
    while orientation not in "LRUD":
        print("Wrong input! It should be L,R,U, or D")
        orientation = input("Place ship left, right, up, down (L,R,U,D):")
    return orientation

def print_board(board):
    # Show the board, one row at a time
    print("  A B C D E F G H I J")
    print(" +-+-+-+-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        print(" +-+-+-+-+-+-+-+-+-+-+")
        row_number = row_number + 1

# Now clear the screen, and the other player starts guessing
print("\n"*50)

guesses_board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

invalidPlacement=True

# Keep playing until we guess all the ships
def placement():

    # We want to loop for the number of battleships chosen by user
    global a
    global invalidPlacement
    a = ask_user_for_ship_number()
    for n in range(int(a)):
        # loop that asks again for ship position information if user attempts to place invalidly
        while invalidPlacement:
            print("Where do you want ship ", n + 1, "?")
            column_number = letters_to_numbers[getMouse()[0]]
            row_number = int(getMouse()[1]) - 1

            # Check that there are no repeats
            if board[row_number][column_number] == 'X':
                print("That spot already has a battleship in it!")

            orien(column_number, row_number, n)
            print(invalidPlacement)
        invalidPlacement=True
        print_board(board)
            # loop for spaces occupied for each ship. Sets up ships corresponding dimensions of ships and orientation

def orien(column_number, row_number, n):
    global invalidPlacement
    b = ask_user_for_ship_orientation()
    for i in range(n + 1):
        if (b == 'D'):
            if (row_number + n > 9):
                invalidPlacement = True
            else:
                invalidPlacement = False
                board[row_number + i][column_number] = 'X'
        elif (b == 'R'):
            if (column_number + n > 9):
                invalidPlacement = True
            else:
                invalidPlacement = False
                board[row_number][column_number + i] = 'X'
        elif (b == 'U'):
            if (row_number - n < 0):
                invalidPlacement = True
            else:
                invalidPlacement = False
                board[row_number - i][column_number] = 'X'
        elif (b == 'L'):
            if (column_number - n < 0):
                invalidPlacement = True
            else:
                invalidPlacement = False
                board[row_number][column_number - i] = 'X'
    if (invalidPlacement == True):
        print("Ship was placed out of bounds. Please try again.")

def guessing():
    #Array of only possible guess numbers
    guess_number = [1,3,6,10,15,21]
    i = 0
    guesses = guess_number[0]
    while i != int(a):
        guesses = guess_number[i]
        i += 1
    for n in range(guesses):
        print("Guess a battleship location")
        column_number = letters_to_numbers[getMouse()[0]]
        row_number = int(getMouse()[1]) - 1

        if guesses_board[row_number][column_number] != ' ':
            print("You have already guessed that place!")
            continue

        # Check that there are no repeats
        if board[row_number][column_number] == 'X':
            print("HIT!")
            guesses_board[row_number][column_number] = 'X'
            guesses = guesses + 1
        else:
            guesses_board[row_number][column_number] = '.'
            print("MISS!")

        print_board(guesses_board)
    print("GAME OVER!")

def run():
    placement()
    guessing()
