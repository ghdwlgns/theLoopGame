import pygame
import sys

from object.MessageBox import MessageBox
from object.Player import Player


def main():
    pygame.init()

    width, height = 700, 500
    screen = pygame.display.set_mode((width, height))

    character = Player(width // 2, height // 2)
    message_box = MessageBox()

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
        character.draw(screen)

        message_box.update("안녕하세요!")
        message_box.draw(screen)
        pygame.display.flip()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
