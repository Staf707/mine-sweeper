import pygame
import random
import math
class Main():
    def __init__(self):
        self.width = 500
        self.height = 500
        self.tiles = 100
        self.bombs = 10
        self.tiles_w = int(math.sqrt(self.tiles))
        self.atlas = pygame.transform.scale(pygame.image.load('texture_atlas.png'), (200,200)) 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('MineSweeper')
        self.clock = pygame.time.Clock()
        self.board = [[None] * 10 for _ in range(10)]
        self.values = [[None] * 10 for _ in range(10)]
        self.found = []
        self.first_tile = False

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.draw()
            pygame.display.update()
        
        else:
            self.end_screen()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN: # x,y (59,39)
                x_pos, y_pos = pygame.mouse.get_pos()
                x_grid, y_grid = math.floor(x_pos/50), math.floor(y_pos/50)
                if self.first_tile == False:
                    self.create_board(x_grid, y_grid)
                    self.first_tile = True
                

    def new(self):
        pass
    def create_board(self, first_tile_x, first_tile_y):
        # 1. clicked tile
        self.board[first_tile_y][first_tile_x] = 0

        # 2. tiles around (safe zone)
        neighbors = self.neighbors(first_tile_x, first_tile_y, 'all')
        for n in neighbors:
            self.board[n[1]][n[0]] = 0
            self.found.append(n)
        print(neighbors)
    
        # 3. place bombs
        zero_positions = [(i, j) for i in range(len(self.board)) for j in range(len(self.board[i])) if self.board[i][j] == None]
        bombs = random.sample(zero_positions, self.bombs)
        for pos in bombs:
            self.board[pos[0]][pos[1]] = 'B'
        
        # 4. determine values
        for i in range(self.tiles_w):
            for j in range(self.tiles_w):
                value = 0
                n = self.neighbors(i, j, 'all')
                
                for cell in range((len(n))):
                    if self.board[n[cell][0]][n[cell][1]] == 'B' and self.board[i][j] != 'B':
                        value += 1
                    elif self.board[i][j] == 'B':
                        self.values[i][j] = 'B'
                if value != None:
                    self.values[i][j] = value

        # 5. change surounding cells
            for cell in self.found: # cell = found tile ex. tile (2,2)
                n = self.neighbors(cell[0], cell[1], 'cross') # neighbor (3,0)
                if n != []:
                    for z in n: # z = neighbor of found tile
                        if self.values[z[0]][z[1]] == None and z not in self.found:
                            self.board[z[0]][z[1]] = None
                            self.found.append(z)
        

                            
                    
                    

                
        print(self.board)
        print(self.values)        
                
        # 6. give outblocks numbers

            

        

    def is_in_bounds(self, row, col):
        return 0 <= row < self.tiles_w and 0 <= col < self.tiles_w

    def neighbors(self, x_pos, y_pos, patern): 
        neighbors = []  

        if patern == "all":
            for r in range(y_pos - 1, y_pos + 2):
                for c in range(x_pos - 1, x_pos + 2):
                    if self.is_in_bounds(r, c) and (r, c) != (x_pos, y_pos):
                        neighbors.append((c, r))
        if patern == "cross":
            for r in range(x_pos - 1, x_pos + 2):
                for c in range(y_pos - 1, y_pos + 2):
                    if self.is_in_bounds(r, c) and (r, c) != (x_pos, y_pos) and self.board[c][r] != None:
                        if r == x_pos or c == y_pos:
                            neighbors.append((c, r))
        
        return neighbors
        
    def crop(self, item):
        if isinstance(item, int):
            if item == 0:
                return (0,0, 50, 50)
            elif item <= 3:
                return (50*item,0,50, 50)
            elif item <= 7:
                return (50*(item-4),50,50,50)
            elif item == 8:
                return (0,100,50,50)
        else:
            if item == 'flag':
                return (100,100,50,50)
            elif item == 'B':
                return (0,150,50,50)
            elif item == None:
                return (50,100,50,50)
  
    def draw(self):
        self.screen.fill((225,225,225))
        for i in range(self.tiles_w):
            for j in range(self.tiles_w):
                self.screen.blit(self.atlas, (50*i,50*j), self.crop(self.board[j][i]))
        




main = Main()
if __name__ == "__main__":
    main.new()
    main.run()