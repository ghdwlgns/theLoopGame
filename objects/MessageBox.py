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
            self.width = 600
            self.height = 100
            self.rect = pg.Rect(x, y, self.width, self.height)
            self.messages = []
            self.font = pg.font.Font('assets/NanumFontSetup_TTF_GOTHIC/NanumGothicLight.ttf', 12)
            self.visible = False
            self.alpha = 150
            self.selected_index = 0

    def update_message(self, message):
        self.messages.append(message)

    def clear_messages(self):
        self.messages = []

    def change_visibility(self):
        self.visible = not self.visible

    def draw(self, player, screen):
        surface = pg.Surface((self.rect.width, self.rect.height), pg.SRCALPHA)
        pg.draw.rect(surface, (0, 0, 0, self.alpha), surface.get_rect())

        screen.blit(surface, (self.rect.x, self.rect.y))

        for i, message in enumerate(self.messages):
            text = self.font.render(message, True, (255, 255, 255))
            screen.blit(text, (self.rect.x, self.rect.y + i * 30 + 20))

        if self.visible:
            pg.draw.rect(screen, (0, 0, 255), self.rect, 2)
        else:
            pg.draw.rect(screen, (0, 0, 0), self.rect, 2)

        if self.visible:
            self.clear_messages()
            self.display_inventory(player, screen)

    def display_inventory(self, player, screen):
        inven_text = [f"{item.name}" for item in player.inventory]
        for i, text in enumerate(inven_text):
            text_surface = self.font.render(text, True, (255, 255, 255))
            screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 40 + i * 30))
