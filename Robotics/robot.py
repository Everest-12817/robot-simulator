from Robotics.DifferentialDriveKinematics import Kinematics
from Engine.Entity import Entity
from Maths.vector2d import Vector2d

ROBOT_TEXTURE_PATH = "assets/png-transparent-differential-wheeled-robot.png"


class Robot(Entity):
    def __init__(self, x, y, width, height, initial_angle):
        super(Robot, self).__init__(x, y, width, height, ROBOT_TEXTURE_PATH)
        self.L = width
        self.R = 0
        self.Angle = initial_angle
        self.Vl = 0
        self.Vr = 0
        self.AngularVelocity = 0
        self.ICC = Vector2d()

    def update(self):
        self.AngularVelocity = Kinematics.calc_angular_vel(self.Vr, self.Vl, self.L)
        self.R = Kinematics.calc_r(self.Vr, self.Vl, self.L)
        self.ICC = Kinematics.calc_ICC(super().x, super().y, self.R, super().rotation)
        self.position = Kinematics.calc_new_position(super().x, super().y, super().rotation, self.R,
                                                     self.AngularVelocity, 0.1)
