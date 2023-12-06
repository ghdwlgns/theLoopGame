import pygame
import sys

from drivers.Display import Display
from drivers.Joystick import Joystick
from objects.MessageBox import MessageBox
from objects.Player import Player


def main():
    pygame.init()
    Joystick()
    display = Display()
    display.init()

    width, height = 700, 500
    screen = pygame.display.set_mode((width, height))

    character = Player(width // 2, height // 2)
    message_box = MessageBox()

    key_states = {
        "up": False,
        "down": False,
        "left": False,
        "right": False
    }

    # 게임 루프
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    key_states["up"] = True
                elif event.key == pygame.K_DOWN:
                    key_states["down"] = True
                elif event.key == pygame.K_LEFT:
                    key_states["left"] = True
                elif event.key == pygame.K_RIGHT:
                    key_states["right"] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    key_states["up"] = False
                elif event.key == pygame.K_DOWN:
                    key_states["down"] = False
                elif event.key == pygame.K_LEFT:
                    key_states["left"] = False
                elif event.key == pygame.K_RIGHT:
                    key_states["right"] = False

        direction_x = key_states["right"] - key_states["left"]
        direction_y = key_states["up"] - key_states["down"]

        if direction_x or direction_y:
            character.start_moving(direction_x, direction_y)
        else:
            character.stop_moving()

        character.update()

        screen.fill((255, 255, 255))
        character.draw(screen)

        message_box.update("안녕하세요!")
        message_box.draw(screen)
        
        pygame.display.update()
        display.disp(screen)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
