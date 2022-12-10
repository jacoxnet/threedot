import pygame
from pygame.locals import *
import sys

pygame.init()
display = pygame.display.set_mode((300, 300))

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Key UP has been pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("Key UP has been released")