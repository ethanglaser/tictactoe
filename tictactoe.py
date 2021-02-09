def displayGrid(info):
    print('   0 1 2')
    print('   _ _ _ ')
    print('  |' + info[0][0] + '|' + info[0][1] + '|' + info[0][2] + '|')
    print('0 |_|_|_|')
    print('  |' + info[1][0] + '|' + info[1][1] + '|' + info[1][2] + '|')
    print('1 |_|_|_|')
    print('  |' + info[2][0] + '|' + info[2][1] + '|' + info[2][2] + '|')
    print('2 |_|_|_|')

def game():
    moves = 1
    while moves <= 9:
        if moves % 2 == 1:
            coords = input('Competitor 1 make your decicion in the name of Lithuania: ')
            splitcoords = coords.split(',')
            xcoord = int(splitcoords[0])
            ycoord = int(splitcoords[1])
            info[ycoord][xcoord] = 'X'
            displayGrid(info)
            moves += 1
        elif moves % 2 == 0:
            coords2 = input('Competitor 2 make your decision. You do not have the great Blessing of Lithuania: ')
            splitcoords2 = coords2.split(',')
            xcoord2 = int(splitcoords2[0])
            ycoord2 = int(splitcoords2[1])
            info[ycoord2][xcoord2] = 'O'
            displayGrid(info)

            moves += 1
        movesleft = 10 - moves
        print('Moves remaining:' , movesleft)
    if moves == 10:
        print('Joyous game. The great land of Lithuania congratulates the winner. The winner shall have a lifelong supply of plentiful green beans. The loser shall never be welcome in Lithuania.')

    return
    
    #process the input
    #check if the move is valid
    #update list, call displaygrid
    #check if player has 3 in a row
    


if __name__ == "__main__":
    info = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] 
    displayGrid(info)
    game()