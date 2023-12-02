import pygame as pg


class Object:
    def __init__(self, x, y, width, height, image_uri):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # self.object_sprite_sheet = pg.image.load(image_uri)
