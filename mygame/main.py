import pygame

from mygame.base.director import Director
from mygame.scenes.main_menu import MainMenuScreen


GAME_FPS = 60
GAME_WIDTH_PX = 1024
GAME_HEIGHT_PX = 720


def main():
    main_menu_scene = MainMenuScreen()
    director = Director(main_menu_scene, GAME_FPS, GAME_WIDTH_PX, GAME_HEIGHT_PX)
    director.loop()


if __name__ == '__main__':
    pygame.init()
    main()
