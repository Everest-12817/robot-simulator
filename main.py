import pygame
from FLL.Field import Field
from Maths.Pose2d import Pose2d
from Robotics.DifferentialDriveRobot import DifferentialDriveRobot


def main():
    pygame.init()
    run = True
    start_pose = Pose2d(100, 100, 0)
    robot = DifferentialDriveRobot(start_pose, 0.015, 0.015)
    robot.Vr = 0.09
    robot.Vl = 0.09
    win = Field(robot)
    while run:
        win.clear_display()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                run = False
        win.check_robot_collision()
        win.render(robot)
        robot.update()
        win.display()
    pygame.quit()


if __name__ == '__main__':
    main()
