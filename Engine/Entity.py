from Maths.Pose2d import Pose2d
import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, texture_path, heading=0):
        super(Entity, self).__init__()
        self._position = Pose2d(x, y, heading)
        self._width = width
        self._height = height
        self._texture_path = texture_path

    def update(self):
        raise NotImplementedError("[Entity] Cannot call update on pure entity")

    def move(self, x, y):
        self._position.x += x
        self._position.y += y

    def rotate(self, rotation):
        self._position.theta += rotation

    @property
    def x(self):
        return self._position.x

    @x.setter
    def x(self, x):
        self._position.x = x

    @property
    def y(self):
        return self._position.y

    @y.setter
    def y(self, y):
        self._position.y = y

    @property
    def heading(self):
        return self._position.theta

    @heading.setter
    def heading(self, heading):
        self._position.theta = heading

    @property
    def w(self):
        return self._width

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @w.setter
    def w(self, w):
        self._width = w

    @property
    def h(self):
        return self._height

    @h.setter
    def h(self, h):
        self._height = h

    @property
    def texture_path(self):
        return self._texture_path

    @texture_path.setter
    def texture_path(self, texture_path):
        self._texture_path = texture_path
