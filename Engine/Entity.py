from Maths.Pose2d import Pose2d
import pygame


class Entity(pygame.sprite.Sprite):
    """
    Base class for all the pygame entities that are drawn to the screen
    """
    def __init__(self, x, y, width, height, texture_path, heading=0):
        """

        :param x: x position of entity
        :param y: y position of entity
        :param width: width of entity
        :param height: height of entity
        :param texture_path: path to entity's texture
        :param heading: heading of entity
        """
        super(Entity, self).__init__()
        self._position = Pose2d(x, y, heading)
        self._width = width
        self._height = height
        self._texture_path = texture_path

    def update(self):
        raise NotImplementedError("[Entity] Cannot call update on pure entity")

    def move(self, x, y):
        """
        Move entity in x and y directions
        :param x: Movement in the x direction
        :param y: Movement in the y direction
        :return: None
        """
        self._position.x += x
        self._position.y += y

    def rotate(self, rotation):
        """
        :param rotation: How much to rotate entity
        :return: None
        """
        self._position.theta += rotation

    @property
    def x(self):
        """
        :return: X position of entity
        """
        return self._position.x

    @x.setter
    def x(self, x):
        """
        :param x: new x position of entity
        :return: None
        """
        self._position.x = x

    @property
    def y(self):
        """
        :return: The y position of the entity
        """
        return self._position.y

    @y.setter
    def y(self, y):
        """
        :param y: New y position of the entity
        :return: None
        """
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
