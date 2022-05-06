from Engine.Entity import Entity
from Maths.vector2d import Vector2d

ROBOT_TEXTURE_PATH = ""


class Robot(Entity):
    def __init__(self, x, y, width, height, l, r, initial_angle):
        super(Robot, self).__init__(x, y, width, height, ROBOT_TEXTURE_PATH)
        self.L = l
        self.R = r
        self.Angle = initial_angle
        self.Vl = 0
        self.Vr = 0
        self.AngularVelocity = 0
        self.ICC = Vector2d()

