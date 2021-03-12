"""
Game Logic Class begins intial game state as it receives user input and communicates to output handler.

"""
from pygameInputHandler import *
from pygameOutputHandler import pyBoard
outputHandler = pyBoard()

# A board is a list of rows, and each row is a list of cells with either an 'X' (a battleship)
# or a blank ' '
board1 = [
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
board2 = [
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
placementBoards = [board1, board2]

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

# Asking the user the total number of ships.
def ask_user_for_ship_number():
    """
     ask user for ship number
        * @pre: none
        * @post: returns a number of ships wanted by player
        * @param: none
        * @description: asks user for number of ships to use in game and checks if number is valid.
    """
    ships = input("Input number of ships to place:")
    while ships not in "123456":
        print("Wrong number! It should be 1, 2, 3, 4, 5, or 6")
        ships = input("Input number of ships to place:")
    return ships

# By writing this as a function, we don't have to repeat it later. It's less code, it makes
# the rest easier to read, and if we improve this, we have to do it only once!
def ask_user_for_board_position():
    '''
    ask user for board position
        * @pre: none
        * @post: returns a position
        * @param: none
        * @description: asks user for a position to place their ship. Checks if valid col & row. Returns column and row.
    '''
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
    '''
     ask user for ship orientation
        * @pre: none
        * @post: returns a direction of ship.
        * @param: none
        * @description: asks user for orientation. checks if its a valid direction (left, right, up, down)
    '''

    orientation = input("Place ship left, right, up, down (L,R,U,D):")
    while orientation not in "LRUD":
        print("Wrong input! It should be L,R,U, or D")
        orientation = input("Place ship left, right, up, down (L,R,U,D):")
    return orientation

def print_board(board):
    """
    print board
        * @pre: takes in player board
        * @post: prints board
        * @param: player's board must be taken called with function.
        * @description: uses board to print a visual board including lines, rows, cols,
    """
    # Show the board, one row at a time
    print("  A B C D E F G H I J")
    print(" +-+-+-+-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        print(" +-+-+-+-+-+-+-+-+-+-+")
        row_number = row_number + 1

# Now clear the screen, and the other player starts guessing
print("\n" * 50)

guesses_board1 = [
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
guesses_board2 = [
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
guessesBoards = [guesses_board1, guesses_board2]

invalidPlacement = True
player = 0
isShipsPlaced = False

def getNumShips():
    """
    getNumShips
            * @pre: None
            * @post: create global variable for number of ship
            * @param: None
            * @description: simply creates global variable for
            //number of ships that is the used in the placement
    """
    global a
    a = ask_user_for_ship_number()

# Keep playing until we guess all the ships
def placement():
    """
        placement
            * @pre: getNumShips is called
            * @post: makes sure all selected number of ships are placed in valid locaton.
            * @param: none
            * @description: function creates loop that runs untill all ships are placed.
    """
    global player
    global isShipsPlaced
    # We want to loop for the number of battleships chosen by user
    global invalidPlacement
    for n in range(int(a)):
        # loop that asks again for ship position information if user attempts to place invalidly
        while invalidPlacement:
            print("Where do you want ship ", n + 1, "?")
            column_number = letters_to_numbers[getMouse()[0]]
            row_number = int(getMouse()[1]) - 1

            # Check that there are no repeats
            if placementBoards[player][row_number][column_number] == 'X':
                print("That spot already has a battleship in it!")

            orientation(column_number, row_number, n)
        invalidPlacement = True
        print_board(placementBoards[player])
    if (player == 1):
        isShipsPlaced = True
    switchplayers()

# loop for spaces occupied for each ship. Sets up ships corresponding dimensions of ships and orientation
def orientation(column_number, row_number, n):
    """
    orientation
        * @pre: column number, row_number, n are passed as integers
        * @post: sets the mark 'X' for all cells the ship should occupy
        * @param: column number of the position clicked, row_number of the
            //position clicked, n is the number of the ship that is marked
        * @description: uses player variable to mark correct board. Loop for
            //spaces occupied for each ship to set dimentsions and based
            //on input for orientation fills cells the ship will occupy
    """
    global player
    global invalidPlacement
    b = ask_user_for_ship_orientation()
    for i in range(n + 1):
        if (b == 'D'):
            if (row_number + n > 9):
                invalidPlacement = True
            else:
                invalidPlacement = False
                placementBoards[player][row_number + i][column_number] = 'X'
        elif (b == 'R'):
            if (column_number + n > 9):
                invalidPlacement = True
            else:
                invalidPlacement = False
                placementBoards[player][row_number][column_number + i] = 'X'
        elif (b == 'U'):
            if (row_number - n < 0):
                invalidPlacement = True
            else:
                invalidPlacement = False
                placementBoards[player][row_number - i][column_number] = 'X'
        elif (b == 'L'):
            if (column_number - n < 0):
                invalidPlacement = True
            else:
                invalidPlacement = False
                placementBoards[player][row_number][column_number - i] = 'X'
    if (invalidPlacement == True):
        print("Ship was placed out of bounds. Please try again.")

def switchplayers():
    """
    switchplayers
            * @pre: None
            * @post: player variable is switched between 0 and 1 every time its called
            * @param: None
            * @description: Switches the global variable player and states which players turn it is.
                //different statement when placing and guessing
    """
    global isShipsPlaced
    global player
    if(not isShipsPlaced):
        print("Player 1 look away as Player 2 places ships")
    else:
        print("Player ",(player+1)," turn to guess")
    player = (player+1)%2

def guessing():
    """
    guessing
            * @pre: placement already called twice (ships need to be already
                //placed in placementBoard for both players
            * @post: fills guessingBoards for both players and properly exits
                //loop (GAME OVER) when all ships are sunk
            * @param: None
            * @description: updates the guessing boards for both players with
                //'.' for misses and 'X' for hits. Each guess checks if all
                //ship have been sunk for either player and exits guessing loop
                //when someone wins
    """
    #Array of only possible guess numbers
    guess_number = [1,3,6,10,15,21]
    i = 0
    guesses = guess_number[0]
    while i != int(a):
        guesses = guess_number[i]
        i += 1
    twoPlayerGuesses=[guesses,guesses]
    shipSpacesHit=[0,0]
    while (shipSpacesHit[0] != twoPlayerGuesses[0] and shipSpacesHit[1] != twoPlayerGuesses[1]):
        print("Guess a battleship location")
        column_number = letters_to_numbers[getMouse()[0]]
        row_number = int(getMouse()[1]) - 1

        if guessesBoards[player][row_number][column_number] != ' ':
            print("You have already guessed that place!")
            continue

        # Check that there are no repeats
        if placementBoards[player][row_number][column_number] == 'X':
            print("HIT!")
            guessesBoards[player][row_number][column_number] = 'X'
            if(player==0):
                shipSpacesHit[0]+=1
            else:
                shipSpacesHit[1] += 1

        else:
            guessesBoards[player][row_number][column_number] = '.'
            print("MISS!")

        print_board(guessesBoards[player])

        if(shipSpacesHit[0] != twoPlayerGuesses[0] and shipSpacesHit[1] != twoPlayerGuesses[1]):
            switchplayers()
    if(shipSpacesHit[0] == twoPlayerGuesses[0]):
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")
    print("GAME OVER!")


def run(setupPack):
    outputHandler.beginGame(setupPack)#Spawns Screen
    outputHandler.updateBoard("hit",player =1,coord = (1,1))


    
    #Call placement twice for both players
    getNumShips()
    placement()
    placement()
    guessing()
