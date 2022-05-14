from Engine.GameWindow import GameWindow
from Engine.TextureLoader import TextureLoader
import pygame

FIELD_TEXTURE_PATH = "assets/Field/2021_CargoConnectMat-300x200.png"


class Field(GameWindow):
    """
    Class represent the robot game field
    This class simulates a robot game field with a robot in it
    The class inherits the game window base class
    """
    def __init__(self, robot, missions=None):
        """
        :param robot: Robot on the game field
        :param missions: missions on the game field
        """
        super(Field, self).__init__()  # TODO : update with real field size
        self.robot = robot
        self.field_texture = TextureLoader.load_texture(FIELD_TEXTURE_PATH).convert()
        self.field_texture = pygame.transform.scale(self.field_texture, (self._screen_height, self._screen_width))
        self.missions = [] if missions is None else missions

    def check_robot_collision(self):
        """
        Checks if the robot collided with a mission
        Prints the mission that the robot collided with
        :return:
        """
        for mission in self.missions:
            if pygame.sprite.spritecollideany(self.robot, mission):
                print(f"Robot collided with mission {mission.name}")

    def clear_display(self):
        """
        Clears the game screen and renders the field image on it
        :return: None
        """
        super().clear_display()
        self._game_window.blit(self.field_texture, [0, 0])
