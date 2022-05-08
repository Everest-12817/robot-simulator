from Robotics.DifferentialDriveKinematics import Kinematics
from Engine.Entity import Entity
from Maths.vector2d import Vector2d
from math import cos, sin , pi

ROBOT_TEXTURE_PATH = "assets/png-transparent-differential-wheeled-robot.png"


class Robot(Entity):
    def __init__(self, x, y, width, height, l, radius, initial_angle):
        super(Robot, self).__init__(x, y, width, height, ROBOT_TEXTURE_PATH, initial_angle)
        self.L = l
        self.R = 0
        self.wheel_radius = radius
        self.Angle = initial_angle
        self.Vl = 0
        self.Vr = 0
        self.AngularVelocity = 0
        self.ICC = Vector2d()

    def update(self):
        self.position = Kinematics.calc_new_position(self,1)
        self.rotation = self.rotation % (2 * pi)
        # x_n, y_n, theta_n = Kinematics.diffdrive(self.x, self.y, self.rotation, self.Vl, self.Vr, 1, self.L)
        # self.x = x_n
        # self.y = y_n
        # self.rotation = theta_n
