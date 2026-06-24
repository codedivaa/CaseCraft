import pygame

from entities.player import Player
from entities.npc import NPC
from ui.dialogue import draw_dialogue
from cases.case_manager import CaseManager

pygame.init()
pygame.mixer.init()

town_map = pygame.image.load(
    "assets/town.png"
)
pygame.mixer.music.load(
    "assets/audio/bg_music.mp3"
)
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
footstep_sound = pygame.mixer.Sound(
    "assets/audio/footstep.mp3"
)

talk_sound = pygame.mixer.Sound(
    "assets/audio/talk.mp3"
)

solved_sound = pygame.mixer.Sound(
    "assets/audio/solved.mp3"
)
WIDTH = 1000
HEIGHT = 700
dialogue_timer = 0

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
clue_data = case_manager.generate_clues()
npcs = [

    NPC(
        300,
        300,
        "Bob",
        clue_data["Bob"]
    ),

    NPC(
        600,
        250,
        "Sarah",
        clue_data["Sarah"]
    ),

    NPC(
        200,
        500,
        "Guard",
        clue_data["Guard"]
    ),

    NPC(
        700,
        500,
        "Owner",
        clue_data["Owner"]
    )
]

current_dialogue = ""
selected_suspect = ""
clues_found = []

game_result = ""

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Talk to NPCs
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

            # Select suspect
            if event.key == pygame.K_1:
                selected_suspect = "Bob"

            if event.key == pygame.K_2:
                selected_suspect = "Sarah"

            if event.key == pygame.K_3:
                selected_suspect = "Guard"

            if event.key == pygame.K_4:
                selected_suspect = "Owner"

            # Accuse suspect
            if event.key == pygame.K_SPACE:

                if selected_suspect == "":

                    game_result = (
                        "Select a suspect first!"
                    )

                elif selected_suspect == case_manager.suspect:

                    game_result = (
                        f"CASE SOLVED! {selected_suspect} did it!"
                    )

                else:

                    game_result = (
                        f"Wrong! {selected_suspect} is innocent."
                    )

    if dialogue_timer > 0:
        dialogue_timer -= 1

    if dialogue_timer == 0:
        current_dialogue = ""
    player.move()

    for npc in npcs:
        npc.update()

    for x in range(0, WIDTH, 32):
        for y in range(0, HEIGHT, 32):
            pygame.draw.rect(
                screen,
                (60, 170, 60),
                (x, y, 32, 32)
            )

    title = font.render(
        "Case: Museum Theft",
        True,
        (255,255,255)
    )
    suspect_text = font.render(
        f"Selected: {selected_suspect}",
        True,
        (255, 255, 0)
    )

    screen.blit(
        suspect_text,
        (20, 60)
    )
    scaled_map = pygame.transform.scale(
        town_map,
        (WIDTH, HEIGHT)
    )

    screen.blit(
        scaled_map,
        (0, 0)
    )
    pygame.draw.rect(
        screen,
        (120, 120, 120),
        (0, 300, 1000, 80)
    )
    pygame.draw.rect(
        screen,
        (80, 80, 80),
        (50, 100, 180, 120)
    )
    police_text = font.render(
        "POLICE",
        True,
        (255, 255, 255)
    )

    screen.blit(
        police_text,
        (80, 140)
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