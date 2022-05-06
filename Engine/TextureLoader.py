import pygame


class TextureLoader:

    @staticmethod
    def load_texture(texture_path):
        try:
            texture = pygame.image.load(texture_path).convert()
        except FileNotFoundError:
            raise Exception("[LOAD TEXTURE] Cannot find texture path")
        return texture
