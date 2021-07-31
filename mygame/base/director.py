import pygame

from mygame.scenes.scene import Scene


class Director:
    """Represents the main object of the game.

    The Director object keeps the game on, and takes care of updating it,
    drawing it and propagate events.

    This object must be used with Scene objects that are defined later."""

    def __init__(self, first_scene: Scene, fps: int, width_px: int, height_px: int):
        self.fps = fps
        self.width_px = width_px
        self.height_px = height_px

        self.active_scene = first_scene
        self.quit_flag = False
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.width_px, self.height_px))
        pygame.display.set_caption("Game Name")

    def loop(self):
        """Main game loop."""

        while not self.quit_flag:
            self.clock.tick(self.fps)

            # Exit events
            events = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                else:
                    events.append(event)

            # Scene executions
            self.active_scene.process_input(events)
            self.active_scene.update()
            self.active_scene.render(self.screen)

            pygame.display.flip()

    def change_scene(self, scene: Scene):
        """Changes the current scene."""
        self.active_scene = scene

    def quit(self):
        self.quit_flag = True
