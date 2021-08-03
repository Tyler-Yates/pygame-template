import math
import random
from typing import List

from shapely.geometry import Polygon


def collides(collision_polygon_1: List[List[float]], collision_polygon_2: List[List[float]]) -> bool:
    polygon1 = Polygon(collision_polygon_1)
    polygon2 = Polygon(collision_polygon_2)
    return polygon1.intersects(polygon2)


def polygon_area(polygon_points: List[List[int]]) -> float:
    polygon = Polygon(polygon_points)
    return polygon.area


def generate_polygon(num_vertices: int, size: int, variation: float) -> List[List[int]]:
    points: List[List[int]] = []

    angles = []
    spacing_radians = math.pi * 2 / num_vertices
    for i in range(num_vertices):
        angles.append(random.uniform(i * spacing_radians, (i + 1) * spacing_radians))

    for i in range(num_vertices):
        angle = angles[i]
        length = random.randint(int(size * (1.0 - variation)), int(size * (1.0 + variation)))

        points.append([int(math.cos(angle) * length), int(math.sin(angle) * length)])

    return points
