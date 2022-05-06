from Maths.vector2d import Vector2d
from math import cos, sin


class Kinematics:
    @staticmethod
    def calc_angular_vel(Vr, Vl, L):
        angular_velocity = (Vr - Vl) / L
        return angular_velocity

    @staticmethod
    def calc_r(Vr, Vl, L):
        R = (L / 2) * ((Vl + Vr) / (Vr - Vl))
        return R

    @staticmethod
    def calc_ICC(x, y, R, angle):
        ICC = Vector2d(x - R * sin(angle), y + R * cos(angle))
        return ICC


