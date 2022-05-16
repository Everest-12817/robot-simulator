from Engine.GameWindow import GameWindow
from Engine.TextureLoader import TextureLoader
import pygame


class BaseField(GameWindow):
    """
    Class represent the robot game field
    This class simulates a robot game field with a robot in it
    The class inherits the game window base class
    """

    def __init__(self, robot, field_texture_path, height=600, width=600, missions=None):
        """

        :param robot: Robot on the game field
        :param field_texture_path:  path to field texture
        :param height: field height
        :param width: field width
        :param missions: list of missions on the field
        """
        super(BaseField, self).__init__(height, width)
        self.robot = robot
        self.field_texture = TextureLoader.load_texture(field_texture_path).convert()
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
        super().clear_display()

