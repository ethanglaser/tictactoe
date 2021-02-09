def displayGrid(info):
    print('   0 1 2')
    print('   _ _ _ ')
    print('  |' + info[0][0] + '|' + info[0][1] + '|' + info[0][2] + '|')
    print('0 |_|_|_|')
    print('  |' + info[1][0] + '|' + info[1][1] + '|' + info[1][2] + '|')
    print('1 |_|_|_|')
    print('  |' + info[2][0] + '|' + info[2][1] + '|' + info[2][2] + '|')
    print('2 |_|_|_|')


def player2input(info): 
    cord1 = input("player 2 where would you like to go on the grid below you must put a input between 0-2 and just the number a comma then the number")
    cord1 =  cord1.split(',')
    xcord1 = int(cord1[0])
    ycord1 = int(cord1[1])
    
    while info[xcord1][ycord1] == 'X' or info[xcord1][ycord1] == 'O':
        cord = input("player 2 you have put an input already used please do one not used beteen 0-2 with a comma inbetween")
        cord =  cord.split(',')
        xcord1 = int(cord[0])
        ycord1 = int(cord[1])
    
    
    info[xcord1][ycord1] = 'O' 
    displayGrid(info)

    return

def player1input(info): 
    cord = input("player 1 where would you like to go on the grid below you must put a input between 0-2 and just the number a comma then the number")
    cord =  cord.split(',')
    xcord = int(cord[0])
    ycord = int(cord[1])
    
    while info[xcord][ycord] == 'X' or info[xcord][ycord] == 'O':
        cord = input("player 2 you have put an input already used please do one not used beteen 0-2 with a comma inbetween")
        cord =  cord.split(',')
        xcord = int(cord[0])
        ycord = int(cord[1])


    
    
    info[xcord][ycord] = 'X' 
    displayGrid(info)
       
    
    return 




def game(info):
    turn = 0
    
    if turn == 10:
        winnerx(info)
        winnero(info)
        print('gamer over')

    while turn < 10:
        if turn % 2 == 0:
            player1input(info)
            winnerx(info)
        if turn % 2 == 1:
            player2input(info)
            winnero(info)





        turn =+1
    return

def winnerx(info):
    if info[0][0] == 'X' and info[0][1]== 'X' and info[0][2] == 'X' :
        print('Player 1 you have won')
    elif info[1][0] == 'X' and info[1][1] == 'X' and info[1][2] == 'X' :
        print('Player 1 you have won')
    elif info[2][0] == 'X' and info[2][1] == 'X' and info[2][2] == 'X' :
        print('Player 1 you have won')
    elif info[0][0] == 'X' and info[1][0] == 'X' and info[2][0] == 'X' :
        print('Player 1 you have won')
    elif info[0][1] == 'X' and info[1][1] == 'X' and info[2][1] == 'X' :
        print('Player 1 you have won')
    elif info[0][2] == 'X' and info[1][2] == 'X' and info[2][2] == 'X' :  
        print('Player 1 you have won')
    elif info[0][0] == 'X' and info[1][1] == 'X' and   info[2][2] == 'X' : 
        print('Player 1 you have won')
    elif info[2][0] == 'X' and info[1][1] == 'X' and info[0][2] == 'X':  
        print('Player 1 you have won')

def winnero(info):
    if info[0][0] == 'O' and info[0][1] == 'O' and info[0][2] == 'O' :
        print('Player 2 you have won')
    elif info[1][0] == 'O' and info[1][1] and info[1][2] == 'O' :
        print('Player 2 you have won')
    elif info[2][0] == 'O' and info[2][1] == 'O' and info[2][2] == 'O' :
        print('Player 2 you have won')
    elif info[0][0] == 'O' and info[1][0] == 'O' and info[2][0] == 'O' :
        print('Player 2 you have won')
    elif info[0][1] == 'O' and info[1][1] == 'O' and info[2][1] == 'O' :
        print('Player 2 you have won')
    elif info[0][2] == 'O' and info[1][2] == 'O' and info[2][2] == 'O' :  
        print('Player 2 you have won')
    elif info[0][0] == 'O' and info[1][1] == 'O' and info[2][2] == 'O' : 
        print('Player 2 you have won')
    elif info[2][0]== 'O' and info[1][1] == 'O' and info[0][2] == 'O':        
        print('Player 2 you have won')

   

if __name__ == "__main__":
    
    info = [[ ' ' , ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] 
    displayGrid(info)
    player1input(info)
    player2input(info)
    game(info)
    winnerx(info)
    winnero(info)

    

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
