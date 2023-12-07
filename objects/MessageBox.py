import pygame as pg
import sys


class MessageBox:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MessageBox, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, x, y):
        if not self.__initialized:
            self.width = 200
            self.height = 100
            self.rect = pg.Rect(x, y, self.width, self.height)
            self.messages = []
            self.font = pg.font.Font("assets/NanumFontSetup_TTF_GOTHIC/NanumGothicLight.ttf", 18)
            self.visible = False
            self.alpha = 150
            self.selected_index = 0

    def update_message(self, message):
        self.messages.append(message)

    def update_messages(self, messges):
        self.messages = messges

    def clear_messages(self):
        self.messages = []

    def change_visibility(self):
        self.visible = not self.visible

    def draw(self, screen):
        surface = pg.Surface((self.rect.width, self.rect.height), pg.SRCALPHA)
        pg.draw.rect(surface, (0, 0, 0, self.alpha), surface.get_rect())

        screen.blit(surface, (self.rect.x, self.rect.y))

        for i, message in enumerate(self.messages):
            print(message)
            text = self.font.render(message, True, (255, 255, 255))
            screen.blit(text, (self.rect.x, self.rect.y + i * 30))

        if self.visible:
            pg.draw.rect(screen, (0, 0, 255), self.rect, 2)
        else:
            self.clear_messages()
            pg.draw.rect(screen, (0, 0, 0), self.rect, 2)

    def display_inventory(self, player):
        inven_text = [f"{item.name}" for item in player.inventory]
        self.update_messages(inven_text)
