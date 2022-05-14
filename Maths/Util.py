M2P = 3779.52


class Util:
    """
    This class contains mathematical utility functions and unit conversion methods
    """

    @staticmethod
    def pixels2meter(pixels):
        """
        Converts pixels to meters
        :param pixels: Amount of pixels
        :return: amount of meters equivalent to the pixels
        """
        return pixels / M2P

    @staticmethod
    def meter2pixels(meters):
        """
        Converts meters to pixels
        :param meters: Amount of meters
        :return: Amount of pixels equivalent to the meters
        """
        return meters * M2P
