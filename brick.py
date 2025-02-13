import pygame

class Brick:
    def __init__(self, x, y, width=50, height=20, color = (255, 174, 185)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.destroyed = False

    def draw(self, screen):
        if not self.destroyed:
            pygame.draw.rect(screen, self.color, self.rect)