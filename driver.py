import pygame
from pygame.locals import *
import sys
from board import Board
from piece import DisplayBoard

PLAYGAME = 0

game_maps = ( "+------------+\n"
            + "|RGY         |\n"
            + "|            |\n"
            + "|     **     |\n"
            + "|     **     |\n"
            + "|            |\n"
            + "|         rgy|\n"
            + "+------------+",

                "+------------+\n"
            + "|R           |\n"
            + "|G           |\n"
            + "|Y    **     |\n"
            + "|     **    r|\n"
            + "|           g|\n"
            + "|           y|\n"
            + "+------------+",

                "+------------+\n"
            + "|R           |\n"
            + "|G    **     |\n"
            + "|Y    **     |\n"
            + "|            |\n"
            + "|     **    r|\n"
            + "|     **    g|\n"
            + "|           y|\n"
            + "+------------+",

                "+------------+\n"
            + "|R    *******|\n"
            + "|G    *******|\n"
            + "|Y    *******|\n"
            + "|            |\n"
            + "|           r|\n"
            + "|******     g|\n"
            + "|******     y|\n"
            + "+------------+",

                "+------------+\n"
            + "|R     ** ***|\n"
            + "|G     ** ***|\n"
            + "|Y           |\n"
            + "|            |\n"
            + "|            |\n"
            + "|            |\n"
            + "|           g|\n"
            + "|** ***     r|\n"
            + "|** ***     y|\n"
            + "+------------+" )

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

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
the_game = game_maps[PLAYGAME]
