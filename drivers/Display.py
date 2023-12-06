import board
from digitalio import DigitalInOut
from PIL import Image
from adafruit_rgb_display import st7789
import pygame
from pygame.locals import *

class Display:
    def __init__(self, surface, width=240, height=240, ):
        self.cs_pin = DigitalInOut(board.CE0)
        self.dc_pin = DigitalInOut(board.D25)
        self.reset_pin = DigitalInOut(board.D24)
        self.BAUDRATE = 24000000
        self.surface = surface

        spi = board.SPI()
        self.display = st7789.ST7789(
            spi,
            height=height,
            y_offset=80,
            rotation=180,
            cs=self.cs_pin,
            dc=self.dc_pin,
            rst=self.reset_pin,
            baudrate=self.BAUDRATE,
        )

    def init(self):
        backlight = DigitalInOut(board.D26)
        backlight.switch_to_output()
        backlight.value = True

    def surface_to_image(self, surface):
        image_data = pygame.image.tostring(surface, 'RGBA')
        width, height = surface.get_size()
        return Image.frombytes('RGBA', (width, height), image_data)

    def disp(self):
        image = self.surface_to_image(self.surface)
        self.display.image(image)