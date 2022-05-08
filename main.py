import pygame
from Engine.GameWindow import GameWindow
from Engine.Entity import Entity
from math import pi
from Robotics.robot import Robot


def main():
    pygame.init()
    run = True
    robot = Robot(100, 100, 100, 100, 0.5, 1, pi / 2)
    robot.Vr = 0.9
    robot.Vl = 0.9
    clock = pygame.time.Clock()
    win = GameWindow()
    while run:
        win.clear_display()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                run = False
        print(robot.position)
        robot.update()
        win.render(robot)
        win.display()
    pygame.quit()


if __name__ == '__main__':
    main()
