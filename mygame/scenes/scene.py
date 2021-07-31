class Scene:
    """Represents a scene of the game.

    Scenes must be created inheriting this class attributes
    in order to be used afterwards as menus, introduction screens,
    etc."""

    def __init__(self):
        pass

    def process_input(self, events):
        raise NotImplementedError("Subclass must implement.")

    def update(self):
        raise NotImplementedError("Subclass must implement.")

    def render(self, screen):
        raise NotImplementedError("Subclass must implement.")
