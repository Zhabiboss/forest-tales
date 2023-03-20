import pygame
from settings import *
from utilities import blitRotateCenter, distance, Particle
import math
import random

class EnemyBase:
    def __init__(self, app):
        self.app = app
        self.x, self.y = 1, 1
        self.texture = self.app.enemy_texture
        self.surface = pygame.Surface(self.app.res, pygame.SRCALPHA)
        self.health = 20
        self.attack_damage = 2
        self.attack_interval = 30
        self.tick = 0

    def AI(self) -> tuple[int, int]:
        dx, dy = 0, 0
        if self.app.player.position[0] < self.position[0]:
            dx -= 0.015
        if self.app.player.position[0] > self.position[0]:
            dx += 0.015
        if self.app.player.position[1] < self.position[1]:
            dy -= 0.015
        if self.app.player.position[1] > self.position[1]:
            dy += 0.015
        return dx, dy
    
    def on_attack(self):
        self.app.player.health -= self.attack_damage
        for i in range(30):
            self.app.player.path_particles.append(Particle(self.app, self.app.player.position[0], self.app.player.position[1], (1 - random.random() * 1.5, 0), (255, random.randint(80, 90), random.randint(80, 90))))
        for i in range(30):
            self.app.player.path_particles.append(Particle(self.app, self.app.player.position[0], self.app.player.position[1], (1 - random.random() * 1.5, 1 - random.random() * 1.5), (255, random.randint(80, 90), random.randint(80, 90))))
        for i in range(30):
            self.app.player.path_particles.append(Particle(self.app, self.app.player.position[0], self.app.player.position[1], (-1 - random.random() * 1.5, 0), (255, random.randint(80, 90), random.randint(80, 90))))
        for i in range(30):
            self.app.player.path_particles.append(Particle(self.app, self.app.player.position[0], self.app.player.position[1], (-1 - random.random() * 1.5, -1 - random.random() * 1.5), (255, random.randint(80, 90), random.randint(80, 90))))

    def update(self):
        self.tick += 1
        if self.health > 0:
            if abs(distance(self.position[0], self.app.player.position[0], self.position[1], self.app.player.position[1])) < 60:
                if self.tick % self.attack_interval == 0 and self.app.player.health > 0:
                    self.on_attack()
            dx, dy = self.AI()
            self.check_wall_collision(dx, dy)
        
    def check_walls(self, x, y):
        if (x, y) in self.app.map.world_map:
            return True 
        return False
    
    def check_wall_collision(self, dx, dy):
        if not self.check_walls(int(self.x + dx), int(self.y + dy)):
            self.x += dx
            self.y += dy

    @property
    def position(self):
        return self.x * tile, self.y * tile
    
    @property
    def map_position(self):
        return self.x, self.y
    
    def draw(self):
        self.app.screen.blit(self.surface, (0, 0))
        self.app.screen.blit(self.texture, (self.position[0] - tile // 2, self.position[1] - tile // 2))
        self.surface = pygame.Surface(self.app.res, pygame.SRCALPHA)