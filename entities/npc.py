import pygame

class NPC:

    def __init__(self, x, y, name, clue):

        self.x = x
        self.y = y

        self.name = name
        self.clue = clue

        self.direction = 1

    def update(self):

        self.x += self.direction

        if self.x > 500:
            self.direction = -1

        if self.x < 250:
            self.direction = 1

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (180,100,255),
            (self.x, self.y, 32, 32)
        )

        font = pygame.font.SysFont(
            None,
            24
        )

        text = font.render(
            self.name,
            True,
            (255, 255, 255)
        )

        screen.blit(
            text,
            (self.x - 10, self.y - 20)
        )

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            32,
            32
        )