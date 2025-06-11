import pygame
from enum import Enum
from .constants import RED, GREEN, YELLOW, GRAY, BWIDTH, BHEIGHT, SQSIZE, SQPADDING
from board import Board

class DisplayBoard:
    def __init__(self, board: Board):
        pygame.init()
        self.board = board
        self.width = BWIDTH * SQSIZE
        self.height = BHEIGHT * SQSIZE
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Three Dot")
        self.win.fill(GRAY)
        
    def draw_board(self):
        for row in range(BHEIGHT):
            for col in range(BWIDTH):
                x = col * SQSIZE + SQPADDING // 2
                y = row * SQSIZE + SQPADDING // 2
                pygame.draw.rect(self.win, WHITE, (x, y, SQSIZE - SQPADDING, SQSIZE - SQPADDING))
                pygame.draw.rect(self.win, BLACK, (x, y, SQSIZE - SQPADDING, SQSIZE - SQPADDING), 1)    

class Piece:

    class PieceType(Enum):
        REGULAR = 1
        OBSTACLE = 2
        TARGET = 3
    
    def __init__(self, row, col, color, type):
        self.row = row
        self.col = col
        self.color = color
        self.type = type
        
    def draw_piece(self, win):
        radius = SQSIZE // 2 - self.PADDING 
        if self.type == self.PieceType.REGULAR:    
            pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        elif self.type == self.PieceType.TARGET: 
            pygame.draw.circle(win, self.color, (self.x, self.y), radius)
            pygame.draw.circle(win, GRAY, (self.x, self.y), radius // 2)
        elif self.type == self.PieceType.OBSTACLE:
            pygame.draw.rect(win, GRAY, (self.x - SQSIZE // 2, self.y - SQSIZE // 2, SQSIZE, SQSIZE))
        
    def __repr__(self):
        return str(self.color)