from Robotics.DriveTrains.BaseDriveTrain import BaseDriveTrain
from Maths.Pose2d import Pose2d
from Robotics.Kinematics.DifferentialDriveKinematics import DifferentialDriveKinematics
from math import cos, sin


class DifferentialDriveTrain(BaseDriveTrain):
    """
    Class for differential drive train objects
    """

    def __init__(self, width):
        """
        :param width: the width of the drive train
        """
        self.vl = 0
        self.vr = 0
        self._width = width

    def drive(self, heading, dt):
        """
        Calculates the distance traveled on a given time frame
        :param heading: The heading of the robot
        :param dt: the time frame of the movement
        :return: pose2d that represents the distance traveled during a given time frame
        """
        velocity = DifferentialDriveKinematics.calculate_velocity(self.vl, self.vr)
        angular_velocity = DifferentialDriveKinematics.calculate_angular_velocity(self.vl, self.vr, self._width)
        x = velocity * cos(heading) * dt
        y = -(velocity * sin(heading) * dt)
        heading = angular_velocity * dt
        return Pose2d(x, y, heading)
