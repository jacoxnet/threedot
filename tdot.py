import pygame
from pygame.locals import *

from board import Board
from constants import SIZE
FPS = 30

def three_dots(game_map):
    the_moves = {"U": "↑", "D": "↓", "L": "←", "R": "→"}
    board = Board(game_map)
    WIN = pygame.display.set_mode((board.cols * SIZE, board.rows * SIZE))
    pygame.display.set_caption("Three Dots")
    run = True
    clock = pygame.time.Clock()
    board.draw(WIN)
    
    while run:    
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("got up")
                    board.move(the_moves["U"])
                elif event.key == pygame.K_DOWN:
                    print("got down")
                    board.move(the_moves["D"])
                elif event.key == pygame.K_RIGHT:
                    print("got right")
                    board.move(the_moves["R"])
                elif event.key == pygame.K_LEFT:
                    print("got left")
                    board.move(the_moves["L"])
                else:
                    pass
        board.draw(WIN)
        pygame.display.update()
    pygame.quit()


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

for game_map in game_maps:
    print(three_dots(game_map))