from Engine import Entity


class Mission(Entity):
    def __init__(self, x, y, width, height, texture_path, name, heading = 0):
        super(Mission, self).__init__(x, y, width, height, texture_path, heading)
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
