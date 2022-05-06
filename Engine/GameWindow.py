from Engine.Entity import Entity
import pygame


class GameWindow:
    def __init__(self, screen_height=600, screen_width=600):
        self._screen_height = screen_height
        self._screen_width = screen_width
        self._game_window = pygame.display.set_mode((screen_width, screen_height))

    def render(self, entity):
        self._game_window.blit(entity.texture, (entity.x, entity.y))

    def display(self):
        pygame.display.flip()
