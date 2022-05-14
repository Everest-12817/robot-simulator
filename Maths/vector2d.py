class Vector2d:
    """
    This class represent a 2d vectoy
    Mostly used to represent coordinates of objects on screen
    """

    def __init__(self, x=0, y=0):
        """
        :param x: the first element of the vector
        :param y: the second element of the vector
        """
        self._x = x
        self._y = y

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

    def __str__(self):
        return f"[{self._x},{self._y}]"

    def __add__(self, other):
        return Vector2d(self._x + other.x, self._y + other.y)

    def __sub__(self, other):
        return Vector2d(self._x - other.x, self._y - other.y)

    def __mul__(self, scalar):
        return Vector2d(self._x * scalar, self._y * scalar)

    def __truediv__(self, scalar):
        return Vector2d(self._x / scalar, self._y / scalar)

    def hadamard(self, other):
        """
              Returns the hadamard (element wise multiplication) of 2 vectors
              :param other: other pose2d object
              :return: The result of hadamard operation between the 2 vectors
        """
        return Vector2d(self._x * other.x, self._y * other.y)
