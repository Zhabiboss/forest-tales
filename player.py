import random
import pygame
from settings import *
from utilities import blitRotateCenter, Particle

class Player:
    def __init__(self, app):
        self.app = app
        self.x, self.y = 1, 1
        self.texture = self.app.player_texture
        self.surface = pygame.Surface(self.app.res, pygame.SRCALPHA)
        self.angle = 0
        self.rotating_speed = 10
        self.health = 20
        self.attack_damage = 2
        self.attack_interval = 30
        self.path_particles = []

    def update(self):
        if self.health > 0:
            dx, dy = 0, 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                dy -= player_speed * self.app.dt
                self.rotating_speed += 3.2
            if keys[pygame.K_s]:
                dy += player_speed * self.app.dt
                self.rotating_speed += 3.2
            if keys[pygame.K_a]:
                dx -= player_speed * self.app.dt
                self.rotating_speed += 3.2
            if keys[pygame.K_d]:
                dx += player_speed * self.app.dt
                self.rotating_speed += 3.2
            self.check_wall_collision(dx, dy)
            self.path_particles.append(Particle(self.app, self.position[0], self.position[1], (-dx * 100 - random.random() * 1.5, -dy * 100 - random.random() * 1.5), (255, 255, 255)))
            self.angle += self.rotating_speed * self.app.dt
        self.rotating_speed *= 0.99
        if self.rotating_speed > 360:
            self.rotating_speed = 360
        for path_p in self.path_particles:
            path_p.update()
            if path_p.lifespan > 255:
                self.path_particles.remove(path_p)

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
        for path_p in self.path_particles:
            path_p.draw()
        pygame.draw.circle(self.surface, (255, 255, 255, 12), self.position, tile * 1.5)
        pygame.draw.circle(self.surface, (255, 255, 255, 20), self.position, tile * 1.2)
        pygame.draw.circle(self.surface, (255, 255, 255, 25), self.position, tile)
        pygame.draw.circle(self.surface, (255, 255, 255, 100), self.position, tile * 0.6)
        pygame.draw.circle(self.surface, (255, 255, 255, 110), self.position, tile * 0.3)
        self.app.screen.blit(self.surface, (0, 0))
        blitRotateCenter(self.app.screen, self.texture, (self.position[0] - tile // 2, self.position[1] - tile // 2), self.angle)
        self.surface = pygame.Surface(self.app.res, pygame.SRCALPHA)