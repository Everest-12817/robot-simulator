class BaseDriveTrain:
    """
    Base class for drive train objects
    """
    def drive(self, heading, dt):
        raise NotImplementedError("[BaseDriveTrain] Cannot call drive on base drive train")
