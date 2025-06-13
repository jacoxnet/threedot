import pygame
from constants import RED, GREEN, YELLOW, GRAY, WHITE, BLACK, SQSIZE, SQPADDING
from board import Board

class DisplayBoard:

    def __init__(self, board: Board):
        pygame.init()
        self.board = board
        self.width = board.cols * SQSIZE
        self.height = board.rows * SQSIZE
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Three Dot")
        self.win.fill(GRAY)
        self.draw_board()
        
    def draw_board(self):
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                x = col * SQSIZE + SQPADDING // 2
                y = row * SQSIZE + SQPADDING // 2
                pygame.draw.rect(self.win, WHITE, (x, y, SQSIZE - SQPADDING, SQSIZE - SQPADDING))
                pygame.draw.rect(self.win, BLACK, (x, y, SQSIZE - SQPADDING, SQSIZE - SQPADDING), 1)    
        for piece in self.board.map.keys():
            if piece in "RGYrgy":
                self.draw_piece(self, piece)
        
    def draw_piece(self, piece):
        radius = SQSIZE // 2 - self.PADDING 
        if piece in "RGY":
            pygame.draw.circle(self.win, self.color[piece], (self.x, self.y), radius)
        elif piece in "rgy":
            pygame.draw.circle(self.win, self.color[piece], (self.x, self.y), radius)
            pygame.draw.circle(self.win, GRAY, (self.x, self.y), radius // 2)
        elif piece == "*":
            # cycle through tuples in map for obstacles
            for item in self.board.map[piece]:
                pygame.draw.rect(self.win, GRAY, (item[0] - SQSIZE // 2, item[1] - SQSIZE // 2, SQSIZE, SQSIZE))
        
    def __repr__(self):
        return str(self.color)