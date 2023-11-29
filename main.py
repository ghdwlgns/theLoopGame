import pygame, sys
from pygame.locals import *

from object.Player import Player


def main():
    pygame.init()

    width, height = 700, 500
    screen = pygame.display.set_mode((width, height))
    background = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()

    character = Player(width // 2, height // 2)

    # 게임 루프
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    character.start_moving("up")
                elif event.key == pygame.K_DOWN:
                    character.start_moving("down")
                elif event.key == pygame.K_LEFT:
                    character.start_moving("left")
                elif event.key == pygame.K_RIGHT:
                    character.start_moving("right")
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    character.stop_moving()

        character.update()

        screen.fill((255, 255, 255))
        screen.blit(character.get_current_sprite(), (character.character_x, character.character_y))

        pygame.display.flip()

        clock.tick(5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
