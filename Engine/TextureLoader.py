import pygame


class TextureLoader:
    """
    This class contains static functions for all managing textures and loading them
    """

    @staticmethod
    def load_texture(texture_path):
        """
        static method
        Used to load texture from texture file path
        :param texture_path: path to texture file
        :return: loaded texture object
        """
        try:
            texture = pygame.image.load(texture_path).convert_alpha()
        except FileNotFoundError:
            raise Exception("[LOAD TEXTURE] Cannot find texture path")
        return texture

    @staticmethod
    def load_text(text, font, color):
        """
        Create text surface that can be rendered by the game window
        :param text: text to render
        :param font: the font of the text
        :param color: the color of the text
        :return: The surface of the text render
        """
        text_surface = font.render(text, False, color)
        return text_surface

    @staticmethod
    def rotate_texture(texture, rotation):
        """
        Rotates a given texture by the rotation parameter
        :param texture: loaded texture object to rotate
        :param rotation: Desirable rotation of texture
        :return: rotated texture object
        """
        orig_rect = texture.get_rect()
        rot_texture = pygame.transform.rotate(texture, rotation)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_texture.get_rect().center
        rot_texture = rot_texture.subsurface(rot_rect).copy()
        return rot_texture
