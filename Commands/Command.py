class Command:

    def execute(self):
        raise NotImplementedError("[Command] Cannot call execute on pure command")