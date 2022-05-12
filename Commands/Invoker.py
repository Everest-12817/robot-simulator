class Invoker:
    def __init__(self, commands=None):
        self.commands = [] if commands is None else commands

    def invoke(self):
        for command in self.commands.copy():
            command.execute()
            self.commands.remove(command)
