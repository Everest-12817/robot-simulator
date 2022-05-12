from Robotics.DifferentialDriveKinematics import Kinematics
from Engine.Entity import Entity
from Maths.Util import Util
import pygame
from math import cos, sin

ROBOT_TEXTURE_PATH = "assets/Robot/png-transparent-differential-wheeled-robot.png"

dt = 0


class Robot(Entity):
    def __init__(self, start_pose, width, height):
        super(Robot, self).__init__(start_pose.x, start_pose.y, Util.meter2pixels(width), Util.meter2pixels(height),
                                    ROBOT_TEXTURE_PATH, start_pose.theta)
        self._vl = 0
        self._vr = 0
        self.lasttime = pygame.time.get_ticks()
        self.AngularVelocity = 0

    @property
    def Vr(self):
        return Util.pixels2meter(self._vr)

    @Vr.setter
    def Vr(self, vr):
        self._vr = Util.meter2pixels(vr)

    @property
    def Vl(self):
        return Util.pixels2meter(self._vl)

    @Vl.setter
    def Vl(self, vl):
        self._vl = Util.meter2pixels(vl)

    def update(self):
        dt = (pygame.time.get_ticks() - self.lasttime) / 1000
        velocity = Kinematics.calculate_velocity(self._vl, self._vr)
        angular_velocity = Kinematics.calculate_angular_velocity(self._vl, self._vr, self._width)
        self.x += velocity * cos(self.heading) * dt
        self.y -= velocity * sin(self.heading) * dt
        self.heading += angular_velocity * dt
        self.lasttime = pygame.time.get_ticks()
