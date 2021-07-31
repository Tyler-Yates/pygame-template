from src.mygame.util.collisions import collides


class TestCollisions:
    def test_collides_true(self):
        base_polygon = [[0, 0], [2, 2], [4, 0]]

        # A polygon should always collide with itself
        assert collides(base_polygon, base_polygon)

        # This polygon is contained completely within base_polygon
        contained_within_polygon = [[0, 0], [1, 1], [2, 0]]
        assert collides(base_polygon, contained_within_polygon)

        # This polygon touches base_polygon only at (0, 0) but that is still a collision
        one_pixel_collision_polygon = [[0, 0], [-2, -2], [-4, 0]]
        assert collides(base_polygon, one_pixel_collision_polygon)

    def test_collides_false(self):
        polygon1 = [[0, 0], [2, 2], [4, 0]]

        # No collision
        not_collides_polygon1 = [[-1, 0], [-2, -2], [-4, 0]]
        assert not collides(polygon1, not_collides_polygon1)
