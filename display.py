import pygame
from constants import RED, GREEN, YELLOW, GRAY, WHITE, BLACK, SQSIZE, SQPADDING
from board import Board

class DisplayBoard:

    def __init__(self, board: Board):
        self.board = board
        self.width = board.cols * SQSIZE
        self.height = board.rows * SQSIZE
        self.win = pygame.display.set_mode((self.width, self.height))
        self.win.fill(BLACK)
        self.draw_board()
        
        
    def draw_board(self):
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                x = col * SQSIZE + SQPADDING // 2
                y = row * SQSIZE + SQPADDING // 2
                pygame.draw.rect(self.win, GRAY, (x, y, SQSIZE - SQPADDING, SQSIZE - SQPADDING))
                pygame.draw.rect(self.win, BLACK, (x, y, SQSIZE - SQPADDING, SQSIZE - SQPADDING), width=2)    
        # first draw targets
        for piece in "rgy":
            self.draw_piece(piece)
        for piece in "RGY":
            self.draw_piece(piece)
        # next draw obstacles
        self.draw_piece("*")
        pygame.display.update()
        
    def draw_piece(self, piece):
        if piece in "RGYrgy":
            radius = SQSIZE // 2 - SQPADDING 
            center_x = self.board.get_piece(piece)[1] * SQSIZE + SQSIZE // 2
            center_y = self.board.get_piece(piece)[0] * SQSIZE + SQSIZE // 2
            pygame.draw.circle(self.win, self.board.get_color(piece), (center_x, center_y), radius)
            if piece in "rgy":
                pygame.draw.circle(self.win, WHITE, (center_x, center_y), radius - SQPADDING)
        elif piece == "*":
        # cycle through tuples in map for obstacles
            for item in self.board.map[piece]:
                x = item[1] * SQSIZE + (2 * SQPADDING)
                y = item[0] * SQSIZE + (2 * SQPADDING)
                pygame.draw.rect(self.win, BLACK, (x, y, SQSIZE - (4 * SQPADDING), SQSIZE - (4 * SQPADDING)))

        
    def __repr__(self):
        return str(self.board.map)