import pygame as pg

from objects.Memo import Memo


class Player:
    def __init__(self, x, y, message_box):
        self.sprite_sheet = pg.image.load('assets/16x16/Character_001.png')
        self.clock = pg.time.Clock()
        self.rows = 4
        self.columns = 4
        self.sprite_width = self.sprite_sheet.get_width() // self.rows
        self.sprite_height = self.sprite_sheet.get_height() // self.columns
        self.current_frame_x = 0
        self.current_frame_y = 0
        self.x = x
        self.y = y
        self.rect = pg.Rect(x, y, self.sprite_width, self.sprite_height)
        self.is_walking = False
        self.direction_x = "left"
        self.direction_y = "up"
        self.inventory = [Memo("쪽지", "설명")]
        self.clock = pg.time.Clock()
        self.inventory_opened = False
        self.inventory_idx = 0

        self.message_box = message_box

    def update(self):
        if self.is_walking:
            self.current_frame_x = (self.current_frame_x + 1) % self.columns

            if self.direction_y == "up":
                self.current_frame_y = 3
                if self.y > 0:
                    self.y -= 5
            elif self.direction_y == "down":
                self.current_frame_y = 0
                if self.y < 500:
                    self.y += 5
            if self.direction_x == "left":
                self.current_frame_y = 1
                if self.x > 0:
                    self.x -= 5
            elif self.direction_x == "right":
                self.current_frame_y = 2
                if self.x < 700:
                    self.x += 5

            self.clock.tick(10)

        else:
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
        return any(existing_item == item for existing_item in self.inventory)

    def remove_item(self, item):
        self.inventory.remove(item)

    def open_inven(self):
        self.inventory_opened = True
        self.inventory_idx = 0

    def close_inven(self):
        self.inventory_opened = False

    def select_item_in_inven(self, direction):
        if self.inventory_opened:
            max_index = len(self.inventory) - 1
            if direction == "up":
                self.inventory_idx = max(0, self.inventory_idx - 1)
            elif direction == "down":
                self.inventory_idx = min(max_index, self.inventory_idx + 1)

    def use_item(self):
        if self.inventory_opened:
            item = self.inventory[self.inventory_idx]
            item.use(self.message_box)

    def get_current_sprite(self):
        frame_x = self.current_frame_x * self.sprite_width
        frame_y = self.current_frame_y * self.sprite_height
        return self.sprite_sheet.subsurface(pg.Rect(frame_x, frame_y, self.sprite_width, self.sprite_height))

    def draw(self, screen):
        screen.blit(self.get_current_sprite(), (self.x, self.y))
