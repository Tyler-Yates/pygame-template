import logging

import pygame

from mygame.state.game_state import GameState
from mygame.state.scene_state import SceneState
from mygame.util.fonts import BASIC_FONT


class Director:
    """Represents the main object of the game.

    The Director object keeps the game on, and takes care of updating it,
    drawing it and propagate events.

    This object must be used with Scene objects that are defined later."""

    def __init__(self, game_state: GameState, scene_state: SceneState, fps: int, width_px: int, height_px: int):
        self.log = logging.getLogger(self.__class__.__name__)

        self.fps = fps
        self.width_px = width_px
        self.height_px = height_px
        self.game_state = game_state
        self.scene_state = scene_state

        self.log.info(f"Starting game with resolution {self.width_px}x{self.height_px} at {self.fps} FPS")

        self.quit_flag = False
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.width_px, self.height_px))
        pygame.display.set_caption("Game Name")

    def loop(self):
        scene = self.scene_state.active_scene
        while not self.quit_flag:
            millis_since_last_frame = self.clock.tick(self.fps)
            time_delta = float(millis_since_last_frame) / 1000.0

            # Exit events
            events = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                else:
                    events.append(event)

            # Scene executions
            scene.process_input(events)
            scene.update(time_delta)
            scene.render(self.screen)

            # We do not want to change scenes mid-frame so wait until the end of the frame to change scenes
            scene = self.scene_state.get_active_scene()

            # Draw performance info
            BASIC_FONT.render_to(self.screen, (self.width_px - 20, 5), f"{millis_since_last_frame}", 'red', size=14)

            pygame.display.flip()

    def quit(self):
        self.quit_flag = True
