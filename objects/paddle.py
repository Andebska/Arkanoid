import pygame
from settings import SCREEN_WIDTH

class Paddle:
    def __init__(self, x, y, width=100, height=10, speed=6):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (139, 126, 102), self.rect)
