import pygame
from Engine.GameWindow import GameWindow
from Engine.Entity import Entity


def main():
    pygame.init()
    run = True
    entity = Entity(100, 100, 100, 100, "assets/smile.png")
    win = GameWindow()
    while run:
        win.clear_display()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                run = False
            if even.type == pygame.KEYDOWN:
                entity.move(10, 0)
                entity.rotate(90)
        win.render(entity)
        win.display()
    pygame.quit()


if __name__ == '__main__':
    main()
