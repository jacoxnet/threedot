import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT
import sys
from board import Board
from display import DisplayBoard
from game_maps import game_maps


PLAYGAME = 1

if __name__ == "__main__":
    # Initialize the game board
    pygame.init()
    pygame.display.set_caption("Three Dot Game")
    board = Board(game_maps[PLAYGAME])
    screen = DisplayBoard(board)
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            # check for presses of the arrow keys
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP:
                    print("Up key pressed")
                    board.move("↑")  # Move the pieces up
                elif event.key == K_DOWN:
                    print("Down key pressed")
                    board.move("↓")  # Move the pieces up
                elif event.key == K_LEFT:
                    print("Left key pressed")
                    board.move("←")  # Move the pieces up
                elif event.key == K_RIGHT:
                    print("Right key pressed")
                    board.move("→")  # Move the pieces up
                else:
                    print("Other key pressed")    
                    pass  # Do nothing
                screen.draw_board()
    pygame.quit()
    sys.exit()
the_game = game_maps[PLAYGAME]
