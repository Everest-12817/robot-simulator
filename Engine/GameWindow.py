from Engine.Entity import Entity
from Engine.TextureLoader import TextureLoader
import pygame


class GameWindow:
    def __init__(self, screen_height=600, screen_width=600):
        self._screen_height = screen_height
        self._screen_width = screen_width
        self._game_window = pygame.display.set_mode((screen_width, screen_height))

    def render(self, entity):
        texture = TextureLoader.load_texture(entity.texture_path)
        texture = pygame.transform.scale(texture, (entity.h, entity.w))
        texture = TextureLoader.rotate_texture(texture, entity.rotation)
        self._game_window.blit(texture, (entity.x, entity.y))

    def display(self):
        pygame.display.flip()

    def clear_display(self):
        self._game_window.fill((255, 255, 255))
