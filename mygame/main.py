import logging

import pygame

from mygame.controllers.controller import Controller
from mygame.frameprocessors.main_menu_scene import MainMenuScene
from mygame.frameprocessors.performance_overlay import PerformanceOverlay
from mygame.state.game_state import GameState
from mygame.state.scene_state import SceneState

logging.basicConfig(level=logging.INFO)

GAME_WIDTH_PX = 1024
GAME_HEIGHT_PX = 720
GAME_FPS = 60
GAME_NAME = "Pygame Template"


def main():
    game_state = GameState()
    scene_state = SceneState()

    main_menu_scene = MainMenuScene(game_state=game_state, scene_state=scene_state)

    scene_state.change_scene(main_menu_scene)

    overlays = [PerformanceOverlay(game_state, scene_state)]

    director = Controller(GAME_NAME, game_state, scene_state, GAME_FPS, GAME_WIDTH_PX, GAME_HEIGHT_PX, overlays)
    director.loop()


if __name__ == '__main__':
    pygame.init()
    main()
