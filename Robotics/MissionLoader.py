from Robotics.Mission import Mission
import xml.etree.ElementTree as ET


class MissionLoader:
    """
    Responsible for loading missions from xml files
    """
    @staticmethod
    def load_missions(mission_path):
        """
        loads missions from xml file into list
        :param mission_path: path to missions data xml file
        :return: a list of loaded missions
        """
        missions = []
        tree = ET.parse(mission_path)
        root = tree.getroot()
        for mission in root.findall('mission'):
            name = mission.get('name')
            height = int(mission.find("height").text)
            width = int(mission.find("width").text)
            x = int(mission.find("x").text)
            y = int(mission.find("y").text)
            heading = mission.find("heading")
            if heading is None:
                missions.append(Mission(x, y, width, height, name))
            else:
                missions.append(Mission(x,y,width,height,name,int(heading.text)))
        return missions
