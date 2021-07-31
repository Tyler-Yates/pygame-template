from typing import List

import pygame
from pygame import Surface
from pygame.event import Event

PLAYER_SIZE = 20
PLAYER_OFFSET_FROM_BOTTOM = 10

PLAYER_SPEED = 120


class PlayerState:
    pos_x: float = 0

    moving_left: bool = False
    moving_right: bool = False

    def handle_events(self, events: List[Event]):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    self.moving_right = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.moving_right = True

    def update(self, time_delta: float):
        if self.moving_left:
            self.pos_x -= PLAYER_SPEED * time_delta
        if self.moving_right:
            self.pos_x += PLAYER_SPEED * time_delta

    def draw_player(self, screen: Surface):
        pos_y = screen.get_height() - PLAYER_OFFSET_FROM_BOTTOM - PLAYER_SIZE
        point1 = [self.pos_x - (PLAYER_SIZE / 2), pos_y + PLAYER_SIZE]
        point2 = [self.pos_x, pos_y]
        point3 = [self.pos_x + (PLAYER_SIZE / 2), pos_y + PLAYER_SIZE]
        pygame.draw.polygon(screen, 'white', [point1, point2, point3], 0)
