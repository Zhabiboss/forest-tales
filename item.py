import pygame
from settings import *

class Item:
    def __init__(self, app, x, y, texture):
        self.app = app
        self.x, self.y = x, y
        self.texture = texture

    def update(self):
        ...

    def draw(self):
        self.app.screen.blit(self.texture, (self.x, self.y))