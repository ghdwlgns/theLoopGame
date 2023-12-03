import pygame as pg


class Player:
    def __init__(self, x, y):
        self.sprite_sheet = pg.image.load('assets/16x16/Character_001.png')
        self.clock = pg.time.Clock()
        self.rows = 4
        self.columns = 4
        self.sprite_width = self.sprite_sheet.get_width() // self.rows
        self.sprite_height = self.sprite_sheet.get_height() // self.columns
        self.current_frame_x = 0
        self.current_frame_y = 0
        self.character_x = x
        self.character_y = y
        self.is_walking = False
        self.direction_x = "left"
        self.direction_y = "up"
        self.inventory = []
        self.clock = pg.time.Clock()

    def update(self):
        if self.is_walking:
            self.current_frame_x = (self.current_frame_x + 1) % self.columns

            if self.direction_y == "up":
                self.current_frame_y = 3
                if self.character_y > 0:
                    self.character_y -= 5
            elif self.direction_y == "down":
                self.current_frame_y = 0
                if self.character_y < 500:
                    self.character_y += 5
            if self.direction_x == "left":
                self.current_frame_y = 1
                if self.character_x > 0:
                    self.character_x -= 5
            elif self.direction_x == "right":
                self.current_frame_y = 2
                if self.character_x < 700:
                    self.character_x += 5

            self.clock.tick(10)

        else: # 대각선 멈춤 귀찮아서 구현 안함.
            if self.direction_y == "up":
                self.current_frame_x = 0
                self.current_frame_y = 3

            elif self.direction_y == "down":
                self.current_frame_x = 0
                self.current_frame_y = 0

            if self.direction_x == "left":
                self.current_frame_x = 0
                self.current_frame_y = 1

            elif self.direction_x == "right":
                self.current_frame_x = 0
                self.current_frame_y = 2

    def start_moving(self, direction_x, direction_y):
        self.is_walking = True
        self.direction_x = "right" if direction_x == 1 else "left" if direction_x == -1 else "stop"
        self.direction_y = "up" if direction_y == 1 else "down" if direction_y == -1 else "stop"

    def stop_moving(self):
        self.is_walking = False

    def add_item(self, item):
        self.inventory.append(item)

    def has_item(self, item):
        # TODO: 인벤토리에 해당 아이템 객체가 존재하는지 확인하는 메서드
        pass

    def remove_item(self, item):
        self.inventory.remove(item)

    def get_current_sprite(self):
        frame_x = self.current_frame_x * self.sprite_width
        frame_y = self.current_frame_y * self.sprite_height
        return self.sprite_sheet.subsurface(pg.Rect(frame_x, frame_y, self.sprite_width, self.sprite_height))

    def draw(self, screen):
        screen.blit(self.get_current_sprite(), (self.character_x, self.character_y))
