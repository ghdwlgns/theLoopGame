import pygame
import sys

from events.TimeLoop import TimeLoop
from objects.Door import Door
from objects.Item import Item
from objects.Key import Key
from objects.MessageBox import MessageBox
from objects.Player import Player


def main():
    pygame.init()

    width, height = 700, 500
    screen = pygame.display.set_mode((width, height))

    player = Player(width // 2, height // 2)
    message_box = MessageBox()
    key = Key("Key", "Sample")
    cake = Door(width - 16, height // 2, "assets/cake.png", key, "Cake")

    timer_interval = 30 * 1000
    pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    time_loop = TimeLoop()

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
                elif event.key == pygame.K_e:
                    if player.rect.colliderect(cake.rect):
                        cake.interact(player=player, message_box=message_box)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    key_states["up"] = False
                elif event.key == pygame.K_DOWN:
                    key_states["down"] = False
                elif event.key == pygame.K_LEFT:
                    key_states["left"] = False
                elif event.key == pygame.K_RIGHT:
                    key_states["right"] = False
            elif event.type == pygame.USEREVENT:
                saved_state = time_loop.save_state(player, [cake])
                print("State saved..")
                pygame.time.delay(1000)
                time_loop.load_state(player, [cake], saved_state)
                print("State loaded..")

        direction_x = key_states["right"] - key_states["left"]
        direction_y = key_states["up"] - key_states["down"]

        if direction_x or direction_y:
            player.start_moving(direction_x, direction_y)
        else:
            player.stop_moving()

        player.update()

        screen.fill((255, 255, 255))
        player.draw(screen)
        cake.draw(screen)

        message_box.update("안녕하세요!")
        message_box.draw(screen)
        pygame.display.flip()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
