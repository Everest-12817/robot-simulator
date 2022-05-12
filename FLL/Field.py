from Engine.GameWindow import GameWindow
from Engine.TextureLoader import TextureLoader
import pygame

FIELD_TEXTURE_PATH = "assets/Field/2021_CargoConnectMat-300x200.png"


class Field(GameWindow):
    def __init__(self, robot, missions=None):
        super(Field, self).__init__()  # TODO : update with real field size
        self.robot = robot
        self.field_texture = TextureLoader.load_texture(FIELD_TEXTURE_PATH).convert()
        self.field_texture = pygame.transform.scale(self.field_texture, (self._screen_height, self._screen_width))
        self.missions = [] if missions is None else missions

    def check_robot_collision(self):
        for mission in self.missions:
            if pygame.sprite.spritecollideany(self.robot, mission):
                print(f"Robot collided with mission {mission.name}")

    def clear_display(self):
        super().clear_display()
        self._game_window.blit(self.field_texture, [0, 0])
