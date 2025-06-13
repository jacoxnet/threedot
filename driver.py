import pygame
from pygame.locals import *
import sys
from board import Board
from display import DisplayBoard
from game_maps import game_maps


PLAYGAME = 0

if __name__ == "__main__":
    # Initialize the game board
    board = Board(game_maps[PLAYGAME])
    screen = DisplayBoard(board)
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False



    pygame.quit()
    sys.exit()
the_game = game_maps[PLAYGAME]
