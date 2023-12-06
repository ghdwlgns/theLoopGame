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
    
    width, height = 240, 240
    screen = pygame.display.set_mode((width, height))

    display = Display(screen)
    display.init()

    message_box = MessageBox(20, 20)
    player = Player(width // 2, height // 2, message_box)

    key = Key("Key", "Sample")
    cake = Chest(width - 16, height // 2, "theLoopGame/assets/cake.png", key, "Cake")

    timer_interval = 30 * 1000
    pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    time_loop = TimeLoop()

    # 게임 루프
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not player.inventory_opened:
                        player.start_moving("up")
                elif event.key == pygame.K_DOWN:
                    if not player.inventory_opened:
                        player.start_moving("down")
                elif event.key == pygame.K_LEFT:
                    if not player.inventory_opened:
                        player.flip_sprite()
                        player.start_moving("left")
                elif event.key == pygame.K_RIGHT:
                    if not player.inventory_opened:
                        player.start_moving("right")
                elif event.key == pygame.K_a:
                    if player.rect.colliderect(cake.rect):
                        cake.interact(player, message_box=message_box)
                    elif player.inventory_opened:
                        message_box.update_message("아이템을 사용하겠습니까?")
                        message_box.change_visibility()

                elif event.key == pygame.K_b:
                    if player.inventory_opened:
                        player.close_inven()
                    else:
                        player.open_inven()
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    player.stop_moving()

            elif event.type == pygame.USEREVENT:
                saved_state = time_loop.save_state(player, [cake])
                print("State saved..")
                pygame.time.delay(1000)
                time_loop.load_state(player, [cake], saved_state)
                print("State loaded..")

        player.update()

        screen.fill((255, 255, 255))
        player.draw(screen)
        cake.draw(screen)
        message_box.draw(screen)

        pygame.display.update()
        display.disp()
        
        pygame.display.flip()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
