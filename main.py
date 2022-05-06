import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    run = True
    while run:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                run = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
