import pygame as pg
import sys


class MessageBox:
    def __init__(self):
        self.width = 600
        self.height = 100
        self.clock = pg.time.Clock()

        self.surface = pg.Surface((self.width, self.height), pg.SRCALPHA)
        self.surface.fill((0, 0, 0, 128))

        self.font = pg.font.Font('assets/NanumFontSetup_TTF_GOTHIC/NanumGothicLight.ttf', 12)

    def update(self, message_text):
        text_surface = self.font.render(message_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.width // 2, 50))
        self.surface.blit(text_surface, text_rect.topleft)

    def draw(self, screen):
        screen.blit(self.surface, (50, self.height + 250))

        pg.display.flip()
