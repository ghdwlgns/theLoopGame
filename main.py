import pygame
import sys

from events.GameObject import GameObject
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

    bg_image = pygame.image.load("assets/ceilings.png")

    Joystick()
    
    width, height = 240, 240
    screen = pygame.display.set_mode((width, height))

    ratio = width / bg_image.get_width()
    resized_height = int(bg_image.get_height() * ratio)

    bg_image = pygame.transform.scale(bg_image, (width, resized_height))

    display = Display(screen)
    display.init()

    message_box = MessageBox(20, 20)

    player_width = [int(32 * ratio), width - int(32 * ratio) * 2]
    player_height = [32, 160]
    player = Player(width // 2, height // 2, player_width, player_height, message_box)

    key = Key("Key", "Sample")
    cake = Chest(width - 48, height // 2, "assets/cake.png", [key], "Cake")

    objects = [cake]

    timer_interval = 5000
    pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    time_loop = GameObject()
    time_loop.save_game_state(player, objects)

    # 게임 루프
    while True:
        print("State saved..")
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

            # elif event.type == pygame.USEREVENT:
            #     pygame.time.delay(1000)
            #     load_data = time_loop.load_game_state()
            #     player.load_state(load_data['player'])
            #     for obj, obj_state in zip(objects, load_data['objects']):
            #         obj.load_state(obj_state)
            #     print("State loaded..")

        for obj in objects:
            if player.rect.colliderect(obj.rect):
                print("Crashed")
                player.stop_moving()
                break
            
        player.update()

        screen.blit(bg_image, (0, 0))
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
