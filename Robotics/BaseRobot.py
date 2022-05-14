from Engine.Entity import Entity
from Maths.Util import Util
import pygame
from Robotics.DriveTrains.BaseDriveTrain import BaseDriveTrain


class BaseRobot(Entity):
    """
    Base class for robot entities
    """
    def __init__(self, start_pose, width, height, robot_texture_path=""):
        """
        :param start_pose: the stating position of the robot
        :param width: the width of the robot
        :param height:  the height of the robot
        """
        width = Util.meter2pixels(width)
        height = Util.meter2pixels(height)
        self.dt = 0
        super(BaseRobot, self).__init__(start_pose.x, start_pose.y, width, height,
                                        robot_texture_path, start_pose.theta)
        self.lasttime = pygame.time.get_ticks()
        self.DriveTrain = BaseDriveTrain()

    def update(self):
        """
        Updates the position of the robot using the kinematics equations of non holonomic differential drive
        :return:
        """
        self.dt = (pygame.time.get_ticks() - self.lasttime) / 1000
        drive_distance = self.DriveTrain.drive(self.heading, self.dt)
        self.position = drive_distance + self.position
        self.lasttime = pygame.time.get_ticks()