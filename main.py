import pygame
from FLL.Field import Field
from Engine.GameWindow import GameWindow
from Maths.Pose2d import Pose2d
from Commands.Invoker import Invoker
from Commands.test_command import test_command
from Robotics.robot import Robot


def main():
    pygame.init()
    run = True
    start_pose = Pose2d(100, 100, 0)
    robot = Robot(start_pose, 0.015, 0.015)
    robot.Vr = 0.05
    robot.Vl = 0.09
    win = Field(robot)
    inv = Invoker()
    inv.add_command(test_command(robot))
    while run:
        win.clear_display()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                run = False
        win.check_robot_collision()
        win.render(robot)
        inv.invoke()
        #robot.update()
        win.display()
        print(robot.position)
    pygame.quit()


if __name__ == '__main__':
    main()
