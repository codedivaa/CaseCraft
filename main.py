import pygame

from entities.player import Player
from entities.npc import NPC
from ui.dialogue import draw_dialogue
from cases.case_manager import CaseManager

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "CaseCraft"
)

clock = pygame.time.Clock()

font = pygame.font.SysFont(
    None,
    40
)

player = Player()

case_manager = CaseManager()

npcs = [

    NPC(
        300,
        300,
        "Bob",
        "I saw a red car outside."
    ),

    NPC(
        600,
        250,
        "Sarah",
        "The museum alarm was off."
    ),

    NPC(
        200,
        500,
        "Guard",
        "A man in black entered."
    ),

    NPC(
        700,
        500,
        "Owner",
        "The painting is priceless."
    )
]

current_dialogue = ""

clues_found = []

game_result = ""

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_e:

                for npc in npcs:

                    zone = npc.get_rect().inflate(
                        80,
                        80
                    )

                    if player.get_rect().colliderect(
                        zone
                    ):

                        current_dialogue = (
                            npc.name +
                            ": " +
                            npc.clue
                        )

                        if npc.clue not in clues_found:
                            clues_found.append(
                                npc.clue
                            )

            if event.key == pygame.K_SPACE:

                if len(clues_found) < 3:

                    game_result = (
                        "Need more clues!"
                    )

                else:

                    guess = "Guard"

                    if guess == case_manager.suspect:

                        game_result = (
                            "CASE SOLVED!"
                        )

                    else:

                        game_result = (
                            "WRONG SUSPECT!"
                        )

                if guess == case_manager.suspect:

                    game_result = (
                        "CASE SOLVED!"
                    )

                else:

                    game_result = (
                        "WRONG SUSPECT!"
                    )

    player.move()

    for npc in npcs:
        npc.update()

    screen.fill(
        (40,120,40)
    )

    title = font.render(
        "Case: Museum Theft",
        True,
        (255,255,255)
    )

    screen.blit(
        title,
        (20,20)
    )
    instructions = font.render(
        "WASD Move | E Talk | SPACE Solve",
        True,
        (255, 255, 255)
    )

    screen.blit(
        instructions,
        (20, 50)
    )

    player.draw(screen)

    for npc in npcs:
        npc.draw(screen)

    if current_dialogue:

        draw_dialogue(
            screen,
            current_dialogue
        )

    y = 80

    for clue in clues_found:

        clue_text = font.render(
            clue,
            True,
            (255,255,255)
        )

        screen.blit(
            clue_text,
            (20,y)
        )

        y += 30

    if game_result:

        result_text = font.render(
            game_result,
            True,
            (255,255,0)
        )

        screen.blit(
            result_text,
            (350,100)
        )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()