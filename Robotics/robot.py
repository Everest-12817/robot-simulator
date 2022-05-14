from Robotics.Kinematics.DifferentialDriveKinematics import DifferentialDriveKinematics
from Robotics.DriveTrains.DifferentialDriveTrain import DifferentialDriveTrain
from Engine.Entity import Entity
from Maths.Util import Util
import pygame
from math import cos, sin

ROBOT_TEXTURE_PATH = "assets/Robot/png-transparent-differential-wheeled-robot.png"


class DifferentialDriveRobot(Entity):
    """"
    A robot entity
    """

    def __init__(self, start_pose, width, height):
        """
        :param start_pose: the stating position of the robot
        :param width: the width of the robot
        :param height:  the height of the robot
        """
        width = Util.meter2pixels(width)
        self.dt = 0
        super(DifferentialDriveRobot, self).__init__(start_pose.x, start_pose.y, width, Util.meter2pixels(height),
                                                     ROBOT_TEXTURE_PATH, start_pose.theta)
        self.lasttime = pygame.time.get_ticks()
        self.DriveTrain = DifferentialDriveTrain(width)

    @property
    def Vr(self):
        """
        :return: The real velocity of robot
        """
        return Util.pixels2meter(self.DriveTrain.vr)

    @Vr.setter
    def Vr(self, vr):
        """
        :param vr: The desirable velocity of the right motor
        :return: None
        """
        self.DriveTrain.vr = Util.meter2pixels(vr)

    @property
    def Vl(self):
        """
          :return: The rela velocity of the robot
        """
        return Util.pixels2meter(self.DriveTrain.vl)

    @Vl.setter
    def Vl(self, vl):
        """
        :param vl: The desirable velocity of the left motor
        :return: None
        """
        self.DriveTrain.vl = Util.meter2pixels(vl)

    def update(self):
        """
        Updates the position of the robot using the kinematics equations of non holonomic differential drive
        :return:
        """
        self.dt = (pygame.time.get_ticks() - self.lasttime) / 1000
        drive_distance = self.DriveTrain.drive(self.heading, self.dt)
        self.position = drive_distance + self.position
        self.lasttime = pygame.time.get_ticks()
