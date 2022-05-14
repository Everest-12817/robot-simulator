class Invoker:
    """
    Invoker executes a set of given commands
    Might change this class
    """
    def __init__(self, commands=None):
        """
        :param commands: a list of commands to execute
        """
        self.commands = [] if commands is None else commands

    def add_command(self, command):
        """
        Adds a command to the list of commands to execute
        :param command: command to add to the list of commands to execute
        :return:
        """
        self.commands.append(command)

    def invoke(self):
        """
        execute the list of commands
        :return: None
        """
        pass


