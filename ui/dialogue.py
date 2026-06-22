import pygame

def draw_dialogue(screen, text):

    font = pygame.font.SysFont(None, 32)

    pygame.draw.rect(
        screen,
        (20,20,20),
        (50,500,900,150)
    )

    pygame.draw.rect(
        screen,
        (255,255,255),
        (50,500,900,150),
        3
    )

    surface = font.render(
        text,
        True,
        (255,255,255)
    )

    screen.blit(
        surface,
        (80,550)
    )