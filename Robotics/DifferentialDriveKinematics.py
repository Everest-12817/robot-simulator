from Maths.vector2d import Vector2d
from Maths.Pose2d import Pose2d
from math import cos, sin, radians


class Kinematics:
    @staticmethod
    def calc_angular_vel(Vr, Vl, l):
        angular_velocity = (Vr - Vl) / l
        return angular_velocity

    @staticmethod
    def calc_R(Vr, Vl, L):
        if Vl == Vr:
            return 0
        R = (L / 2) * ((Vl + Vr) / (Vr - Vl))
        return R

    @staticmethod
    def calc_ICC(x, y, R, theta):
        ICC = Vector2d(x - R * sin(theta), y + R * cos(theta))
        return ICC

    @staticmethod
    def calc_new_position(robot, t):
        if robot.Vl == robot.Vr:
            theta_n = robot.rotation
            x_n = robot.x + robot.Vl * t * cos(robot.rotation)
            y_n = robot.y + robot.Vl * t * sin(robot.rotation)
        else:
            R = Kinematics.calc_R(robot.Vr, robot.Vl, robot.L)
            ICC = Kinematics.calc_ICC(robot.x, robot.y, R, robot.rotation)
            robot.AngularVelocity = Kinematics.calc_angular_vel(robot.Vr, robot.Vl, robot.L)
            dtheta = robot.AngularVelocity * t
            x_n = cos(dtheta) * (robot.x - ICC.x) - sin(dtheta) * (robot.y - ICC.y) + ICC.x
            y_n = sin(dtheta)*(robot.x-ICC.x) + cos(dtheta)*(robot.y-ICC.y) + ICC.y
            theta_n = robot.rotation + dtheta
        return Pose2d(x_n, y_n, theta_n)

    @staticmethod
    def diffdrive(x, y, theta, v_l, v_r, t, l):
        # straight line
        if (v_l == v_r):
            theta_n = theta
            x_n = x + v_l * t * cos(theta)
            y_n = y + v_l * t * sin(theta)
        # circular motion
        else:
            # Calculate the radius
            R = l / 2.0 * ((v_l + v_r) / (v_r - v_l))
            # computing center of curvature
            ICC_x = x - R * sin(theta)
            ICC_y = y + R * cos(theta)
            # compute the angular velocity
            omega = (v_r - v_l) / l
            # computing angle change
            dtheta = omega * t
            # forward kinematics for differential drive
            x_n = cos(dtheta) * (x - ICC_x) - sin(dtheta) * (y - ICC_y) + ICC_x
            y_n = sin(dtheta) * (x - ICC_x) + cos(dtheta) * (y - ICC_y) + ICC_y
            theta_n = theta + dtheta
        return x_n, y_n, theta_n