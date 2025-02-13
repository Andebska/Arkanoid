import pygame

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE

class GameOverScreen:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.font = pygame.font.Font(None, 50)
        self.button_font = pygame.font.Font(None, 40)

        self.default_size = (300, 50)
        self.hover_size = (280, 45)

        self.try_again_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, *self.default_size)
        self.exit_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 70, *self.default_size)

    def draw(self, hovered_try_again=False, hovered_exit=False):
        self.screen.fill(BLACK)

        game_over_text = self.font.render("GAME OVER", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        self.screen.blit(game_over_text, game_over_rect)

        score_text = self.button_font.render(f"Your score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(score_text, score_rect)

        try_again_size = self.hover_size if hovered_try_again else self.default_size
        self.try_again_rect = pygame.Rect(SCREEN_WIDTH // 2 - try_again_size[0] // 2, SCREEN_HEIGHT // 2, *try_again_size)
        pygame.draw.rect(self.screen, WHITE, self.try_again_rect)
        try_again_text = self.button_font.render("TRY AGAIN", True, BLACK)
        self.screen.blit(try_again_text, try_again_text.get_rect(center=self.try_again_rect.center))

        exit_size = self.hover_size if hovered_exit else self.default_size
        self.exit_rect = pygame.Rect(SCREEN_WIDTH // 2 - exit_size[0] // 2, SCREEN_HEIGHT // 2 + 70, *exit_size)
        pygame.draw.rect(self.screen, WHITE, self.exit_rect)
        exit_text = self.button_font.render("EXIT", True, BLACK)
        self.screen.blit(exit_text, exit_text.get_rect(center=self.exit_rect.center))

        pygame.display.flip()

    def wait_for_click(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            hovered_try_again = self.try_again_rect.collidepoint(mouse_pos)
            hovered_exit = self.exit_rect.collidepoint(mouse_pos)

            self.draw(hovered_try_again, hovered_exit)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hovered_try_again:
                        return "restart"
                    if hovered_exit:
                        pygame.quit()
                        exit()

