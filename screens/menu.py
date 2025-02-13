import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 60)
        self.button_font = pygame.font.Font(None, 50)
        self.default_size = (300, 50)
        self.hover_size = (280, 45)
        self.button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, *self.default_size)

    def draw(self, hovered=False):
        self.screen.fill(BLACK)

        title_text = self.font.render("ARKANOID", True, (255, 174, 185))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        self.screen.blit(title_text, title_rect)

        if hovered:
            button_size = self.hover_size
        else:
            button_size = self.default_size

        self.button_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_size[0] // 2, SCREEN_HEIGHT // 2, *button_size)

        button_text = self.button_font.render("START GAME", True, BLACK)
        pygame.draw.rect(self.screen, (255, 174, 185), self.button_rect)
        self.screen.blit(button_text, button_text.get_rect(center=self.button_rect.center))

        pygame.display.flip()


    def wait_for_click(self):
        running = True

        while running:
            mouse_pos = pygame.mouse.get_pos()
            hovered = self.button_rect.collidepoint(mouse_pos)
            self.draw(hovered)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and hovered:
                    running = False
