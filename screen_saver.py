import pygame

pygame.init()


class Vec2d:

    def __add__(self, n):
        pass

    def __sub__(self, n):
        pass

    def __mul__(self, n):
        pass

    def __len__(self):
        pass

    def int_pair(n1: int, n2: int):
        return (n1, n2)


class Polyline:

    def add_points(self, v):
        """
        Adds points to polyline.
        """
        pass

    def set_points(self):
        """
        Recalc coordinates of the points
        """
        pass

    def draw_points(self):
        """
        Draw polyline
        """
        pass


class Knot(Polyline):

    def get_knot(self):
        pass
