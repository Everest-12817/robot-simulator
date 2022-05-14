from math import degrees
from Engine.Colors import black
from Engine.TextureLoader import TextureLoader
import pygame


class GameWindow:
    """
    Base game window class
    This class creates the game window and is responsible for rendering entities to the game window
    """

    def __init__(self, screen_height=600, screen_width=600):
        self._screen_height = screen_height
        self._screen_width = screen_width
        self._game_window = pygame.display.set_mode((screen_width, screen_height))

    def render(self, entity):
        """
        Renders entity to game  screen

        :param entity: entity to render to screen
        :return: None
        """
        texture = TextureLoader.load_texture(entity.texture_path)
        texture = pygame.transform.scale(texture, (entity.h, entity.w))
        texture = TextureLoader.rotate_texture(texture, degrees(entity.heading))
        self._game_window.blit(texture, (entity.x, entity.y))

    def render_text(self, text, color=black, x=0, y=0):
        """
        Renders text to game window
        :param text: the text to render to screen
        :param color: the color of the text
        :param x: the position of the text
        :param y: the y position of the text
        :return: None
        """
        font = pygame.font.SysFont("calibri", 30)
        texture_surface = TextureLoader.load_text(text, font, color)
        self._game_window.blit(texture_surface, (x, y))

    def display(self):
        """
        Display entities to screen
        :return: None
        """
        pygame.display.flip()

    def clear_display(self):
        """
        Cleans the game screen
        :return: None
        """
        self._game_window.fill(black)
