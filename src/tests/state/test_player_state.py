from ...mygame.state.player_state import PlayerState


class TestPlayerState:
    def test_movement_fps(self):
        """We want to ensure that movement is not affected by FPS."""
        player = PlayerState()

        player.moving_left = True

        # If we double the FPS the player should move at half the speed
        time_scale = 2

        player.pos_x = 0
        player.update(1)
        position1 = player.pos_x

        player.pos_x = 0
        player.update(1.0 / time_scale)
        position2 = player.pos_x

        assert position1 == position2 * time_scale
