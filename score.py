import pygame

class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 30)

    def add_points(self, points):
        self.score += points

    def draw(self, screen):
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(text, (10, 10))