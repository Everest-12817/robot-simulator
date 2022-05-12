import pygame
from Engine.GameWindow import GameWindow
from Maths.Pose2d import Pose2d
from Engine.Entity import Entity
from math import pi
from Robotics.robot import Robot


def main():
    pygame.init()
    run = True
    start_pose = Pose2d(100, 100, 0)
    robot = Robot(start_pose, 0.01 * 3779.52, 0.01 * 3779.52)
    robot.Vr = 0.05 * robot.m2p
    robot.Vl = 0.05 * robot.m2p
    win = GameWindow()
    while run:
        win.clear_display()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                run = False
        win.render(robot)
        robot.update()
        win.display()

    pygame.quit()


if __name__ == '__main__':
    main()
