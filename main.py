import pygame
import sys

from events.TimeLoop import TimeLoop
from objects.Chest import Chest
from objects.Door import Door
from objects.Item import Item
from objects.Key import Key
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
    message_box = MessageBox(width - 650, height - 450)
    player = Player(width // 2, height // 2, message_box)

    key = Key("Key", "Sample")
    cake = Chest(width - 16, height // 2, "assets/cake.png", key, "Cake")

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
                    if not player.inventory_opened:
                        key_states["up"] = True
                elif event.key == pygame.K_DOWN:
                    if not player.inventory_opened:
                        key_states["down"] = True
                elif event.key == pygame.K_LEFT:
                    if not player.inventory_opened:
                        key_states["left"] = True
                elif event.key == pygame.K_RIGHT:
                    if not player.inventory_opened:
                        key_states["right"] = True
                elif event.key == pygame.K_e:
                    if player.rect.colliderect(cake.rect):
                        cake.interact(player, message_box=message_box)
                    elif player.inventory_opened:
                        message_box.update_message("아이템을 사용하겠습니까?")
                        message_box.change_visibility()

                elif event.key == pygame.K_q:
                    if player.inventory_opened:
                        player.close_inven()
                    else:
                        player.open_inven()
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

        pygame.display.update()
        display.disp(screen)
        message_box.draw(player, screen)

        pygame.display.flip()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
