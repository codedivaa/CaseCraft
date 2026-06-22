import pygame

class Player:

    def __init__(self):
        self.x = 500
        self.y = 350
        self.speed = 5

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.speed

        if keys[pygame.K_s]:
            self.y += self.speed

        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (255,200,100),
            (self.x,self.y,32,32)
        )

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            32,
            32
        )