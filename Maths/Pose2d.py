from Maths.vector2d import Vector2d


class Pose2d:
    """
    This class represents a 2d position of entity in the game window
    which includes it's x and y position, and it's rotation
    """
    def __init__(self, x=0, y=0, theta=0):
        """
        :param x: position x coordinates
        :param y:  position y coordinates
        :param theta: position theta
        """
        self._x = x
        self._y = y
        self._theta = theta

    def vector(self):
        """
        :return: A 2d vector representation of a given pose2d
        """
        return Vector2d(self._x, self._y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def theta(self):
        return self._theta

    @theta.setter
    def theta(self, heading):
        self._theta = heading

    def __str__(self):
        return f"[{self._x},{self._y},{self._theta}]"

    def __add__(self, other):
        return Pose2d(self._x + other.x, self._y + other.y, self._theta + other.theta)

    def __sub__(self, other):
        return Pose2d(self._x - other.x, self._y - other.y, self._theta - other.theta)

    def __mul__(self, scalar):
        return Pose2d(self._x * scalar, self._y * scalar, self._theta * scalar)

    def __truediv__(self, scalar):
        return Pose2d(self._x / scalar, self._y / scalar, self._theta / scalar)

    def __iadd__(self, other):
        self._x += other.x
        self._y += other.y
        self._theta += other.theta

    def __isub__(self, other):
        self._x -= other.x
        self._y -= other.y
        self._theta = other.theta

    def __imul__(self, scalar):
        self._x *= scalar
        self._y *= scalar
        self._theta *= scalar

    def __idiv__(self, scalar):
        self._x /= scalar
        self._y /= scalar
        self._theta /= scalar

    def __eq__(self, other):
        self._x = other.x
        self._y = other.y
        self._theta = other.theta

    def hadamard(self, other):
        """
        Returns the hadamard (element wise multiplication) of 2 positions
        :param other: other pose2d object
        :return: The result of hadamard operation between the 2 positions
        """
        return Pose2d(self._x * other.x, self._y * other.y, self._theta * other.theta)
