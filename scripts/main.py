import pygame
import random
import math
class Main():
    def __init__(self):
        self.width = 500
        self.height = 500
        self.tiles = 100
        self.tiles_w = int(math.sqrt(self.tiles))
        self.atlas = pygame.transform.scale(pygame.image.load('texture_atlas.png'), (200,200)) 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('MineSweeper')
        self.clock = pygame.time.Clock()
        self.board = [[0] * 10 for _ in range(10)]
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
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN: # x,y (59,39)
                x_pos, y_pos = pygame.mouse.get_pos()
                x_grid, y_grid = math.floor(x_pos/50), math.floor(y_pos/50)
                if self.first_tile == False:
                    self.create_board(x_grid, y_grid)
                    self.first_tile = True
                

    def new(self):
        pass
    def create_board(self, first_tile_x, first_tile_y):

        self.board[first_tile_y][first_tile_x] = 'found'
        # make 8 tiles around also found
        self.board[first_tile_y][first_tile_x + 1] = 'found'
        self.board[first_tile_y][first_tile_x - 1] = 'found'
        
        self.board[first_tile_y - 1][first_tile_x] = 'found'
        self.board[first_tile_y - 1][first_tile_x + 1] = 'found'
        self.board[first_tile_y - 1][first_tile_x - 1] = 'found'

        self.board[first_tile_y + 1][first_tile_x] = 'found'
        self.board[first_tile_y + 1][first_tile_x + 1] = 'found'
        self.board[first_tile_y + 1][first_tile_x - 1] = 'found'

        # Get the indices of all the zeros
        zero_positions = [(i, j) for i in range(len(self.board)) for j in range(len(self.board[i])) if self.board[i][j] == 0]

        # Randomly select 10 unique positions
        bombs = random.sample(zero_positions, 10)

        # Replace the selected positions with 5
        for pos in bombs:
            self.board[pos[0]][pos[1]] = 'bomb'
            
    def crop(self, item):
        if isinstance(item, int):
            if item == 0:
                return (50,100,50,50)
            elif item <= 3:
                return (50*item,0,50, 50)
            elif item <= 7:
                return (50*(item-4),50,50,50)
            elif item == 8:
                return (0,100,50,50)
        else:
            if item == 'flag':
                return (100,100,50,50)
            elif item == 'bomb':
                return (0,150,50,50)
            elif item == 'found':
                return(0,0,50,50)

                

        
    def draw(self):
        self.screen.fill((225,225,225))
        for i in range(self.tiles_w):
            for j in range(self.tiles_w):
                self.screen.blit(self.atlas, (50*i,50*j), self.crop(self.board[j][i]))
        




main = Main()
if __name__ == "__main__":
    main.new()
    main.run()