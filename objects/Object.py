from abc import ABC, abstractmethod

import pygame as pg


class Object(ABC):
    def __init__(self, x, y, width, height, image_uri, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.object_sprite_sheet = pg.image.load(image_uri)
        self.name = name
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    # 상호작용 함수
    @abstractmethod
    def interact(self, character, message_box):
        pass

    def draw(self, screen):
        screen.blit(self.object_sprite_sheet, (self.x, self.y))
