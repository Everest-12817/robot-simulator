class BaseDriveTrain:
    """
    Base class for drive train objects
    """
    def drive(self, heading, dt):
        """
         Calculates the distance traveled on a given time frame
         :param heading: The heading of the robot
         :param dt: the time frame of the movement
         :return: pose2d that represents the distance traveled during a given time frame
         """
        raise NotImplementedError("[BaseDriveTrain] Cannot call drive on base drive train")
