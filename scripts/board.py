import random


def draw(_board):
    line = '-'
    print('   ', end=' ')
    for i in range(width):
        print('  ' + str(i), end= ' ')
        
        line = line + '----'
    line = '    ' + line
    print('\n')
    print(line)
    
    for y in range(width):
        print(y, '  |', end=' ')
        for x in range(width):
            
            if _board[x][y] == None or _board[x][y] == 'somethingFFKJFK':
                print(' ' + ' |', end=' ')
            else:
                print(str(_board[x][y]) + ' |', end=' ')
        print('\n' + line)

def firstplay(x_input, y_input):

    # 1. set tile to found
    board[x_input][y_input] = 0

    # 2. find neightbours and set them to found
    neighbors = find_neighbors(x_input, y_input, 'all')
    for neighbor in neighbors:
        board[neighbor[0]][neighbor[1]] = 0
        found.append((neighbor[1],neighbor[0]))
    # 3. place mines

    zero_positions = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == None]
    mines = random.sample(zero_positions, amount_mines)
    for pos in mines:
        board[pos[0]][pos[1]] = 'M'
        values[pos[0]][pos[1]] = 'M'
    
    # 4. determine values

    for i in range(width):
        for j in range(width):
            value = 0
            n = find_neighbors(i, j, 'all')
            for cell in n:
                if board[cell[0]][cell[1]] == 'M' and board[i][j] != 'M':
                    value += 1

            if values[i][j] != 'M':
                values[i][j] = value

    check_expansion()
    
def check_expansion():
    # 5. check expansion main island

    for found_tile in found:
        neighbor = find_neighbors(found_tile[0], found_tile[1], 'cross')
        for n in neighbor: # neighbor from CROSS
            if board[n[0]][n[1]] != 0 and board[n[0]][n[1]] != 'M' and  values[n[0]][n[1]] == 0:
                board[n[0]][n[1]] = 0
                found.append((n[0], n[1]))
    
    # 6. check expansion expand 
    
    for found_tile in found.copy():
        neighbor = find_neighbors(found_tile[0], found_tile[1], 'cross')
        for n in neighbor:
            board[n[0]][n[1]] = 0
            found.append((n[0], n[1]))


def find_neighbors(x, y, patern):
    neighbors = []

    if patern == 'all':
        for r in range(y - 1, y + 2):
                for c in range(x - 1, x + 2):
                    if is_in_bounds(r, c) and (c, r) != (x, y):
                        neighbors.append((c, r))

    if patern == "cross":
        for r in range(y - 1, y + 2):
            for c in range(x - 1, x + 2):
                if is_in_bounds(r, c) and (c, r) != (x, y):
                    if (abs(y - r) + abs(x -c)) == 1:
                        neighbors.append((c, r))

    return neighbors

def is_in_bounds(row, col):
    return 0 <= row < width and 0 <= col < width
width = int(input('Choose the width of the board: '))
amount_mines = int(input('Choose the number of mines: '))
board = [[None]  * width for _ in range(width)]
values = [[None]  * width for _ in range(width)]
found = []
while True: 
        
    draw(board)
    draw(values)
    x_input = int(input('x:'))
    y_input = int(input('y:'))
    if  0 <= x_input < width and 0 <= y_input < width:
        firstplay(y_input, x_input)
    
    else:
        print('not in list')
        quit()
        
    


    