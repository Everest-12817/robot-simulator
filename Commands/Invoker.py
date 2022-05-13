class Invoker:
    def __init__(self, commands=None):
        self.commands = [] if commands is None else commands

    def add_command(self, command):
        self.commands.append(command)

    def invoke(self):
        if len(self.commands) == 0:
            print("[Invoker] No command to execute")
            return
        command = self.commands[0]
        if command.condition is None:
            command.execute()
            self.commands.pop(0)
        elif command.condition:
            command.execute()
        else:
            self.commands.pop(0)



