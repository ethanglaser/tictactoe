
def displayGrid(info):
    print('   0 1 2')
    print('   _ _ _ ')
    print('  |' + info[0][0] + '|' + info[0][1] + '|' + info[0][2] + '|')
    print('0 |_|_|_|')
    print('  |' + info[1][0] + '|' + info[1][1] + '|' + info[1][2] + '|')
    print('1 |_|_|_|')
    print('  |' + info[2][0] + '|' + info[2][1] + '|' + info[2][2] + '|')
    print('2 |_|_|_|')
    print("ayo")



if __name__ == "__main__":
    info = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] 
    displayGrid(info)

    # Use the input() function to take in the choices of each player
    # ex: coordinates = input("Player 1, which coordinates would you like to place an X?")
    # Remember that all input comes in strings, use int() to convert to an integer
    # Check the array each move to see if there is a 3 in a row
    # Check the array to make sure each inputted coordinate is not already occupied






# Tic Tac Toe
# 2 players
# players take turns, one after the other
# 3x3 grid
# X's and O's
# Choose a space that hasn't already been chosen
# Aim is to get 3 in a row - vertical, horizontal, or diagonal
# Game ends when a player wins or all spaces are filled

# Code considerations
# need to get input (can assume both players on same computer)
# need to display the grid
# need to track whose turn it is
# need to determine if chosen space is open
# need to check if the game is over/if a player has won
# need to repeat this process if game not over
