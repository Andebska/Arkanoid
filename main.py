import pygame
from game import Game
from menu import Menu
from settings import SCREEN_WIDTH,SCREEN_HEIGHT

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arkanoid")

menu = Menu(screen)
menu.wait_for_click()

game = Game()
game.run()

pygame.quit()