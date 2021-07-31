from typing import List

from pygame import Surface
from pygame.event import Event

from mygame.scenes.scene import Scene
from mygame.util.fonts import BASIC_FONT


MAIN_MENU_BACKGROUND_COLOR = (200, 200, 200)

MAIN_MENU_TEXT = "Main Menu"
MAIN_MENU_TEXT_SIZE = 64


class MainMenuScreen(Scene):
    """ Welcome screen of the game, the first one to be loaded."""

    def __init__(self):
        super().__init__()

    def process_input(self, events: List[Event]):
        pass

    def update(self):
        pass

    def render(self, screen: Surface):
        screen.fill(MAIN_MENU_BACKGROUND_COLOR)

        text_rect = BASIC_FONT.get_rect(MAIN_MENU_TEXT, size=MAIN_MENU_TEXT_SIZE)
        text_rect.center = screen.get_rect().center
        BASIC_FONT.render_to(screen, text_rect, MAIN_MENU_TEXT, 'black', size=MAIN_MENU_TEXT_SIZE)
