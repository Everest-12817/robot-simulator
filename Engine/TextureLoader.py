import pygame


class TextureLoader:

    @staticmethod
    def load_texture(texture_path):
        try:
            texture = pygame.image.load(texture_path).convert()
        except FileNotFoundError:
            raise Exception("[LOAD TEXTURE] Cannot find texture path")
        return texture

    @staticmethod
    def rotate_texture(texture, rotation):
        orig_rect = texture.get_rect()
        rot_texture = pygame.transform.rotate(texture, rotation)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_texture.get_rect().center
        rot_texture = rot_texture.subsurface(rot_rect).copy()
        return rot_texture
