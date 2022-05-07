from Maths.vector2d import Vector2d
from Maths.Pose2d import Pose2d
from math import cos, sin , inf


class Kinematics:
    @staticmethod
    def calc_angular_vel(Vr, Vl, L):
        angular_velocity = (Vr - Vl) / L
        return angular_velocity

    @staticmethod
    def calc_r(Vr, Vl, L):
        if Vl == Vr:
            return inf
        R = (L / 2) * ((Vl + Vr) / (Vr - Vl))
        return R

    @staticmethod
    def calc_ICC(x, y, R, angle):
        ICC = Vector2d(x - R * sin(angle), y + R * cos(angle))
        return ICC

    @staticmethod
    def calc_new_position(x, y, angle, R, w, dt):
        d_angle = w * dt
        new_x = -R * sin(angle) + R*sin(angle + d_angle) + x
        new_y = R * cos(angle) - R * cos(angle * d_angle) + y
        new_angle = angle + d_angle
        return Pose2d(new_x, new_y, new_angle)
