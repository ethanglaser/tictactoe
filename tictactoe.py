def displayGrid(info):
    print('   0 1 2')
    print('   _ _ _ ')
    print('  |' + info[0][0] + '|' + info[0][1] + '|' + info[0][2] + '|')
    print('0 |_|_|_|')
    print('  |' + info[1][0] + '|' + info[1][1] + '|' + info[1][2] + '|')
    print('1 |_|_|_|')
    print('  |' + info[2][0] + '|' + info[2][1] + '|' + info[2][2] + '|')
    print('2 |_|_|_|')


def newimput(info):
    where = input("Player 1, Where would you like to go?")
    where = where.split(",")
    xcord = int(where[0])
    ycord = int(where[1])
    info[xcord][ycord] = "x"
    displayGrid(info)


    return

def newimput2(info):
    where = input("Player 2, Where would you like to go?")
    where = where.split(",")
    xcord = int(where[0])
    ycord = int(where[1])
    info[xcord][ycord] = "o"
    displayGrid(info)

    return

if __name__ == "__main__":
    info = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] 
    displayGrid(info)
    for value in range(0,8):
        newimput(info)
        newimput2(info)
        displayGrid(info)