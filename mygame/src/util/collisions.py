from typing import List

from shapely.geometry import Polygon


def collides(collision_polygon_1: List[List[float]], collision_polygon_2: List[List[float]]) -> bool:
    polygon1 = Polygon(collision_polygon_1)
    polygon2 = Polygon(collision_polygon_2)
    return polygon1.intersects(polygon2)
