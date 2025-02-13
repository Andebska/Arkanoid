import pygame
from pytk.util import center

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE

class WinScreen:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.font = pygame.font.Font(None, 50)
        self.button_font = pygame.font.Font(None, 40)

        self.trophy = pygame.image.load("trophy.png")
        self.trophy = pygame.transform.scale(self.trophy, (150, 150))
        self.trophy_rect = self.trophy.get_rect(center=(SCREEN_WIDTH // 2, 120))

        self.default_size = (300, 50)
        self.hover_size = (280, 45)

        self.play_again_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 20, *self.default_size)
        self.exit_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 90, *self.default_size)

    def draw(self, hovered_play_again=False, hovered_exit=False):
        self.screen.fill(BLACK)

        congrats_text = self.font.render("CONGRATULATIONS!", True, WHITE)
        congrats_rect = congrats_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
        self.screen.blit(congrats_text, congrats_rect)

        score_text = self.button_font.render(f"Your score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 -20))
        self.screen.blit(score_text, score_rect)

        self.screen.blit(self.trophy, self.trophy_rect)

        play_again_size = self.hover_size if hovered_play_again else self.default_size
        self.play_again_rect = pygame.Rect(SCREEN_WIDTH // 2 - play_again_size[0] // 2, SCREEN_HEIGHT // 2 + 30, *play_again_size)
        pygame.draw.rect(self.screen, WHITE, self.play_again_rect)
        try_again_text = self.button_font.render("PLAY AGAIN", True, BLACK)
        self.screen.blit(try_again_text, try_again_text.get_rect(center=self.play_again_rect.center))

        exit_size = self.hover_size if hovered_exit else self.default_size
        self.exit_rect = pygame.Rect(SCREEN_WIDTH // 2 - exit_size[0] // 2, SCREEN_HEIGHT // 2 + 100, *exit_size)
        pygame.draw.rect(self.screen, WHITE, self.exit_rect)
        exit_text = self.button_font.render("EXIT", True, BLACK)
        self.screen.blit(exit_text, exit_text.get_rect(center=self.exit_rect.center))

        pygame.display.flip()

    def wait_for_click(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            hovered_play_again = self.play_again_rect.collidepoint(mouse_pos)
            hovered_exit = self.exit_rect.collidepoint(mouse_pos)

            self.draw(hovered_play_again, hovered_exit)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hovered_play_again:
                        return "restart"
                    if hovered_exit:
                        pygame.quit()
                        exit()
