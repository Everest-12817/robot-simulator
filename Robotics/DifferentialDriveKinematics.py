from Maths.vector2d import Vector2d
from math import cos, sin


class Kinematics:
    @staticmethod
    def calculate_angular_velocity(vl, vr, width):
        angular_velocity = (vr - vl) / width
        return angular_velocity

    @staticmethod
    def calc_R(vl, vr, L):
        if vl == vr:
            return 0
        R = (L / 2) * ((vl + vr) / (vr - vl))
        return R

    @staticmethod
    def calc_ICC(x, y, R, theta):
        ICC = Vector2d(x - R * sin(theta), y + R * cos(theta))
        return ICC

    @staticmethod
    def calculate_velocity(vl, vr):
        return (vl + vr) / 2
