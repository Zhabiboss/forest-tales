import pygame
from settings import *
from utilities import blitRotateCenter
import random

positions = {}
def init_background(app, width_, height_, texture_name):
    for i in range(width_):
        for j in range(height_):
            positions[i, j] = (app.screen, pygame.transform.scale(pygame.image.load(f"Resources/{texture_name}.png"), (tile, tile)), (i * tile, j * tile), random.choice([0, 90, 180, 270]))

def draw_background(app, width_, height_, texture_name):
    for i in range(width_):
        for j in range(height_):
            blitRotateCenter(*positions[i, j])