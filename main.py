import pygame
import random
from Config import *
from Class import *
from network import *

win = pygame.display.set_mode((width, height))
pygame.display.set_caption(clientcaption)

clientNumber = 0

clock = pygame.time.Clock()

player1 = player(1200, win, path)
player1.newhand()

button1 = button(path + "Draw", 100, 100, win)

def main():
    run = True
    while run == True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            player1.event_handler(event)
            button1.event_handler(event, player1.drawcards)

        win.fill((255, 255, 255))
        player1.drawhand()
        button1.draw()
        clock.tick(120)
        pygame.display.update()

main()