from Maths.vector2d import Vector2d
from math import cos, sin


class DifferentialDriveKinematics:
    """
    This class contains kinematics functions for non holonomic differential
    """
    @staticmethod
    def calculate_angular_velocity(vl, vr, width):
        """
        Calculates the angular velocity of the robot
        :param vl: the velocity of the left motor
        :param vr: the velocirt of the right motor
        :param width: the width of the robot
        :return: The angular velocity of the robot
        """
        angular_velocity = (vr - vl) / width
        return angular_velocity

    @staticmethod
    def calc_R(vl, vr, L):
        """
        Calculates the signed distance from the ICC to the midpoint between the wheels
        :param vl: The velocity of the left motor
        :param vr: The velocity of the right motor
        :param L: The width of the robot
        :return: The signed distance from the ICC to the midpoint between the wheels
        """
        if vl == vr:
            return 0
        R = (L / 2) * ((vl + vr) / (vr - vl))
        return R

    @staticmethod
    def calc_ICC(x, y, R, theta):
        """
        Calculates the Instantaneous Center of Curvature of the robot
        :param x: the x position of the robot
        :param y: the y position of the robot
        :param R: the signed distance from the ICC to the midpoint between the wheels
        :param theta: the current heading of the robot
        :return: The instantaneous center of curvature of the robot
        """
        ICC = Vector2d(x - R * sin(theta), y + R * cos(theta))
        return ICC

    @staticmethod
    def calculate_velocity(vl, vr):
        """
        Calculates the velocity of the robot
        :param vl: the velocity of the left motor
        :param vr: the velocity of the right motor
        :return: the velocity of the robot
        """
        return (vl + vr) / 2
