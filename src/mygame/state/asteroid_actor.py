from typing import List

import pygame
from pygame.surface import Surface

from src.mygame.interfaces.actor import Actor


class Asteroid(Actor):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.speed = 240
        self.size = 20

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
        pygame.draw.polygon(screen, "white", self.get_collision_polygon(), 0)
