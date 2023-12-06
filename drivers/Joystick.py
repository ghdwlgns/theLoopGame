import RPi.GPIO as GPIO
import keyboard
import pygame as pg
from pygame.locals import *

class Joystick:
    def __init__(self):
        self.BUTTON_MAP = {5: 'K_b', 6: 'K_a', 27: 'K_LEFT', 23: 'K_RIGHT', 17: 'K_UP', 22: 'K_DOWN', 4: 'C'}
        GPIO.setmode(GPIO.BCM)

        for pin in self.BUTTON_MAP.keys():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pin, GPIO.BOTH, callback=lambda k: self.gpio_to_keyboard(k), bouncetime=300)

    def gpio_to_keyboard(self, pin):
        key = self.BUTTON_MAP.get(pin)
        if key:
            if GPIO.input(pin) == GPIO.LOW:
                pg.event.post(pg.event.Event(KEYDOWN, {'key': getattr(pg.locals, key)}))
            else:
                pg.event.post(pg.event.Event(KEYUP, {'key': getattr(pg.locals, key)}))
