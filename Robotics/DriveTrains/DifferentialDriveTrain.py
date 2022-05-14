from Robotics.DriveTrains.BaseDriveTrain import BaseDriveTrain
from Maths.Util import Util
from Maths.Pose2d import Pose2d
from Robotics.Kinematics.DifferentialDriveKinematics import DifferentialDriveKinematics
from math import cos, sin


class DifferentialDriveTrain(BaseDriveTrain):
    def __init__(self, width):
        self.vl = 0
        self.vr = 0
        self._width = width

    def drive(self, heading, dt):
        velocity = DifferentialDriveKinematics.calculate_velocity(self.vl, self.vr)
        angular_velocity = DifferentialDriveKinematics.calculate_angular_velocity(self.vl, self.vr, self._width)
        x = velocity * cos(heading) * dt
        y = -(velocity * sin(heading) * dt)
        heading = angular_velocity * dt
        return Pose2d(x, y, heading)

