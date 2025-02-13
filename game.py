import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BRICK_ROWS, BRICK_COLUMNS, FPS, BLACK
from paddle import Paddle
from ball import Ball
from brick import Brick
from score import Score
from game_over import GameOverScreen
from win_screen import WinScreen

class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Arkanoid")
        self.clock = pygame.time.Clock()

        self.paddle = Paddle(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 30)
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.bricks = self.create_bricks()
        self.score = Score()
        self.next_speed_increase = 80

    def create_bricks(self):
        bricks = []
        brick_width = SCREEN_WIDTH // BRICK_COLUMNS
        brick_height = 30
        brick_spacing = 5

        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLUMNS):
                x = col * brick_width + brick_spacing // 2
                y = row * (brick_height + brick_spacing) + 50
                bricks.append(Brick(x, y, brick_width - brick_spacing, brick_height))

        return bricks

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        if all(brick.destroyed for brick in self.bricks):
            win_screen = WinScreen(self.screen, self.score.score)
            action = win_screen.wait_for_click()
        else:
            game_over_screen = GameOverScreen(self.screen, self.score.score)
            action = game_over_screen.wait_for_click()

        if action == "restart":
            self.__init__()
            self.run()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.paddle.move(keys)
        self.ball.move()

        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.speed_y *= -1

        for brick in self.bricks:
            if not brick.destroyed and self.ball.rect.colliderect(brick.rect):
                brick.destroyed = True
                self.ball.speed_y *= -1
                self.score.add_points(10)

        if self.score.score >= self.next_speed_increase:
            self.ball.increase_speed()
            self.next_speed_increase += 80

        if self.ball.rect.bottom > SCREEN_HEIGHT:
            self.running = False

        if all(brick.destroyed for brick in self.bricks):
            self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        for brick in self.bricks:
            brick.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.flip()