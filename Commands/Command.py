class Command:

    def __init__(self):
        self._command_name = ""
        self.condition = None

    @property
    def command_name(self):
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        self._command_name = command_name

    def execute(self):
        raise NotImplementedError("[Command] Cannot call execute on pure command")

    def __str__(self):
        raise NotImplementedError("[Command] Cannot call str on pure command")
