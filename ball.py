import pygame
from settings import SCREEN_WIDTH

class Ball:
    def __init__(self, x, y, radius = 10):
        self.rect = pygame.Rect(x, y, radius * 2, radius * 2)
        self.speed_x = 3
        self.speed_y = -3
        self.speed_increase = 0.5
        self.max_speed = 10

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1

        if self.rect.top <= 0:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)

    def increase_speed(self):
        if abs(self.speed_x) < self.max_speed:
            self.speed_x += self.speed_increase if self.speed_x > 0 else -self.speed_increase
        if abs(self.speed_y) < self.max_speed:
            self.speed_y += self.speed_increase if self.speed_y > 0 else -self.speed_increase


