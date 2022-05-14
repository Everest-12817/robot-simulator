from Robotics.DifferentialDriveKinematics import Kinematics
from Engine.Entity import Entity
from Maths.Util import Util
import pygame
from math import cos, sin

ROBOT_TEXTURE_PATH = "assets/Robot/png-transparent-differential-wheeled-robot.png"

dt = 0


class Robot(Entity):
    """"
    A robot entity
    """
    def __init__(self, start_pose, width, height):
        """
        :param start_pose: the stating position of the robot
        :param width: the width of the robot
        :param height:  the height of the robot
        """
        super(Robot, self).__init__(start_pose.x, start_pose.y, Util.meter2pixels(width), Util.meter2pixels(height),
                                    ROBOT_TEXTURE_PATH, start_pose.theta)
        self._vl = 0
        self._vr = 0
        self.lasttime = pygame.time.get_ticks()
        self.AngularVelocity = 0

    @property
    def Vr(self):
        """
        :return: The real velocity of robot
        """
        return Util.pixels2meter(self._vr)

    @Vr.setter
    def Vr(self, vr):
        """
        :param vr: The desirable velocity of the right motor
        :return: None
        """
        self._vr = Util.meter2pixels(vr)

    @property
    def Vl(self):
        """
          :return: The rela velocity of the robot
        """
        return Util.pixels2meter(self._vl)

    @Vl.setter
    def Vl(self, vl):
        """
        :param vl: The desirable velocity of the left motor
        :return: None
        """
        self._vl = Util.meter2pixels(vl)

    def update(self):
        """
        Updates the position of the robot using the kinematics equations of non holonomic differential drive
        :return:
        """
        dt = (pygame.time.get_ticks() - self.lasttime) / 1000
        velocity = Kinematics.calculate_velocity(self._vl, self._vr)
        angular_velocity = Kinematics.calculate_angular_velocity(self._vl, self._vr, self._width)
        self.x += velocity * cos(self.heading) * dt
        self.y -= velocity * sin(self.heading) * dt
        self.heading += angular_velocity * dt
        self.lasttime = pygame.time.get_ticks()
