import pygame
from settings import *
from utilities import fonts

class Dialog:
    def __init__(self, app, title, text):
        self.text = text
        self.title = title
        self.app = app
        self.skipped = False

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.skipped = True

    def draw(self):
        if not self.skipped:
            self.app.screen.blit(self.app.dialog_texture, (width // 2 - self.app.dialog_texture.get_width() // 2, height - 20 - self.app.dialog_texture.get_height()))
            title = fonts["big"].render(self.title, True, "black")
            self.app.screen.blit(title, (width // 2 - title.get_width() // 2 - 280, height - 20 - self.app.dialog_texture.get_height() // 2 - 70 - title.get_height() // 2))
            text = fonts["small"].render(self.text, True, "black")
            self.app.screen.blit(text, (width // 2 - title.get_width() // 2 - 280, height - 20 - self.app.dialog_texture.get_height() // 2 - 30 - title.get_height() // 2))