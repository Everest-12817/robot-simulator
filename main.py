import pygame
from Engine.GameWindow import GameWindow
from Engine.Entity import Entity
from Robotics.robot import Robot


def main():
    pygame.init()
    run = True
    robot = Robot(100, 100, 100, 100, 0)
    robot.Vr = 10
    robot.Vl = 1
    clock = pygame.time.Clock()
    win = GameWindow()
    while run:
        win.clear_display()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                run = False
        clock.tick(5)
        robot.update()
        win.render(robot)
        win.display()
    pygame.quit()


if __name__ == '__main__':
    main()
