from Robotics.DriveTrains.DifferentialDriveTrain import DifferentialDriveTrain
from Robotics.BaseRobot import BaseRobot
from Maths.Util import Util

ROBOT_TEXTURE_PATH = "assets/Robot/png-transparent-differential-wheeled-robot.png"


class DifferentialDriveRobot(BaseRobot):
    """"
    A differential drive robot entity
    """

    def __init__(self, start_pose, width, height):
        """
        :param start_pose: the stating position of the robot
        :param width: the width of the robot
        :param height:  the height of the robot
        """
        super(DifferentialDriveRobot, self).__init__(start_pose, width, height, ROBOT_TEXTURE_PATH)
        self.DriveTrain = DifferentialDriveTrain(self.w)

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
