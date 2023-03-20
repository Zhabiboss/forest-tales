import pygame
import sys
from settings import *
from map import *
from player import *
from background import *
from dialog import *
from enemy import *
from utilities import distance
from overlay import *
from item import *

class Application:
    def __init__(self):
        pygame.init()
        self.res = self.width, self.height = res
        self.screen = pygame.display.set_mode(self.res)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.dt = 1 / self.fps
        self.init_textures()
        self.initialize()

    def init_textures(self):
        self.player_texture = pygame.transform.scale(pygame.image.load("Resources/player.png"), (tile, tile))
        self.dialog_texture = pygame.image.load("Resources/dialog.png")
        self.enemy_texture = pygame.transform.scale(pygame.image.load("Resources/base_enemy.png"), (tile, tile))
        self.player_overlay_texture = pygame.transform.scale(pygame.image.load("Resources/health_overlay.png"), (tile, tile))
        init_background(self, 8, 8, "dirt")

    def initialize(self):
        self.map = Map(self)
        self.player = Player(self)
        self.e = EnemyBase(self)
        self.d = Dialog(self, "Title", "Text")
        self.overlay = Overlay(self)
        self.items = [Item(app, )]

    def update(self):
        self.player.update()
        self.e.update()
        self.overlay.update()
        pygame.display.update()
        self.clock.tick(self.fps)
        self.dt = 1 / self.fps
        pygame.display.set_caption(f"fps: {self.clock.get_fps() :.2f} dt: {self.dt :.2f}")

    def draw(self):
        self.screen.fill((0, 0, 0))
        draw_background(self, 8, 8, "dirt")
        self.map.draw()

        self.player.draw()
        self.e.draw()
        self.overlay.draw()

        self.d.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.d.on_event(event)

    def run(self):
        while True:
            self.events()
            self.draw()
            self.update()
    
if __name__ == "__main__":
    app = Application()
    app.run()