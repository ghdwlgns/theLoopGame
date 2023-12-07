from abc import ABC, abstractmethod

import pygame as pg


class Object(ABC):
    def __init__(self, x, y, image_uri, name):
        self.x = x
        self.y = y
        self.object_sprite_sheet = pg.image.load(image_uri)
        self.width = 30
        self.height = 30
        self.name = name
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    # 상호작용 함수
    @abstractmethod
    def interact(self, character, message_box):
        pass

    def draw(self, screen):
        screen.blit(self.object_sprite_sheet, self.rect.topleft)

    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def load_state(self):
        pass
