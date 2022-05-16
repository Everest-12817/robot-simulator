from Engine.GameWindow import GameWindow
from Engine.TextureLoader import TextureLoader
from Robotics.BaseField import BaseField
import pygame

FIELD_TEXTURE_PATH = "assets/Field/2021_CargoConnectMat-300x200.png"
FLL_FIELD_HEIGHT = 0  # TODO update with real height
FLL_FIELD_WIDTH = 0  # TODO update with real width


class FllField(BaseField):
    """
    Class represent the robot game field
    This class simulates a robot game field with a robot in it
    The class inherits the game window base class
    """

    def __init__(self, robot,  missions=None):
        """
        :param robot: Robot on the game field
        :param missions: missions on the game field
        """
        super(FllField, self).__init__(robot, FIELD_TEXTURE_PATH, 600, 600,
                                       missions)  # TODO : update with real field size
        self.robot = robot
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
