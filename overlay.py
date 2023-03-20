import pygame
from settings import *

class PlayerHealthOverlay:
    def __init__(self, app):
        self.app = app
        self.playerHealth = self.app.player.health
        self.font = pygame.font.SysFont("Consolas", 16, bold = True)
        self.text = self.font.render(f"Health: {self.playerHealth}", True, "green")

    def update(self):
        self.playerHealth = self.app.player.health
        self.font = pygame.font.SysFont("Consolas", 16, bold = True)
        self.text = self.font.render(f"Health: {self.playerHealth}", True, "green")

    def draw(self):
        pygame.draw.rect(self.app.screen, (0, 0, 0), (0, 0, self.text.get_width() + self.app.player_overlay_texture.get_width() + 30, self.app.player_overlay_texture.get_height()))
        self.app.screen.blit(self.text, (self.app.player_overlay_texture.get_width() + 10, 0))
        self.app.screen.blit(self.app.player_overlay_texture, (0, 0))

class Overlay:
    def __init__(self, app):
        self.app = app
        self.elements = [PlayerHealthOverlay(self.app)]
        
    def update(self):
        for element in self.elements:
            element.update()

    def draw(self):
        for element in self.elements:
            element.draw()