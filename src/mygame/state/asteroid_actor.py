from random import randrange
from typing import List

import pygame
import pygame.gfxdraw
from pygame.surface import Surface

from src.mygame.constants.engine_constants import GAME_WIDTH_PX
from src.mygame.interfaces.actor import Actor

BASE_SPEED = 200
MINIMUM_SIZE = 20
MAXIMUM_SIZE = 150


class Asteroid(Actor):
    def __init__(self, pos_x: float = None, pos_y: float = None, size: float = None):
        super().__init__()
        if pos_x:
            self.pos_x = pos_x
        else:
            self.pos_x = randrange(0, GAME_WIDTH_PX)

        if size is None:
            self.size = randrange(MINIMUM_SIZE, MAXIMUM_SIZE)
        else:
            self.size = size

        if pos_y:
            self.pos_y = pos_y
        else:
            self.pos_y = -self.size * 2

        self.speed = float(MAXIMUM_SIZE - MINIMUM_SIZE) / self.size * BASE_SPEED

    def get_collision_polygon(self) -> List[List[float]]:
        point1 = [self.pos_x - self.size, self.pos_y - self.size]
        point2 = [self.pos_x + self.size - 3, self.pos_y - 2]
        point3 = [self.pos_x + 2, self.pos_y + self.size]
        point4 = [self.pos_x - 5, self.pos_y]
        return [point1, point2, point3, point4]

    def process_input(self, events):
        pass

    def update(self, time_delta: float):
        self.pos_y += self.speed * time_delta

    def render(self, screen: Surface):
        pygame.gfxdraw.aapolygon(screen, self.get_collision_polygon(), (255, 255, 255))
        pygame.gfxdraw.filled_polygon(screen, self.get_collision_polygon(), (255, 255, 255))
        pygame.gfxdraw.aapolygon(screen, self.get_collision_polygon(), (200, 200, 200))
