import pygame
from settings import *

_ = False
map_ = [[1, 1, 1, 1, 1, 1, 1, 1],
        [1, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, 1],
        [1, _, _, _, 1, _, _, 1],
        [1, _, _, _, _, _, _, 1],
        [1, _, _, 1, _, _, _, 1],
        [1, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]

class Map:
    def __init__(self, app):
        self.world_map = {}
        for j, row in enumerate(map_):
            for i, value in enumerate(row):
                if value:
                    self.world_map[i, j] = value
        #print(self.world_map)
        self.app = app

        self.textures = {
            1: pygame.transform.scale(pygame.image.load("Resources/cobble.png"), (tile, tile)),
            2: pygame.transform.scale(pygame.image.load("Resources/dirt.png"), (tile, tile))
        }

    def draw(self):
        for i in self.world_map:
            self.app.screen.blit(self.textures[self.world_map[i]], (i[0] * tile, i[1] * tile, tile, tile))