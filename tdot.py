import pygame
from pygame.locals import *

from board import Board
from constants import SIZE, THE_MOVES
FPS = 2

def three_dots(game_map):    
    board = Board()
    pygame.init()
    time1 = pygame.time.get_ticks()
    board.read_in_board_string(game_map)
    time1 = pygame.time.get_ticks() - time1
    WIN = pygame.display.set_mode((board.cols * SIZE, board.rows * SIZE))
    pygame.display.set_caption("Three Dots")
    run = True
    clock = pygame.time.Clock()
    board.draw(WIN)
    pygame.display.update()
    time2 = pygame.time.get_ticks()
    solution = board.find_path()
    time2 = pygame.time.get_ticks() - time2
    print(solution)
    for m in solution:
        clock.tick(FPS)
        board.move(m)
        board.draw(WIN)
        pygame.display.update()        
    print (time1, "ms to read in ", time2, "ms to solve")
    input("press return")
    pygame.quit()


game_maps = ( 
            #   "+------------+\n"
            # + "|RGY         |\n"
            # + "|            |\n"
            # + "|     **     |\n"
            # + "|     **     |\n"
            # + "|            |\n"
            # + "|         rgy|\n"
            # + "+------------+",

            #   "+------------+\n"
            # + "|R           |\n"
            # + "|G           |\n"
            # + "|Y    **     |\n"
            # + "|     **    r|\n"
            # + "|           g|\n"
            # + "|           y|\n"
            # + "+------------+",

            #   "+------------+\n"
            # + "|R           |\n"
            # + "|G    **     |\n"
            # + "|Y    **     |\n"
            # + "|            |\n"
            # + "|     **    r|\n"
            # + "|     **    g|\n"
            # + "|           y|\n"
            # + "+------------+",

            #   "+------------+\n"
            # + "|R    *******|\n"
            # + "|G    *******|\n"
            # + "|Y    *******|\n"
            # + "|            |\n"
            # + "|           r|\n"
            # + "|******     g|\n"
            # + "|******     y|\n"
            # + "+------------+",

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
            + "+------------+" ,
            
              "+---------------+\n"
            + "|           * * |\n"
            + "| **  **    * * |\n"
            + "| **    * *    g|\n"
            + "|     *** *   r |\n"
            + "| Y     * *    y|\n"
            + "| RG            |\n"
            + "|               |\n"
            + "+---------------+" ,
            
              "+---------------+\n"
            + "|      g **     |\n"
            + "|   **   **     |\n"
            + "|   **yr **     |\n"
            + "| R      ** * * |\n"
            + "|  Y     ** * * |\n"
            + "| G             |\n"
            + "|               |\n"
            + "+---------------+\n"
            )

three_dots(game_maps[2])