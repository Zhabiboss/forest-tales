import pygame
from settings import *
import math

pygame.init()

fonts = {
    "big": pygame.font.Font("Resources/Consolas.ttf", 32, bold = True),
    "small": pygame.font.Font("Resources/Consolas.ttf", 20)
}

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

class Particle:
    def __init__(self, app, x, y, starting_acc, color = (255, 255, 255)):
        self.x, self.y = x, y
        self.velocity = [0, 0]
        self.app = app
        self.starting_acc = starting_acc
        self.color = color
        self.lifespan = 0

    def update(self):
        self.velocity[0] += self.starting_acc[0]
        self.velocity[1] += self.starting_acc[1]
        self.starting_acc = (0, 0)
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.velocity[0] *= 0.99
        self.velocity[1] *= 0.99
        self.lifespan += 10

    def draw(self):
        r = self.color[0] - self.lifespan if self.color[0] > self.lifespan else 0
        g = self.color[1] - self.lifespan if self.color[1] > self.lifespan else 0
        b = self.color[2] - self.lifespan if self.color[2] > self.lifespan else 0
        pygame.draw.rect(self.app.screen, (r, g, b), (self.x - 1, self.y - 1, 2, 2))

def distance(a1, b1, a2, b2):
    return math.sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2)