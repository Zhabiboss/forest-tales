import pygame
from settings import *

class Inventory:
    def __init__(self, app):
        self.capacity = 64
        self.items = []
        self.app = app

    def update(self):
        ...

    def draw(self):
        ...