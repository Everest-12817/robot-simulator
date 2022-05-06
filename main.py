import pygame
from Engine.GameWindow import GameWindow
from Engine.Entity import Entity


def main():
    pygame.init()
    run = True
    entity = Entity(100, 100, 100, 100, "C:/Users/user/Documents/GitHub/robot-simulator/assets/smile.png")
    win = GameWindow()
    while run:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                run = False
        win.render(entity)
    pygame.quit()


if __name__ == '__main__':
    main()
