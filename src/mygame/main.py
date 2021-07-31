import logging

import pygame

from controllers.controller import Controller
from frameprocessors.performance_overlay import PerformanceOverlay
from src.mygame.controllers.scene_controller import SceneController
from state.game_state import GameState

logging.basicConfig(level=logging.INFO)

GAME_WIDTH_PX = 1024
GAME_HEIGHT_PX = 720
GAME_FPS = 60
GAME_NAME = "Pygame Template"


def main():
    game_state = GameState()
    scene_controller = SceneController(game_state)

    overlays = [PerformanceOverlay(game_state, scene_controller)]

    director = Controller(GAME_NAME, game_state, scene_controller, GAME_FPS, GAME_WIDTH_PX, GAME_HEIGHT_PX, overlays)
    director.loop()


if __name__ == "__main__":
    pygame.init()
    main()
