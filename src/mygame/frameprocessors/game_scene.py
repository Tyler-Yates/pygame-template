import logging
from typing import List, TYPE_CHECKING

from pygame import Surface
from pygame.event import Event

from src.mygame.constants.scene_enum import SceneEnum
from src.mygame.interfaces.scene import Scene
from src.mygame.state.asteroid_actor import Asteroid
from src.mygame.state.game_state import GameState
from src.mygame.util.collisions import collides
from src.mygame.util.fonts import BASIC_FONT

if TYPE_CHECKING:
    from src.mygame.controllers.scene_controller import SceneController

BACKGROUND_COLOR = (50, 50, 50)

SCORE_TEXT_PREFIX = "Score: "
SCORE_TEXT_SIZE = 20


class GameScene(Scene):
    """
    Scene that handles actual gameplay.
    """

    def __init__(self, game_state: GameState, scene_controller: "SceneController"):
        super().__init__(game_state, scene_controller)

        self.log = logging.getLogger(self.__class__.__name__)

        self.asteroid_tick = 0
        self.score_tick = 0

    def process_input(self, events: List[Event]):
        self.game_state.player.process_input(events)

    def update(self, time_delta: float):
        self.game_state.player.update(time_delta)

        player_collision_polygon = self.game_state.player.get_collision_polygon()

        for asteroid in self.game_state.asteroids:
            asteroid.update(time_delta)
            asteroid_collision_polygon = asteroid.get_collision_polygon()
            if collides(player_collision_polygon, asteroid_collision_polygon):
                self.scene_controller.change_active_scene(SceneEnum.MainMenu)

        if self.score_tick > 100:
            self.score_tick = 0
            self.game_state.score += 1

        if self.asteroid_tick > 5000:
            self.asteroid_tick = 0
            self.log.info(f"Creating new asteroid. Existing asteroids: {len(self.game_state.asteroids)}")
            self.game_state.asteroids.append(Asteroid(100, -100))

        tick = int(time_delta * 1000)
        self.asteroid_tick += tick
        self.score_tick += tick

    def render(self, screen: Surface):
        screen.fill(BACKGROUND_COLOR)

        # Score in upper-left
        score_text = SCORE_TEXT_PREFIX + str(self.game_state.score)
        BASIC_FONT.render_to(screen, (5, 5), score_text, "white", size=SCORE_TEXT_SIZE)

        # Player
        self.game_state.player.render(screen)

        # Clear any asteroids off the screen
        self.game_state.asteroids[:] = [
            asteroid for asteroid in self.game_state.asteroids if asteroid.pos_y < screen.get_height() + 100
        ]

        # Now render any asteroids left
        for asteroid in self.game_state.asteroids:
            asteroid.render(screen)
